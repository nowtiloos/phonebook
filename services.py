import csv
import re

from tabulate import tabulate


class CsvExecutor:
    def __init__(self, file: str, encoding: str = "utf-8") -> None:
        self.file = file
        self.encoding = encoding

    def read_data(self) -> list[dict]:
        with open(file=self.file, mode="r", encoding=self.encoding, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            data: list[dict] = [row for row in reader]
            return data

    def add_one(self, contact_data: dict):
        fieldnames = contact_data.keys()

        with open(file=self.file, mode="a", encoding=self.encoding, newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(contact_data)

    def search(self, search_term: str, search_field: str) -> list[dict]:
        contacts: list[dict] = self.read_data()
        regex_pattern = re.compile(f"^{search_term}", re.IGNORECASE)

        search_results = [contact for contact in contacts if regex_pattern.search(contact[search_field])]
        return search_results

    def delete(self, identifier: str) -> bool:
        contacts: list[dict] = self.read_data()

        for index, contact in enumerate(contacts):
            if contact.get("id") == identifier:
                del contacts[index]
                break
        else:
            print(f"Контакт с id {identifier} не найден\n")
            return False

        self._rewrite(data=contacts)

        return True

    def patch(self, identifier: str, new_data: dict) -> bool:
        contacts = self.read_data()

        for contact in contacts:
            if contact.get("id") == identifier:
                contact.update(new_data)
                break
        else:
            return False

        self._rewrite(data=contacts)

        return True

    def _rewrite(self, data):
        with open(file=self.file, mode="w", encoding=self.encoding, newline="") as csvfile:
            fieldnames = data[0].keys() if data else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)


class Paginator:
    def __init__(self, data: list[dict], page_size: int, sort_by: str) -> None:
        self.data = sorted(data, key=lambda x: x[sort_by])
        self.page_size = page_size

    def get_total_pages(self) -> int:
        return (len(self.data) + self.page_size - 1) // self.page_size

    def get_current_page_data(self, current_page: int) -> list[dict]:
        start = (current_page - 1) * self.page_size
        end = start + self.page_size
        return self.data[start:end]

    def display_page(self, current_page: int) -> None:
        current_page_data = self.get_current_page_data(current_page)
        table = tabulate(tabular_data=current_page_data, headers="keys", tablefmt="grid")
        print(table)

    def show(self):
        err: str = ""
        total_pages: int = self.get_total_pages()
        current_page: int = 1

        while True:
            self.display_page(current_page)
            if err:
                print(err)
            user_input = input(f"Страница {current_page}/{total_pages}. Введите номер страницы или 'exit' для выхода: ")
            if user_input.lower() == 'exit':
                break

            try:
                page_number = int(user_input)
                if 1 <= page_number <= total_pages:
                    current_page = page_number
                    err = ""
                else:
                    err = f"ВНИМАНИЕ! >>> Некорректный номер страницы. Введите номер страницы от 1 до {total_pages}."
            except ValueError:
                err = "ВНИМАНИЕ! >>> Некорректный ввод. Введите номер страницы или 'exit' для выхода."

import csv
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

            if csvfile.tell() == 0:  # Проверка, если файл пуст
                writer.writeheader()

            writer.writerow(contact_data)


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

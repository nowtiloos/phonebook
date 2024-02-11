import uuid

from services import CsvExecutor, Paginator
from config import settings
from schemas import Contact


def add_contact():
    contact = Contact(id=uuid.uuid4(),
                      surname=input("Введите фамилию контакта: ").title(),
                      name=input("Введите имя контакта: ").title(),
                      patronymic=input("Введите отчество контакта: ").title(),
                      organization=input("Введите название организации: ").title(),
                      work_phone=input("Введите рабочий номер телефона: "),
                      personal_phone=input("Введите личный номер телефона: "))
    executor: CsvExecutor = CsvExecutor(file=settings.FILE_NAME)
    executor.add_one(contact.model_dump())
    print(f"\nКонтакт добавлен в {settings.FILE_NAME}\n")


def find_contact(page_size=settings.PAGE_SIZE, sort_by=settings.SORT_BY) -> None:
    executor: CsvExecutor = CsvExecutor(file=settings.FILE_NAME)
    headers: dict = {key: value for key, value in enumerate(Contact.model_fields.keys(), start=1)}

    search_field = int(input(f"Введите номер столбца для поиска\n{headers}: "))
    search_term = input("Введите ключевое слово для поиска: ").title()

    match: list[dict] = executor.search(search_term=search_term, search_field=headers.get(search_field))

    paginator: Paginator = Paginator(data=match, page_size=page_size, sort_by=sort_by)
    paginator.show()


def delete_contact():
    executor: CsvExecutor = CsvExecutor(file=settings.FILE_NAME)
    identifier = input("Введите id контакта для удаления: \n")
    if executor.delete(identifier=identifier):
        print(f"Контакт с id {identifier} удален\n")


def patch_contact():
    executor: CsvExecutor = CsvExecutor(file=settings.FILE_NAME)
    identifier = input("Введите id контакта: ")
    contact = Contact(id=identifier,
                      surname=input("Введите фамилию контакта: ").title(),
                      name=input("Введите имя контакта: ").title(),
                      patronymic=input("Введите отчество контакта: ").title(),
                      organization=input("Введите название организации: ").title(),
                      work_phone=input("Введите рабочий номер телефона: "),
                      personal_phone=input("Введите личный номер телефона: "))
    if executor.patch(identifier=identifier, new_data=contact.model_dump()):
        print(f"Контакт с id {identifier} обновлен\n")


def show_contacts(page_size=settings.PAGE_SIZE, sort_by=settings.SORT_BY) -> None:
    """Показывает все записи из телефонной книги"""
    executor: CsvExecutor = CsvExecutor(file=settings.FILE_NAME)
    contacts: list[dict] = executor.read_data()

    paginator: Paginator = Paginator(data=contacts, page_size=page_size, sort_by=sort_by)
    paginator.show()

import sys

from controllers import add_contact, find_contact, delete_contact, show_contacts


def main():
    if len(sys.argv) <= 1:
        print(f"""Для запуска скрипта введите
python {sys.argv[0]} <аргумент> """)
        return

    argument = sys.argv[1]

    match argument:
        case "add":
            add_contact()
        case "find":
            find_contact()
        case "delete":
            delete_contact()
        case "show":
            show_contacts()
        case _:
            print("Неверное действие. Доступные действия: add, find, delete, show.")


if __name__ == "__main__":
    main()

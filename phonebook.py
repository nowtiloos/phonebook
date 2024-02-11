from controllers import add_contact, find_contact, delete_contact, show_contacts, patch_contact


def main():
    controllers = [show_contacts, find_contact, add_contact, patch_contact, delete_contact]

    while True:
        print("Выберите операцию:")
        for i, action in enumerate(controllers, start=1):
            print(f"{i}. {action.__name__.replace('_', ' ').title()}")
        print("0. Exit\n")

        operation = input("Введите номер операции: ")

        if operation.isdigit() and 0 <= int(operation) <= len(controllers):
            index = int(operation)
            if index == 0:
                print("Программа завершена.")
                break
            else:
                if controllers[index - 1]():
                    continue
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующую операцию.")


if __name__ == "__main__":
    main()

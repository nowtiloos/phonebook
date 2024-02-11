from controllers import add_contact, find_contact, delete_contact, show_contacts


def main():
    actions = [add_contact, find_contact, delete_contact, show_contacts]

    while True:
        print("Выберите действие:")
        for i, action in enumerate(actions, start=1):
            print(f"{i}. {action.__name__.replace('_', ' ').title()}")
        print("0. Exit")

        choice = input("Введите номер действия: ")

        if choice.isdigit() and 0 <= int(choice) <= len(actions):
            index = int(choice)
            if index == 0:
                print("Программа завершена.")
                break
            else:
                if actions[index - 1]():
                    continue
        else:
            print("Некорректный ввод. Пожалуйста, выберите существующее действие.")


if __name__ == "__main__":
    main()

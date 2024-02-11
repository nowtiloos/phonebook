from controllers import add_contact, find_contact, delete_contact, show_contacts, patch_contact
from services import MainMenu


def main():
    controllers = [show_contacts, find_contact, add_contact, patch_contact, delete_contact]
    menu = MainMenu(controllers=controllers)

    menu.show()


if __name__ == "__main__":
    main()

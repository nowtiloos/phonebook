from controllers import add_contact, feature_search, delete_contact, show_contacts, patch_contact
from services import MainMenu


def main():
    controllers: tuple = (show_contacts, feature_search, add_contact, patch_contact, delete_contact)
    menu: MainMenu = MainMenu(controllers=controllers)

    menu.show()


if __name__ == "__main__":
    main()

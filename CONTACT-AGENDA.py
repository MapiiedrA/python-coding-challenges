def my_agenda(): 
    agenda = {}

    def insert_contact(name: str):
        """Ask for a phone number and insert it into agenda for given name."""
        phone = input("Enter the contact's phone number: ")
        if phone.isdigit() and 0 < len(phone) <= 11:
            agenda[name] = phone
            print(f"Contact {name} saved.")
        else:
            print("You must enter a phone number with a maximum of 11 digits.")

    while True:
        print()
        print("1. Search Contact")
        print("2. Insert Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        option = input("\nSelect an option: ")

        match option:
            case "1":
                name = input("Enter the name of the contact to search for: ")
                if name in agenda:
                    print(f"The phone number for {name} is {agenda[name]}.")
                else:
                    print(f"Contact {name} does not exist.")
            case "2":
                name = input("Enter the contact name: ")
                if name:
                    insert_contact(name)
                else:
                    print("Name cannot be empty.")
            case "3":
                name = input("Enter the name of the contact to update: ")
                if name in agenda:
                    insert_contact(name)
                else:
                    print(f"Contact {name} does not exist.")
            case "4":
                name = input("Enter the name of the contact to delete: ")
                if name in agenda:
                    del agenda[name]
                    print(f"Contact {name} deleted.")
                else:
                    print(f"Contact {name} does not exist.")
            case "5":
                print("Exiting Agenda.")
                break
            case _:
                print("Invalid option. Please choose an option from 1 to 5.")


if __name__ == "__main__":
    my_agenda()

# by MapiiedrA 12/8/2026
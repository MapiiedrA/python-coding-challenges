# Lists
my_list = ["Mauricio", "Black", "Wolfy", "Piedra"]
print(my_list)
my_list.append("MapiiedrA") # insertion # used to add data to the list. its order will correspond to insertion order.
print(my_list)
my_list.remove("Mauricio") # deletion
print(my_list)
print(my_list[1]) # access
my_list[1] = "Cuervillo" # update + insertion of new data.
print(my_list)
my_list.sort() # sorting (by default it sorts alphabetically; for numbers it would be from lowest to highest)
print(my_list)

# Tuples # more secure constructor type that is immutable.
my_tuple = ("Mauricio", "Piedra", "MapiiedrA", "32")
print(type(my_tuple))
print(my_tuple[1]) # access
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # sorting # this creates an object of type tuple
print(my_tuple)
print(type(my_tuple))

# Sets # a set is a Hashset, sets do not duplicate data.
my_set = {"Mauricio", "Piedra", "MapiiedrA", "32"}
print(my_set)
print(type(my_set))
my_set.add("mapiedra3223@gmail.com") # insertion
print(my_set)
my_set.remove("Mauricio") # deletion
print(my_set)
my_set.update

my_set = set(sorted(my_set)) # CANNOT BE SORTED, BY SYSTEM DEFINITION IT IS UNORDERED.
print(my_set)
print(type(my_set))

# Dictionaries

my_dict: dict = {"name":"Mauricio",
                "surname":"Piedra",
                "alias":"MapiiedrA",
                "age":"32"
} # The difference between a set and a Dict is that dicts are ordered by key-value pairs, unlike sets.
my_dict["email"] = "mapiedra3223@gmail.com" # insertion
print(my_dict)
del my_dict["surname"] # deletion
print(type(my_dict))
print(my_dict["name"]) # access
my_dict["age"] = "33" # update
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # sorting # Note: dicts are ordered in modern Python.
print(my_dict)
print(type(my_dict))

"""
* EXTRA CHALLENGE (optional):
 * Create a terminal-based contact agenda.
 * - You must implement functionalities to search, insert, update, and delete contacts.
 * - Each contact must have a name and a phone number.
 * - The program should first ask which operation you want to perform, and then
 *   request the necessary data to carry it out.
 * - The program must not allow non-numeric phone numbers or numbers with more than 11 digits
 *   (or whatever number of digits you choose).
 * - An option to exit the program must also be provided.
 """

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

# Review variables/errors that don't work and the rest of the code # Fixed, was missing an if statement for __name__ == "__main__".
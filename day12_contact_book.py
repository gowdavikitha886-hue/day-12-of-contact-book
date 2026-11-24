
# Day 12: Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        print("\n===== SAVED CONTACTS =====")

        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)

def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Contact found!")
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Main menu
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Thank you for using Contact Book!")
        print("Day 12 completed!")
        break

    else:
        print("Invalid choice! Please try again.")

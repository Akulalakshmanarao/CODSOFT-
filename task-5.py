# Contact Book
contacts = []  

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Store Name: ")
    phone = input("Phone Number: ")
    email = input("Email Address: ")
    address = input("Store Address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")


def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return

    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")


def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone number: ")

    found = False
    for contact in contacts:
        if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
            print("\n Contact Found")
            print("Name   :", contact["name"])
            print("Phone  :", contact["phone"])
            print("Email  :", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print(" No contact matched your search.")

def update_contact():
    view_contacts()
    if not contacts:
        return

    choice = int(input("\nEnter contact number to update: ")) - 1

    if 0 <= choice < len(contacts):
        print("\n--- Update Contact ---")
        contacts[choice]["name"] = input("New Store Name: ")
        contacts[choice]["phone"] = input("New Phone Number: ")
        contacts[choice]["email"] = input("New Email: ")
        contacts[choice]["address"] = input("New Address: ")

        print(" Contact updated successfully!")
    else:
        print(" Invalid selection.")


def delete_contact():
    view_contacts()
    if not contacts:
        return

    choice = int(input("\nEnter contact number to delete: ")) - 1

    if 0 <= choice < len(contacts):
        deleted = contacts.pop(choice)
        print(f"{deleted['name']} deleted successfully!")
    else:
        print("Invalid selection.")


def main_menu():
    while True:
        print("Contact Management System\n")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("done.")
            break
        else:
            print("Please enter a valid option.")

main_menu()
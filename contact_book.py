import os

CONTACT_FILE = "contacts.txt"

def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, "r") as file:
        lines = file.readlines()
    contacts = [line.strip().split("|") for line in lines]
    return contacts

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        for contact in contacts:
            file.write("|".join(contact) + "\n")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts = load_contacts()
    contacts.append([name, phone, email, address])
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    print("Contacts List:")
    for contact in contacts:
        print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if search_term in contact[0] or search_term in contact[1]:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
            found = True
    if not found:
        print("No contacts found.")

def update_contact():
    search_term = input("Enter name or phone number to search for update: ")
    contacts = load_contacts()
    updated_contacts = []
    found = False
    for contact in contacts:
        if search_term in contact[0] or search_term in contact[1]:
            found = True
            print(f"Current details - Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}, Address: {contact[3]}")
            name = input("Enter new Name (leave blank to keep current): ") or contact[0]
            phone = input("Enter new Phone Number (leave blank to keep current): ") or contact[1]
            email = input("Enter new Email (leave blank to keep current): ") or contact[2]
            address = input("Enter new Address (leave blank to keep current): ") or contact[3]
            updated_contacts.append([name, phone, email, address])
        else:
            updated_contacts.append(contact)
    if found:
        save_contacts(updated_contacts)
        print("Contact updated successfully!")
    else:
        print("No contacts found.")

def delete_contact():
    search_term = input("Enter name or phone number to delete: ")
    contacts = load_contacts()
    updated_contacts = [contact for contact in contacts if search_term not in contact[0] and search_term not in contact[1]]
    if len(updated_contacts) < len(contacts):
        save_contacts(updated_contacts)
        print("Contact deleted successfully!")
    else:
        print("No contacts found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

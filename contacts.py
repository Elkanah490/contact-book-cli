
FILENAME = "contacts.txt"
contacts = []

def load_contacts():
    contacts = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line=line.strip()
                if line:
                    name, phone, email=line.split("|")
                    contacts.append({"name": name, "phone": phone, "email": email})

    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        for contact in contacts:
            line=f"{contact['name']}|{contact["phone"]}|{contact["email"]} \n"
            f.write(line)


def add_contact(contacts):
    print("\n--- Add Contact ---")
    name=input("Name: ").strip()
    phone=input("Phone: ").strip()
    email=input("Email: ").strip()

    if not name:
        print("Name cannot be empty.")
        return
    
    contacts.append({"name": name, "phone": phone, "email":email })
    save_contacts(contacts)
    print(f"Contact '{name}' added succesfully.")

def view_contacts(contacts):
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts saved yet.")
        return
        
    for i, contact in enumerate(contacts):
            print(f"{i + 1}.{contact['name']}")
            print(f" Phone : {contact['phone']}")
            print(f" Email : {contact['email']}")
            print()


def find_contact(contacts, name):
    name = name.lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            return contact
    return None

def search_contact(contacts):
    print("\n --- Search Contact ---")
    name=input("Enter name to search: ").strip()
    contact=find_contact(contacts,name)

    if contact:
        print(f"\nFound:")
        print(f"  Name  : {contact['name']}")
        print(f"  Phone : {contact['phone']}")
        print(f"  Email : {contact['email']}")

    else:
        print(f"No contact found with name '{name}'.")

def delete_contact(contacts):
    print("\n--- Delete Contact ---")
    name = input("Enter name to delete: ").strip()
    contact = find_contact(contacts, name)

    if contact:
        contacts.remove(contact)
        save_contacts(contacts)
        print(f"Contact '{contact['name']}' deleted.")
    else:
        print(f"No contact found with name '{name}'.")

def update_contact(contacts):
    print("\n --- Update Contact ---")
    name = input("Enter name of contact to update: ").strip()
    contact=find_contact(contacts, name) 

    if not contact:
        print(f"No contact found with name '{name}' ") 
        return  
    print(f"Updating '{contact['name']}' — press Enter to keep current value.")

    new_name = input(f"  Name  [{contact['name']}]: ").strip()
    new_phone = input(f"  Phone [{contact['phone']}]: ").strip()
    new_email = input(f"  Email [{contact['email']}]: ").strip()

    if new_name:
        contact["name"] = new_name
    if new_phone:
        contact["phone"] = new_phone
    if new_email:
        contact["email"] = new_email

    save_contacts(contacts)
    print("Contact updated successfully.")


def show_menu():
    print("\n========== CONTACT BOOK ==========")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    print("==================================")

def main():
    contacts=load_contacts()
    print(f"Loaded {len(contacts)} contacts.")

    while True:
        show_menu()
        choice = input("Choose an option(1-6): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()

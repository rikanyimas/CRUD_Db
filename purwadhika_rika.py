data_store =  [{"id": '1', 
                "name": 'rika', 
                "age": '12', 
                "email": 'rika@gmail.com', 
                "phone": '098765'}]
next_id = 3 
def create(name, age, email, phone):
    global next_id
    data_store.append({"id": next_id, "name": name, "age": age, "email": email, "phone": phone})
    print(f"Record added with ID: {next_id}")
    next_id += 2

def read(record_id=None):
    if record_id:
        for record in data_store:
            if record["id"] == record_id:
                return record
        return "Record not found."
    return data_store

def update(record_id, updated_data):
    for record in data_store:
        if record["id"] == record_id:
            record.update(updated_data)
            return f"Record with ID {record_id} updated."
    return "Record not found."

def delete(record_id):
    # Find the record
    for i, record in enumerate(data_store):
        if record["id"] == record_id:
            # Ask for confirmation
            confirmation = input(f"Are you sure you want to delete the record with ID {record_id}? (yes/no): ").lower()
            if confirmation == 'yes':
                del data_store[i]
                print(f"Record with ID {record_id} deleted.")
                return True
            else:
                print("Deletion cancelled.")
                return False

    print("Record not found.")
    return False
#1 DEFINE MENU 
def menu():
    while True:
        print("\n--- Welcome to RS Peony Patient Database, Please input your request  ---")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            while True:
                print("\n--- Choose your option ---")
                print("1. Create data")
                print("2. Back to main menu")
                read_choice = input("Enter your choice (1-2): ")

                if read_choice == '1':
                    name = input("Enter name: ")
                    age = input("Enter age: ")
                    email = input("Enter email: ")
                    phone = input("Enter phone: ")
                    create(name, age, email, phone)
                
                elif read_choice == '2':
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 2.")

        elif choice == '2':
            while True:
                print("\n--- Choose your option ---")
                print("1. Read all data")
                print("2. Read specific data")
                print("3. Back to main menu")
                read_choice = input("Enter your choice (1-3): ")

                if read_choice == '1':
                    print(read())

                elif read_choice == '2':
                    record_id = input("Enter record ID to read: ")
                    record_id = record_id if record_id.isdigit() else None
                    if record_id:
                        print(read(record_id))
                    else:
                        print("Invalid ID.")

                elif read_choice == '3':
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 to 3.")

        elif choice == '3':
            record_id = int(input("Enter ID to update: "))
            print("Enter new values (leave blank to keep current value):")
            name = input("New name: ")
            age = input("New age: ")
            email = input("New email: ")
            phone = input("New phone: ")
            updated_data = {"name": name, "age": age, "email": email, "phone": phone}
            # Removing empty entries from updated_data
            updated_data = {k: v for k, v in updated_data.items() if v}
            print(update(record_id, updated_data))

        elif choice == '4':
            record_id = int(input("Enter record ID to delete: "))
            delete(record_id)

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 to 5.")


menu()
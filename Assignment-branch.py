# user_menu.py

def get_user_info():
    try:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        school = input("Enter your school: ")

        with open("user_data.txt", "w") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"School: {school}\n")

        print("User information has been saved.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    while True:
        print("User Information App Menu:")
        print("1. Enter User Information")
        print("2. Exit")

        choice = input("Select an option (1/2): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()

# user_info_extended.py

def get_user_info():
    try:

        nationality = input("Enter your nationality: ")
        home_address = input("Enter your home address: ")
        telephone_number = input("Enter your telephone number: ")
        occupation = input("Enter your occupation: ")

        with open("user_data.txt", "w") as file:

            file.write(f"Nationality: {nationality}\n")
            file.write(f"Home Address: {home_address}\n")
            file.write(f"Telephone Number: {telephone_number}\n")
            file.write(f"Occupation: {occupation}\n")

        print("User information has been saved.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main_menu():
    while True:
        print("User Information App Menu:")
        print("1. Enter User Information")
        print("2. Exit")

        choice = input("Select an option (Yes/NO): ")

        if choice == "Yes":
            get_user_info()
        elif choice == "NO":
            print("Thank you for your answer. SEE YOU!")
            break
        else:
            print("Invalid, Please try again.")

if __name__ == "__main__":
    main_menu()

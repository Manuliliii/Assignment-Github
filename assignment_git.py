# main.py

def main():
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

if __name__ == "__main__":
    main()

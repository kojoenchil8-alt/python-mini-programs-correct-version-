def show_menu():
    print("Menu:")
    print("1. Rock, Paper, Scissors")
    print("2. Random Password Generator")
    print("3. How to Use")
    print("4. Quit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Launching Rock Paper Scissors...")
        elif choice == "2":
            print("Launching Random Password Generator...")
        elif choice == "3":
            print("Launching How to Use...")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
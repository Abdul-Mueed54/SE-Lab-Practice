students = {}

def show_menu():
    print("\n=== Grade Book ===")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("GoodBye!")
            break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()

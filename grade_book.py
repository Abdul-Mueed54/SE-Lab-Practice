students = {}

def show_menu():
    print("\n=== Grade Book ===")
    print("0. Exit")
    print("1. Calculate Grade")

def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 55:
            return "C"
    elif average >= 40:
            return "D"
    return "F"

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "0":
            print("GoodBye!")
            break
        elif choice == "1":
             Average = int(input("Enter Average Marks out of 100:"))
             print("Grade:", calculate_grade(Average))
             break
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()

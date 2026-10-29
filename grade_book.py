students = {}

def show_menu():
    print("\n=== Grade Book ===")
    print("1. Calculate Grade ")
    print("2. Add student")
    print("0. Exit")

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

def add_student(): 
    name = input("Student name: ") 
    marks = input("Marks separated by spaces-: ") 
    students[name] = [int(m) for m in marks.split()] 
    print(f"Added {name}.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("GoodBye!")
            break
        elif choice == "1":
             Average = int(input("Please enter Average marks out of 100:"))
             print("Grade: ", calculate_grade(Average))
             break
        elif choice == "2": 
            add_student()
        else:
            print("Invalid Option.")

if __name__ == "__main__":
    main()

import os
doc_path = os.path.expanduser('~/Documents')

while True:
    print("==== Student Records ====")
    print("1. Register Student")
    print("2. Open Student Records")
    print("3. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

    except ValueError as e:
        print("Invalid input. Please enter an integer (1-3).")
        continue

    if choice == 1:
        print("\n=== Register Student ===")
        
        while True:
            try:
                student_id = int(input("Enter Student ID: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for Student ID.")
        
        fullName = input("Enter Student's Full Name: ")
        program = input("Enter Student Program: ")

        while True:
            try:
                age = int(input("Enter Student's Age: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for Age.")

        gender = input("Enter Student's Gender: ")
        bday = input("Enter Student's Birthday (MM/DD/YYYY): ")

        while True:
            try:
                contactNum = int(input("Enter Student's Contact Number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for Contact Number.")
        
        data = [f"Student No.: {student_id}",
                f"Full Name: {fullName}",
                f"Age: {age}",
                f"Program: {program}",
                f"Gender: {gender}",
                f"Birthday: {bday}",
                f"Contact Number: {contactNum}"]
        
        file_path = os.path.join(doc_path, f"{student_id}.txt")

        with open(file_path, "w") as f:
            for line in data:
                f.write(line + "\n")
        
        print(f"Student record for ID {student_id} has been saved.\n")

    elif choice == 2:
        print("=== Search Student Record ===")

        try:
            student_id = int(input("Enter Student No.: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for Student ID.")
            continue


        file_path = os.path.join(doc_path, f"{student_id}.txt")


        try:
            with open(file_path, "r") as f:
                record = f.readlines()
                print(f"\n--- Student Record for ID {student_id} ---")
                for line in record:
                    print(line.strip())
                    print("------------------------------")
        
        except FileNotFoundError:
            print(f"File for Student ID {student_id} not found.")
    
    elif choice == 3:
        print("Thank you for using the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-3).")

Choice = "Y"

while Choice.upper() == "Y":

    student_name = input("Enter student name: ")

    mark1 = float(input("Enter Mark 1: "))
    mark2 = float(input("Enter Mark 2: "))
    mark3 = float(input("Enter Mark 3: "))

    average = (mark1 + mark2 + mark3) / 3

    print("\nStudent Name:", student_name)
    print("Average Mark:", round(average, 2))

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    Choice = input("\nEnter another student? (Y/N): ").strip().upper()

print("Program Ended.")

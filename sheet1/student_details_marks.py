def display_student_details():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    
    total = sum(marks)
    average = total / len(marks)
    
    print("\n--- Student Mark List ---")
    print(f"Name: {name}")
    print(f"Roll No: {roll_no}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")

if __name__ == "__main__":
    display_student_details()

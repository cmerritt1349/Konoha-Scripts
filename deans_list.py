# Name: Casey Merritt
# File: deans_list.py
# Description: This app accepts student names and GPAs and determines
#              whether each student qualifies for the Dean's List
#              or the Honor Roll. The program continues
#              accepting students until 'ZZZ' is entered as the last name.

while True:
    # Ask for last name
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

    # Quit if last name is ZZZ
    if last_name == 'ZZZ':
        print("Exiting program. Goodbye!")
        break 

    # Ask for first name and GPA
    first_name = input("Enter student's first name: ")   
    gpa = float(input("Enter student's GPA: ")) 

    # Test GPA and print result
    if gpa >= 3.5:
        print(f"{first_name} {last_name} with a {gpa} GPA has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} with a {gpa} GPA has made the Honor Roll!")
    else: 
        print(f"{first_name} {last_name} with a {gpa} GPA did not qualify for the Dean's List or Honor Roll.")

    print() # blank line between students
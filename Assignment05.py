# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Andy Sul,11/11/2024, Modified script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            first_name, last_name, course = line.strip().split(',')
            student_data = {"first_name": first_name, "last_name": last_name, "course_name": course}
            students.append(student_data)
except FileNotFoundError:
    print("No previous enrollment data found. A new file will be created.")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Input first name
            while True:
                student_first_name = input("Enter the student first name: ")
                if not student_first_name:
                        raise ValueError("Student First Name cannot be empty.")
                break

            # Input last name
            while True:
                student_last_name = input("Enter the student last name: ")
                if not student_last_name:
                    raise ValueError("Student Last Name cannot be empty.")
                break

            # Input the course name
            course_name = input("Enter the course name: ")

            # Store the student data in a dictionary
            student_data = {"first_name": student_first_name, "last_name": student_last_name, "course_name": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course_name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                for student in students:
                    csv_data = f"{student['first_name']}, {student['last_name']}, {student['course_name']}\n"
                    file.write(csv_data)
                print("The data has been successfully saved to the file.")
        except IOError as e:
            print(f"Error writing to file: {e}")

    # Stop the loop
    elif menu_choice == "4":
        print("Exiting the program...")
        break # Exits the while loop and ends the program

print("Program Ended")

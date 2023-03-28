# Write a Python program to perform the above task. Get the name, age and training location from
# the user and store this information into a list of dictionaries with the keys - 'Name' , 'Age' and
# 'Location'. Also display the name of the students in a particular training location while entering
# the desired training location. Refer the sample input and output for more clarifications.
# Note :
# If the no. of student details to be created is entered as zero or negative number, then display the
# message "Invalid Input" and terminate the program.
# If the age of the student entered is <=10 and>20, display "Invalid Input" and terminate the
# program.
# If you enter the training location to find out the student is not in the existing list of dictionaries,
# then display the message "Invalid location " and terminate the program


# Create an empty list to store student details
students = []

# Get the number of student details to be created from the user
students_num = int(input("Enter the number of student details to be created: "))

# Check if the number of student details is valid
if students_num <= 0:
    print("Invalid Input")
    exit()

# Loop through and get the student details from the user
for i in range(students_num):        
    name = input(f'Enter {i+1} Student name: ')
    age = int(input('Enter the age: '))
    location = input('Enter Student location: ')

# Check if the age is valid
    if age <= 10 or age >20:
        print("Invalid Input")
        exit()
    student = {}

    # Create a dictionary with the student details and add it to the list
    student['name'] = name
    student['age'] = age
    student['location'] = location
    students.append(student)

# Get the desired training location from the user

filter_location = input("\nEnter the training location to find the students: ")

# Loop through the students and display the names of the students in the desired training location
found = False
for student in students:
    if student["location"] == filter_location:
        found = True
        print(student["name"])

# Check if the location was found
if not found:
    print("Invalid location")


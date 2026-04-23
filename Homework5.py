
#Unit 1 Beginner
# Create your RGB color tuple here
RGB_tuple = (0, 0, 0)

# Print each color channel
print(RGB_tuple[0])
print(RGB_tuple[1])
print(RGB_tuple[2])

# Create palette list and add color
palette = [RGB_tuple]

# Print the palette
print(palette)

#Intermediate
# Create student tuples
student1 = ("Bob", 93, 19)
student2 = ("Kevin", 74, 20)
student3 = ("Lisa", 79, 18)
# Store in classroom list
classroom = [student1, student2, student3]

# Print second student's name using double subscripting
print(classroom[1][0])

# Unpack first student's information
name1 = classroom[0][0]
grade1 = classroom[0][1]
age1 = classroom[0][2]

# Print formatted message
print(f"Name: {name1}, Grade: {grade1}, Age: {age1}")

#Advanced
# Create original student tuple
studentOriginal = ("Jim", [80, 85, 90], 85)
student = ("Jim", [80, 85, 90], 85)

# Add fourth exam score
student[1].append(68)

# Calculate new average
additiveGrade = 0
for grade in student[1]:
    additiveGrade += grade
finalGrade = additiveGrade / len(student[1])

# Create new tuple with updated final grade
studentUpdated = ("Jim", student[1], finalGrade)

# Print both tuples
print(studentOriginal)
print(studentUpdated)

#Unit 2 Beginner
homework_grades = [90, 87, 89]
date = (4, 20, 2026)

def boost_grades(grades_list):
    i = 0
    for grade in grades_list:
        grades_list[i] += 5
        print(f"test {grades_list}")
        i += 1
    return grades_list

print(boost_grades(homework_grades)) #We use a list for grades because the amount of grades can be added or subtracted and a tuple for date because dates only consist of 3 variables which are month, day, and year
    
#Intermediate
def find_range(*args):
    smallest = args[0]
    largest = args[0]
    
    for i in args:
        if i < smallest:
            smallest = i
    
    for i in args:
        if i > largest:
            largest = i
    
    range = (smallest, largest)
    return range

test_scores3 = [34, 86, 17]
test_scores7 = [34, 86, 17, 57, 97, 26]

print(find_range(*test_scores3))
print(find_range(*test_scores7))

test_scores = [78, 92, 85, 88, 91]
print(find_range(*test_scores))

#Advanced
student_list = [("Jimbo", 56), ("Marie", 89), ("Steve", 76)]

def calculate_statistics(*args):
    count = 0
    sum = 0
    for grade in range(len(student_list)):
        count += 1
        sum += student_list[grade][1]
    average = sum / len(student_list)
    statistics = (count, sum, average)
    return statistics

def update_student_records(student_list, bonus):
    new_student_list = []
    grades = []
    for student in range(len(student_list)):
        grades.append(student_list[student][1])
    stats = calculate_statistics(grades)
    for student in range(len(student_list)):
        if grades[student] <= stats[2]:
            new_student_tuple = (student_list[student][0], grades[student] + bonus)
            new_student_list.append(new_student_tuple)
        else:
            new_student_list.append(student_list[student])
    print(new_student_list)

update_student_records(student_list, 5)

#Unit 3 Beginner
nested_list = [
                [1, 2, 3], 
                [4, 5, 6,], 
                [7, 8, 9,]
]
print(nested_list)
print(nested_list[1][1])
for i in range(len(nested_list)):
    for j in range(len(nested_list)):
        print(f"{nested_list[i][j]}", end="")
    print("")
    
#Intermediate
student_grades = [45, 78, 92, 61, 88, 73, 55, 90, 82]
passing_grades = [g for g in student_grades if g >= 60]
print(passing_grades)
letter_grades = ["A" for p in passing_grades if p >= 90]
letter_grades += ("B" for p in passing_grades if p >= 80 and p < 90)
letter_grades += ("C" for p in passing_grades if p >= 70 and p < 80)
letter_grades += ("D" for p in passing_grades if p >= 60 and p < 70)
print(letter_grades)

#Advanced
mult_table = [[i * j for j in range(1, 5)] for i in range(1, 5)]
for row in mult_table:
    print(row)
    
def sum_diagonal():
    squares_old = []
    for x in range(1, 5):
        squares_old.append(x ** 2)
    return(squares_old)

print("")
print(sum_diagonal())
evens_gen = (x**2 for x in range(10))
for i in range(1, 6):
    print(next(evens_gen))
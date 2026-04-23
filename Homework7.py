"""
Student Grade Tracker
CS 1300 — Lecture 5 Mini-Project

A modular, well-tested program that collects exam scores,
calculates a letter grade and academic standing, and
displays a formatted report.
"""

#averages grades, returs scores, and prints reciept
def bad_grade_tracker():
    name = input("Student name: ")
    scores = []
    for i in range(3): #gets score
        s = int(input(f"Exam {i+1} score: "))
        if s < 0 or s > 100:
            print("Invalid!")
            return
        scores.append(s)
    avg = sum(scores) / len(scores)
    if avg >= 90: grade = "A" #determines letter grade
    elif avg >= 80: grade = "B"
    elif avg >= 70: grade = "C"
    elif avg >= 60: grade = "D"
    else: grade = "F"
    if avg >= 90: standing = "Dean's List"
    elif avg >= 70: standing = "Good Standing"
    elif avg >= 60: standing = "Academic Probation"
    else: standing = "Academic Warning"
    print("=" * 30) #prints reciept
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print("=" * 30)
    

# Step 1: Get student name
def get_student_name(): #gets student name
    name = input("Student name: ")
    return name #returns student name
    
 
 #gets student scores
def get_student_scores(): #optains input scores here
    scores = []
    for i in range(3): #gets score
        s = int(input(f"Exam {i+1} score: "))
        score_is_valid(s)
        scores.append(s)
    return scores #returns scores for use in other methods
    
    
# Step 2: Calculate letter grade
def calculate_letter_grade(avg): #calculates letter grade from average
    if avg >= 90: grade = "A"
    elif avg >= 80: grade = "B"
    elif avg >= 70: grade = "C"
    elif avg >= 60: grade = "D"
    else: grade = "F"
    return grade #returns letter grade 
  
#calculates standing
def calculate_standing(avg): #calculates academic standing from average grade
    if avg >= 90: standing = "Dean's List"
    elif avg >= 70: standing = "Good Standing"
    elif avg >= 60: standing = "Academic Probation"
    else: standing = "Academic Warning"
    return standing #returns academic standing
    
    
# Step 3: Display report
def display_report(name, scores, avg, grade, standing): #displays information in an organized way
    print_divider()
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print_divider()

def print_divider(): #prints divider
    print("=" * 30)

def score_is_valid(s): #tests if previously inputted scaore is valid
    if s < 0 or s > 100:
        print("Invalid!")
        return
    

def calculate_average(scores): #Calculates average of the previously inputted scores
    avg = sum(scores) / len(scores)
    return avg #Returns the average

def main(): #main program/all functions put together
    name = get_student_name()
    scores = get_student_scores()
    avg = calculate_average(scores)
    grade = calculate_letter_grade(avg)
    standing = calculate_standing(avg)
    display_report(name, scores, avg, grade, standing)
    
def test_grade_tracker(): #tests grade tracker
    ave_expected = 85
    test_scores = [80, 85, 90]
    grade_expected = "B"
    standing_expected = "Good Standing"
    
    ave_test = calculate_average(test_scores)
    grade_test = grade = calculate_letter_grade(ave_test)
    standing_test = calculate_standing(ave_test)
    
    if ave_expected == ave_test:
        print("Average test Passed")
    else:
        print("Average test failed")
    
    if grade_expected == grade_test:
        print("Grade test Passed")
    else:
        print("Grade test failed")
        
    if standing_expected == standing_test:
        print("Standing test Passed")
    else:
        print("Standing test failed")
    
    
    
    
    
main()

print("\n Tests:")
test_grade_tracker()
    

# Create stubs for each function your main() calls.
# Example:
# def get_student_name():
# pass
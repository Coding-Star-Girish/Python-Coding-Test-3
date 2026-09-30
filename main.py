grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Ethan": 88
}


total_score = 0
for name in grade_book:
    total_score += grade_book[name]

class_average = total_score / len(grade_book)
print(f"Class Average: {class_average:.2f}")


top_student = max(grade_book, key=grade_book.get)
top_score = grade_book[top_student]

bottom_student = min(grade_book, key=grade_book.get)
bottom_score = grade_book[bottom_student]

print(f"Top Scorer: {top_student} with a score of {top_score}")
print(f"Bottom Scorer: {bottom_student} with a score of {bottom_score}")
print("-" * 40)


search_name = input("Enter the student name you want to look up: ")


student_grade = grade_book.get(search_name)

if student_grade is not None:
    print(f"✨ {search_name}'s grade is {student_grade}.")
else:
    print(f"Sorry, '{search_name}' was not found in the grade book.")

# 1. Write a program of  5 students in dictionary with 3 subjects each.
student_marks = {
    'Eloise': [95, 88, 92],
    'Bethany': [70, 65, 78],
    'Racie': [55, 60, 45],
    'George': [85, 90, 88],
    'Eve': [99, 98, 100]
}

def calculate_avg_and_grade(marks):
    results = {}
    for name, subjects in marks.items():
        avg = sum(subjects) / len(subjects)
        # Use proper comparison operators (>=)
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "Fail!!!!"
        results[name] = {'avg': avg, 'grade': grade}
    # Return *after* processing all students
    return results

# Compute results
student_results = calculate_avg_and_grade(student_marks)

print('Student results:')
for name, data in student_results.items():
    print(f"Name: {name}, Average: {data['avg']:.2f}, Grade: {data['grade']}")

# Find top scorer by average
top_scorer_name = max(student_results, key=lambda n: student_results[n]['avg'])
top_scorer_average = student_results[top_scorer_name]['avg']

print(f"\nTop scorer: {top_scorer_name} with average marks {top_scorer_average:.2f}")


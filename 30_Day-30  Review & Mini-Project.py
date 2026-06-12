import csv

def save_grades(students, filename="grades.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Math", "Science", "Average"])
        for name, scores in students.items():
            avg = sum(scores) / len(scores)
            # Fix: Extract math score (index 0) and science score (index 1)
            writer.writerow([name, scores[0], scores[1], f"{avg:.2f}"])
    print(f"Data successfully saved to {filename}")

# Filled with test scores: [Math, Science]
student_data = {
    "Alice": [85, 92],
    "Bob": [78, 81],
    "Charlie": [95, 89]
}

save_grades(student_data)

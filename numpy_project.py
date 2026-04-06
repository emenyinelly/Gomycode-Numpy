import numpy as np

# ── Instruction 2: get number of students and subjects ───────────────────────

while True:
    try:
        num_students = int(input("Enter the number of students: "))
        num_subjects = int(input("Enter the number of subjects:  "))
        if num_students <= 0 or num_subjects <= 0:
            print("Both values must be greater than zero.\n")
            continue
        break
    except ValueError:
        print("Please enter whole numbers only.\n")

# ── Instruction 3: create the marks array (students × subjects) ──────────────

marks = np.zeros((num_students, num_subjects), dtype=float)

# ── Instruction 4: fill in each student's marks ──────────────────────────────

student_names = []

print()
for i in range(num_students):
    name = input(f"Enter name for Student {i + 1}: ").strip()
    student_names.append(name if name else f"Student {i + 1}")

    for j in range(num_subjects):
        while True:
            try:
                mark = float(input(f"  Subject {j + 1} marks (0–100): "))
                if 0 <= mark <= 100:
                    marks[i][j] = mark
                    break
                else:
                    print("  Marks must be between 0 and 100.")
            except ValueError:
                print("  Please enter a valid number.")
    print()

# ── Instruction 5: total marks per student ───────────────────────────────────

totals = np.sum(marks, axis=1)           # sum across subjects for each student

# ── Instruction 6: percentage per student ────────────────────────────────────

max_marks = num_subjects * 100
percentages = (totals / max_marks) * 100

# ── Instruction 7: grade per student ─────────────────────────────────────────

def get_grade(percentage: float) -> str:
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

grades = [get_grade(p) for p in percentages]

# ── Instruction 8: display results in tabular format ─────────────────────────

col_name       = 18
col_total      = 10
col_percentage = 12
col_grade      = 6
line_width     = col_name + col_total + col_percentage + col_grade + 3

print("=" * line_width)
print(
    f"{'Student':<{col_name}}"
    f"{'Total':>{col_total}}"
    f"{'Percentage':>{col_percentage}}"
    f"{'Grade':>{col_grade}}"
)
print("=" * line_width)

for i in range(num_students):
    print(
        f"{student_names[i]:<{col_name}}"
        f"{totals[i]:>{col_total}.1f}"
        f"{percentages[i]:>{col_percentage}.2f}%"
        f"{grades[i]:>{col_grade}}"
    )

print("=" * line_width)

# ── Summary statistics using NumPy ───────────────────────────────────────────

print(f"\n{'Class Summary':}")
print(f"  Highest percentage : {np.max(percentages):.2f}%  ({student_names[np.argmax(percentages)]})")
print(f"  Lowest  percentage : {np.min(percentages):.2f}%  ({student_names[np.argmin(percentages)]})")
print(f"  Class average      : {np.mean(percentages):.2f}%")
print(f"  Passed (>= 50%)    : {np.sum(percentages >= 50)} student(s)")
print(f"  Failed  (< 50%)    : {np.sum(percentages < 50)} student(s)")
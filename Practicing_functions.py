students = ["Ali", "Buse", "Can", "Derin", "Ece", "Fatih", "Gül"]
scores   = [72, 45, 88, 91, 60, 34, 77]
#Write get_grade(score) — returns "A" (≥90), "B" (≥75), "C" (≥60), or "F" (below 60)

def get_grade(score):   
        if score >= 90: return 'A'
        elif score >= 75: return 'B'
        elif score >= 60 : return 'C'
        else: return 'F'
#Write format_report(name, score) — returns a string like "Ali | 72 | C" using get_grade() inside it
def format_report(name, score):
            return f"{name} | {score} | {get_grade(score)}"
#Write print_all_reports(students, scores) — loops through both lists and prints every student's report
def print_all_reports(students, scores):
    for s, sc in zip(students, scores):
        print(format_report(s, sc))
#Write class_summary(scores) — returns the average (rounded to 1dp), the highest score, and the lowest score as three separate values
def class_summary(scores):
    avg = round(sum(scores)/len(scores),1)
    highest = max(scores)
    lowest = min(scores)
    return avg, highest, lowest
#Write get_failing(students, scores) — returns a list of names of students who got an F, using get_grade() inside it
def get_failing(students, scores):
    failing = []
    for s, sc in zip(students, scores):
        if get_grade(sc) =='F':
            failing.append(s)
    return failing

print_all_reports(students, scores)
avg, highest, lowest = class_summary(scores)
print(f"Average: {avg} | Highest{highest} | Lowest{lowest}")
print(f"Failing: {get_failing(students, scores)}")
    
my_exams = {'Maths': 89, 'Turkish':98}
def calculate_average(scores_dict):
    total_sum = 0
    for score in scores_dict.values():
        total_sum += score
    average = total_sum /len(scores_dict)
    if average >=90:
        print("Simon, You are a genius!!")
    elif average >=70:
        print("Thats solid, Keep working!")
    else:
        print("Its time to hit the books Buddy!")
    return average
print(calculate_average(my_exams))

with open("results.txt", "w") as file:
    for subject, score in my_exams.items():
        file.write(f"{subject}:{score}\n")
try:
    with open("results.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Whoops, The file is doesn't exist")
#HAVING USER INPUT
while True:
    new_subject = input("Enter the subject name :")
    if new_subject == "quit":
        break    
    new_score = int(input("Enter the score :"))
    with open("results.txt","a") as file:
        file.write(f"{new_subject}:{new_score}\n")
print("New records saved")
all_scores ={}
with open("results.txt","r") as file:
    for line in file:
        name, score = line.strip().split(":")
        all_scores[name] = int(score)
final_average = calculate_average(all_scores)
print(f"Your Final Grade is {final_average}")

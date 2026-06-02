# ============================================================
# DATE    : 31 May 2026
# TOPIC   : Python Loops
# LEARNED : Difference between break and continue.
#           range(i+1, len()) trick to avoid duplicate pairs.
#           Print before doubling in a while loop.
# SKILLS  : for, while, break, continue, nested loops
#1. I fixed a bug where I was using a tuple (1,4 ) in a loop instead of using a range(1,4) to iterate between 1 to 4. 
#2. Using the while loop to print doubled numbers, I was doubling the value before printing leading to an overrage , by shifting the print statement, I managed to correct the error.
#3. In order to get pairs of numbers in a list that add to a specific value, I used nested for loops, where I learnt that using range(i+j, len(LIST)) helps me iterate through the numbers once to avoid same pairs but in different order. meaning j always stays ahead of i.
# ============================================================
numbers = [4, 17, 3, 29, 8, 42, 15, 7, 23, 11, 36, 2, 19, 50, 6]
# Use a for loop to print every number and its square side by side, e.g. 4 → 16
for number in numbers:
    print(f"{number} → {number**2}")
#Use a while loop to keep doubling a starting value of 1 until it exceeds 100. Print each doubled value
value = 1
while value <=100:
    print(value)
    value*=2
#Loop through numbers and use continue to skip multiples of 3. Print the rest.
for number in numbers:
    if number %3==0:
        continue
    print(number)

#Loop through numbers and use break to stop the moment you hit a number greater than 40. Print everything up to (not including) that number.
for number in numbers:
    if number >40:
        break
    print(number)

#Use nested loops to find every pair (a, b) from the list where a + b == 25. Print each pair once.
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == 25:
            print(numbers[i], numbers[j])


    

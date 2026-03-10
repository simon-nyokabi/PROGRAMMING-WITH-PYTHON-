def number_pattern(n):
    # I check for integer:
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    #We need positive values only
    if n < 1 :
        return 'Argument must be an integer greater than 0.'
# Assigning result to an empty string
    result = ''
    # Get the required numbers, remember the last is included.
    for numbers in range(1, n+1):
        result += str(numbers) + ' '
    #Get the return, strip to remove the additional spaces,.
    return result.strip()
print(number_pattern(4)) #Test data
print(number_pattern(12))



    


    
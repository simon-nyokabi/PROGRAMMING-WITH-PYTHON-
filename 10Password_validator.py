#defining the function
def password_check(password):

    missing_requirements = []
    #checkking the lengh 
    length_enough = len(password) >= 8
    #checking the presence of numbers
    has_digit = any([char.isdigit() for char in password])

    #checking uppercases
    has_upper = any([char.isupper() for char in password])

    #checking for special characters
    special_chars = '!@#$%^&*'
    has_special_char = any([char in special_chars for char in password])
    #checking for spaces

    # I need to tell the user where their errors are 
   
    if ' ' in password:
        missing_requirements.append('Password cannot have spaces')
            
    if not length_enough :
        missing_requirements.append('Password is too short')
        
    if not has_digit:
        missing_requirements.append('Password must have a digit(0-9)')
        
    if not has_upper:
        missing_requirements.append('Password must have an uppercase')
       
    if not has_special_char:
        missing_requirements.append('Password must have a special character')
    
       
    if not missing_requirements:
        return 'Strong pasword'
    else:
        return f'Weak password. {', '.join(missing_requirements)}' #join makes the output readable for the user
if __name__ == "__main__":  
    my_pass=input('Enter your password: ')
    print(password_check(my_pass))


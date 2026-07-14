#function to evaluate the strength of a password
def check_password_strength(password):  
    if not password:
        print("Password cannot be empty.")
        return 
    #list to store validation message
    errors = []   

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    #initialize password strength score
    score = 0

    #allowed special character
    special_characters = "!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"
    
    #check each character in the password
    for char in password:
        if char.isupper(): #check the given password has at least one uppercase letter
            has_upper = True 
        if char.islower(): #check the given password has at least one lowercase letter
            has_lower = True
        if char.isdigit(): #check the given password has at least one digit
            has_digit = True
        if char in special_characters: #check the given password has at least one special character
            has_special = True
    
    #calculate and store password strength
    if len(password) >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    #add validation message for missing requirements
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not has_upper:
        errors.append("Add at least one uppercase letter.")
    if not has_lower:
        errors.append("Add at least one lowercase letter.")
    if not has_digit:
        errors.append("Add at least one digit.")
    if not has_special:
        errors.append("Add at least one special character.")
    
    #display password strength and suggestion
    print(f"Password Score: {score}/5")
    if score == 5:
        print("Strong Password.")
    elif score >= 3:
        print("Medium Password.\nSuggestions:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Weak Password.\nSuggestions:")
        for error in errors:
            print(f"- {error}")

#take the input from the user
password = input("Enter your password: ")
check_password_strength(password) #call the function
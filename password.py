import random as rd

lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nums = ["0","1","2","3","4","5","6","7","8","9"]
special_char = ["@","%","+","/","\ ","'","!","#","$","?",":",".","(",")","{","}","[","]","-","_","."]


def password_lower(digits):
    temp = []

    while len(temp) != digits:
        attempt = rd.choice(lower_case)
        temp.append(attempt)

    joined_password = "".join(temp)
    print(joined_password)

def password_lower_upper(digits):
    # dictionary of the list to be randomly chosen
    m = {0:lower_case, 1:upper_case}
    temp = [] #temporary list to append the digits chose

    while len(temp) != digits:
        list_choice = rd.choice(range(0,2)) #choose the list, then choose a digit from that list
        attempt = rd.choice(m[list_choice])
        temp.append(attempt)

    joined_password = "".join(temp) #Joining the separated values of the temp list
    print(joined_password)


def password_lower_upper_nums(digits):
    m = {0: lower_case, 1: upper_case, 2: nums}
    temp = []

    while len(temp) != digits:
        list_choice = rd.choice(range(0,3))
        attempt = rd.choice(m[list_choice])
        temp.append(attempt)

    joined_password = "".join(temp)
    print(joined_password)


def password_lower_upper_nums_special(digits):
    m = {0: lower_case, 1: upper_case, 2: nums, 3: special_char}
    temp = []

    while len(temp) != digits:
        list_choice = rd.choice(range(0, 4))
        attempt = rd.choice(m[list_choice])
        temp.append(attempt)

    joined_password = "".join(temp)
    print(joined_password)


def create_password():
    #Input prompts
    lower = "To create a password with lower case press 0."
    lower_upper = "To create a password with lower and upper cases press 1."
    lower_upper_nums = "To create a password with numbers, lower and upper cases press 2."
    lower_upper_nums_special = "To create a password with numbers, special characters, lower and upper cases press 3."

    choice = int(input(f"{lower}\n{lower_upper}\n{lower_upper_nums}\n{lower_upper_nums_special}\n ----------"))
    n_digits = int(input(f"\n Enter the length of the password.\n---------"))

    if choice == 0:
        password_lower(n_digits)
    elif choice == 1:
        password_lower_upper(n_digits)
    elif choice == 2:
        password_lower_upper_nums(n_digits)
    elif choice == 3:
        password_lower_upper_nums_special(n_digits)
    else:
        print("Invalid input.")

create_password()

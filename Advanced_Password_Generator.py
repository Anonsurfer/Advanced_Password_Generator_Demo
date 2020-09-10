import time
import os
import sys
def Design():
    os.system('cls')
    print("\t\t\t\tWelcome To Random Password Generator!")
    print("Select anyone of the following options")
    print("1.Generate Random Password with strings Only")
    print("2.Generate Random Password with numbers only")
    print("3.Generate Random Password with strings and number")
    print("4.Read_Me")
    print("5.Exit")
    x = int(input("Choice anyone of the following option:" ))
    if x == 1:
        os.system('cls')
        Generate_Random_Password_With_Strings_Only()
    elif x == 2:
        os.system('cls')
        Generate_Random_Password_With_Integers_Only()
    elif x == 3:
        os.system('cls')
        Generate_Random_Password_With_StringsAndNumbers()
    elif x == 4:
        os.system('cls')
        Read_Me()
    elif x == 5:
        os.system('cls')
        sys.exit()
    else:
        os.system('cls')
        print("You need to choice any one option from 1-5! ")
        print("Try again !")
        print("Sending back To Main Menu........")
        time.sleep(3)
        Design()
def Generate_Random_Password_With_Strings_Only():
    import random
    import string
    random_string = ""
    user_choice = 0
    letters = string.ascii_lowercase
    print("\t\t\t\tWelcome To Random Password Generator!(Strings)")
    print("This section of the generator will generate passwords with only strings")
    print("How many characters do you want in your password ? ")
    user_choice = int(input("Enter the amount of characters you want in your password: "))
    os.system('cls')
    for x in range(user_choice):
        random_string = random_string + random.choice(letters)
    print("Sucessful created a random password with {} characters".format(user_choice))
    print("Password Generated: {}".format(random_string))
    print("Do you want to save this as your password ?")
    print("Type y and hit enter for saving this password in computer")
    print("Type n and hit enter for generating a new password ")
    print("Type 'main' to goto Main-Menu ")
    user_input = input("Enter your choice: ")
    if user_input == "y" or user_input == "Y":
        os.system('cls')
        #Let's write into a file 
        file = open("C:\\Desktop\password.txt",'w') # Change this file path value as per as your desire ;)
        print("Write down the subject for your password like")
        print("Facebook password/Gmail Password/ Yahoo Password etc")
        user_choice = input("Enter your subject for the password: ")
        file.writelines(user_choice)
        file.write('\n')
        file.writelines("Password: " + random_string)
        file.close()
        print("Saved!")
        print("Your password has been saved in file = 'C:\\Users\Admin\Documents\password.txt' ") # Change this file path value as per as your desire ;)
        print("Saved!")
    elif user_input == "n" or user_input == "N":
        os.system('cls')
        print("Sending you back to this page's menu !")
        time.sleep(2)
        Generate_Random_Password_With_Strings_Only()
    elif user_input == "main":
        os.system('cls')
        print("Sending you back to Main_Menu")
        time.sleep(2)
        Design()
    else:
        os.system('cls')
        print("Sorry. We didn't understood you !")
        print("Sending you back to this page's menu")
        time.sleep(2)
        Generate_Random_Password_With_Strings_Only()
def Generate_Random_Password_With_Integers_Only():
    import random
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    random_number = ""
    print("\t\t\t\tWelcome To Random Password Generator!(Numbers)")
    print("This section of the generator will generate passwords with only numbers")
    print("How many characters do you want in your password ? ")
    user_choice = int(input("Enter the amount of characters you want in your password: ")) 
    os.system('cls')
    for x in range(user_choice):
        random_number = random_number + random.choice(numbers)
    print("Sucessful created a random password with {} characters".format(user_choice))
    print("Password Generated: {}".format(random_number))
    print("Do you want to save this as your password ?")
    print("Type y and hit enter for saving this password in computer")
    print("Type n and hit enter for generating a new password ")
    print("Type 'main' and hit enter for going to Menu-Main" )
    user_input = input("Enter your choice: ")
    if user_input == "y" or user_input == "Y":
        os.system('cls')
        #Let's write into a file 
        #file = open("C:\\Desktop\password.txt",'w') # Change this file path value as per as your desire ;) 
        print("Write down the subject for your password like")
        print("Facebook password/Gmail Password/ Yahoo Password etc")
        user_choice = input("Enter your subject for the password: ")
        file.writelines(user_choice)
        file.write('\n')
        file.writelines("Password: " + random_number)
        file.close()
        print("Saved!")
        print("Your password has been saved in file = 'C:\\Users\Admin\Documents\password.txt' ") # Change this file path value as per as your desire ;)
    elif user_input == "n" or user_input == "N":
        os.system('cls')
        print("Sending you back to this page's menu !")
        time.sleep(2)
        Generate_Random_Password_With_Integers_Only()
    elif user_input == "main":
        os.system('cls')
        print("Sending you back to Main_Menu")
        time.sleep(2)
        Design()    
    else:
        os.system('cls')
        print("Sorry. We didn't understood you !")
        print("Sending you back to this page's menu")
        time.sleep(2)
        Generate_Random_Password_With_Integers_Only()

def Generate_Random_Password_With_StringsAndNumbers():    
    import random
    import string
    random_number = ""
    random_string = ""
    user_choice = 0
    letters = string.ascii_lowercase
    numbers_in_list = ["1","2","3","4","5","6","7","8","9","0"]
    print("\t\t\t\tWelcome To Random Password Generator!(Strings and Number)")
    print("This section of the generator will generate passwords with combination of strings and numbers")
    print("How many characters do you want in your password ? ")
    number = int(input("Enter a number: "))
    os.system('cls')
    final_number_mod = number // 2
    addition_number = number - final_number_mod
    for x in range(final_number_mod):
        random_number = random_number + random.choice(numbers_in_list)
    for x in range(addition_number):
        random_string = random_string + random.choice(letters)
        random_string_number = random_string + random_number
    random_string_number_shuffled = ''.join(random.sample(random_string_number,len(random_string_number)))
    print("Sucessful created a random password with {} characters".format(number))
    print("Password Generated: {}".format(random_string_number_shuffled))
    print("Do you want to save this as your password ?")
    print("Type y and hit enter for saving this password in computer")
    print("Type n and hit enter for generating a new password ")
    print("Type 'main' and hit enter for going to main menu")
    user_input = input("Enter your choice: ")
    if user_input == "y" or user_input == "Y":
        os.system('cls')
        #Let's write into a file 
        file = open("C:\\Desktop\password.txt",'w') # Change this file path value as per as your desire ;)
        print("Write down the subject for your password like")
        print("Facebook password/Gmail Password/ Yahoo Password etc")
        user_choice = input("Enter your subject for the password: ")
        file.writelines(user_choice)
        file.write('\n')
        file.writelines("Password: " + random_string)
        file.close()
        print("Saved!")
        print("Your password has been saved in file = 'C:\\Users\Admin\Documents\password.txt' ") # Change this file path value as per as your desire ;)
        print("Saved!")
    elif user_input == "n" or user_input == "N":
        os.system('cls')
        print("Sending you back to this page's menu !")
        time.sleep(2)
        Generate_Random_Password_With_StringsAndNumbers()
    elif user_input == "main":
        os.system('cls')
        print("Sending you back to Main_Menu")
        time.sleep(2)
        Design()
    else:
        os.system('cls')
        print("Sorry. We didn't understood you !")
        print("Sending you back to this page's menu")
        time.sleep(2)
def Read_Me():
    print("\t\t\t\tWelcome To READ-ME")
    print("In this python program users will be able to generate random passwords with as many character's as they want")
    print("There are 3 categories in the this program")
    print("1.User's Will be able to generate passwords only containing strings")
    print("2.User's Will be able to generate passwords only containing numbers")
    print("3.User's will be able to generate passwords contains both strings and numbers")
    print("User's will also be able to save there passwords into a specific location of there computer")
    print("The passwords will be saved in text file ")
    print("I have mentioned the file open function, you just need to change the file location in the file function in the program and replace it with your desired file path !")
    print("Happy coding ;)")
    input()
Design()

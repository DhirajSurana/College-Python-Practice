user_input = input('Enter Your Characters\n')
if(ord(user_input) >= 65 and ord(user_input) <= 90):
    print('Uppercase')
elif(ord(user_input) >= 97 and ord(user_input) <= 122):
    print('Lowercase')
elif(ord(user_input) >= 48 and ord(user_input) <= 57):
    print('Digit')
else:
    print('Special Character')

MAGIC_NUMBER = 44
while True:
    user_unput = int(input('Enter a number: '))
    if user_unput == 44:
        print('perfect!')
        break
    elif user_unput > 44 :
        print('too high!')
    else:
        print('too low!')
Day = input('Day (0-6)?')
Day = int(Day)
if(Day == 0):
    print('Sunday')
elif(Day == 1):
    print('Monday')
elif(Day == 2):
    print('Tuesday')
elif(Day == 3):
    print('Wednesday')
elif(Day == 4):
    print('Thursday')
elif(Day == 5):
    print('Friday')
elif(Day == 6):
    print('Saturday')
else:
    print('not a valid day of the week')
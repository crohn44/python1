Day = input('Day? (Monday - Sunday) ')
Day = Day.lower()

daysoftheweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
dayindex = daysoftheweek.index(Day)

if 5 <= dayindex:
    print('Sleep in!')
else:
    print('Work!')
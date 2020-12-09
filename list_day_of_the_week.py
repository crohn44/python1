dayindex = input('Day (0-6)?')
dayindex = int(dayindex)
daysoftheweek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = daysoftheweek.pop(dayindex)
print(day)
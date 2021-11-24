all_seconds = int(input('Введите количество секунд:'))
hours = all_seconds // 3600
minutes = (all_seconds % 3600) // 60
seconds = ((all_seconds % 3600) % 60)
if hours < 10:
    hoursnew = str(0) + str(hours)
else:
    hoursnew = hours

if minutes < 10:
    minutesnew = str(0) + str(minutes)
else:
    minutesnew = minutes

if seconds < 10:
    secondsnew = str(0) + str(seconds)
else:
    secondsnew = seconds

print(f'{hoursnew}:{minutesnew}:{seconds}')

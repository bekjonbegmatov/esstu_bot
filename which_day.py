import datetime

day_of_weak = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

def get_dey_of_weak():
    current_date = datetime.date.today()
    day_of_week = current_date.strftime("%A")
    index = 0
    for i in range(len(day_of_weak)):
        if day_of_weak[i] == day_of_week:
            index = i
    if index == 0:
        return 'Понедельник'
    elif index == 1:
        return 'Вторник'
    elif index == 2 :
        return 'Среда'
    elif index == 3 :
        return 'Четверг'
    elif index == 4 :
        return 'Пятница'
    elif index == 5:
        return 'Суббота'

print(get_dey_of_weak())
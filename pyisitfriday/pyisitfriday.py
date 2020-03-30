from datetime import date

weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

if __name__ == "__main__":
    today = date.today()
    weekday = today.weekday()

    print('Is it friday???')
    if (weekday == 4):
        print('YES it\'s Friday!')
    else:
        print(f'NO, it\'s just {weekDays[weekday]}')

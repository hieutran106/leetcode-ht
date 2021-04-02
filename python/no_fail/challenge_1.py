import datetime
import calendar

def solution(input: str) -> int:
    input_datetime = datetime.datetime.strptime(input, "%Y-%m-%d");
    input_date = datetime.date(input_datetime.year, input_datetime.month, input_datetime.day)
    current_year = input_date.year
    if calendar.isleap(current_year):
        delta = datetime.date(current_year, 2, 29) - input_date
        days = delta.days
        if days >= 0:
            return days

    if calendar.isleap(current_year + 1):
        delta = datetime.date(current_year + 1, 2, 29) - input_date
        return delta.days
    elif calendar.isleap(current_year + 2):
        delta = datetime.date(current_year + 2, 2, 29) - input_date
        return delta.days
    elif calendar.isleap(current_year + 3):
        delta = datetime.date(current_year + 3, 2, 29) - input_date
        return delta.days
    elif calendar.isleap(current_year + 4):
        delta = datetime.date(current_year + 4, 2, 29) - input_date
        return delta.days

    return -1


if __name__ == "__main__":
    my_input = input()
    result = solution(my_input)
    print(result)

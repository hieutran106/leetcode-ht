import datetime
import calendar


def solution(input: str) -> int:
    input_datetime = datetime.datetime.strptime(input, "%Y-%m-%d")
    input_date = datetime.date(
        input_datetime.year, input_datetime.month, input_datetime.day
    )
    current_year = input_date.year
    if calendar.isleap(current_year):
        delta = datetime.date(current_year, 2, 29) - input_date
        days = delta.days
        if days >= 0:
            return days

    # next year can be 1 --> 8 year
    for i in range(1, 9):
        if calendar.isleap(current_year + i):
            next_year = datetime.date(current_year + i, 2, 29)
            delta = next_year - input_date
            return delta.days

    return -1


if __name__ == "__main__":
    my_input = input()
    result = solution(my_input)
    print(result)

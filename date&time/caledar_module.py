# Problem: Calendar Module
# Platform: HackerRank
# Concept: Date & Time / Calendar


import calendar

month, day, year = map(int, input().split())

weekday = calendar.weekday(year, month, day)

days = [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY"
]

print(days[weekday])
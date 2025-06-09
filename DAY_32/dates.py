import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
day_of_week = now.weekday()
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)
print(day_of_week)


date_of_birth = dt.datetime(year=2000, month=11, day=27)
print(date_of_birth)






from datetime import datetime, date, time, timedelta

data1 = date.today()
data2 = date(2019, 8, 6)

hora1 = time(18, 24, 14)
hora2 = time(16, 23, 48)

print(data1)
print(hora1)
print()
print(data2)
print(hora2)

print()
print("data:", data1 < data2)
print("hora:", hora1 > hora2)

print()
print(data2)
print(data2 + timedelta(days=2)) # sumamos 2 dias
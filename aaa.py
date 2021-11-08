import datetime
date_list = input().split()
date = datetime.date(int(date_list[0]),int(date_list[1]), int(date_list[2]))
days_plus = int(input())
date_plus = datetime.timedelta(days_plus)

f_date = date_plus + date
for i in str(f_date).split('-'):
    print(int(i), end = ' ')

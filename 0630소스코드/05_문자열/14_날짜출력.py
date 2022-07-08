from datetime import date, datetime, timedelta

current_time = datetime.now()
print("현재시간 : {0}".format(current_time))
print("1일 2시간 후 : {0}".format(current_time+timedelta(days=1,hours=2)))
print("1시간 전 : {0}".format(current_time+timedelta(hours=-1)))
print("1시간 후 : {0}".format(current_time+timedelta(hours=1)))

today = datetime.today()
now = datetime.now()
print("today : ", today)
print("now : ", now)
print(today.strftime('%Y-%m-%d %H:%M:%s'))
print(today.strftime('%y-%m-%d %H:%M %p'))
str_date = "2019-06-25 17:35:20"
print(type(str_date))

date1 = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print(type(date1))
print("date : ",date1)

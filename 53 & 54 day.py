import module

# import module and do calculation then print it

# Q1
module.Funsum(8,1)
module.Funsubc(4,2)
module.Funmulti(6,6)
module.Fundiv(8,2)

# Q2 + Q3
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days =1)

print("yesterday: " ,yesterday)
print("today :", today)
print("tomorrow: ", tomorrow)

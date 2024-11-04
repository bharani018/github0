
import datetime

x = datetime.datetime.now()

print(x.strftime("%a")) #short form of day "fri"
print(x.strftime("%A")) # long day "Friday"

print(x.strftime("%d")) # today date eg:01

print(x.strftime("%b")) #short month 
print(x.strftime("%B")) #long month

print(x.strftime("%m")) #month in number

print(x.strftime("%y"))
print(x.strftime("%Y"))

print(x.strftime("%H")) #hour
print(x.strftime("%M")) #minute
print(x.strftime("%S")) #seconds

txt = "Hello, welcome to my world . Hi"

new = txt.split()
print(new)

import re
x1 = re.split(" ", txt)
print(x1)

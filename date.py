#1ex
from datetime import date,timedelta

cur_date = date.today()
new_date = cur_date-timedelta(days=5)
print(new_date)
#2ex
cur_date = date.today()
new_date = cur_date-timedelta(days=1)
new_date1 = cur_date+timedelta(days=1)
print(new_date,cur_date,new_date1)
#3ex
mics = datetime.now()
mics = mics.replace(microsecond=0)
print(mics)
#4ex
from datetime import datetime,timedelta
cur_date = datetime.now()

new_date = cur_date-timedelta(days=1)

print(cur_date,new_date,sep="\n")
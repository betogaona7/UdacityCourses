
from datetime import datetime, date

in_date = "2012-06-29"
fi_date = "2013-06-31"

date_format = "%Y-%m-%d"
initial_date = datetime.strptime(in_date, date_format)
final_date = datetime.strptime(fi_date, date_format)
dif = final_date - initial_date

print(dif.days)


#Pendient - Quiz 10 row abacus - Lesson 2 poblem set(optional) 2
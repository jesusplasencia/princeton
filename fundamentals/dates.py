from datetime import date, timedelta;

date.fromisoformat("2019-12-04");
date.fromisoformat("20191204");
date.fromisoformat("2021-W01-1");

myDateWeekAfter = date.today() + timedelta(days = 7); # Add 7 days
myDateMonthAfter = date.today() + timedelta(weeks = 4); # Add 4 weeks
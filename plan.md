I WRITE ALL MY FILES IN BASE VIM

What I know so far 22:42

FILE Naming FORMAT:
ctg_tick_XXXX(year)XX(month)XX(date)_XXXX(increases)_XXXXXXXX(8 digit hash, still unsure)

DATA FORMAT:
Timestamp,Price,Size
2024-09-17 13:25:36.365,402.2953300693472,105

PROBLEMS WITH DATA
1. negative numbers (price)
2024-09-17 13:25:12.812,-402.4094279499778,997

2. missing prices
2024-09-17 13:25:31.759,,103

3. small prices / commas not in the correct location
2024-09-17 13:25:29.649,40.24517762792956,96

4. ???22:50 Could it be outside of hours? 9:30 -> 16:00

Where to go next:
Top down, front interface then back functionality

https://www.geeksforgeeks.org/python-oops-concepts/

23:31
Using datetime for the interval in data_interface isn't working well, ill make it a struct
https://www.geeksforgeeks.org/python-datetime-datetime-class/
https://www.geeksforgeeks.org/string-slicing-in-python/

23:38
finished my interval grabber
and tested

23:49
finished the timeframe grabber
and tested
TODO output generation

00:02
I realised datetime.timedelta exists
I will use it
https://stackoverflow.com/questions/36075197/how-to-modify-datetime-datetime-hour-in-python

00:11
ok I am ready to work on the backend
https://www.geeksforgeeks.org/how-to-import-a-class-from-another-file-in-python/
csv time
https://docs.python.org/3/library/csv.html

00:22
https://www.geeksforgeeks.org/python-list-files-in-a-directory/

00:56
I got my find files method to work, now I have it narrowed to the days
time to work on data cleaning

01:22
https://www.geeksforgeeks.org/multithreading-python-set-1/

01:28
so I am reading the files well

01:49
I need to use a time type, im at 3 hours. Need to speed up

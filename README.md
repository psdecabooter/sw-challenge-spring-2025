If you want to see my time-stampped trail of though, look at plan.md
<br>
In order to use my solution, you must run the frontend file with python3.
There are 3 parts:
1. frontend - communicates with use
2. backend - does the computation
3. interface - communicates between the back and frontend

I have two example outputs:
1. output.csv
used the inputs:
2024-09-17 00:09:20.000
2024-09-18 01:00:00.000
30m

2. output2.csv
used the inputs:
2024-09-18 00:09:20.000
2024-09-19 01:00:00.000
4s20m4h

I unfortunately ran into a problem with python threading which my inexperience did not allow me to fix,
so please keep your start and end times within a day and a half of each other for best effect

To understand how to format your input and why I made my cleaning decisions, please see their respective files (frontend & backend)
However, ill give a short description of each here:
Formatting:
- Format your interval input as '4s', '15m', '2h', '1d', '1h30m'
- Format your datetimes as YYYY-MM-DD HH:MM:SS.xxx (remember the thousandths of a second)
- Finally the path name of your output file
<br>
# Data Cleaning Pipeline:
What does it mean for the data to be clean? I have discovered 4 discrepencies and I will now explain them to you:
<ol> 
<li> Negative prices: <br>2024-09-17 13:25:12.812,-402.4094279499778,997 </li>
<li> Missing prices: <br>2024-09-17 13:25:31.759,,103 </li>
<li> 2 digit prices / decimal point in the incorrect location: <br>2024-09-17 13:25:29.649,40.24517762792956,96 </li>
<li> The last error is harder to identify: Trading hours <br>
   I believe this since regular trading hours are from 9:30 AM to 4:00PM EST. <br>
   However, the guidelines are slightly misleading.
   They say "All timestamps are in Eastern Standard Time (UTC)."
   Is it supposed to be UTC or EST?
   Since the previous line specifies EST for trading hours, and since it is typed out that way long-form
   I wll assume that trades outside of regular hours are outliers and thus should not be counted.
</li>
</ol>

<br>
Challenges to be solved:
<ul>
<li>What does the 8 digit hash mean on the file format?</li> 
<li> How can I more efficiently analyze the intervals?
     <ul>
     <li>Maybe construct a data structure that holds each interval and more data (start time, end time, start file, end file)</li>
     </ul>
</li>
<li>How can I fix the multithreading issue in the cleaning step, i.e. how do I limit the number of threads active and Identify how many can be active </li>
<li>I think the code for volume might be wrong, I would change that </li> 
<li>Handle empty intervals better thatn just returning an empty line</li>
</ul>
<br>
Retrospective:
<ul>
<li>Through more research, I have learned that this data is called time series data</li>
<li> If I were to implement the cleaning funciton again:
     <ul>
     <li>I would create a queue with all of the file names, and then I would have 10 threads that just cycle through the queue</li>
     <li>It would be better if I hade a thread lock, but if pressed for time again I would just assign each thread to a single file, and then create new threads for each individual file when popping from the queue</li>
     </ul>
</li>
<li> I am still unsure of the best way to handle the OHLCV with threads:
     <ul>
     <li> The advantages of my previous solution was that it was O(n) where n is the number of lines across csvs, and that it had a relatively-low memory overhead</li>
     <li> The disadvantage was that it was not multi-threaded</li>
     </ul>
</li>
</ul>

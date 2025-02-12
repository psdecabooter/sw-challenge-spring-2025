from datetime import datetime
#- **Functionality Requirements**:
#    - **Time Interval Input**:
#        - Accept time intervals as strings (e.g., “4s”, "15m", "2h", "1d", "1h30m").
#        - Support combinations of days, hours, minutes, and seconds.
#    - **Time Frame Selection**:
#        - Accept start and end datetime values to specify the data range.
#    - **Output Generation**:
#        - Produce flat files (e.g., CSV) containing OHLCV bars for the specified intervals and time frame.
#        - Each OHLCV record should include:
#            - **Open Price**: First trade price within the interval.
#            - **High Price**: Highest trade price within the interval.
#            - **Low Price**: Lowest trade price within the interval.
#            - **Close Price**: Last trade price within the interval.
#            - **Volume**: Total volume traded within the interval.

#This class will handle the inteface with the user
#Will handle csv interactions and creating OHLCV
#2 input methods:
#Time interval input
#Time frame selection
#Create the OHLCV on the intervals between the two date times
#Use the time interval as steps
class data_interface:

    # datetime objects holding start and end times
    start_time = None
    end_time = None

    # interval_t ovbject holding our interval
    interval = None

    # structured data for holding the interval
    class interval_t:
        hour = 0
        minute = 0
        second = 0
        day = 0
        def __init__(self, second, minute, hour, day):
            self.second = second
            self.minute = minute
            self.hour = hour
            self.day = day

        # used for debugging
        def to_string(self):
            return f"{self.second}s{self.minute}m{self.hour}h{self.day}d"




    def __init__(self):
        pass

    # This method will add our time frame
    # Our date-time objects look like This
    # 2024-09-16 18:10:13.077
    def add_time_frame(self, start_time, end_time):
        datetime_format = "%Y-%m-%d %H:%M:%S.%f"
        self.start_time = datetime.strptime(start_time, datetime_format)
        self.end_time = datetime.strptime(end_time, datetime_format)

    #This function handles the input of start time strings
    #Accept time intervals as strings (e.g., “4s”, "15m", "2h", "1d", "1h30m")
    #Support combinations of days, hours, minutes, and seconds
    #start_time and end_time are both strings
    #will raise an error if the string is invalid
    def get_interval(self, time_string):
        # values for later
        seconds = 0
        days = 0
        minutes = 0
        hours = 0

        # ill use indexing and slices to get the numbers
        last_found = 0
        for i in range(len(time_string)):
            char = time_string[i]
            if char == 's':
                seconds = int(time_string[last_found:i])
                last_found = i+1
            elif char == 'm':
                minutes = int(time_string[last_found:i])
                last_found = i+1
            elif char == 'h':
                hours = int(time_string[last_found:i])
                last_found = i+1
            elif char == 'd':
                days = int(time_string[last_found:i])
                last_found = i+1
            elif not char.isnumeric():
                raise ValueError("Time string is invalid");
        self.interval = self.interval_t(seconds,minutes,hours,days)

start = input()
end = input()
interface = data_interface()
interface.add_time_frame(start,end)
print(f"START: {interface.start_time}")
print(f"END: {interface.end_time}")

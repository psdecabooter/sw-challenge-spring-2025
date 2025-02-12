from datetime import datetime, timedelta, time
import threading
import csv
import os

# this class will handle the csv files
# we will also clean the data
#
# what tools do I want:
# clean all data
# get all csv's in a time period
# analyse the csv's in a time period by interval
class data_backend:

    def __init__(self):
        pass

    # Data cleaning pipeline
    # What does it mean for the data to be clean?
    # I have discovered 4 discrepencies and I will now explain them to you
    # 1. Negative prices
    #   2024-09-17 13:25:12.812,-402.4094279499778,997
    # 2. Missing prices
    #   2024-09-17 13:25:31.759,,103
    # 3. 2 digit prices / decimal point in the incorrect location
    #   2024-09-17 13:25:29.649,40.24517762792956,96
    # 4. The last error is harder to identify: Trading hours
    #   Since regular trading hours are from 9:30 AM to 4:00PM EST
    #   However, the guidelines are misleading.
    #   They say "All timestamps are in Eastern Standard Time (UTC)."
    #   Is it supposed to be UTC or EST?
    #   Since the previous line specifies EST for trading hours, and since it is typed out that way long-form
    #   I wll assume that trades outside of regular hours are outliers and should not be counted
    # I will attempt to use threads to format data, I will use git to store my state before I test
    def clean_data(self, directory, file_names):
        threads = [threading.Thread(target=self.clean_data_helper, args=(directory,file_name)) for file_name in file_names]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        print("done")

    # helper method which will be used by the threads
    def clean_data_helper(self, directory, file_name):
        try:
            #store the valid lines
            valid_lines = []

            # start and end of trading hours
            start_trading = time(hour=9,minute=30, second=0,microsecond=0)
            end_trading = time(hour=16, second=0,microsecond=0)
            # format for parsing datetime
            datetime_format = "%Y-%m-%d %H:%M:%S.%f"

            #open the csv file to read
            csvfile = open(os.path.join(directory,file_name), "r")

            spamreader = csv.reader(csvfile, delimiter=',')
            # skip header
            first_row = next(spamreader, None)
            #handle empty files
            if first_row == None:
                csvfile.close()
                return
            valid_lines.append(first_row)
            #loop through rows
            for row in spamreader:
                # checks condition 2
                if (row[1]) == "": continue
                # checks condition 1&3
                if (float(row[1])) < 100: continue
                # check condition 4
                date = datetime.strptime(row[0], datetime_format)
                if date.time() < start_trading or date.time() > end_trading: continue
                valid_lines.append(row)
            csvfile.close()

            #open the csv file to write
            csvfile = open(os.path.join(directory,file_name), "w")
            writer = csv.writer(csvfile)
            writer.writerows(valid_lines)

            csvfile.close()
        except FileNotFoundError:
            # if reading the file fails just quit
            return

    # start_time and end_time are both datetime objects
    # FILE Naming FORMAT:
    # ctg_tick_XXXX(year)XX(month)XX(date)_XXXX(increases)_XXXXXXXX(8 digit hash)
    def find_files(self, directory, start_time, end_time):

        # get all files
        all_files = list(filter(lambda string: string.endswith(".csv"), os.listdir(directory)))

        # filtered files
        filtered_files = []

        # I must use a time delta to loop through
        # must strip vlues below day so it doesn't mess with the while
        copy_end = end_time.replace(second=0,minute=0,hour=0,microsecond=0)
        copy_start = start_time.replace(second=0,minute=0,hour=0,microsecond=0)
        while copy_start <= copy_end:
            
            # I tested how start_time.month returns, and I figured I need to pad it
            day_string = f"ctg_tick_{copy_end.year}{str(copy_end.month).zfill(2)}{str(copy_end.day).zfill(2)}"

            for file_name in all_files:
                if file_name.startswith(day_string):
                    filtered_files.append(file_name)


            #termination
            copy_start += timedelta(days=1)
        
        return filtered_files


backend = data_backend()
file_names = backend.find_files("./data/", datetime(year=2024,month=9,day=16),datetime(year=2024,month=9,day=17))
backend.clean_data("./data/",file_names)
print(file_names[0])


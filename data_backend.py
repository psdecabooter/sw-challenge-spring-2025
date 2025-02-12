from datetime import datetime, timedelta
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

    # start_time and end_time are both datetime objects
    # FILE Naming FORMAT:
    # ctg_tick_XXXX(year)XX(month)XX(date)_XXXX(increases)_XXXXXXXX(8 digit hash)
    def find_files(self, directory, start_time, end_time):

        # get all files
        all_files = list(filter(lambda string: string.endswith(".csv"), os.listdir(directory)))

        # filtered files
        filtered_files = []

        # I must use a time delta to loop through
        # must strip vlues below day
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
        
        for file_name in filtered_files:
            print(file_name)


backend = data_backend()
backend.find_files("./data/", datetime(year=2024,month=9,day=16),datetime(year=2024,month=9,day=17))



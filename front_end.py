from data_interface import data_interface

class frontend:
    def __init__(self):
        print("Welcome to Patrick DeCabooter's OHLCV generator")
        print("First input a time interval")
        print("Format your input as '4s', '15m', '2h', '1d', '1h30m'")
        print("s for seconds, m for minutes, h for hours, d for days")
        time_string = input()
        print("Now input two datetimes; a start and stop time")
        print("Format them as YYYY-MM-DD HH:MM:SS.xxx")
        start_time = input()
        stop_time = input()
        print("Finally the path name of your output file")
        output_file = input()
        
        d_i = data_interface()
        try:
            d_i.add_time_frame(start_time, stop_time)
        except:
            print("error with adding interval")
            return
        try:
            d_i.get_interval(time_string)
        except:
            print("Error with time strings, check you have all values")
            return
        try:
            d_i.output_generation(output_file)
        except:
            print("error with output file")
            return

f = frontend()       

import time
current_time_struct = time.localtime()
day_of_year = current_time_struct.tm_yday
year = current_time_struct.tm_year
print(f"今天是 {year} 年的第 {day_of_year} 天。")

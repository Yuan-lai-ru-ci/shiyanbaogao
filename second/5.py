t = 10000000
hour = t//60
minute_sheng = t%60
day = hour//24
hour_sheng = hour%24
year = day//365
day_sheng = day%24
print(year, day_sheng,hour_sheng,minute_sheng)



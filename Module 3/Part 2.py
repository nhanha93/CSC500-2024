current_time = int(input("What is your current time(in hours)?: "))
wait_hours = int(input("How many hours you want to wait for the alarm?: "))
alarm_time = int(current_time + wait_hours)
if alarm_time < 24:
    print("The alarm goes off at: ", alarm_time)
else:
    print("The alarm goes off at: ", alarm_time - 24)

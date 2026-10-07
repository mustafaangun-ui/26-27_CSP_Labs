Starting_Milliseconds = 10000123
Hours = Starting_Milliseconds // 3600000
Seconds_Left_Over = Starting_Milliseconds % 3600
Minutes = Seconds_Left_Over // 60
Seconds = Seconds_Left_Over % 60


print("Starting seconds: ", Starting_Milliseconds)
print("Hours: ", Hours)
print("Minutes: ", Minutes)
print("Seconds: ", Seconds)

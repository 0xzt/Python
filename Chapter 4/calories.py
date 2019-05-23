# The following equations estimate the calories burned when exercising (source):

# Men: Calories = ( (Age x 0.2017) — (Weight x 0.09036) + (Heart Rate x 0.6309) — 55.0969 ) x Time / 4.184

# Women: Calories = ( (Age x 0.074) — (Weight x 0.05741) + (Heart Rate x 0.4472) — 20.4022 ) x Time / 4.184

# Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output calories burned for men and women.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('Men: %0.2f calories' % calories_man)

# Ex: If the input is:

# 49
# 155
# 148
# 60
# Then the output is:

# Men: 489.78 calories
# Women: 580.94 calories

#-----

#''' Men: Calories = ((Age x 0.2017) - (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''
#''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''

age_years = int(input())
weight_pounds = int(input())
heart_bpm = int(input())
time_seconds = int(input())

calories_man = ((age_years * 0.2017) - (weight_pounds * 0.09036) + (heart_bpm * 0.6309) - 55.0969) * time_seconds / 4.184
calories_woman = ((age_years * 0.074) - (weight_pounds * 0.05741) + (heart_bpm * 0.4472) - 20.4022 ) * time_seconds / 4.184 

print('Men: %0.2f calories' % calories_man)
print('Women: %0.2f calories' % calories_woman)
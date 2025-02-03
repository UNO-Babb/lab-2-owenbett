#FutureTime.py
#Name:Owen Betts
#Date:01/31/2025
#Assignment: Lab 02 Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour-6) % 24
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  hours = input("How many hours? :")
  #Ask user for minutes
  minuets = input("How many minuets? :")
  moreMins = (60 * int(hours) + int(minuets))

  futureMins = (currentMinute + moreMins) % 60
  extraHour = ( (currentHour + (currentMinute + moreMins) // 60) % 24)
  print(str(extraHour), ":", str(futureMins))

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()

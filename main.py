def is_leap(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
year = int(input("Enter Year: "))
if is_leap(year):
  print("Leap")
else:
  print("Not Leap")
  

"""
RECORD CHECK  -  my version
===========================

Name  :Rumana Jannat Ritu
Lane  :  AI
Date  :30/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


label = input("Enter label: ")    
value = float(input("Enter value: "))     
limit = float(input("Enter limit: "))     


difference = limit - value 
percent = (difference / limit) * 100     


if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f" {"Used:":<10} {value:>10.2f}")
print(f" {"Total:":<10} {limit:>10.2f}")

# your report lines go here
print(f" {"Free:":<10} {difference:>10.2f}")
print(f" {"Percent:":<10} {percent:>10.2f}%")
print(f" {"Status:":<10} {status:>10}")

print("=" * 34)


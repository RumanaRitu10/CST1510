"""
RECORD CHECK  -  my version
===========================

Name  :Rumana Jannat Ritu
Lane  :  AI 
Date  :08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def status_of(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"



label = input("Enter label")     
value = float(input("Enter value"))     
limit = float(input("Enter limit"))   

def check(value, limit):
    """Calculate the difference and percentage of value against limit."""
    difference = limit - value
    percent = (value / limit) * 100 if limit != 0 else 0
    return difference, percent


difference, percent = check(value, limit)
status = status_of(percent)         


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
# your report lines go here
print(f"  Used: {value:6.2f}")
print(f"  Total: {limit:6.2f}")
print(f"  Free: {difference:6.2f}")
print(f"  Percent: {percent:6.2f}%")
print(f"  Status: {status}")
print("=" * 34)


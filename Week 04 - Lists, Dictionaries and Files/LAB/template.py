"""
RECORD CHECK  -  my version
===========================

Name  :Rumana Jannat Ritu
Lane  :  AI 
Date  :16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

from matplotlib.pylab import record


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

def load_records(path):
    """Load records from a file and return a list of dictionaries."""
    records = []
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(',')
            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }
            records.append(record)
    return records

records = load_records(r"C:\Users\USER\Documents\CST1510\Week 04 - Lists, Dictionaries and Files\LAB\records_sample.txt")  # replace with your code


for item in records:
    difference, percent = check(item["value"], item["limit"])
    status = status_of(percent)
    print(item["label"], item["value"], item["limit"], difference, percent, status)

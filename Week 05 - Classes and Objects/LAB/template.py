"""
RECORD CHECK  -  my version
===========================

Name  :Rumana Jannat Ritu
Lane  :  AI 
Date  :24/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class Record:
    """Store a record and check its value against a limit."""

    over_limit_count = 0  

    def __init__(self, label, value, limit):
        """Initialise a record with its label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the value compared with the limit."""
        percentage = (self.value / self.limit) * 100

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

def load_records(path):
    """Read records from a file and return a list of Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            record = Record(label, float(value), float(limit))
            records.append(record)

    return records


records = load_records(r"C:\Users\USER\Documents\CST1510\Week 05 - Classes and Objects\LAB\records_sample.txt")


for record in records:

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"  Label  : {record.label}")
    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")
    over_limit_count = 0
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

    print("=" * 34)


print()
print("FINAL SUMMARY")
print("=" * 34)
print(f"Total records       : {len(records)}")
print(f"Records over limit  : {over_limit_count}")
print("=" * 34)
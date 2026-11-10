"""
RECORD CHECK  -  my version
===========================

Name  :Rumana Jannat Ritu
Lane  :  AI 
Date  :6/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
  """Clean and parse a raw, messy survey line into a structured dictionary."""
  line = raw_line.strip().lower()
  survey_part, rest = line.split(",", 1)
  data = {"survey": survey_part.strip()}

  for piece in rest.split(","):
    key, value = piece.split("=")
    data[key.strip()] = float(value.strip())

  return data


def status_of(data):
  """Evaluate survey rating and return the status (FLAGGED or OK)."""
  rating = data["rating"]
  if rating < 3:
    return "FLAGGED"
  else:
    return "OK"
  

raw_records = [
    " Survey_2026 , rating=4 , age=23 ",
    "SURVEY_2027 , RATING=2 , AGE=30",
    " survey_2028 , rating=5 , age=22 ",
    "SURVEY_2029 , RATING=1 , AGE=45",
    " survey_2030 , rating=4 , age=28 ",
]


for raw_record in raw_records:
  try:
    data = parse_line(raw_record)
    status = status_of(data)
    print(data, "->", status)
  except ValueError:
    print(f"Could not parse: {raw_record}")

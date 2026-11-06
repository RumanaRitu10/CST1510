# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:
    def __init__(self,label,value,limit)
        self . label = "R-001"
        self . value = 87
        self . limit = 100
        
        def status (percent): # this parameter should be self
            return percent
        
        
r = Record('M00123',90,100)
r2 = Record('M00124',80,100)

print(r.status(95))

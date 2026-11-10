# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

piece = "note=server=east"
key, value = piece.split("=",1) # Limits the split to 1,yielding 2 parts)

print(key, value)

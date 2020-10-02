# Use words.txt as the file name
fname = input("Enter file name: ")
file_opening = open(fname)
reading = file_opening.read().rstrip()
upper_casing = reading.upper()
print(upper_casing)
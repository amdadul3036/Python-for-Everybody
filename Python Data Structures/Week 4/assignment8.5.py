fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
data=[]
for each in fh:
    if each.startswith("From") and len(each.split())>2:
        temp=each.split()
        data.append(temp[1])
for each in data:
    print(each)
print("There were", len(data), "lines in the file with From as the first word")
fname = raw_input("Enter the file: ")
if len(fname)<1:fname = "mbox-short.txt"
handle = open(fname)

count = 0
d = dict()

for line in handle:
    if not line.startswith("From"):
        continue
    line = line.split()
    if line[0]=='From':
        line1 = line[1]
        for word in line1.split():
            if word not in d:
                d[word] = 1
            else:
                d[word]+=1
        count+=1


maximum = None
k = None
for key,value in d.items():
    if maximum is None or value>maximum:
        maximum = value
        k = key
        
print(k,maximum)
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = list()
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    time = words[5].split()
    for hour in time:
        hour = hour.split(":")
        hours.append(hour[0])

for hour in hours:
    counts[hour] = counts.get(hour,0) + 1

tmp = list()
for k,v in counts.items():
    newt = (k,v)
    tmp.append(newt)

tmp = sorted(tmp)

for v,k in tmp:
    print(v,k)

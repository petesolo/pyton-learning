# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Invalid file name')
    quit()

count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    extLine = line.rstrip()
    vPos = extLine.find(' ')
    cValue = float(extLine[vPos:])
    total = total + cValue
    count = count + 1
print('Average spam confidence:',total/count)

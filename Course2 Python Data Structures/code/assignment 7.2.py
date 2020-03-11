fname = input("Enter file name:")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        pos = line.find(":")
        line = line[pos+1:]
        total = total + float(line.lstrip())
print("Average spam confidence:",total/count)

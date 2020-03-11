name = input("Enter file name:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From '):
        time = line.split()[5]
        hour = time.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

for (k,v) in sorted(counts.items()):
    print(k,v)

name = input("Enter file name:")
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        person = line.split()[1]
        counts[person] = counts.get(person,0) + 1

bigperson = None
bigcount = None
for k,v in counts.items():
    if bigcount is None or v > bigcount:
        bigperson = k
        bigcount = v

print(bigperson, bigcount)

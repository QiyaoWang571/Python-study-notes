fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line1 = line.rstrip()
    print(line1.upper())

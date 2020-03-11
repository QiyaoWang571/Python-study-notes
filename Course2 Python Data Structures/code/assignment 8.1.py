fname = input("Enter file name: ")
fh = open(fname)
words = list()
for line in fh:
    word = line.split()
    for i in word:
        if i not in words:
            words.append(i)
words.sort()
print(words)

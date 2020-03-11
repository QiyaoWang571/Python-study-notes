text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
snum = text[pos:]
num = float(snum)
print(num)

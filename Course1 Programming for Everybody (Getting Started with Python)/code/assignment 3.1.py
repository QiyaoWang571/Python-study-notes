#ass3.1
hours = input('Enter Hours:')
rate = input('Enter rate:')
h = float(hours)
r = float(rate)
if h <= 40:
    pay = h*r
else:
    pay = 40 * r + (h-40) * (1.5*r)
print(pay)

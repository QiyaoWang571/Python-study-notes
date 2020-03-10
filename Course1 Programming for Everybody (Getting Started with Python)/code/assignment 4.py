#ass4
def computepay(h,r):
    if h <= 40:
        total = h * r
    else:
        normal = 40 * r
        special = (h - 40) * 1.5 * r
        total = normal + special
    return total

hours = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hours)
r = float(rate)
p = computepay(h,r)
print("Pay",p)

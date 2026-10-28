import sys

p = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

si = (p * r * t) / 100

print("Principal Amount:", p)
print("Rate of Interest:", r)
print("Time:", t, "years")
print("Simple Interest:", si)
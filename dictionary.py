import evenorodd
import prime
import composite
n,m=map(int,input().split())
d={"Even":[],"Odd":[],"Prime":[],"Composite":[]}
for i in range(n,m+1):
  if evenorodd.even(i):
    d["Even"].append(i)
  else:
    d["Odd"].append(i)
  if prime.isprime(i):
    d["Prime"].append(i)
  elif composite.iscomposite(i):
    d["Composite"].append(i)
print(d)

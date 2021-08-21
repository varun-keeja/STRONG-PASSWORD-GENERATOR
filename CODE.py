import random
print("Welcome to Password Generator")
a=list("abcdefghijklmnopqrstuvwxyz")
n=list("1234567890")
s=list("!@#$%^&*")
l=int(input("How many letters you want ? \nType any number between 0 and 23\n"))
la=[]
for i in range(0,l):
  r=random.randint(0,l)
  la.append(r)
al=[]
for i in la:
  al.append(a[i])
nu=int(input("How many numbers you want ? \nType any number between 0 and 9\n"))
na=[]
for i in range(0,nu):
  r=random.randint(0,nu)
  na.append(r)
an=[]
for i in na:
  an.append(n[i])
sc=int(input("How many special charachters you want ? \nType any number between 0 and 7\n"))
scl=[]
for i in range(0,sc):
  r=random.randint(0,sc)
  scl.append(r)
lcs=[]
for i in scl:
  lcs.append(s[i])
nl=al+an+lcs
random.shuffle(nl)
password= ""
for i in nl:
  password+=i
print(f"Your password is {password}")

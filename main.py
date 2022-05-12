import random 
def hash(value):
  hashedd = 0
  hashed = []
  for i in value[::-1]:
       print(i)
       hashed.append((ord(i)) + 10)
  print(hashed)
  for i in hashed:
    hashedd = i + hashedd + 58
  return hashedd
 
print(hash(input("Enter string to be hashed:")))

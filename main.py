import random 
def hash(value):
  hashedd = 0
  hashed = []
  for i in value[::-1]:
       print(i)
       hashed.append((ord(i)+(random.randint(1,100))))
  print(hashed)
  for i in hashed:
    hashedd = i + hashedd
  return hashedd
 
print(hash(input("Enter string to be hashed:")))

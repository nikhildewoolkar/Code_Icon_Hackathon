import pandas as pd

df = pd.read_csv (r'test123.csv')
d=df.values.tolist()
# f=[list(item) for item in set(tuple(row) for row in d)]
# print(len(f))
hi = pd.read_csv (r'RESULT.csv')
h=hi.values.tolist()
hii = pd.read_csv (r'RESULT1.csv')
c=0
for i in range(len(h)):
  c+=1
  if(h[i] in f):
    hii.hit_or_miss[i]= "0"
  else:
    hii.hit_or_miss[i]= "1"
hii.to_csv('output.csv')
print(hii)
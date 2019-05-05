#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.naive_bayes import GaussianNB
import numpy as np
import random
import csv


# In[2]:


x,y = [],[]

f = open("TrainsetTugas4ML.csv","r")
reader = csv.reader(f)
next(reader)

for d in reader:
    x.append([float(d[0]),float(d[1])])
    y.append(int(d[2]))
x



# In[7]:


a,b,c,d,e,f,g = [],[],[],[],[],[],[]
temp = 0
        
for i in range(7):
    x1,y1 = [],[]
    for j in range (len(x)):
        temp = random.randint(0,297)
        x1.append(x[temp])
        y1.append(y[temp])
    clf = GaussianNB()
    clf.fit(x1,y1)
#     print x1    
    for k in x:
        if i == 0 :
            a.append(int(clf.predict([k])))
        elif i == 1 :
            b.append(int(clf.predict([k])))
        elif i == 2 :
            c.append(int(clf.predict([k])))
        elif i == 3 :
            d.append(int(clf.predict([k])))
        elif i == 4 :
            e.append(int(clf.predict([k])))
        elif i == 5 :
            f.append(int(clf.predict([k])))
        elif i == 6 :
            g.append(int(clf.predict([k])))


# In[8]:


hasil = []
satu,dua=0,0
for i in range(len(x)):
    temp = []
    temp.append([a[i],b[i],c[i],d[i],e[i],f[i],g[i]])
    satu = temp[0].count(1)
    dua = temp[0].count(2)
    if satu > dua:
        hasil.append(1)
    else:
        hasil.append(2)
        
print(hasil)


# In[12]:


total = 0.0

for i in range(len(y)) :
#     print(y[i])
#     print(hasil[i])
    if y[i] == hasil[i]:
        total += 1
print('Akurasi')       
print(str((total/298)*100) + ' %')


# In[ ]:





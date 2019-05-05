#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.naive_bayes import GaussianNB
import numpy as np
import random
import csv


# In[17]:


x,y = [],[]

f = open("TrainsetTugas4ML.csv","r")
reader = csv.reader(f)
next(reader)

for d in reader:
    x.append([float(d[0]),float(d[1])])
    y.append(int(d[2]))

xt = []
g = open("TestsetTugas4ML.csv","r")
reader = csv.reader(g)
next(reader)

for d in reader:
    xt.append([float(d[0]),float(d[1])])




# In[22]:


a,b,c,d,e,m,n = [],[],[],[],[],[],[]
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
    for k in xt:
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
            m.append(int(clf.predict([k])))
        elif i == 6 :
            n.append(int(clf.predict([k])))


# In[33]:


hasil = []
satu,dua=0,0
for i in range(len(xt)):
    temp = []
    temp.append([a[i],b[i],c[i],d[i],e[i],m[i],n[i]])
    satu = temp[0].count(1)
    dua = temp[0].count(2)
    if satu > dua:
        hasil.append(1)
    else:
        hasil.append(2)
        
print(hasil)


# In[34]:


h = open("TebakanTugas4ML.csv","w")
w = csv.writer(h)
w.writerow(['Class'])


# In[35]:


for row in hasil :
    print(row)
    w.writerow([str(row)])


# In[36]:


f.close()
g.close()
h.close()


# In[ ]:





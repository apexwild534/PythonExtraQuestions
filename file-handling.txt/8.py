import pickle
f=open('file123.dat','rb')
dict1=pickle.load(f)
f.close()
print(dict1)
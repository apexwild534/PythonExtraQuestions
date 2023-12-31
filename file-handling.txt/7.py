import pickle
dict1={'python':90, 'java':95, 'c++':85}
f=open('file7.dat','wb')
pickle.dump(dict1,f)
f.close()
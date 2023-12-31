def foperation():
    import pickle
    list1=[10,20,30,40,100]
    f=open('list.dat','wb')
    pickle.dump(list1,f)
    print("List Added To Binary File")
    f.close()

foperation()
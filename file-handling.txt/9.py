def binfile():
    import pickle
    file=open('data.dat','wb')
    while True:
        x=int(input("Enter the integer: "))
        pickle.dump(x,file)
        ans= input("Do you want to enter more data (y/n): ")
        if ans.lower()=='n':
            break
    file.close()
    file=open('data.dat','rb')
    try:
        while True:
            y=pickle.load(file)
            print(y)
    except EOFError:
        pass
    file.close()

binfile()
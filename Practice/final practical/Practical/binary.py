import pickle
f = open(r"Athletics.dat", "rb")
def read(f):
    try:
        while True:
            d=pickle.load(f)
            print(type(d))
    except EOFError:
        print("End of file reached")
def write () :
    f=open ("Athletics.dat", 'ab')
    list="d"
    pickle.dump (list, f)
    f.close ()
write()
read(f)
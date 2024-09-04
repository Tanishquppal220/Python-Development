import pickle

def copy_records(src, dest):
    src_file = open(src, 'rb')
    dest_file = open(dest, 'wb')

    try:
        while True:
            record = pickle.load(src_file)
            if 'Athletics' in record:
                pickle.dump(record, dest_file)
    except EOFError:
        pass

    src_file.close()
    dest_file.close()

copy_records('sports.dat', 'Athletics.dat')

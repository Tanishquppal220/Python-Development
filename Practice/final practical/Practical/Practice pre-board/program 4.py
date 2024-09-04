import csv

def add(fid, fname, fprice):
    with open(r'Practice pre-board\furdata.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([fid, fname, fprice])


def search():
    with open(r'Practice pre-board\furdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            if int(row[2]) > 10000:
                print(row)


add('F1', 'Sofa', 19000)
add('F2', 'Table', 5000)
add('F3', 'Chair', 12000)

search()

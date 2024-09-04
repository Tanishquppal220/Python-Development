def DISPLAYWORDS(filename):
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if len(word) < 4:
                    print(word,end=",")


DISPLAYWORDS('Practice pre-board\STORY.txt')

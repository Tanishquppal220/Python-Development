def count_uppercase(filename):
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            for char in line:
                if char.isupper():
                    count += 1
    return count


print(count_uppercase('Practice pre-board\STORY.txt'))

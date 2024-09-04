def count_A(filename):
    with open(filename, 'r') as file:
        count = sum(1 for line in file if line.startswith('A'))
    return count


print(count_A('Practice pre-board\STORY.txt'))

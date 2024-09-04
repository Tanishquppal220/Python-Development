with open('Text file.txt', 'w') as f:
    f.write('apple\nbanana\ncherry\ngrape\norange\npear\nkiwi\n')
with open('Text file.txt', 'r') as input_file, open('program_3.txt', 'w') as output_file:
    for line in input_file:
        if 'a' in line:
            output_file.write(line)
print("Opration Successfully Done")
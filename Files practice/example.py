# Using "r+" mode
with open(r"C:\Users\Tanishq\Desktop\School-work\Tanishq\Development\School-Class 12\Files practice\example.txt", "r+") as file:
    content = file.read()
    file.write("New content added.")
    file.seek(0)
    updated_content = file.read()

print("Original content:")
# print(content)
print("\nUpdated content:")
print(updated_content)

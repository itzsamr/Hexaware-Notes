# Text File
with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Binary File
with open("example.bin", "wb") as file:
    file.write(b"\xDE\xAD\xBE\xEF")

with open("example.bin", "rb") as file:
    content = file.read()
    print(content)

"manejo de archivos"

tecnologiabackend = ["python", "\njava"]

file = open("my_files/file3.txt", "a+")
file.writelines(tecnologiabackend)
file = open("my_files/file3.txt", "r")

for newline in file:
    print(newline)

file.close()


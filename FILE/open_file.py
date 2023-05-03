file = open("test1.txt", mode="wt", encoding="utf-8")

file.write("hello world")

file.close()

file = open("test1.txt", mode="r", encoding="utf-8")

print(file.read()) # reads everything
print(file.read(6)) # reads only 6 characters

print(file.readline()) # reads until \n
content = ""
while line != " ":
    line = file.readline()
    content += line

file.close()
with open("example.txt", "a") as file:
    for x in range(10):
        file.write(f"Add another {x} lines\n")

pattern = [str(n) for n in range(1,8)]
with open("example.txt", "r") as file:
    lines = file.readlines()

with open("example.txt", "w") as file:
    for i in lines:
        if any(n in i for n in pattern):
            file.write(i)

with open("example.txt", "r") as file:
    print(file.read())
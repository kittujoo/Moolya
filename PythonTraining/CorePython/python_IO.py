

file = open("io_test.txt")
def file_line():
    print(file.readlines())
    print(file.readline())

    lines = file.readlines()
    for line in lines:
        print(line.strip())

    file.close()

def with_open_func():
    with open("io_test.txt", "a") as writer :
        writer.write("\nJavaScript")

    with open("io_test.txt", "r") as reader:
        data = reader.readlines()
        print(reversed(data))

    with open("new_io_test.txt", "w") as writer:
        for line in reversed(data):
            writer.write(line.strip()+'\n')


with_open_func()
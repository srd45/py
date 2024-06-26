name = "Dave"
count = 1

def greeting(name):
    color = "blue"
    global count
    count += 1
    print(color)
    print(name)
    

greeting("John")

def another():
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("Dave")

another()

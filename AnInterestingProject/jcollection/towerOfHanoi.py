from AnInterestingProject.jcollection.stack import Stack

#Largest disk on bottom, smallest on top

def setup(numberOfDisks):
    rod = Stack()
    for disk in reversed(range(1, numberOfDisks + 1)):
        rod.push(disk)
    return rod

def moveDisk(from_stack, to_stack):
    if to_stack.peek() == None or (to_stack.peek() > from_stack.peek()):
        to_stack.push(from_stack.pop())
    else:
        raise ValueError("Illegal Move Exception")

def doTheHanoi(rod_1):
    rod_2 = Stack()
    rod_3 = Stack()
    moveDisk(rod_1, rod_3)#smallest
    moveDisk(rod_1, rod_2)
    moveDisk(rod_3, rod_2)
    moveDisk(rod_1, rod_3)
    moveDisk(rod_2, rod_1)
    moveDisk(rod_2, rod_3)
    moveDisk(rod_1, rod_3)
    return rod_3

actual = doTheHanoi(setup(3))
expected = setup(3)
print(actual == expected)










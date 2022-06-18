from collections import deque


dq = None
choiceDict =None
choice = None

def popQueue():
    global de, choice, choiceDict
    print(f"Dequeue is now : ******* {de} ************ \n")

    if choice == 5:
        de.popleft()
    if choice == 6:
        de.pop()
    print(f"Dequeue is now : ******* {de} ************ \n")

def rotateQueue():
    global de, choice, choiceDict
    print(f"Dequeue is now : ******* {de} ************ \n")
    rotate = int(input(f"\t\t{choiceDict[choice][1]}"))

    if choice == 3:
        de.rotate(rotate-(2*rotate))
    if choice == 4:
        de.rotate(rotate)
    print(f"Dequeue is now : ******* {de} ************ \n")

def insertQueue():
    global de, choice, choiceDict
    queueElements = input(f"\t\t{choiceDict[choice][1]}").split(" ")
    if choice == 1:
        if len(queueElements) == 1:
            de.append(queueElements[0])
        else:
            de.extendleft(queueElements)
    if choice == 2:
        if len(queueElements) == 1:
            de.append(queueElements[0])
        else:
            de.extend(queueElements)

    print(f"Dequeue is now : ******* {de} ************ \n")
def printMainMenu():
    global de, choiceDict, choice
    print("*"*20)
    print("\t\t1: Insert to the left end of the queue\n")
    print("\t\t2: Insert to the right end of the queue\n")
    print("\t\t3: Rotate queue to the left\n")
    print("\t\t4: Rotate queue to the right\n")
    print("\t\t5: Pop element from left end of the queue:\n")
    print("\t\t6: Pop element from right end of the queue:\n")
    print("\t\t7: exit\n")
    choice = int(input("Enter your choice:  "))

    if choice in [1, 2, 3, 4]:
        choiceDict[choice][0]()

    printMainMenu()

def main():
    global de, choiceDict
    de = deque([])

    choiceDict = {
                             1 : [insertQueue, 'Enter Elements (separated by space) to insert the left end of the queue:'],
                             2 : [insertQueue, 'Enter Elements (separated by space) to insert the right end of the queue:'],
                             3 : [rotateQueue, 'Enter Number of times to rotate queue to the left :'],
                             4 : [rotateQueue, 'Enter Number of times to rotate queue to the right :'],
                             5: [popQueue],
                             6: [popQueue],
                             7: [exit]
                           }
    printMainMenu()


if __name__ == '__main__':
    main()

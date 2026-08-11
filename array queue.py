parking = [None]*5
front = -1
rear = -1
def enqueue(car):
    global front, rear
    if rear == 4:
        print("Parking Full - No space for new car")
    else:
        if front==-1:
            front=0

        rear+=1
        parking[rear]=car
        print("Car Parked:", car)
def dequeue():
    global front, rear
    if front==-1 or front>rear:
        print("Parking is Empty")
    else:
        print("Car Leaving:", parking[front])
        front+=1
def display():
    if front==-1 or front>rear:
        print("Parking is Empty")
    else:
        print("Cars in Parking:", parking[front:rear+1])

while True:
    print("\n===== CAR PARKING MANAGEMENT =====")
    print("1. Park Car")
    print("2. Remove Car")
    print("3. Display Cars")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        car=input("Enter Car Number: ")
        enqueue(car)
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        print("Exiting Parking Management System")
        break
    else:
        print("Invalid Choice")

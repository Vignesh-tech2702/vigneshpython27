

a = list(map(int, input("Enter roll numbers: ").split()))
x = int(input("Enter roll number to search: "))


found = False

for i in range(len(a)):
    if a[i] == x:
        print("Linear Search: Roll number found at position", i + 1)
        found = True
        break

if not found:
    print("Linear Search: Roll number not found")


a.sort()
low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == x:
        print("Binary Search: Roll number found at position", mid + 1)
        found = True
        break
    elif x > a[mid]:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Binary Search: Roll number not found")

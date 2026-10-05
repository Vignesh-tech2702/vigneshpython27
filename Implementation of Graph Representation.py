

n = int(input("Enter number of users: "))


matrix = [[0 for _ in range(n)] for _ in range(n)]


adj_list = [[] for _ in range(n)]

e = int(input("Enter number of connections: "))

print("Enter connections (u v):")

for _ in range(e):
    u, v = map(int, input().split())

    
    matrix[u][v] = 1
    matrix[v][u] = 1

    adj_list[u].append(v)
    adj_list[v].append(u)


print("\nAdjacency Matrix:")
print("   ", end="")
for i in range(n):
    print(i, end=" ")
print()

for i in range(n):
    print(i, ":", end=" ")
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


print("\nAdjacency List:")
for i in range(n):
    print(i, "->", adj_list[i])


u, v = map(int, input("\nEnter two users to check connection: ").split())

print("\nChecking using Adjacency Matrix:")
if matrix[u][v] == 1:
    print(u, "and", v, "are directly connected.")
else:
    print(u, "and", v, "are not directly connected.")

print("\nChecking using Adjacency List:")
if v in adj_list[u]:
    print(u, "and", v, "are directly connected.")
else:
    print(u, "and", v, "are not directly connected.")

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self, data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return

        queue=[self.root]

        while queue:
            current=queue.pop(0)
            if current.left is None:
                current.left=new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right=new_node
                return
            else:
                queue.append(current.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

tree=BinaryTree()
books=["Data Structures" , "Computer Networks" , "Operating Systems" , "Python rogramming"]
for book in books:
    tree.insert(book)
print("Book Titles in Inorder Traversal")
tree.inorder(tree.root)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            current = queue.pop(0)

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    
    def preorder(self, root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)


    
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    
    def search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        return (self.search(root.left, data) or
                self.search(root.right, data))

    
    def delete(self, data):
        if self.root is None:
            print("Tree is empty")
            return

        
        if (self.root.left is None and
                self.root.right is None):

            if self.root.data == data:
                self.root = None
                print(data, "deleted")
            else:
                print(data, "not found")
            return

        queue = [self.root]

        node_to_delete = None
        deepest_node = None
        parent_of_deepest = None

        
        while queue:
            current = queue.pop(0)

            if current.data == data:
                node_to_delete = current

            if current.left:
                parent_of_deepest = current
                deepest_node = current.left
                queue.append(current.left)

            if current.right:
                parent_of_deepest = current
                deepest_node = current.right
                queue.append(current.right)

        if node_to_delete is None:
            print(data, "not found")
            return

        
        node_to_delete.data = deepest_node.data

        
        if parent_of_deepest.right == deepest_node:
            parent_of_deepest.right = None
        else:
            parent_of_deepest.left = None

        print(data, "deleted")




tree = BinaryTree()

books = [
    "Data Structures",
    "Computer Networks",
    "Operating Systems",
    "Python Programming"
]


for book in books:
    tree.insert(book)

print("Books inserted successfully.")



print("\nInorder Traversal:")
tree.inorder(tree.root)



print("\nPreorder Traversal:")
tree.preorder(tree.root)



print("\nPostorder Traversal:")
tree.postorder(tree.root)



book = "Operating Systems"

print("\nSearch Operation:")

if tree.search(tree.root, book):
    print(book, "is found")
else:
    print(book, "is not found")



print("\nBefore Deletion - Inorder:")
tree.inorder(tree.root)

tree.delete("Computer Networks")

print("\nAfter Deletion - Inorder:")
tree.inorder(tree.root)

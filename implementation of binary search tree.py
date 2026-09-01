class LogEntry:
    def __init__(self, visitor_name, entry_time, purpose):
        self.visitor_name = visitor_name
        self.entry_time = entry_time
        self.purpose = purpose


class Node:
    def __init__(self, log):
        self.log = log
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    
    def insert(self, visitor_name, entry_time, purpose):
        new_log = LogEntry(visitor_name, entry_time, purpose)
        new_node = Node(new_log)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if visitor_name.lower() < current.log.visitor_name.lower():

                if current.left is None:
                    current.left = new_node
                    return

                current = current.left

            else:

                if current.right is None:
                    current.right = new_node
                    return

                current = current.right

    
    def search(self, root, visitor_name):

        if root is None:
            return None

        if visitor_name.lower() == root.log.visitor_name.lower():
            return root.log

        if visitor_name.lower() < root.log.visitor_name.lower():
            return self.search(root.left, visitor_name)

        return self.search(root.right, visitor_name)

    
    def delete(self, root, visitor_name):

        if root is None:
            return None

        if visitor_name.lower() < root.log.visitor_name.lower():

            root.left = self.delete(root.left, visitor_name)

        elif visitor_name.lower() > root.log.visitor_name.lower():

            root.right = self.delete(root.right, visitor_name)

        else:
            
            if root.left is None and root.right is None:
                return None

            
            if root.left is None:
                return root.right

            
            if root.right is None:
                return root.left

            
            successor = self.find_min(root.right)

            root.log = successor.log

            root.right = self.delete(
                root.right,
                successor.log.visitor_name
            )

        return root

    
    def find_min(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    
    def inorder(self, root):

        if root is not None:
            self.inorder(root.left)

            print(
                root.log.visitor_name,
                "|",
                root.log.entry_time,
                "|",
                root.log.purpose
            )

            self.inorder(root.right)

    
    def preorder(self, root):

        if root is not None:
            print(
                root.log.visitor_name,
                "|",
                root.log.entry_time,
                "|",
                root.log.purpose
            )

            self.preorder(root.left)
            self.preorder(root.right)

    
    def postorder(self, root):

        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)

            print(
                root.log.visitor_name,
                "|",
                root.log.entry_time,
                "|",
                root.log.purpose
            )

    
    def count(self, root):

        if root is None:
            return 0

        return (
            1
            + self.count(root.left)
            + self.count(root.right)
        )




tree = BinarySearchTree()


tree.insert("Rahul", "09:00 AM", "Meeting")
tree.insert("Anita", "09:30 AM", "Project Discussion")
tree.insert("Suresh", "10:00 AM", "Interview")
tree.insert("Priya", "10:30 AM", "Document Submission")
tree.insert("Kiran", "11:00 AM", "Enquiry")




print("\n========== INORDER TRAVERSAL ==========")
print("Visitor Name | Entry Time | Purpose")
tree.inorder(tree.root)


print("\n========== PREORDER TRAVERSAL ==========")
print("Visitor Name | Entry Time | Purpose")
tree.preorder(tree.root)


print("\n========== POSTORDER TRAVERSAL ==========")
print("Visitor Name | Entry Time | Purpose")
tree.postorder(tree.root)




name = "Suresh"

result = tree.search(tree.root, name)

print("\n========== SEARCH RESULT ==========")

if result is not None:
    print("Visitor Found")
    print("Visitor Name :", result.visitor_name)
    print("Entry Time   :", result.entry_time)
    print("Purpose      :", result.purpose)
else:
    print("Visitor Not Found")


total = tree.count(tree.root)

print("\n========== TOTAL ENTRIES ==========")
print("Total Log Entries:", total)




delete_name = "Anita"

tree.root = tree.delete(tree.root, delete_name)

print("\n========== AFTER DELETION ==========")
print("Deleted Visitor:", delete_name)

tree.inorder(tree.root)

print("\nTotal Entries After Deletion:",
      tree.count(tree.root))

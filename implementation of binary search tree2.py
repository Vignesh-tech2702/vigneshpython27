class Node:
    def __init__(self, entry_time, visitor_name):
        self.entry_time = entry_time
        self.visitor_name = visitor_name
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, entry_time, visitor_name):
        new_node = Node(entry_time, visitor_name)

        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.entry_time < current.entry_time:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, root, entry_time):
        if root is None or root.entry_time == entry_time:
            return root

        if entry_time < root.entry_time:
            return self.search(root.left, entry_time)

        return self.search(root.right, entry_time)

    def delete(self, root, entry_time):
        if root is None:
            return root

        if entry_time < root.entry_time:
            root.left = self.delete(root.left, entry_time)

        elif entry_time > root.entry_time:
            root.right = self.delete(root.right, entry_time)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self._min_value_node(root.right)

            root.entry_time = temp.entry_time
            root.visitor_name = temp.visitor_name

            root.right = self.delete(root.right, temp.entry_time)

        return root

    def _min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def count(self, root):
        if root is None:
            return 0

        return 1 + self.count(root.left) + self.count(root.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(f"Time: {root.entry_time} | Visitor: {root.visitor_name}")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(f"Time: {root.entry_time} | Visitor: {root.visitor_name}")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f"Time: {root.entry_time} | Visitor: {root.visitor_name}")

    # Display function
    def display(self):
        print("\n--- Current Log Book Entries ---")

        if self.root is None:
            print("Log book is empty.")
        else:
            self.inorder(self.root)


def main():
    tree = BinaryTree()

    while True:
        print("\n--- Log Book Management System ---")
        print("1. Insert Log Entry")
        print("2. Delete Log Entry")
        print("3. Search Log Entry")
        print("4. Traverse Log Entries")
        print("5. Count Total Entries")
        print("6. Display Log Entries")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            entry_time = input(
                "Enter entry time (e.g., 09:30 AM): "
            ).strip()

            visitor_name = input(
                "Enter visitor name: "
            ).strip()

            tree.insert(entry_time, visitor_name)

            print("Log entry added successfully!")
            tree.display()

        elif choice == '2':
            entry_time = input(
                "Enter entry time to delete (e.g., 09:30 AM): "
            ).strip()

            if tree.search(tree.root, entry_time):
                tree.root = tree.delete(tree.root, entry_time)

                print("Log entry deleted successfully!")
                tree.display()
            else:
                print("Log entry not found.")
                tree.display()

        elif choice == '3':
            entry_time = input(
                "Enter entry time to search (e.g., 09:30 AM): "
            ).strip()

            result = tree.search(tree.root, entry_time)

            if result:
                print(
                    f"Found! Time: {result.entry_time} | "
                    f"Visitor: {result.visitor_name}"
                )
            else:
                print("Log entry not found.")

            tree.display()

        elif choice == '4':
            print("\nChoose Traversal Type:")
            print("1. Inorder")
            print("2. Preorder")
            print("3. Postorder")

            t_choice = input(
                "Enter traversal choice (1-3): "
            ).strip()

            if tree.root is None:
                print("No log entries found.")

            elif t_choice == '1':
                print("\n--- Inorder Traversal ---")
                tree.inorder(tree.root)

            elif t_choice == '2':
                print("\n--- Preorder Traversal ---")
                tree.preorder(tree.root)

            elif t_choice == '3':
                print("\n--- Postorder Traversal ---")
                tree.postorder(tree.root)

            else:
                print("Invalid traversal choice.")

        elif choice == '5':
            total = tree.count(tree.root)
            print(f"Total entries in log book: {total}")
            tree.display()

        elif choice == '6':
            tree.display()

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


if __name__ == "__main__":
    main()

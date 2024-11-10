class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Recursive function to insert a key in the BST
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    # Public method to initiate insertion
    def insert_value(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert(self.root, key)

    # Function to delete a node
    def delete_node(self, root, key):
        # Base case
        if root is None:
            return root

        # Recursive case to find the node to delete
        if key < root.value:
            root.left = self.delete_node(root.left, key)
        elif key > root.value:
            root.right = self.delete_node(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the in-order successor
            temp = self.find_min(root.right)
            root.value = temp.value
            root.right = self.delete_node(root.right, temp.value)

        return root

    # Function to find the minimum value node
    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    # Helper function to print the tree in-order
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.value, end=" ")
            self.inorder_traversal(root.right)

    # Public method to initiate deletion and print
    def delete_and_print(self, key):
        print(f"Deleting {key}...")
        self.root = self.delete_node(self.root, key)
        self.inorder_traversal(self.root)
        print("\n")

# Initialize the tree
bst = BinarySearchTree()
values = [42, 12, 53, 8, 16, 2, 22, 19, 60, 57, 65]
for value in values:
    bst.insert_value(value)

# Perform deletions as specified and print the tree after each deletion
bst.delete_and_print(16)  # Remove node 16
bst.delete_and_print(12)  # Remove node 12
bst.delete_and_print(42)  # Remove node 42

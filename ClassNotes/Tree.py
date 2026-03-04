class Node:
    def __init__(self, data):
        # Constructor
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        # Tree starts empty
        self.root = None

    def insert(self, data):
        # Insert method (level-order for simplicity)
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

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

bt = BinaryTree()

bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)

print("Inorder:")
bt.inorder(bt.root)

print("\nPreorder:")
bt.preorder(bt.root)

print("\nPostorder:")
bt.postorder(bt.root)
from node import Node

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def insert(self, root, obj):
        if root is None:
            return Node(obj)
        
        if obj.grade < root.element.grade:
            root.left = self.insert(root.left, obj)
        else:
            root.right = self.insert(root.right, obj)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and obj.student_id < root.left.element.student_id:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and obj.student_id > root.right.element.student_id:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and obj.student_id > root.left.element.student_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and obj.student_id < root.right.element.student_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def display(self, root):
        if root is not None:
            self.display(root.left)
            print(root.element)
            self.display(root.right)

    def search(self, root, match_function):
        if root is None:
            return None
        
        if match_function(root.element):
            return root.element
        
        left = self.search(root.left, match_function)

        if left:
            return left

        return self.search(root.right, match_function)

    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def display_tree_diagram(self, node, indent="", last=True):
    
        if node is not None:
            # Print the current indentation
            print(indent, end="")

            # Print branch
            if last:
                print("└── ", end="")
                indent += "    "
            else:
                print("├── ", end="")
                indent += "│   "

            # Print current node (you can include more info)
            print(f"{node.element.name}({node.element.grade})[{node.element.student_id}]")

            # Recurse: left first, then right
            self.display_tree_diagram(node.left, indent, False)
            self.display_tree_diagram(node.right, indent, True)
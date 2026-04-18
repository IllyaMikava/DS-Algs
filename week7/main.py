from binary_tree import BinaryTree

if __name__ == "__main__":
    print("====================================")
    print("Binary Tree Demo")
    print("====================================\n")

    tree = BinaryTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)

    print("Binary Tree created with root value 10 and added values 5, 15, 3, 7.")

    print("Inorder Traversal of the Binary Tree:")
    tree.inorder(tree.root)

    print("\n\nPreorder Traversal of the Binary Tree:")
    tree.preorder(tree.root)

    print("\n\nPostorder Traversal of the Binary Tree:")
    tree.postorder(tree.root)   
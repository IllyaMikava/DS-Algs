from avl_tree import AVLTree
from student import Student

def main():
    avl = AVLTree()

    root = None
    
    root = avl.insert(root, Student("Alice", 85, 1001))
    root = avl.insert(root, Student("Bob", 90, 1002))
    root = avl.insert(root, Student("Charlie", 80, 1003))
    root = avl.insert(root, Student("David", 95, 1004))
    root = avl.insert(root, Student("Eve", 88, 1005))

    print("in-order traversal of the AVL tree:")
    avl.display(root)

    student = avl.search(root, lambda s: s.name == "Bob")

    if student:
        print(f"Student found: {student.name}, Grade: {student.grade}")
    else:
        print("Student not found.")

    print("AVL Tree Diagram:")
    avl.display_tree_diagram(root)

if __name__ == "__main__":
    main()
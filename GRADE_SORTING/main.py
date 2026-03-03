import csv
import os
import time
from models.student import Student
from data_loader.data_loader import DataLoader
from sorter.bubble_sort import BubbleSort


base_dir = os.path.dirname(__file__)  # folder where main.py is
file_path = os.path.join(base_dir, "data", "students.csv")
file_path1 = os.path.join(base_dir, "data_loader", "data_loader.py")


if __name__ == "__main__":
    loader = DataLoader(file_path)
    
    # student_data = loader.get_all_data()
    # student_data = loader.get_by_module("Generative AI")
    
    student_data = loader.get_data_by_size(1000) # Get only first 1000 records for testing
    print(f"Loaded {len(student_data)} student records.")

    bubble_sort = BubbleSort()

    start = time.perf_counter()
    bubble_sorted_students = bubble_sort.sort(
        student_data, 
        key=lambda s: s.grade
    )
    end = time.perf_counter()
    
    print(f"Execution time: {end - start:.6f} seconds")

    # print the last 10 students (highest grades)
    print("Top 10 students in Generative AI:")
    for student in bubble_sorted_students[-10:][::-1]:
        print(student)
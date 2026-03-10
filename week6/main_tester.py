import time
import os
import matplotlib.pyplot as plt
from data_loader.data_loader import SalesDataLoader
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort

def time_sort(sorter, data, key_function, runs=3):
    """
    Returns average execution time over multiple runs
    (reduces timing noise).
    """
    total = 0
    for _ in range(runs):
        data_copy = data.copy()
        start = time.perf_counter()
        sorter.sort(data_copy, key=key_function)
        end = time.perf_counter()
        total += (end - start)
        
    return total / runs

def main():
    dataset_sizes = [250, 500, 1000, 2000, 4000, 8000, 16000]
    
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "data", "sales.csv")

    loader = SalesDataLoader(csv_path)
    loader.load_data()
    
    algorithms = {
        "Bubble Sort": BubbleSort(),
        "Selection Sort": SelectionSort(),
        "Insertion Sort": InsertionSort(),
        "Quick Sort": QuickSort(),
        "Merge Sort": MergeSort(),
    }
    
    key_function = lambda sale: sale.total_sales
    
    # Store results
    results = {name: [] for name in algorithms.keys()}
    
    print("\nRunning automated performance analysis...\n")
    
    for size in dataset_sizes:
        print(f"Dataset size: {size}")
        data = loader.get_data_by_size(size)
        
        for name, sorter in algorithms.items():
            elapsed = time_sort(sorter, data, key_function)
            results[name].append(elapsed)
            print(f"  {name}: {elapsed:.6f} seconds")
            
        print()
        
    # ---------------------------
    # Plot Results
    # ---------------------------
    plt.figure()
    
    for name, times in results.items():
        plt.plot(dataset_sizes, times, label=name)
        
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Performance Comparison")
    plt.legend()
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    main()
from data_loader.data_loader import SalesDataLoader
from business.company import Company
from sorter.bubble_sort import BubbleSort
from sorter.insertion_sort import InsertionSort
from sorter.merge_sort import MergeSort
from sorter.quick_sort import QuickSort
from sorter.selection_sort import SelectionSort
import time
import os

def print_menu():
    print("\n========== Sales Data Menu ==========")
    print("1. Show total sales count")
    print("2. Show total revenue")
    print("3. Choose sorting algorithm")
    print("4. Sort sales (using selected algorithm)")
    print("5. Show Top N sales")
    print("6. Exit")
    print("=======================================")

def choose_sorter():
    print("\nChoose Sorting Algorithm:")

    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    print("5. Merge Sort")

    choice = input("Enter choice: ")

    match choice:

        case "1":
            return BubbleSort()

        case "2":
            return SelectionSort()

        case "3":
            return InsertionSort()

        case "4":
            return QuickSort()

        case "5":
            return MergeSort()

        case _:
            print("Invalid choice. Defaulting to Quick Sort.")
            return QuickSort()
        
def main():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "data", "sales.csv")

    loader = SalesDataLoader(csv_path)
    loader.load_data()
    sales_data = loader.get_all_data()

    company = Company("techCorp", sales_data)

    current_sorter = QuickSort()

    while True:
        print_menu()
        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                print("Total Sales Records:",company.total_sales_count())
            case "2":
                print("Total Revenue:",company.total_revenue())
            case "3":
                current_sorter = choose_sorter()
                print("Sorting algorithm selected successfully.")
            case "4":
                start = time.perf_counter()
                sorted_sales = company.sort_sales(
                                        current_sorter,
                                        key_function=lambda x: x.total_sales)

                end = time.perf_counter()

                print(f"\nSorting completed in {end - start:.6f}seconds.")
                print("First 5 results:")
                for sale in sorted_sales[:5]:
                    print(sale)
            
            case "5":
                n = int(input("Enter N: "))
                print(f"Retrieving top {n} sales using {current_sorter.__class__.__name__}...")
            
                # These lines must be indented to stay inside the case block
                top_sales = company.get_top_sales(current_sorter, n)
            
                print(f"\nTop {n} Sales:")
                for sale in top_sales:
                    print(sale)
                
            case "6":
                print("EXITING PROGRAM...")
                break

            case _:
                print("invalid choice!!!")

if __name__ == "__main__":
    main()
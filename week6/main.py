import time
import os
from data_loader.data_loader import SalesDataLoader
from business.company import company
from sorter.bubble_sort import BubbleSort

if __name__ == "__main__":

    print("====================================")
    print("Sales Company Sorting Demo")
    print("====================================\n")

    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "data", "sales.csv")

    loader = SalesDataLoader(csv_path)
    loader.load_data()  # don't forget this line!

    # Load only the first 1000 records for testing
    sales_data = loader.get_data_by_size(1000)

    print(f"Loaded {len(sales_data)} sales records.\n")

    # -----------------------------------
    # 2. Create Company Object
    # -----------------------------------
    company = company("TechCorp", sales_data)

    print("Company Summary:")
    print(f"Total Records: {company.total_sales_count()}")
    print(f"Total Revenue: {company.total_revenue():,.2f}\n")

    # -----------------------------------
    # 3. Choose Sorting Algorithm
    # -----------------------------------
    bubble_sort = BubbleSort()

    # -----------------------------------
    # 4. Time Sorting Operation
    # -----------------------------------
    start = time.perf_counter()

    sorted_sales = company.sort_sales(
        bubble_sort,
        key_function=lambda sale: sale.total_sales
    )

    end = time.perf_counter()

    print(f"Sorting Time: {end - start:.6f} seconds\n")

    # -----------------------------------
    # 5. Display Top 10 Sales
    # -----------------------------------
    print("Top 10 Sales (Highest Total Sales):\n")

    # Since Bubble Sort sorts in ascending order,
    # we retrieve the top 10 by iterating backwards
    top_sales = company.get_top_sales(
        bubble_sort,
        n=10
    )

    for sale in top_sales:
        print(sale)

    print("\nDemo Complete.")
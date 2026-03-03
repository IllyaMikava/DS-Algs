class company:
    def __init__(self, name, sales_list=None):
        self.name = name
        self.__sales = sales_list if sales_list is not None else []

    def add_sale(self, sale):
        self.__sales.append(sale)

    def get_sales(self):
        return self.__sales.copy()
    
    def total_sales_count(self):
        return len(self.__sales)
    
    def sort_sales(self, sorter, key_function = lambda x: x):
        return sorter.sort(self.__sales, key = key_function)
    
    def total_revenue(self):
        return sum(sale.total_sales for sale in self.__sales) 
    
    def get_top_sales(self, sorter, n=10):
    # Step 1: Use the sorting algorithm
        sorted_sales = sorter.sort(
                       self.__sales,
                       key=lambda x: x.total_sales
                        )

    # Step 2: Collect top N using backward while loop
        top_sales = []
        index = len(sorted_sales) - 1  # Start at last element

        while index >= 0 and len(top_sales) < n:
            top_sales.append(sorted_sales[index])
            index -= 1  # Move backwards

        return top_sales
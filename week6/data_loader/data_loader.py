import csv
from models.sale import Sale

class SalesDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.__sales = []
    
    def load_data(self):
        with open(self.file_path, newline='',encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sale = Sale(
                    transaction_id=row['Transaction_ID'],
                    product=row['Product'],
                    region=row['Region'],
                    quantity=row['Quantity'],
                    unit_price=row['Unit_Price'],
                    total_sales=row['Total_Sales'],
                    date=row['Date'])
                
                self.__sales.append(sale)
    
    def get_all_data(self):
        return self.__sales.copy()
    
    def get_data_by_size(self, size):
        if size < 0:
            raise ValueError("size must be non negatative!!")
        
        return self.__sales[:size]
    
    def get_by_product(self, product_name):
        results = []

        for sale in self.__sales:
            if sale.product == product_name:
                results.append(sale)

        return results

    def get_by_region(self, region_name):
        results = []

        for sale in self.__sales:
            if sale.region == region_name:
                results.append(sale)
            
        return results
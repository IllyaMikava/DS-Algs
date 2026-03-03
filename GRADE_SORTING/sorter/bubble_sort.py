from sorter.sorter_adt import Sorter

class BubbleSort(Sorter):
    def sort(self, data, key = lambda x: x):
        n = len(data)
        arr = data.copy()

        for i in range(n):
            for j in range(0, n - 1):
                if key(arr[j]) > key(arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
        return arr
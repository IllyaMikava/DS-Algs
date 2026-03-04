from sorter.sorter_adt import Sorter

class InsertionSort(Sorter):
    def sort(self, data, key = lambda x:x):
        arr = data.copy()

        for i in range(1, len(data)):

            current = arr[i]
            j = i - 1

            while j >= 0 and key(current) < key(arr[j]):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = current

        return arr
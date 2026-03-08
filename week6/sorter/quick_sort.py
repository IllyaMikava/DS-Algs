from sorter.sorter_adt import Sorter


class QuickSort(Sorter):

    def sort(self, data, key=lambda x: x):

        arr = data.copy()
        self.quickSort(arr, 0, len(arr) - 1, key)
        return arr


    def partition(self, arr, low, high, key):

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            if key(arr[j]) < key(pivot):
                i += 1
                self.swap(arr, i, j)

        self.swap(arr, i + 1, high)

        return i + 1


    def swap(self, arr, i, j):

        arr[i], arr[j] = arr[j], arr[i]


    def quickSort(self, arr, low, high, key):

        if low < high:

            pi = self.partition(arr, low, high, key)

            self.quickSort(arr, low, pi - 1, key)
            self.quickSort(arr, pi + 1, high, key)
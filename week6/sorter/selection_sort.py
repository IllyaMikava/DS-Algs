from sorter.sorter_adt import Sorter

class SelectionSort(Sorter):

    def sort(self, data, key=lambda x: x):

        arr = data.copy()
        n = len(arr)

        for i in range(n):

            # assume first unsorted element is minimum
            min_index = i

            # find the actual minimum element
            for j in range(i + 1, n):
                if key(arr[j]) < key(arr[min_index]):
                    min_index = j

            # swap
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr
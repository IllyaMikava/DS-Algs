from sorter.sorter_adt import Sorter

class MergeSort(Sorter):

    def sort(self, data, key=lambda x: x):

        arr = data.copy()
        self.merge_sort(arr, key)
        return arr


    def merge_sort(self, arr, key):

        if len(arr) > 1:

            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            # recursive calls
            self.merge_sort(left, key)
            self.merge_sort(right, key)

            i = j = k = 0

            # merge the two halves
            while i < len(left) and j < len(right):

                if key(left[i]) <= key(right[j]):
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1

                k += 1

            # copy remaining elements
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
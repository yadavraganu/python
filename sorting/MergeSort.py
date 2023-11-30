# Complexity : O(n2)
# Space Complexity : O(1)
class MergeSort:
    def sort(self, lst: list[int]) -> list[int]:
        if len(lst) > 1:
            mid = len(lst)//2
            left = lst[:mid]
            right = lst[mid:]
            self.sort(left)
            self.sort(right)
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                lst[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                lst[k] = right[j]
                j += 1
                k += 1


Obj = MergeSort()
Input = [1, 23, 2, 5, 1, 0, 66, 4, 2, 1, 1, 3, 3, 5, 5]
Obj.sort(Input)
print(Input)
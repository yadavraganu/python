# Complexity : O(n2)
# Space Complexity : O(1)
class SelectionSort:
    def sort(self, lst: list[int]) -> list[int]:
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst


Obj = SelectionSort()
Input = [1, 23, 2, 5, 1, 0, 66, 4, 2, 1, 1, 3, 3, 5, 5]
print(Obj.sort(Input))
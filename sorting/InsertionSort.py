# Complexity : O(n2)
# Space Complexity : O(1)
class InsertionSort:
    def sort(self, lst: list[int]) -> list[int]:
        for i in range(1, len(lst)):
            while lst[i - 1] > lst[i] and i > 0:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                i -= 1
        return lst


Obj = InsertionSort()
Input = [1, 23, 2, 5, 1, 0, -1, 4, 22, 1, 1, 3, 3, 5, 5]
print(Obj.sort(Input))

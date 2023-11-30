# Complexity : O(n2)
# Space Complexity : O(1)
class BubbleSort:
    def sort(self, lst: list[int]) -> list[int]:
        swap = True
        while swap:
            swap = False
            for i in range(0, len(lst)-1):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swap = True
        return lst


Obj = BubbleSort()
Input = [1, 23, 2, 5, 1, 0, 66, 4, 2, 1, 1, 3, 3, 5, 5]
print(Obj.sort(Input))

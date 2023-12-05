# Complexity : O(Nlog(N))
# Space Complexity : O(log(N))
class QuickSort:
    def partition(self, lst, low, high, debug = True):
        if debug:
            print('=' * 40)
            print(f"Calling partition function with low = {low},high = {high},lst = {lst}\n")
        i = low + 1
        j = high
        pivot = lst[low]
        while True:
            if debug:
                print(f"Outer While Start Loop i = {i}, j = {j}, pivot value = {pivot} ,lst = {lst}")
            while i <= j and lst[i] <= pivot:
                i += 1
            while i <= j and lst[j] >= pivot:
                j -= 1
            if i <= j:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                if debug:
                    print(f"Outer While Loop End i = {i}, j = {j}, pivot value = {pivot} ,lst = {lst}")
                break
        lst[j], lst[low] = lst[low], lst[j]
        if debug:
            print(f"\nPivot Index is = {j}")
        return j

    def sort(self, lst, low, high, debug = True):
        if debug:
            print('=' * 50)
            print(f"Calling sort function with low = {low},high = {high},lst = {lst}")
        if low < high:
            pivot = self.partition(lst, low, high, debug)
            self.sort(lst, low, pivot-1, debug)
            self.sort(lst, pivot + 1, high, debug)


Obj = QuickSort()
Input = [1, 23, 2, 5, 1, 0, 66, 4, 2, 1, 1, 3, 3, 5, 5]
Obj.sort(Input,0, len(Input)-1,False)
print(Input)

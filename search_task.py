class Task():
    arr = []
    x = 0
    def __init__(self,arr,x):
        self.arr = arr
        self.x = x
    
    def refuct(self):
        arr = self.arr[-1:]+self.arr[:-1]
        return arr

    def search(self):
        low = 0
        high = len(self.arr) - 1
        mid = 0
        while low <= high:
    
            mid = (high + low) // 2
    
            if arr[mid] < self.x:
                low = mid + 1
    
            elif arr[mid] > self.x:
                high = mid - 1
    
            else:
                return mid
    
        return -1


 
arr = [ 1,2, 3, 4, 10, 20,30 ]
x = 3

result = Task(arr, x)
print(result.search())

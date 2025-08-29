class Solution:
    def reverseArray(self, arr):
        # code here
        start = 0
        end = len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]  # swap
            start += 1
            end -= 1
        
        
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    sol = Solution()
    sol.reverseArray(arr)
    print("Reversed array:", *arr)
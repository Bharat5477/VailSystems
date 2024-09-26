# left rotate
class Solution:
    def rotateleft(self, arr, k):
        print("Original Array ", arr)
        n = len(arr)
        if k < 0:
            return "Use Positive value"
        k = k % n
        temp = [0] * n
        for i in range(n - k):
            temp[i] = arr[k + i]
        print("After moving last k element to front -> ", temp)

        for i in range(k):
            temp[n - k + i] = arr[i]
        print("After moving first k elements to to last -> ", temp)

        for i in range(n):
            arr[i] = temp[i]
        return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    rotatedArray = Solution().rotateleft(arr, k)
    print("Rotate Array after ", k, "rotate -> ", rotatedArray)

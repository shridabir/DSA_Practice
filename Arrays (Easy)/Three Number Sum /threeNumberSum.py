#two pointer approach O(n^2) time | O(n) space to store triplets
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    n = len(array)
    triplets = []

    for i in range (n - 2):
        #skip duplicates for the first number
        if i > 0 and array[i] == array[i - 1]:
            continue

        left = i + 1
        right = n - 1
        while left < right:
            summ = array[i] + array[left] + array[right]
            if summ == targetSum:
                triplets.append([array[i], array[left], array[right]])
                # Check 1: Skip duplicates for the left pointer
                while left < right and array[left] == array[left + 1]:
                    left += 1
                # Check 2: Skip duplicates for the right pointer
                while left < right and array[right] == array[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif summ < targetSum:
                left += 1
            else:
                right -= 1

    return triplets

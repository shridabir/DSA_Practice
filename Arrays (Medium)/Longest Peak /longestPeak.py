def longestPeak(array):
    # Write your code here.
    longestPeakLength = 0
    i = 1 #start from 2nd ele as first ele can't be a peak

    while i < len(array) - 1:
        #find the peaks
        isPeak = array[i - 1] < array[i] and array[i + 1] < array[i]

        #if ele is not a peak continue searching for it
        if not isPeak:
            i += 1
            continue

        #if ele is a peak:
        #keep looking to left side until there are strictly decreasing elements
        leftIdx = i - 2 #we already know i - 1 is < i. So start from i - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        #similarly for right side
        rightIdx = i + 2 # we already know i + 1 is > i. So start from i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        #find length of current peak
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightIdx #calculate len for next peaks

    return longestPeakLength
    pass

def mergeOverlappingIntervals(intervals):
    # Write your code here.
    #sort the intervals according to first value of interval
    sortedIntervals = sorted(intervals, key = lambda x: x[0])

    mergedIntervals = [] #output array
    currentInterval = sortedIntervals[0] #first interval is current
    #add it in output array
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval #we care only about end of current Interval as we will update that if overlaps
        nextIntervalStart, nextIntervalEnd = nextInterval

        #overlap condition
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd) #update the end of currentInterval with max of ends of both intervals
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
            
    return mergedIntervals

  

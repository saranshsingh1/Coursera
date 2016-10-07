with open("QuickSort.txt", 'r') as f:
	array = [int(i.strip()) for i in f.readlines()]

fcomparison = 0
mcomparison = 0
lcomparison = 0

def quicksortLast(array, start, end):
    '''Recursive calls to QuickSort when pivot is last element'''

    if start >= end: return

    pivot = partitionLast(array, start, end)

    quicksortLast(array, start, pivot-1)
    quicksortLast(array, pivot+1, end)
    return array


def partitionLast(array, begin, end):
    '''Partition Subroutine when Pivot is last element'''

    array[begin], array[end] = array[end], array[begin]
    global lcomparison
    i = begin
    for j in range(begin+1, end+1):
        lcomparison += 1
        if array[j] <= array[begin]:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[i], array[begin] = array[begin], array[i]
    return i


def quicksortMedian(array, start, end):
    '''Recursive calls to QuickSort when pivot is median of 3 elements'''

    if start >= end: return

    pivot = partitionMedian(array, start, end)

    quicksortMedian(array, start, pivot-1)
    quicksortMedian(array, pivot+1, end)
    return array

def partitionMedian(array, begin, end):
    '''Partition Subroutine when Pivot is Median'''
    global mcomparison
    left, right = array[begin], array[end]
    if not len(array) % 2:
        middle = array[len(array) // 2]
    else:
        middle = array[(len(array) // 2) + 1]

    pivotIndex = median(left, middle, right)

    array[begin], array[pivotIndex] = array[pivotIndex], array[begin]

    i =  begin
    for j in range(begin+1, end+1):
        mcomparison += 1
        if array[j] < array[begin]:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i], array[begin] = array[begin], array[i]
    return i


def median(a, b, c):
    return (sum([a, b, c]) - min(a, b, c) - max(a, b, c))


def quicksortFirst(array, start, end):
    '''Recursive calls to QuickSort when pivot is first element'''

    if start >= end: return

    pivot = partitionFirst(array, start, end)

    quicksortFirst(array, start, pivot-1)
    quicksortFirst(array, pivot+1, end)
    return array


def partitionFirst(array, begin, end):
    '''Partition Subroutine when Pivot is 1st element'''

    global fcomparison
    i = begin
    for j in range(begin+1, end+1):
        fcomparison += 1
        if array[j] <= array[begin]:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[i], array[begin] = array[begin], array[i]
    return i

# quicksortFirst(array, 0, len(array)-1) ---> 162085
# quicksortLast(array, 0, len(array)-1) ---> 164123
# quicksortMedian(array, 0, len(array)-1) ---> 138382
# print mcomparison
# print lcomparison
# print fcomparison

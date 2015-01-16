# zeroes out repeats

def zeroOut(arr):
    s = set()

    print "Before:", arr

    for i in xrange(len(arr)):
        element = arr[i]
        if(element in s):
            arr[i] = 0
        else:
            s.add(element)

    print "After: ", arr

    print

    return arr


zeroOut([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0])
zeroOut([1,1,2,2,3,3,4,4])
zeroOut([1] * 5)
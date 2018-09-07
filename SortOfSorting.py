from week10 import HashTable
import math

def insertion_sort(lis):
    '''
    sorts stuff
    '''
    for curr_i in range(1, len(lis)):
        # i is the curr_i
        item = lis[curr_i]
        j = curr_i - 1
        while j >= 0 and item < lis[j]:
            lis[j+1], lis[j] = lis[j], lis[j+1]
            j -= 1
        #lis[j+1] = item


def _merge(lis1, lis2):
    '''
    '''
    result = []
    while len(lis1) > 0 and len(lis2) > 0:
        if lis1[0] > lis2[0]:
            result.append(lis2.pop(0))
        else:
            result.append(lis1.pop(0))
    if len(lis1) == 0:
        result += lis2
    elif len(lis2) == 0:
        result += lis1
    return result

def merge_sort(lis):
    '''
    sorts stuff recursively
    '''
    if len(lis) <= 1:
        result = lis
    else:
        left = merge_sort(lis[:len(lis)//2])
        right = merge_sort(lis[len(lis)//2:])
        result = _merge(left, right)
    return result


def quick_sort(lis):
    '''
    sorts stuff by chopping into three eh
    '''
    l, e, g = [],[],[]
    if len(lis) <= 1:
        result = lis
    else:
        pivot = lis[0]
        for item in lis:
            if item > pivot:
                g.append(item)
            elif item == pivot:
                e.append(item)
            else:
                l.append(item)
        if len(l) > 1:
            l = quick_sort(l)
        if len(g) > 1:
            g = quick_sort(g)
        result = l + e + g
    return result


def in_place_qs(lis):
    '''
    dicks
    '''
    pivot = lis[0]
    l, r = 1, len(lis) - 1
    while l <= r:
        if lis[l] < pivot:
            l += 1
        elif lis[i] > pivot:
            r -= 1
        else:
            lis[r], lis[l] = lis[l], lis[r]
    pivot, lis[r] = lis[r], pivot
    result = in_place_qs(lis)

    return result


def partition(lis, left, right):
    '''
    parts the titions
    '''
    if left < right:
        # arbitrarily choose pivot, we choose first item to avoid bounds
        pivot = lis[left]
        # keep track of original left and right
        leftmost = left
        rightmost = right
        p_index = left  # pivot index always lefmost item
        left += 1 #  go up by one in the left index before starting loop
        dunce = False
        while not dunce:
            # keep increasing left index until it either crosses right, or
            # once the item at the left index is smaller than the pivot. (L)
            while left <= right and lis[left] <= pivot:
                left += 1
            # keep decreasing right index until it either crosses left, or
            # once the item at the right index is larger than the pivot. (G)
            while right >= left and lis[right] >= pivot:
                right -= 1
            # if the left index hasnt crossed the right index, switch the
            # items at those indexes, and continue the while loop
            if left < right:
                lis[left], lis[right] = lis[right], lis[left]
            # if the left index crosses the right index, that means that
            # every item has been scanned through, and we can exit loop
            else:
                dunce = True
        # after, we gotta switch the original leftmost indexed item with the
        # current changed up right indexed item
        lis[leftmost], lis[right] = lis[right], lis[leftmost]
        # finally, recursively continue to sort the left and right parts of
        # the list from where our left and right indices crossed.
        partition(lis, p_index, right-1)
        partition(lis, right+1, rightmost)
        # list mutation happens.


def ipqs(lis):
    '''
    '''
    partition(lis, 0, len(lis)-1)
    return lis



def hash_sort(lis):
    ''' lis gotta have stuff from 0 - 100 '''
    hash_t = HashTable(100)
    for item in lis:
        hash_t.put(item)
        new_lis = []
    for item in hash_t._array:
        if type(item) == list:
            new_lis = new_lis + item
        elif item != None:
            new_lis.append(item)
    return new_lis


def uhh(n):
    side = (((-2)*math.cos(2*math.pi/n)+2)**0.5)*n
    return side

thing = uhh(99999)/2
print(thing)
def pascal(k):
    ''' int -> (list)
	generates k first rows of pascals triangle stored in a list
	'''
    # base case, k is one
    if k == 1:
        array = [1]
    elif k == 2:
        array = [1,1]
    else:
        array = [1]
        prev = pascal(k-1)
        for i in range(1, len(prev)):
            new = prev[i] + prev[i-1]
            array.append(new)
        array.append(1)
    return array

def print_pascal(k):
    ''' int -> (none)
	prints the pascal triangle up to layer k
	'''
    for i in range(1, k+1):
        string = ''
        line = pascal(i)
        while len(line) != 0:
            string += str(line.pop()) + ' '
        print(string, '\n')
        


def linear_rec(k):
    ''' (int) -> (int, int)
    '''
    if k == 2:
        i, j = (1, 1)
    else:
        temp_i, temp_j = linear_rec(k-1)
        i, j = temp_j, (3*temp_j + 4*temp_i)
    return (i, j)

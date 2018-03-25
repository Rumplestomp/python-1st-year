def finer(s):
    '''
    '''
    if len(s) <= 2:
        result = s
    else:
        result = s[0] + finer(s[2:]) + s[1]
    return result

def second_to_last(s):
    '''
    '''
    ours = s
    curr = finer(s)
    nex = finer(curr)
    while nex != ours:
        curr = nex
        nex = finer(curr)
    return (curr)

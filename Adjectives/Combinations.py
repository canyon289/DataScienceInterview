from itertools import combinations

def cl(n,k):
    '''
    k combination of out length n set
    '''
    return len(list(combinations(range(n),k)))
    
numerator =  cl(5,4) * cl(19,1) + cl(5,5)*cl(19,0)
denominator = cl(24, 5)

numerator/denominator
import pytest
from MinSmallNetwork import find_max_min_strong

def test_circular():
    '''
    Tests to make sure circular add is working correctly
    '''
    n = find_max_min_strong(3,1)
    assert n.add_edge(0,4) == {0:{1}, 1:{0}, 2:set()}
    return
    
def test_simple_three():
    n = find_max_min_strong(3,3)
    assert n.create_network() == {0: {1,2}, 1: {0,2}, 2: {0,1}}
    

def test_strong_four():
    n = find_max_min_strong(4,6)
    true_value = {0:{1,2,3}, 1:{0,2,3}, 2:{0,1,3}, 3:{0,1,2}}
    assert n.create_network() == true_value
'''
Given a matrix of friends find all the circles
'''
import ipdb
import datetime
from read_files import 


def read_answers(file_num):
    file_name = "output/output0{0}.txt".format(file_num)

    with open(file_name, 'r') as file:
        ans = file.read()
    return int(ans)


def read_matrix(file_num):
    '''
    Reads in input file and creates friends dictionary
    '''
    
    file_name = "input/input0{0}.txt".format(file_num)

    with open(file_name, 'r') as file:
        input_list = file.read().split("\n")
    n = input_list.pop(0)

    #Construct friends dict
    relationships = {}
    for num_person, friends in enumerate(input_list):
        relationships[str(num_person)] = []

        for num_friend, friend in enumerate(friends):
            if friend == 'Y' and str(num_friend) != str(num_person):
                relationships[str(num_person)].append(str(num_friend))
                
    return relationships


def expand_tree(top_level, relationships):
    '''
    Given a top level person expand their friends group as much as possible
    finding every path of friends

    The big assumption I'm making here is that if I make a complete tree
    of friends with no repeats in the path itll be the complete path of friends
    '''

    finished_path = []
    to_expand = [top_level]

    while len(to_expand) > 0:
        path = to_expand.pop(0)
        last_friend = path[-1]
        remaining_nodes = (set(relationships[last_friend]) - set(path))

        if len(remaining_nodes) == 0:
            finished_path.append(path)
        else:
            for friend in remaining_nodes:
                to_expand.append(path + friend)

    return finished_path

def compile_trees(relationships):
    '''
    Expand all the friend trees and find the unique number of sets of friends
    '''
    compiled_sets = []
    for top_level in relationships:
        compiled_sets += expand_tree(top_level, relationships)

    #Get only unique sets
    unique_set = list(set([frozenset(circle) for circle in compiled_sets]))
    unique_set.sort(key = len, reverse = True)

    #Get the largest circles

    large_friend_circle = []

    finished = False
    while finished == False:
        large_set = unique_set.pop(0)
        remaining_sets = []

        for small_set in unique_set:
            if len(small_set-large_set) > 0:
                remaining_sets.append(small_set)
        large_friend_circle.append(large_set)

        if len(remaining_sets) > 0:
            unique_set = remaining_sets

        else:
            finished = True

    return len(large_friend_circle)

    
for num in range(10):
    relationships = read_matrix(num)
    ans = find_circles(relationships)
    answer = read_answers(num)
    correct = (ans == answer)
    print("{0} Correct:{1}".format(ans,correct))
'''
The second iteration of the friends finding algorithm
'''

import ipdb

def read_answers(file_num):
    file_name = "output/output0{0}.txt".format(file_num)

    with open(file_name, 'r') as file:
        ans = file.read()
    return int(ans)


def read_input(file_num):
    file_name = "input/input0{0}.txt".format(file_num)
    
    with open(file_name, 'r') as file:
        input_list = [line.strip() for line in file.readlines()]
    
    n = input_list.pop(0)
    return input_list

    
def read_matrix(input_list):
    '''
    Reads in input file and creates friends dictionary
    '''

    #Construct friends dict
    relationships = {}
    for num_person, friends in enumerate(input_list):
        relationships[str(num_person)] = []

        for num_friend, friend in enumerate(friends):
            if friend == 'Y' and str(num_friend) != str(num_person):
                relationships[str(num_person)].append(str(num_friend))
            
    return relationships


def find_circles(friends_dict):
    '''
    Iterate through friends dict to find friends
    '''


    def find_friends(person):
        '''
        Recursive function that does Depth First Search of all friends
        '''
        if person not in visited:
            visited.append(person)
            for friend in friends_dict[person]:
                find_friends(friend)
            return
        return

    visited = []
    circle = 0
    root = []
    for person in range(len(friends_dict)):
        person = str(person)
        if person not in visited:
            find_friends(person)
            circle +=1
    return circle
    


for num in range(10):
    input_text = read_input(num)
    relationships = read_matrix(input_text)
    ans = find_circles(relationships)
    answer = read_answers(num)
    correct = (ans == answer)
    print("{0} Correct:{1}".format(ans,correct))


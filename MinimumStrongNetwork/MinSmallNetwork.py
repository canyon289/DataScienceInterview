'''
Finds the minimum strongest network given nodes and edges
'''
import ipdb

class find_max_min_strong():

    def __init__(self, max_n, max_edges):
        self.max_n = max_n
        self.max_edges = max_edges
        self.relationships = {n:set() for n in range(max_n)}
        self.edges_placed = 0
        return


    def add_edge(self, source, target):
        if target >= self.max_n:
            target = target % (self.max_n)

        if target not in self.relationships[source]:
            self.relationships[source].add(target)
            self.relationships[target].add(source)

            self.edges_placed +=1
        return self.relationships


    def create_network(self):
        base_adder = 1
        loop_adder = 0
        n =0

        #Add all the loops
        while self.edges_placed < self.max_edges:
            #While adder is less than max n
            while (base_adder + loop_adder)  < self.max_n:
                #While the node being iterated is less than the maximum
                while n < self.max_n:

                    #Stop adding edges if all are placed
                    if self.edges_placed == self.max_edges:
                        break
                    else:
                        self.add_edge(n, n+(loop_adder+base_adder))
                        n+=1

                #Continue connectiong nodes
                loop_adder += 2
                n = 0
            #Strong Connections Start
            base_adder += 1
            loop_adder = 0

        print("All Edges Placed")
        print("Last Nodes {0}:{1}".format(n, n+(loop_adder+base_adder)))

        answer = self.min_max_strong_num(n, n+(loop_adder+base_adder))
        print("Maximum min strongest network: {0}".format(answer))
        return self.relationships


    def min_max_strong_num(self, last_n, last_target):
        '''
        Given the results of the last connection find
        the number
        '''
        return len(self.relationships[last_n] & self.relationships[last_target])+2


if "__name__" == __main__:
    find_max_min_strong(4,6).create_network()

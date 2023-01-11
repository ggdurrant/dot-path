import numpy as np

class Dot:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
class Graph:

    nodes = None
    width = None
    height = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = np.zeros(shape=(height, width), dtype=str)
        for row in range(self.height):
            for col in range(self.width):
                self.nodes[row,col] = '-'

        self.print_graph()

    def print_graph(self):
        for row in range(len(self.nodes)):
            row_str = ''
            for col in range(len(self.nodes[row])):
                row_str += ' '+str(self.nodes[row,col])+' '
            print(row_str)

    def input_nodes(self):
        row = 0
        col = 0
        for row in range(self.height):
            for col in range(self.width):
                # while True:
                    # try: 
                    #     while node_val < 0 or node_val > 9:
                    #         node_val = int(input('Enter node value: '))
                    #     break
                    # except ValueError:
                    #     print('Enter a positive integer less than 10. Try again: ')
                node_val = input('Enter node value: ')
                if node_val == '':
                    node_val = '-'
                self.nodes[row,col] = node_val
                self.print_graph()


if __name__ == '__main__':
    graph = Graph(6,5)
    graph.input_nodes()
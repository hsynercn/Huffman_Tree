from collections import OrderedDict
from heapq import heappush, heappop, heapify
from Node import Node

class HuffmanTree:
    def __init__(self, dir):
        """Reads txt file, calculates symbol counts"""
        txt_file = None
        file = None
        try:
            file = open(dir, 'r')
            txt_file = file.read()

        except IOError:
            print('Can\'t open:' + dir)
        finally:
            if file != None:
                file.close()

        self.symbol_map = dict()
        self.parse_content(txt_file)
        self.root = None
        print(self.symbol_map)

    def parse_content(self, text):
        """Parse text to symbol count map"""
        for char in text:
            if char not in self.symbol_map:
                self.symbol_map[char] = 0
            self.symbol_map[char] += 1
        #self.symbol_map = OrderedDict(sorted(self.symbol_map.items(), key=lambda t: t[1], reverse=True))

    def construct_tree(self):
        heap = [[wt, Node(sym, wt)] for sym, wt in self.symbol_map.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            left_node = lo[1]
            right_node = hi[1]
            new_node = Node("NODE", lo[0] + hi[0])
            new_node.left = left_node
            new_node.right = right_node
            heappush(heap, [new_node.freq, new_node])
        print(heap)
        self.root = heappop(heap)[1]

    def print_tree(self, node):

        if(node == None):
            return
        else:
            print(node.symbol, node.freq)
            self.print_tree(node.left)
            self.print_tree(node.right)


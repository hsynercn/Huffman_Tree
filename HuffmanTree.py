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

    def construct_tree(self):
        heap = [[wt, Node(sym, wt)] for sym, wt in self.symbol_map.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            left_node = hi[1]
            right_node = lo[1]
            new_node = Node("NODE", lo[0] + hi[0])
            new_node.left = left_node
            new_node.right = right_node
            heappush(heap, [new_node.freq, new_node])
        print(heap)
        self.root = heappop(heap)[1]

    def string_tree(self, node):

        if node is None:
            return ""
        else:
            return "(" + self.string_tree(node.left) + str(node.symbol) + self.string_tree(node.right) + ")"




    def get_tree_abstract(self):
        binary_summary = ""
        symbol_summary = ""
        return self.get_node_abstract(self.root, binary_summary, symbol_summary)

    def get_node_abstract(self, node, binary_summary, symbol_summary):
        if node.right is None and node.left is None:
            if node.symbol == "Node":
                raise Exception("Tree leaf is not leaf!")
            else:
                symbol_summary += node.symbol
                return binary_summary, symbol_summary
        if node.left is not None:
            binary_summary += "0"
            #print("left ", binary_summary)
            (binary_summary, symbol_summary) = self.get_node_abstract(node.left, binary_summary, symbol_summary)
        if node.right is not None:
            binary_summary += "1"
            #print("right", binary_summary)
            (binary_summary, symbol_summary) = self.get_node_abstract(node.right, binary_summary, symbol_summary)
        return binary_summary, symbol_summary

    def reconstruct_tree(self, binary_summary: str, symbol_summary) -> str:
        node_stack = list()
        root = Node("ROOT", None)
        node_stack.append(root)
        next_point = 1
        previous = None
        for x in binary_summary:
            if x is "0":
                node = node_stack.pop()
                node_stack.append(node)
                node.left = Node(next_point, None)
                node_stack.append(node.left)
                print("left, parent:", node.symbol, "child:", node.left.symbol)
            if x is "1":
                node = node_stack.pop()
                node = node_stack.pop()
                node.right = Node(next_point, None)
                node_stack.append(node.right)
                print("right, parent:", node.symbol, "child:", node.right.symbol)
            next_point += 1

        node_stack = list()
        node_stack.append(root)
        symbol_index = 1
        while len(node_stack) is not 0:
            node = node_stack.pop()
            if node.left is not None and node.right is not None:
                node_stack.append(node.left)
                node_stack.append(node.right)
            else:
                print("node.symbol located", symbol_summary[len(symbol_summary)-symbol_index])
                node.symbol = symbol_summary[len(symbol_summary)-symbol_index]
                symbol_index += 1
        return root








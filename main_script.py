from HuffmanTree import HuffmanTree

location = ".\\sample_texts\\sample_text_1.txt"
huffman_tree = HuffmanTree(location)
huffman_tree.construct_tree()
huffman_tree.print_tree(huffman_tree.root)
from HuffmanTree import HuffmanTree

location = ".\\sample_texts\\sample_text_1.txt"
huffman_tree = HuffmanTree(location)
huffman_tree.construct_tree()
#huffman_tree.string_tree(huffman_tree.root)
binary_summary, symbol_summary = huffman_tree.get_tree_abstract()
print(binary_summary, symbol_summary)
rec = huffman_tree.reconstruct_tree(binary_summary, symbol_summary)
print(huffman_tree.string_tree(rec))
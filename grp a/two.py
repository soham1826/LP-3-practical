import heapq

# A Huffman Tree Node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
        # symbol name (character)
        self.symbol = symbol
        # node left of current node
        self.left = left
        # node right of current node
        self.right = right
        # tree direction (0/1)
        self.huff = ''
    
    # for comparing nodes (needed for priority queue)
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Utility function to print Huffman codes for all symbols
# in the newly created Huffman tree
def printNodes(node, val=''):
    # Huffman code for current node
    newVal = val + str(node.huff)
    
    # if node is not an edge node (i.e., it has children)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    # if node is an edge node (i.e., no children), display its Huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

# Characters for Huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']
# Frequency of characters
freq = [5, 9, 12, 13, 16, 45]

# List containing unused nodes
nodes = []

# Converting characters and frequencies into Huffman tree nodes
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

# Building the Huffman Tree
while len(nodes) > 1:
    # Pop two smallest nodes
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    
    # Assign directional values
    left.huff = 0
    right.huff = 1
    
    # Combine the two nodes to create a new parent node
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    
    # Push the new node back into the heap
    heapq.heappush(nodes, newNode)

# Huffman Tree is ready! Now print the codes
printNodes(nodes[0])

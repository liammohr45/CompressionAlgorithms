
import heapq
from collections import deque
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparator function for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    print(frequency)
    return frequency

def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman Tree

def generate_huffman_codes(node, prefix="", code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_huffman_codes(node.left, prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_coding(text):
    frequency_table = build_frequency_table(text)
    root = build_huffman_tree(frequency_table)
    huffman_codes = generate_huffman_codes(root)
    return root, huffman_codes


def display_huffman_tree(root):
    if root is None:
        return "The tree is empty"

    result = []
    queue = deque([(root, 0)])  # Queue holds tuples of (node, level)

    while queue:
        node, level = queue.popleft()

        # Representing the node with character, frequency, and tree level
        node_repr = f"{' ' * 4 * level}Char: {node.char if node.char else 'None'}, Freq: {node.freq}"
        result.append(node_repr)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return "\n".join(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Example usage
    exp_text = "abbcccddddeeeee"
    tree, codes = huffman_coding(exp_text)

    # Display the Huffman codes
    print(codes)
    print(display_huffman_tree(tree))



import heapq
from collections import defaultdict
import pickle

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def build_frequency_table(self, text):
        freq = defaultdict(int)
        for ch in text:
            freq[ch] += 1
        return freq

    def build_tree(self, freq_table):
        heap = [Node(char, freq) for char, freq in freq_table.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            n1 = heapq.heappop(heap)
            n2 = heapq.heappop(heap)
            merged = Node(freq=n1.freq + n2.freq)
            merged.left = n1
            merged.right = n2
            heapq.heappush(heap, merged)
        return heap[0]

    def build_codes(self, root):
        codes = {}
        def generate(node, current_code):
            if node is None:
                return
            if node.char is not None:
                codes[node.char] = current_code
                return
            generate(node.left, current_code + "0")
            generate(node.right, current_code + "1")
        generate(root, "")
        return codes

    def compress(self, text):
        freq_table = self.build_frequency_table(text)
        root = self.build_tree(freq_table)
        codes = self.build_codes(root)
        encoded = ''.join(codes[ch] for ch in text)
        return encoded, root

    def encode_binary(self, bitstring):
        b = bytearray()
        for i in range(0, len(bitstring), 8):
            byte = bitstring[i:i+8]
            b.append(int(byte.ljust(8, '0'), 2))
        return bytes(b)

    def bytes_to_binary(self, b):
        return ''.join(f"{byte:08b}" for byte in b)

    def decompress(self, bitstring, root):
        result = []
        node = root
        for bit in bitstring:
            node = node.left if bit == '0' else node.right
            if node.char is not None:
                result.append(node.char)
                node = root
        return ''.join(result)

import sys
import queue
import heapq
from collections import Counter


class Huffman(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __eq__(self, other):
        return Huffman.__check(other) and self.freq == other.freq
    
    def __lt__(self, other):
        return Huffman.__check(other) and self.freq < other.freq
    
    def __gt__(self, other):
        return Huffman.__check(other) and self.freq > other.freq
    
    def __check(other):
        if other is None:
            return False
        if not isinstance(other, Huffman):
            return False
        return True

def merge(heap):
    '''
        Removes the first two nodes from
        the priority queue to create a new one and
        Put this newer back merged node into the queue (like a tree)
        '''
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    merged = Huffman(None, n1.freq + n2.freq)
    merged.left = n1
    merged.right = n2
    heapq.heappush(heap, merged)

def merge1(heap):
    '''
        Removes the first two nodes from
        the priority queue to create a new one and
        Put this newer back merged node into the queue (like a tree)
        '''
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    merged = Huffman(None, n1.freq + n2.freq)
    merged.left = n1
    merged.right = n2
    heapq.heappush(heap, merged)

def conv_to_pq(d):
    '''
        Put Huffman List a priority queue
        '''
    heap = []
    for k, v in d.items():
        heapq.heappush(heap, Huffman(k, v))
        heapq.heappush(heap, Huffman('\0',0))
    return heap

def recur_var_value(codes,tree, root, current=''):
    '''
        Huffman's Encoded code
        
        '''
    if root is not None:
        if root.char is not None:
            codes[root.char] = current
            tree[current] = root.char
            return
        recur_var_value(codes,tree, root.left, current + "0")
        recur_var_value(codes,tree, root.right, current + "1")


def huffman_encoding(text):
    '''
        Executes Encoding Scheme
        '''
    repeat=0
    if text=="":
        print("Null Character; Empty String Please Specify a Valid String")
        return -1,-1
    elif len(text)>0:
        #print(text)
        for i in range(1,len(text)):
            if text[i]==text[i-1]:
                print('Repeated Characters')
                repeat=1
    
        heap = conv_to_pq(Counter(text))
        if(repeat):
            merge1(heap)
else:
    while len(heap) > 1:
        # merge
        merge(heap)
    
    codes, tree = {}, {} # Declare two Empty Dicts for Encoded Text and Tree
    recur_var_value(codes,tree, heapq.heappop(heap))
    encoded_text = ''.join([codes[c] for c in text])
    #print(encoded_text)
    #if len(encoded_text)>0:
    return encoded_text,tree

def huffman_decoding(encoded_text,tree):
    current = ""
    decoded_text = ""
    for bit in encoded_text:
        current += bit
        if (current in tree):
            character = tree[current]
            decoded_text += character
            current = ""
    return decoded_text

if __name__ == "__main__":
    codes = {}
    #Test Case
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    #Test Case :- Corner Case { Empty String}
    corner_case_1 = ""
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(corner_case_1)))
    print ("The content of the data is: {}\n".format(corner_case_1))
    
    # Test Case :- Corner Case {Repeated String}
    corner_case_2 = "SSSSS"
    print ("The size of the data is: {}\n".format(sys.getsizeof(corner_case_2)))
    print ("The content of the data is: {}\n".format(corner_case_2))
    
    
    encoded_data,tree  = huffman_encoding(a_great_sentence)
    
    #Output :-
    '''
        The size of the data is: 69
        The content of the data is: The bird is the word
        1000111111100100001101110000101110110110100011111111001101010011100001
        The size of the encoded data is: 36
        The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001
        The size of the decoded data is: 69
        The content of the encoded data is: The bird is the word
        '''
    encoded_data,tree  = huffman_encoding(corner_case_1)
    
    #Output :-
    '''
        Null Character; Empty String Please Specify a Valid String
        
        '''
    encoded_data,tree  = huffman_encoding(corner_case_2)
    #Output :-
    '''
        The size of the encoded data is: 28
        The content of the encoded data is: 1111100010101
        The size of the decoded data is: 58
        The content of the encoded data is: SSSSS AAA
        '''
    if (encoded_data != -1):
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    if (encoded_data != -1):
        decoded_data = huffman_decoding(encoded_data, tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))



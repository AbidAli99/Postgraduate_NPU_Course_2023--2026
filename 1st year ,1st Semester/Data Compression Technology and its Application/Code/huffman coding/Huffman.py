import heapq

class Huffman:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.encoded_data = ""

    def make_frequency_dict(self, data):
        """
        Create a dictionary with the frequency of each symbol in the input data
        """
        # check if the input data is a string
        if not isinstance(data, str):
            raise ValueError("Invalid input data. Data must be a string.")
        # create an empty frequency dictionary
        frequency = {}
        # count the frequency of each symbol
        for symbol in data:
            if symbol not in frequency:
                frequency[symbol] = 0
            frequency[symbol] += 1
        return frequency

    def make_heap(self, frequency):
        """
        Create a heap from the frequency dictionary
        """
        # add each symbol to the heap
        for key in frequency:
            heapq.heappush(self.heap, (frequency[key], key))

    def merge_nodes(self):
        """
        Merge nodes of the heap until there's only one left
        """
        # merge nodes until there's only one left
        while len(self.heap) > 1:
            lo = heapq.heappop(self.heap)
            hi = heapq.heappop(self.heap)

            # merge the two nodes and add it back to the heap
            merged = (lo[0] + hi[0], lo[1] + hi[1])
            heapq.heappush(self.heap, merged)

            # update the codes for each symbol in the merged nodes
            for symbol in lo[1]:
                self.codes[symbol] = '0' + self.codes.get(symbol, '')
            for symbol in hi[1]:
                self.codes[symbol] = '1' + self.codes.get(symbol, '')

    def encode_data(self, data):
        """
        Encode the input data with the created codes
        """
        # add the encoded data for each symbol
        for symbol in data:
            self.encoded_data += self.codes[symbol]
    
    def make_codes(self):
        """
        Create the codes from the merged nodes
        """
        for symbol in self.make_frequency_dict("").keys():
            self.codes[symbol] = ''

        for symbol in self.make_frequency_dict("").keys():
            node = [item for item in self.heap if symbol in item[1]][0]
            code = ''
            while node != self.heap[0]:
                parent = [item for item in self.heap if item[1] in node[1]][0]
                if node == parent[1]:
                    code = '0' + code
                else:
                    code = '1' + code
                node = parent
            self.codes[symbol] = code

    def update_tree(self, symbol):
        """
        Update the tree and encoded data when a new symbol is added
        """
        # check if the symbol is already in the codes dictionary
        if symbol in self.codes:
            # if so, simply add the code for the symbol to the encoded data
            self.encoded_data += self.codes[symbol]
        else:
            # otherwise, increment the frequency of the symbol in the heap
            for node in self.heap:
                if symbol in node[1:]:
                    node[0] += 1
                    break  # symbol found, exit loop

            # rebuild the heap
            heapq.heapify(self.heap)

            # update the tree
            self.merge_nodes()

            # create a temporary codes dictionary with the updated codes
            tmp_codes = {}
            for symbol, code in self.codes.items():
                tmp_codes[symbol] = '1' + code
            tmp_codes[symbol] = '0'

            # update the encoded data
            self.encoded_data += tmp_codes[symbol]

            # update the codes dictionary
            self.codes = tmp_codes

    def compress(self, data):
        """
        Compress the input data entered by the user
        """
        # initialize the Huffman tree and codes dictionary with the input data
        frequency = self.make_frequency_dict(data)
        self.make_heap(frequency)
        self.merge_nodes()
        self.make_codes()

        # encode the data symbol by symbol and update the Huffman tree and codes dictionary
        self.encoded_data = ""
        for symbol in data:
            self.update_tree(symbol)

        return self.encoded_data

    def decode_data(self, encoded_data):
        """
        Decode the encoded data back to the original data
        """
        data = ""
        current_code = ""

        for bit in encoded_data:
            current_code += bit
            for symbol, code in self.codes.items():
                if current_code == code:
                    data += symbol
                    current_code = ""
                    break

        return data

    def decompress(self, encoded_data):
        """
        Decompress the encoded data entered by the user
        """
        data = self.decode_data(encoded_data)

        return data
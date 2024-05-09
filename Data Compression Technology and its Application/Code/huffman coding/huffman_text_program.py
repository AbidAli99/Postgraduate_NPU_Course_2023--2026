import sys
import time
from Huffman import Huffman

#initialize the tree class
huffman = Huffman()

while True:
    user_input = input("Welcome to the Forward-looking Huffman Coding\n"
      "Enter:\n"
      "'c' to compress data\n"
      "'d' to decompress data\n"
    #   "'u' to update the tree\n"
      "'q' to quit\n"
      "Response: ")
    
    if user_input.lower() == 'c':
        data = input("\nEnter the data to compress: ")
        start_time = time.time()
        compressed = huffman.compress(data)
        end_time = time.time()
        print("\nCompressed data: ", compressed)
        print("\nTime taken: {:.6f} seconds".format(end_time - start_time))
        print()
    elif user_input.lower() == 'd':
        encoded_data = input("\nEnter the encoded data to decompress: ")
        start_time = time.time()
        decompressed = huffman.decompress(encoded_data)
        end_time = time.time()
        print("\nDecompressed data: ", decompressed)
        print("\nTime taken: {:.6f} seconds".format(end_time - start_time))
        print()
    # elif user_input.lower() == 'u':
    #     update()
    elif user_input.lower() == 'q':
        sys.exit()
    else:
        print("Invalid input. Please try again.")
import sys
import time
import os
from Huffman import Huffman

# initialize the tree class
huffman = Huffman()

while True:
    user_input = input("Welcome to the Forward-looking Huffman Coding\n"
                       "Enter:\n"
                       "'c' to compress data\n"
                       "'d' to decompress data\n"
                       "'q' to quit\n"
                       "Response: ")

    if user_input.lower() == 'c':
        input_filename = input("Enter the filename to compress: ")
        output_filename = input("Enter the filename to store the compressed data: ")
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            print('Begininig sequence...\nReading file data...', flush=True)
            
            original_size = os.path.getsize(input_filename)

            data = input_file.read()

            print('File reading complete.\nRunning compression sequence...', flush=True)

            start_time = time.time()
            compressed_data = huffman.compress(data)
            end_time = time.time()

            print('Compression complete!\nWriting to new file...', flush=True)
            output_file.write(compressed_data)

            compressed_size = os.path.getsize(output_filename)
            compression_ratio = original_size / compressed_size

            print(f"Compressed data saved in {output_filename}")
            print('\nOriginal File Size: ', original_size)
            print('\nNew File Size: ', compressed_size)
            print("Time taken to compress the data: {:.6f} seconds".format(end_time - start_time))
            print(f"Compression Ratio: {compression_ratio:.3f}\n")

    elif user_input.lower() == 'd':
        input_filename = input("Enter the filename to decompress: ")
        output_filename = input("Enter the filename to store the decompressed data: ")
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            print('Beginning sequence...\nReading compressed file data...', flush=True)

            compressed_size = os.path.getsize(input_filename)
            
            compressed_data = input_file.read()

            print('File reading complete.\nRunning decompression sequence...', flush=True)

            start_time = time.time()
            decompressed_data = huffman.decompress(compressed_data)
            end_time = time.time()

            print('Decompression complete!\nWriting to new file...', flush=True)
            output_file.write(decompressed_data)

            original_size = os.path.getsize(output_filename)
            compression_ratio = (compressed_size - original_size) / compressed_size

            print(f"Decompressed data saved in {output_filename}")
            print('\nOriginal Compressed File Size: ', compressed_size)
            print('\nNew File Size: ', original_size)
            print("Time taken to decompress the data: {:.6f} seconds".format(end_time - start_time))
            print(f"Compression Ratio: {compression_ratio:.3f}\n")

    elif user_input.lower() == 'q':
        sys.exit()

    else:
        print("Invalid input. Please try again.")

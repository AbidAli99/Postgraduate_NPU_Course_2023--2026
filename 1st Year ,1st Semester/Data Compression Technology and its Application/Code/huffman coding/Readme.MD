#Forward-Looking Huffman Encoding Scheme
## Introduction

Huffman coding is one such algorithms that has become increasingly popular due to its efficiency in compressing large amounts of data into smaller sizes with minimal loss or distortion. As a data compression algorithm, Huffman coding is based on the frequency of occurrence of each character in the data. It is a lossless compression technique, which means that the original data can be exactly reconstructed from the compressed data. Huffman coding is widely used in various applications, such as image and video compression, text compression, and communication systems.

## How The Traditional Huffman Coding Works
### Encoding

Huffman coding creates a binary tree where each leaf node represents a character and the path from the root to the leaf represents the code for that character. The algorithm analyzes each symbol in a stream, assigns a code based on frequency count, and constructs a binary tree where frequently occurring characters have shorter codes. The data is encoded by traversing the tree, producing the code for each character. Huffman coding minimizes the average number of bytes needed to represent characters, resulting in smaller compressed files and significant storage and transmission savings.

### Decoding

The decoding process in Huffman coding is a simple yet crucial step that enables the reconstruction of the original data from the compressed data. The decoding process requires the same Huffman tree that was used for encoding the data, so the tree must be transmitted or stored along with the encoded data to be able to decode it. The decoding process begins by navigating the Huffman tree using the code for each character to find the corresponding character in the data, starting from the root of the Huffman tree. Each code in the encoded data is then decoded by following the path of 0s and 1s that make up the code, and once a leaf node is reached, the character represented by that node is the decoded character for the corresponding code. This process is repeated until all the codes have been decoded, and the original data is reconstructed.

## Challenges of The Traditional Algorithm

While Huffman coding is a powerful and efficient technique for lossless data compression, it does have some limitations. One of the main limitations of Huffman coding is that it requires knowledge of the character frequencies in the data to construct the tree which can be a problem for data that is not well-structured or has a high degree of randomness. For example, if the data is highly random, the character frequencies will be difficult to predict, making it hard to construct the tree. This can result in a less efficient compression, as the algorithm cannot take advantage of the character frequencies to create shorter code words for more frequently occurring characters. 

In addition, the algorithm is sensitive to changes in the data. The algorithm requires that the tree be reconstructed whenever the character frequencies change. This can be a problem for data streams that are constantly changing, such as live video or audio streams. In these cases, the tree would need to be reconstructed at regular intervals, which can be computationally intensive and can result in a delay in the compression process.

## The Update?

This project presents an improved version of the traditional Huffman coding algorithm, by using dynamic trees that can be re-coded if the frequency of a symbol changes. This allows the algorithm to adapt to changing frequencies of the symbols in the input data, making it more efficient for data streams where the frequencies of the symbols change over time, such as in text as it is being typed. The proposed forward-looking algorithm is expected to be useful in various applications where data is streaming, such as text-based communications and multimedia streaming.

## Instructions

The novel implementation is in the Huffman class, find in the file with the same name. 

Two separate programs were written to access the aforementioned class.
- The `huffman_text_program` allows users to compress and decompress strings or texts. This program performs the various operations and outputs the results in the terminal.

- The `huffman_files_program` allows users to compress and decompress files. Currently, only files containing texts are supported. The results are outputed in a text file, with a name determined by the user.

To user either program:

1. Running the 2 above program  (can use 2mb.txt and story.txt files for testing if needed)
2. Then following the prompts that can be seen in screen
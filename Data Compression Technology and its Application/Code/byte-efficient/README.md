# `Byte Efficient`

*ByteEfficient* is a flexible and convenient Python companion, designed to reduce the size of data files using gzip compression, especially useful for scenarios involving large amounts of data that need to be stored or transmitted efficiently.

- Supports a wide range of file formats, such as text, CSV, JSON, and binary files, without compromising data integrity.
- Provides detailed information about the compression process, including original and compressed file sizes, and compression ratio.
- Accepts input and output file paths as command-line arguments for flexibility and customization.

## Prerequisites & Installation

- Ensure you have Python 3.x installed on your system to run the script.
- Basic familiarity with running Python scripts from the command line.
- Run script file `python byte_efficient.py -input_folder -output_folder --overwrite` directly.


## How to Run the program in Windows

* Python run command: python byte_efficient.py
* input folder : "D:\..\..\..\input_folder\input_file.txt"
* output folder : "D:\..\..\..\output_folder\ioutput_file.gz"

## Example

python byte_efficient.py "D:\Masters NPU Semeter\1st Semester\Data Compression Technology and its Application\byte-efficient\input_folder\input_file.txt" "D:\Masters NPU Semeter\1st Semester\Data Compression Technology and its Application\byte-efficient\output_folder\output_file.gz" --overwrite

'''

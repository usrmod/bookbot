# BookBot - Book Statistics Analyzer

A command-line Python application that analyzes text files to provide comprehensive statistics including total word count and character frequency distribution. Perfect for analyzing large books and documents!

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Function Reference](#function-reference)
- [Output Format](#output-format)
- [Examples](#examples)
- [Development](#development)
- [Troubleshooting](#troubleshooting)

## Features

- **Word Count Analysis**: Accurately counts total words in any text file
- **Character Frequency Analysis**: Identifies all characters and their occurrence count
- **Sorted Character Distribution**: Displays characters sorted by frequency (highest to lowest)
- **Case-Insensitive Analysis**: Treats uppercase and lowercase letters as the same character
- **Command-Line Interface**: Simple and intuitive CLI with file path argument
- **Error Handling**: Validates input and provides helpful usage instructions
- **Modular Design**: Separated statistics functions for easy maintenance and testing

## Prerequisites

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Linux (Fedora), Windows, or macOS
- **Text Editor**: Any editor (nano, vim, gedit, etc.) for editing Python files

### Python Dependencies

None! This project uses only Python standard library modules.

## Installation

### On Fedora Linux

**Step 1:** Verify Python installation

python3 --version

text

Should output Python 3.8 or higher

**Step 2:** Create project directory

mkdir ~/bookbot
cd ~/bookbot

text

**Step 3:** Create project files

Create `main.py` and `stats.py` in the `~/bookbot` directory (see code provided)

**Step 4:** Create books directory (optional)

mkdir ~/bookbot/books

text

Place your text files (.txt) in this directory for analysis

## Usage

### Basic Command

python3 main.py <path_to_book>

text

### Examples

**Analyze a book file:**

python3 main.py ~/bookbot/books/frankenstein.txt

text

**Analyze from current directory:**

python3 main.py book.txt

text

**Analyze any text file:**

python3 main.py ~/Documents/myfile.txt

text

### Output Display

The program displays results in three sections:

1. **Header**: Shows file path being analyzed
2. **Word Count**: Total number of words in the file
3. **Character Count**: All characters sorted by frequency

### Error Messages

**If no file path provided:**

Usage: python3 main.py <path_to_book>

text

**If file not found:**

FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'

text

## Project Structure

bookbot/
├── main.py # Entry point and file handling
├── stats.py # Statistics calculation functions
└── books/ # Directory for text files (optional)
├── frankenstein.txt
└── other_books.txt

text

## Function Reference

### main.py

#### `get_book_text(file_path_input)`

**Purpose**: Reads and returns the entire contents of a text file

**Parameters:**
- `file_path_input` (str): Path to the text file to read

**Returns:**
- `str`: Complete file contents

**Example:**

text = get_book_text("books/frankenstein.txt")
print(type(text)) # Output: <class 'str'>

text

#### `main()`

**Purpose**: Entry point for the BookBot application

**Behavior:**
1. Validates command-line arguments
2. Displays header and file path
3. Calls statistics functions from stats module
4. Prints formatted results

**Command-line Arguments:**
- `argv[1]`: File path to analyze (required)

**Example execution flow:**

python3 main.py books/frankenstein.txt
↓
Validates argument exists
↓
Reads file contents
↓
Calculates word count
↓
Calculates character frequency
↓
Displays sorted results

text

### stats.py

#### `word_count(text)`

**Purpose**: Counts total number of words in text

**Parameters:**
- `text` (str): Text to analyze

**Returns:**
- `int`: Total word count

**Algorithm:**
- Splits text by whitespace
- Counts each resulting element

**Example:**

result = word_count("Hello world from Python")
print(result) # Output: 4

text

#### `repeat_char(text)`

**Purpose**: Counts occurrence of each character (case-insensitive)

**Parameters:**
- `text` (str): Text to analyze

**Returns:**
- `dict`: Character → frequency mapping

**Algorithm:**
1. Convert text to lowercase
2. Create dictionary with all characters as keys (initialized to 0)
3. Iterate through each character and increment count
4. Return populated character count dictionary

**Example:**

result = repeat_char("Hello")
print(result)
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

text

**Note:** Only lowercase letters are keys; case-insensitive counting

#### `sorted_list(text)`

**Purpose**: Displays characters sorted by frequency (highest to lowest)

**Parameters:**
- `text` (str): Text to analyze

**Returns:**
- `None` (prints results to console)

**Algorithm:**
1. Gets character counts from `repeat_char()`
2. Sorts dictionary by values in descending order
3. Iterates through sorted items
4. Prints each character and its count

**Example output:**

e: 11506
t: 11220
a: 5026
o: 3143
i: 3130

text

## Output Format

BookBot displays results in a formatted report:

============ BOOKBOT ============
Analyzing book found at /path/to/book.txt...

----------- Word Count ----------
Found 77325 total words

--------- Character Count -------
e: 11506
t: 11220
a: 5026
o: 3143
i: 3130
n: 3056
s: 2769
h: 2609
r: 2553
d: 1817
...

text

## Examples

### Example 1: Analyze Frankenstein

cd ~/bookbot
python3 main.py books/frankenstein.txt

text

**Output:**

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------
Found 77325 total words

--------- Character Count -------
e: 11506
t: 11220
a: 5026
...

text

### Example 2: Analyze Custom Text File

**Create a test file:**

cat > ~/bookbot/test.txt << 'EOF'
The quick brown fox jumps over the lazy dog.
This is a simple test file for BookBot.
EOF

text

**Run analysis:**

python3 main.py ~/bookbot/test.txt

text

**Output:**

============ BOOKBOT ============
Analyzing book found at ~/bookbot/test.txt...

----------- Word Count ----------
Found 17 total words

--------- Character Count -------
e: 4
o: 4
t: 4
a: 3
s: 3
...

text

## Development

### Running the Application

cd ~/bookbot
python3 main.py books/frankenstein.txt

text

### Debugging

Add print statements to trace execution:

In stats.py

def word_count(text):
word_count = 0
for each in text.split():
word_count += 1
print(f"Debug: Found {word_count} words") # Add this line
return word_count

text

### Extending Functionality

**Add average word length:**

In stats.py

def avg_word_length(text):
words = text.split()
if len(words) == 0:
return 0
total_chars = sum(len(word) for word in words)
return total_chars / len(words)

text

**Add sentence count:**

def sentence_count(text):
return text.count('.') + text.count('!') + text.count('?')

text

### Testing Individual Functions

python3 << 'EOF'
from stats import word_count, repeat_char, sorted_list

test_text = "hello world hello python"
print(f"Word count: {word_count(test_text)}")
print(f"Characters: {repeat_char(test_text)}")
sorted_list(test_text)
EOF

text

## Troubleshooting

### No file provided

**Error:**

Usage: python3 main.py <path_to_book>

text

**Solution:** Provide the file path as argument:

python3 main.py books/frankenstein.txt

text

### File not found

**Error:**

FileNotFoundError: [Errno 2] No such file or directory: 'books/frankenstein.txt'

text

**Solutions:**

1. Check file path exists:

ls -la ~/bookbot/books/

text

2. Use absolute path:

python3 main.py /home/fedora/bookbot/books/frankenstein.txt

text

3. Verify file name (case-sensitive):

Wrong:

python3 main.py books/Frankenstein.txt
Correct:

python3 main.py books/frankenstein.txt

text

### No output or incorrect results

**Check file permissions:**

chmod 644 ~/bookbot/books/frankenstein.txt

text

**Verify file is text format:**

file ~/bookbot/books/frankenstein.txt
Should output: text/plain or similar

text

**Test with simple file:**

echo "test file" > ~/bookbot/test.txt
python3 main.py ~/bookbot/test.txt

text

### Character encoding issues

**For UTF-8 encoded files:**

Verify file encoding

file -i ~/bookbot/books/frankenstein.txt
Convert if needed

iconv -f ISO-8859-1 -t UTF-8 old_file.txt > new_file.txt

text

## Tips for Best Results

- **Large Files**: Works best with text files under 10MB
- **Encoding**: Ensure files are UTF-8 encoded for best compatibility
- **Special Characters**: Non-alphabetic characters are included in the count
- **Performance**: Analysis is fast - even large books process in seconds

## License

This project is open source and available for educational purposes.

## Credits

Built with:
- **Python 3**: Programming language
- **Standard Library**: `sys`, file I/O operations, dictionary handling

Perfect for learning Python basics including:
- File I/O operations
- Dictionary data structures
- List comprehensions and sorting
- Command-line argument handling
- Function modularity

---

**Happy analyzing! 📚**

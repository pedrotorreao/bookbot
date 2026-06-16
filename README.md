# BookBot

BookBot is a command-line utility written in Python that analyzes text files (such as books) to produce an objective summary report of their contents. It is designed to perform basic document parsing, word counting, and character frequency analysis.

## Features

- **Word Count**: Calculates the total number of words in the document.
- **Character Frequency Analysis**: Counts the occurrence of every alphabetic character (case-insensitively) and returns them sorted from most frequent to least frequent.
- **Console Report Generator**: Formats and prints the collected statistics to the terminal in a clean, readable layout.

## Project Structure

- `main.py`: The entry point for the CLI application. Coordinates parsing, statistics computation, and report generation.
- `parser.py`: Contains helper functions to read and load the contents of text files.
- `stats.py`: Contains the core logic for counting words, calculating character counts, and sorting frequencies.
- `reports.py`: Formats the analysis results into a structured console report.
- `books/`: A directory containing sample public-domain books (in `.txt` format) for analysis.

## Installation & Requirements

- Python 3.x
- No external dependencies are required.

## Usage

Run the tool by executing the `main.py` script and providing the path to a text file as an argument:

```bash
python3 main.py <path_to_book>
```

For example, to analyze the included text *Frankenstein*:

```bash
python3 main.py books/frankenstein.txt
```

### Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------

e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
z: 235
============= END ===============
```

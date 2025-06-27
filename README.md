# Data Parsing Scripts for Unstructured & Semi-Structured Data

This repository contains a versatile Python script designed to parse unstructured and semi-structured data from various file formats and convert it into clean, structured CSV files. The project demonstrates robust parsing techniques using regular expressions for log files and leveraging the Pandas library for HTML table extraction.

## Features

- **Multi-Format Parsing:** Capable of processing both application `.log` files and `.html` files containing tables.
- **Robust Log Parsing:** Uses regular expressions (`re`) to reliably extract timestamps, log levels, and messages, even with case-insensitive log levels (e.g., `[INFO]` vs. `[info]`) and empty messages.
- **Intelligent HTML Table Extraction:** Automatically identifies and extracts the first data table from a local HTML file using Pandas.
- **Dynamic Parser Selection:** The script intelligently selects the correct parsing function based on the input file's extension (`.log` or `.html`).
- **Clean CSV Output:** Saves the structured data into a well-formatted CSV file, ready for analysis or import into other tools. The DataFrame index is excluded for cleaner output.
- **Interactive Execution:** A user-friendly command-line interface prompts the user for the file they wish to parse.

## Tech Stack

- **Language:** Python 3.8+
- **Libraries:**
  - **Pandas:** For data structuring, analysis, and I/O operations (HTML parsing, CSV writing).
  - **re:** Standard Python library for regular expression operations.

## Setup and Installation

Follow these steps to set up and run the project on your local machine.

**1. Clone the repository:**

```bash
git clone https://github.com/Fusion831/-Scripts-to-Parse-Unstructured-Semi-Structured-Data.git
cd -Scripts-to-Parse-Unstructured-Semi-Structured-Data
```

**2. Install the necessary library:**
The script requires the Pandas library. If you don't have it installed, run the following command:

```bash
pip install pandas
```

*(Note: You may need to use `pip3` depending on your Python installation.)*

## Usage

The script is run interactively from the command line. It will prompt you to enter the name of the file you want to parse.

### Example 1: Parsing a Log File

1. Run the script:

    ```bash
    python parse_data.py
    ```

2. When prompted, enter the name of the log file:

    ```bash
    Enter the file name to parse (e.g., app.log or report.html): app.log
    ```

3. **Output:**
    The script will print the head of the parsed DataFrame, a count of messages by log level, and save the full structured data to `parsed_log_data.csv`.

    ```bash
    Parsed Log Data:
                    Timestamp Log Level                                            Message
    0 2023-10-27 10:00:01      INFO                 User 'admin' logged in successfully.
    1 2023-10-27 10:00:05      INFO                       Data processing task #12345 started.
    2 2023-10-27 10:01:15     DEBUG  Checking connection for service 'db_connector'.
    3 2023-10-27 10:02:00   WARNING                      High memory usage detected: 85%
    4 2023-10-27 10:02:30     ERROR  Failed to connect to database: Connection timed ...

    INFO        2
    DEBUG       1
    WARNING     1
    ERROR       1
    CRITICAL    1
    Name: Log Level, dtype: int64
    ```

### Example 2: Parsing an HTML File

1. Run the script:

    ```bash
    python parse_data.py
    ```

2. When prompted, enter the name of the HTML file:

    ```bash
    Enter the file name to parse (e.g., app.log or report.html): report.html
    ```

3. **Output:**
    The script will print the head of the extracted table and save the full data to `parsed_html_data.csv`.

    ```bash
    Parsed HTML Data:
          Month Region  Sales (USD)
    0       July  North       15,200
    1       July  South        8,500
    2     August  North       18,100
    3  September   West       12,400
    ```

## How It Works

- **Log Parser (`parse_log_file`):** Reads the file line by line and applies a compiled regular expression (`re.compile`) to each line. The pattern uses `re.IGNORECASE` to handle different log level casings. If a line matches, captured groups (timestamp, level, message) are extracted into a dictionary and later converted to a Pandas DataFrame. Malformed lines are skipped.

- **HTML Parser (`parse_html_file`):** Leverages the powerful `pandas.read_html()` function, which scans an HTML document, finds all `<table>` tags, and converts them into a list of DataFrames. This script assumes the target data is in the first table found.

## Future Improvements

- [ ] Implement command-line arguments (using `argparse`) for a more professional and automatable interface (e.g., `python parser.py --input app.log --output logs.csv`).
- [ ] Add a parser for JSON data from a local file or a live API endpoint.
- [ ] Incorporate more advanced error handling and logging for the parsing process itself.

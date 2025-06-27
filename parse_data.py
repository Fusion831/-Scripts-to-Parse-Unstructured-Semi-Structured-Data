import pandas as pd
import re

def parse_log_file(file_path):
    """
    Parses a log file and extracts relevant information into a DataFrame.
    
    Args:
        file_path (str): Path to the log file.
    
    Returns:
        pd.DataFrame: DataFrame containing parsed log entries.
    """
    # Regex to capture the three main parts of a log line.
    # Breaking it down:
    # \[([^\]]+)\]   - Group 1: Capture everything not a ']' inside square brackets (Timestamp)
    # \s             - A single whitespace
    # \[([^\]]+)\]   - Group 2: Capture everything not a ']' inside square brackets (Log Level)
    # \s-\s          - A space, a hyphen, a space
    # (.*)           - Group 3: Capture everything else until the end of the line (Message)
    log_pattern = re.compile(r'\[([^\]]+)\]\s\[([^\]]+)\]\s-\s(.*)', re.IGNORECASE)
    parsed_data = []
    with open(file_path,'r') as file:
        for line in file:
            match= log_pattern.match(line)
            if match:
                timestamp,log_level,message = match.groups()
                parsed_data.append({
                    'Timestamp': timestamp,
                    'Log Level': log_level.upper(),
                    'Message': message
                })
            else:
                print(f"Line did not match pattern or was malformed: {line.strip()}")
            
        return pd.DataFrame(parsed_data)
    

def parse_html_file(file_path):
    """
    Parses an HTML file and extracts relevant information into a DataFrame.
    
    Args:
        file_path (str): Path to the HTML file.
    
    Returns:
        pd.DataFrame: DataFrame containing parsed HTML entries.
    """
    df= pd.read_html(file_path)
    if df:
        return df[0]  # Assuming the first table is the one we want
    else:
        raise ValueError("No tables found in the HTML file.")

    







if __name__ == "__main__":
    
    input_file_name=input("Enter the file name to parse (e.g., app.log or data.html): ")
    if input_file_name.endswith('.log'):
        df = parse_log_file(input_file_name)
        print("Parsed Log Data:")
        print(df.head())
        print(df['Log Level'].value_counts())
        df.to_csv('parsed_log_data.csv', index=False)
    elif input_file_name.endswith('.html'):
        df = parse_html_file(input_file_name)
        print("Parsed HTML Data:")
        print(df.head())
        df.to_csv('parsed_html_data.csv', index=False)
    else:
        print("Unsupported file format. Please provide a .log or .html file.")
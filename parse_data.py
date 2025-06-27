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
    log_pattern = re.compile(r'\[([^\]]+)\]\s\[([^\]]+)\]\s-\s(.*)')
    parsed_data = []
    with open(file_path,'r') as file:
        for line in file:
            match= log_pattern.match(line)
            if match:
                timestamp,log_level,message = match.groups()
                parsed_data.append({
                    'Timestamp': timestamp,
                    'Log Level': log_level,
                    'Message': message
                })
            else:
                print(f"Line did not match pattern or was malformed: {line.strip()}")
            
        return pd.DataFrame(parsed_data)
    









if __name__ == "__main__":
    
    log_file_path = 'app.log'  
    df = parse_log_file(log_file_path)
    print(df.head())  
    print(df.info())
    print(f'Number of Log Levels recevied in analysis: {df['Log Level'].value_counts()}')
    df.to_csv('parsed_log_data.csv', index=False)
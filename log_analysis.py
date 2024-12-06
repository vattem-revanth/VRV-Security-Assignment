import re
import csv
from collections import defaultdict
from typing import Dict, Tuple, List

# Configuration constants
LOG_FILE_PATH = 'sample.log'
FAILED_LOGIN_THRESHOLD = 3

def parse_log_file(file_path: str) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int]]:
    """
    Parse log file and extract key metrics.
    
    Args:
        file_path (str): Path to the log file
    
    Returns:
        Tuple containing:
        - IP request counts
        - Endpoint access counts
        - Failed login attempts per IP
    """
    # Initialize tracking dictionaries
    ip_count = defaultdict(int)
    endpoint_count = defaultdict(int)
    failed_login_attempts = defaultdict(int)

    # Regular expression pattern for parsing log entries
    log_pattern = r'(\d+\.\d+\.\d+\.\d+).*?"(GET|POST) (.*?) HTTP.*? (\d{3})'

    with open(file_path, 'r') as log_file:
        for line in log_file:
            match = re.search(log_pattern, line)
            if match:
                ip_address, _, endpoint, status_code = match.groups()

                # Count requests and endpoint accesses
                ip_count[ip_address] += 1
                endpoint_count[endpoint] += 1

                # Track failed login attempts
                if status_code == '401' or 'Invalid credentials' in line:
                    failed_login_attempts[ip_address] += 1

    return ip_count, endpoint_count, failed_login_attempts

def generate_formatted_output(data: Dict[str, int], title: str, columns: List[str]) -> None:
    """
    Generate formatted output for a given dataset.
    
    Args:
        data (dict): Data to be displayed
        title (str): Section title
        columns (list): Column names for output
    """
    print(f"\n=== {title} ===")
    print(f"{columns[0]:<20} {columns[1]}")
    print("-" * 40)
    
    # Sort data in descending order and print
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_data:
        print(f"{key:<20} {value}")

def save_analysis_to_csv(sections: List[Tuple[str, List[Tuple[str, int]], List[str]]]) -> None:
    """
    Save log analysis results to CSV file.
    
    Args:
        sections (list): Analysis sections to save
    """
    with open('log_analysis_results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        for title, data, columns in sections:
            # Write section header
            writer.writerow(columns)
            
            # Write data rows
            for item in data:
                writer.writerow(list(item))
            
            # Add blank row between sections
            writer.writerow([])

def analyze_log() -> None:
    """
    Perform comprehensive log file analysis.
    """
    # Parse log file and extract metrics
    ip_count, endpoint_count, failed_login_attempts = parse_log_file(LOG_FILE_PATH)

    # Prepare analysis sections
    analysis_sections = [
        (
            "Requests per IP", 
            sorted(ip_count.items(), key=lambda x: x[1], reverse=True),
            ['IP Address', 'Request Count']
        ),
        (
            "Most Accessed Endpoint", 
            [max(endpoint_count.items(), key=lambda x: x[1])],
            ['Endpoint', 'Access Count']
        ),
        (
            "Suspicious Activity", 
            sorted(
                {ip: count for ip, count in failed_login_attempts.items() 
                 if count >= FAILED_LOGIN_THRESHOLD}.items(), 
                key=lambda x: x[1], 
                reverse=True
            ),
            ['IP Address', 'Failed Login Count']
        )
    ]

    # Display analysis sections
    for title, data, columns in analysis_sections:
        generate_formatted_output(dict(data), title, columns)

    # Save analysis to CSV
    save_analysis_to_csv(analysis_sections)

if __name__ == "__main__":
    analyze_log()
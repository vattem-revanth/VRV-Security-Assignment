# Log File Analysis Tool

This project is a Python-based tool to analyze web server log files. It extracts key insights such as the number of requests from different IPs, the most accessed endpoints, and suspicious activity like repeated failed login attempts. The analysis results are displayed in the console and saved as a CSV file.

---

## Features

1. **Request Tracking:**  
   Tracks the number of requests from each IP address.

2. **Endpoint Analysis:**  
   Identifies the most frequently accessed endpoints.

3. **Suspicious Activity Detection:**  
   Detects IPs with multiple failed login attempts exceeding a configurable threshold.

4. **Formatted Output:**  
   Displays insights in a clear, tabular format in the console.

5. **CSV Export:**  
   Saves all analyzed data into a CSV file for further review.

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/username/log-analysis-tool.git
   cd log-analysis-tool
   ```

2. Install Python 3.6+.

3. Install dependencies (if any):  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Place your log file in the project directory and update the `LOG_FILE_PATH` in `log_analysis.py` with the file name.

2. Run the script:  
   ```bash
   python log_analysis.py
   ```

3. Check the console for insights and find the CSV output as `log_analysis_results.csv` in the project directory.

---

## File Structure

```
├── log_analysis.py          # Main script for log analysis
├── sample.log               # Example log file
├── log_analysis_results.csv # Generated CSV output (after running the script)
└── README.md                # Project documentation
```

---

## Configuration

- **LOG_FILE_PATH**: Path to the log file for analysis.  
- **FAILED_LOGIN_THRESHOLD**: Number of failed login attempts considered as suspicious (default: `3`).

---

## Example Input (Log Entry)

```
192.168.1.1 - - [12/Mar/2023:14:32:45 +0000] "GET /home HTTP/1.1" 200
192.168.1.2 - - [12/Mar/2023:14:33:12 +0000] "POST /login HTTP/1.1" 401
```

---

## Example Output (Console)

```
=== Requests per IP ===
IP Address           Request Count
----------------------------------------
192.168.1.1          10
192.168.1.2          5

=== Most Accessed Endpoint ===
Endpoint             Access Count
----------------------------------------
/home                50

=== Suspicious Activity ===
IP Address           Failed Login Count
----------------------------------------
192.168.1.2          3
```

---

## Contributing

1. Fork the repository.  
2. Create a feature branch.  
3. Commit your changes.  
4. Submit a pull request.

---

# Log File Analysis Tool 🚀

A Python-based tool to analyze web server log files. This tool identifies key metrics such as IP request counts, most accessed endpoints, and potential suspicious activity like repeated failed login attempts. Analysis results are displayed in the console and saved as a CSV file for further review. 📊

---

## Features 🛠️

1. **🔍 Request Tracking:**  
   Counts the number of requests from each IP address.

2. **📂 Endpoint Analysis:**  
   Finds the most frequently accessed endpoints.

3. **🚨 Suspicious Activity Detection:**  
   Highlights IPs with failed login attempts exceeding a set threshold.

4. **🖥️ Formatted Output:**  
   Displays results in a user-friendly, tabular format.

5. **📄 CSV Export:**  
   Saves all analyzed data in a CSV file.

---

## Installation ⚙️

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

## Usage 📘

1. Add your log file (e.g., `sample.log`) to the project directory. Update the `LOG_FILE_PATH` in `log_analysis.py` if needed.

2. Run the script:  
   ```bash
   python log_analysis.py
   ```

3. View the output in the console and find the generated CSV file named `log_analysis_results.csv`.

---

## File Structure 📂

```
├── log_analysis.py          # Main script
├── sample.log               # Example log file
├── log_analysis_results.csv # CSV output (generated after running the script)
└── README.md                # Project documentation
```

---

## Configuration ⚙️

- **LOG_FILE_PATH:** Path to the log file to analyze.  
- **FAILED_LOGIN_THRESHOLD:** Number of failed login attempts to flag as suspicious (default: `3`).

---

## Example Input (Log Snippet) 📝

```
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
```

---

## Example Output (Console) 💻

### **Requests per IP**
```
IP Address           Request Count
----------------------------------------
192.168.1.1          7
203.0.113.5          9
10.0.0.2             6
198.51.100.23        6
192.168.1.100        7
```

### **Most Accessed Endpoint**
```
Endpoint             Access Count
----------------------------------------
/home                8
```

### **Suspicious Activity**
```
IP Address           Failed Login Count
----------------------------------------
203.0.113.5          10
192.168.1.100        8
```

---

## Example Output (CSV) 📄

| IP Address       | Request Count |
|-------------------|---------------|
| 192.168.1.1       | 7             |
| 203.0.113.5       | 9             |
| ...               | ...           |

---

## Contributing 🤝

1. Fork the repository.  
2. Create a feature branch.  
3. Commit your changes.  
4. Submit a pull request.

---

## License 📜

This project is licensed under the MIT License.

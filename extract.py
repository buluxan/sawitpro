import re

# Initialize variables to store metrics
error_count = 0
total_response_time = 0
total_transactions = 0

# Define a regular expression pattern to match log entries
log_pattern = r'\[(.*?)\] \[(.*?)\] \[(\d+)\] \[(\d+)ms\] \[(.*?)\] \[(.*?)\] \[(.*?)\]'

# Open and read the log file
with open('sample.log', 'r') as log_file:
    for line in log_file:
        match = re.match(log_pattern, line)
        if match:
            _, _, status_code, response_time_ms, _, _, _ = match.groups()
            status_code = int(status_code)
            response_time_ms = int(response_time_ms)

            # Check if the status code is 400 or 500
            if status_code >= 400 and status_code < 600:
                error_count += 1

            total_transactions += 1
            total_response_time += response_time_ms

# Calculate average response time
average_response_time = total_response_time / total_transactions if total_transactions > 0 else 0

# Print the extracted metrics
print("Error Count (status codes 400 and 500):", error_count)
print("Average Response Time (ms):", average_response_time)
print("Total Number of Transactions:", total_transactions)

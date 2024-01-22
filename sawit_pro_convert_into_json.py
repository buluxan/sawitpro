import re
import json
import datetime

# Initialize variables to store metrics
error_count = 0
total_response_time = 0
total_transactions = 0
log_data = []

# Define a regular expression pattern to match log entries
log_pattern = r'\[(.*?)\] \[(.*?)\] \[(\d+)\] \[(\d+)ms\] \[(.*?)\] \[(.*?)\] \[(.*?)\]'

# Open and read the log file
with open('sample.log', 'r') as log_file:
    for line in log_file:
        match = re.match(log_pattern, line)
        if match:
            timestamp, service_name, status_code, response_time_ms, user_id, transaction_id, additional_info = match.groups()
            log_entry = {
                'timestamp': timestamp,
                'service_name': service_name,
                'status_code': int(status_code),
                'response_time_ms': int(response_time_ms),
                'user_id': user_id,
                'transaction_id': transaction_id,
                'additional_info': additional_info
            }
            
            # Check if the status code is 400 or 500
            if status_code.startswith('4') or status_code.startswith('5'):
                error_count += 1

            total_transactions += 1
            total_response_time += int(response_time_ms)

            log_data.append(log_entry)

# Calculate average response time
average_response_time = total_response_time / total_transactions if total_transactions > 0 else 0

# Create a dictionary for metrics
metrics = {
    'error_count': error_count,
    'average_response_time_ms': average_response_time,
    'total_transactions': total_transactions
}

# Create a structured JSON object for ingestion
log_metrics = {
    'timestamp': datetime.datetime.now().isoformat(),
    'log_metrics': metrics,
    'error_logs': log_data
}

# Convert the log metrics and data to JSON format
log_metrics_json = json.dumps(log_metrics, indent=4)

# Print and write the structured JSON to a file
print("Structured Log Metrics:")
print(log_metrics_json)

with open('log_metrics.json', 'w') as log_metrics_file:
    log_metrics_file.write(log_metrics_json)

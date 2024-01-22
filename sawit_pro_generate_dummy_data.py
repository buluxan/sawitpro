import random
import time

# List of possible service names and user IDs for generating dummy data
service_names = ["svc_red", "svc_blue", "svc_pink"]
user_ids = ["1", "2", "3"]

# Open a file for writing
with open('sample.log', 'w') as log_file:
    for _ in range(100):  # Adjust the number of log entries as needed
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        service_name = random.choice(service_names)
        status_code = random.choice(["200", "400", "500"])
        response_time_ms = random.randint(1, 1000)
        user_id = random.choice(user_ids)
        transaction_id = random.randint(1000, 9999)
        additional_info = f"Additional info for transaction {transaction_id}"

        log_entry = f"[{timestamp}] [{service_name}] [{status_code}] [{response_time_ms}ms] [{user_id}] [{transaction_id}] [{additional_info}]\n"

        log_file.write(log_entry)

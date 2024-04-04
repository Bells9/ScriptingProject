import psutil
import schedule
import time
import logging

# Configure logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Function to log messages
def log_message(message):
    logging.info(message)

# Function to print alerts to the console
def print_alert(message):
    print(f"ALERT: {message}")

# Health check functions
def check_cpu_usage(threshold=50):
    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > threshold:
        message = f"High CPU usage detected: {cpu_usage}%"
        log_message(message)
        print_alert(message)

def check_memory_usage(threshold=80):
    memory_usage = psutil.virtual_memory().percent

    if memory_usage > threshold:
        message = f"High memory usage detected: {memory_usage}%"
        log_message(message)
        print_alert(message)

def check_disk_space(path='/', threshold=75):
    try:
        disk_usage = psutil.disk_usage(path).percent
        if disk_usage > threshold:
            message = f"Low disk space detected: {disk_usage}%"
            log_message(message)
            print_alert(message)
    except Exception as e:
        log_message(f"Error checking disk space: {e}")

# Function to run health checks
def run_health_checks():
    log_message("Running system health checks...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    log_message("Health checks completed.")

# Schedule health checks to run every minute
schedule.every(1).minutes.do(run_health_checks)

# Main loop to run scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

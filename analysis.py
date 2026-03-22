# Your first line of Python code
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Count failed logins per user
failed_logins = df[df["login_status"] == "failed"]
failed_count = failed_logins.groupby("username").size()

print("Failed login attempts by user:")
print(failed_count)

# Detect suspicious users (more than 2 failed attempts)
suspicious_users = failed_count[failed_count > 2]

print("\nSuspicious users (more than 2 failed attempts):")
print(suspicious_users)

# Count logins per IP
ip_counts = df.groupby("ip_address").size()

print("\nActivity by IP address:")
print(ip_counts)
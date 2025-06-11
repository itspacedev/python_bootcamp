import os

# Get the value of an environment variable
virtual_env = os.environ.get("VIRTUAL_ENV")

print(f"VIRTUAL_ENV => {virtual_env}")

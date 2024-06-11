from datetime import datetime

# Define the date string
date_str = "2021-01-01"
date_str2 = "2022-01-01"


# Convert the date string to a datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
date_obj2 = datetime.strptime(date_str2, "%Y-%m-%d")

# Convert the datetime object to a timestamp
timestamp = date_obj.timestamp()
timestamp2 = date_obj2.timestamp()

print(timestamp)
print(timestamp2)

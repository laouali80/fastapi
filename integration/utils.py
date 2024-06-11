from datetime import datetime

# Define possible date formats
date_formats = [
    "%Y",                # Format for year only: "2022"
    "%Y-%m-%d",          # Format for year-month-day: "2022-12-23"
    "%Y-%m-%dT%H:%M:%SZ", # Format for full timestamp: "2021-02-16T20:09:53Z"
    '%Y/%m/%d'
]

def convert_to_timestamp(date_string):
    if date_string:
        for date_format in date_formats:
            try:
                # Try to convert the date string to a datetime object
                datetime_obj = datetime.strptime(date_string.strftime(date_format), date_format)
                # datetime_obj = date_string
                # Convert the datetime object to a timestamp
                return int(datetime_obj.timestamp())
            except ValueError:
                # If the format doesn't match, continue to the next format
                raise ValueError("Date format not recognized")
        # If no formats match, raise an error
        raise ValueError("Date format not recognized")
    return None

# # Example date strings
# date_strings = ["2022", "2022-12-23", "2021-02-16T20:09:53Z"]

# for date_string in date_strings:
#     timestamp = convert_to_timestamp(date_string)
#     print(f"Date String: {date_string} -> Timestamp: {timestamp}")

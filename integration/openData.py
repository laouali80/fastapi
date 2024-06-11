import requests
from dotenv import load_dotenv
import os


load_dotenv()


# get the API token
api_token = os.getenv("api_key")


# Define the base URL
base_url = "https://healthsites.io/api/v3/facilities/"


def faliticies(page=1, country=None, extent=None, created_from=None, latest_to=None):
    """Fecthes facilities by page number."""

    # Define the parameters
    params = {
        "api-key": api_token,
        "page": page,      # Replace with the actual page number
        "country": country,  # Replace with the actual country name
        "extent": extent,   # Replace with the actual extent value
        "from": created_from,        # Replace with the actual from date
        "to": latest_to,            # Replace with the actual to date
        # "flat-properties": "true",  # Replace with the actual flat-properties value
        # "tag-format": "tag_format", # Replace with the actual tag format
        # "output": "output_format"   # Replace with the actual output format
    }

    # Make the GET request
    response = requests.get(base_url, params=params)


    # Check for HTTP errors
    response.raise_for_status()

    # Parse the JSON response
    result = response.json()

    return result


def statistic(country=None, extent=None, created_from=None, latest_to=None):
    """Fecthes all health facilities statistic (number facilities, hospital, clinic,.....)."""

    # Define the base URL
    url = base_url + "statistic/"

    # Define the parameters
    params = {
        "api-key": api_token,
        "country": country,  # Replace with the actual country code
        "extent": extent,   # Replace with the actual extent value
        "from": created_from,        # Replace with the actual from date
        "to": latest_to,            # Replace with the actual to date
        # "flat-properties": "true",  # Replace with the actual flat-properties value
        # "tag-format": "tag_format", # Replace with the actual tag format
        # "output": "output_format"   # Replace with the actual output format
    }

    # Make the GET request
    response = requests.get(url, params=params)


    # Check for HTTP errors
    response.raise_for_status()

    # Parse the JSON response
    result = response.json()

    return result
    

def facility(osm_type, osm_id):
    """Fecthes a specific facility."""

    # Define the base URL
    url = base_url + f"{osm_type}/{osm_id}"

    # Define the parameters
    params = {
        "api-key": api_token,
        "osm_type": osm_type,
        "osm_id": osm_id
        
    }

    # Make the GET request
    response = requests.get(url, params=params)


    # Check for HTTP errors
    response.raise_for_status()

    # Parse the JSON response
    result = response.json()

    return result


# Print or process the result
# print(statistic())
import requests
import datetime

# KEV Lister
# Author: Syed Huda
# Description: This script fetches a list of known exploited vulnerabilities (CVE IDs) from CISA's JSON feed
# and saves them to a text file named kev-cves-{date}.txt.

def fetch_and_parse_cve_ids(url):
    """Fetch and parse CVE IDs from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for HTTP errors

        data = response.json()
        return [vulnerability['cveID'] for vulnerability in data.get('vulnerabilities', [])]
    except Exception as e:
        return f"Error occurred: {e}"

def save_cve_ids_to_file(cve_ids, file_name):
    """Save the CVE IDs to a file."""
    with open(file_name, 'w') as file:
        for cve_id in cve_ids:
            file.write(cve_id + '\n')

def display_banner():
    """Display the program banner."""
    print("=================================================")
    print("                 KEV Lister                      ")
    print("     Known Exploited Vulnerabilities Lister      ")
    print("=================================================")

# Display the banner
display_banner()

# URL to fetch the JSON data from
url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

# Fetch and parse CVE IDs
cve_ids = fetch_and_parse_cve_ids(url)

# Get the current date in YYYY-MM-DD format
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Define the file name
file_name = f"kev-cves-{current_date}.txt"

# Save the CVE IDs to the file
save_cve_ids_to_file(cve_ids, file_name)

print(f"CVE IDs saved to {file_name}")

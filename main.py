import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = "https://www.example.com/"

# Make a request to the website and get the response
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML response
soup = BeautifulSoup(response.content, "html.parser")

# Find the "Search Postings" section
search_postings_section = soup.find("div", class_="search-postings")

# Find the first 5 postings in the "Search Postings" section
postings = search_postings_section.find_all("div", class_="posting")[:5]

# Create a list to store the data for each posting
posting_data = []

# Loop through the postings and extract the data
for posting in postings:
    # Get the estimated value
    estimated_value = posting.find("span", class_="estimated-value").text

    # Get the notes
    notes = posting.find("span", class_="notes").text

    # Get the description
    description = posting.find("span", class_="description").text

    # Get the closing date
    closing_date = posting.find("span", class_="closing-date").text

    # Add the data to the list of posting data
    posting_data.append({
        "estimated_value": estimated_value,
        "notes": notes,
        "description": description,
        "closing_date": closing_date
    })

# Print the list of posting data
print(posting_data)

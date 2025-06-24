#!/usr/bin/env python3
"""
Web Page Evidence Extractor

This script prompts the user for a web page URL, then:
1. Retrieves the web page using the requests library.
2. Parses the HTML with BeautifulSoup.
3. Extracts the page title.
4. Extracts all hyperlink URLs from <a> tags.
5. Extracts all image URLs from <img> tags.
6. Prints the title, links, and image filenames.
7. Downloads and saves each image to a local folder named 'images'.
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_page_info(url):
    """
    Given a URL, extract and return:
      - the page title,
      - all hyperlink URLs, and
      - all image URLs.
    """
    # Retrieve the web page content
    response = requests.get(url)
    response.raise_for_status()  # Raise error if the request fails

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the page title (if available)
    title = soup.title.string.strip() if soup.title and soup.title.string else 'No title found'

    # Extract all hyperlinks from <a> tags
    links = []
    for a_tag in soup.find_all('a', href=True):
        # Handle relative URLs by joining with the base URL
        link = urljoin(url, a_tag['href'])
        links.append(link)

    # Extract all image URLs from <img> tags
    images = []
    for img_tag in soup.find_all('img', src=True):
        img_url = urljoin(url, img_tag['src'])
        images.append(img_url)

    return title, links, images

def save_image(img_url, folder='images'):
    """
    Download an image from img_url and save it to the specified folder.
    Returns the filename under which the image was saved.
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Get the image content using a GET request
    response = requests.get(img_url)
    response.raise_for_status()  # Raise error if download fails

    # Extract filename from the image URL
    parsed_url = urlparse(img_url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = 'image.jpg'  # Fallback filename

    # Create the full file path
    file_path = os.path.join(folder, filename)

    # Save the image content to a file (in binary mode)
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return filename

def main():
    # Prompt the user for the URL of the web page
    url = input("Enter the URL of the web page: ").strip()
    print("\nExtracting information from:", url)

    # Extract page title, links, and image URLs
    try:
        title, links, images = extract_page_info(url)
    except Exception as e:
        print("Error retrieving the page:", e)
        return

    # Print the extracted page title
    print("\nPage Title:")
    print(title)

    # Print all the links found on the page
    print("\nLinks found on the page:")
    for link in links:
        print(link)

    # Process the images: print the filename and save the image locally
    print("\nImages found on the page and saved locally:")
    for img_url in images:
        try:
            filename = save_image(img_url)
            print("Saved image:", filename)
        except Exception as e:
            print("Error saving image from", img_url, ":", e)

if __name__ == "__main__":
    main()


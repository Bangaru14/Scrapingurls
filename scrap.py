
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
from collections import Counter


# Set the start and end dates
start_date = datetime.date(2023, 5, 22)
end_date = datetime.date(2023, 8, 8)

# Initialize the Selenium WebDriver (you need to specify the path to your driver)
driver = webdriver.Chrome()

# Open the T-Series YouTube channel
driver.get("https://www.youtube.com/user/tseries")

# Create a list to store video URLs
video_urls = []

# Loop through the videos on the channel
while True:
    # Scroll down to load more videos (you may need to adjust this based on the YouTube layout)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Find all video elements on the page
    video_elements = soup.find_all("div", class_="style-scope ytd-grid-video-renderer")
    
    for video in video_elements:
        # Extract the video URL and description
        video_url = "https://www.youtube.com" + video.a["href"]
        description = video.find("yt-formatted-string", id="description-text").text
        
        # Extract the video upload date from the description (you'll need to implement this)
        # Check if the upload date is within the specified range
        # Append the video URL to the list if it is
        
        # Your code for extracting and verifying the upload date goes here
        
    # Check if the last video's upload date is before the start date
    # If yes, break the loop
    if video_upload_date < start_date:
        break

# Close the Selenium WebDriver
driver.quit()

# Print the collected video URLs
for url in video_urls:
    print(url)

# Combine all video URLs into one string
all_urls = " ".join(video_urls)

# Count the occurrences of each character
char_count = Counter(all_urls)

# Find the most common character
most_common_char, count = char_count.most_common(1)[0]

# Print the most common character and its count
print(f"The most frequently repeated character is '{most_common_char}' with {count} occurrences.")

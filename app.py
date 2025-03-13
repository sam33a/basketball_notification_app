import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime
import time

# Placeholder for the notification logic
st.title('Basketball Injury Notification System')

# Here you would implement the logic to fetch and display notifications

def check_player_health():
    # List of local news sources to scrape
    sources = [
        'https://www.localnews1.com',  # Replace with actual local news site URLs
        'https://www.localnews2.com',
        'https://www.localnews3.com'
    ]
    notifications = []

    # Fetch and parse each source
    for source in sources:
        try:
            response = requests.get(source)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Example: Find articles mentioning player health
            articles = soup.find_all('article')
            for article in articles:
                title = article.find('h2').text
                link = article.find('a')['href']
                if 'healthy' in title.lower():
                    notifications.append((title, link))
        except Exception as e:
            print(f'Error fetching {source}: {e}')  # Error handling

    return notifications

# Main loop to check for updates every minute on Tuesdays from 9 AM onwards
while True:
    current_time = datetime.datetime.now()
    if current_time.weekday() == 1 and current_time.hour >= 9:  # Check if it's Tuesday 9 AM or later
        notifications = check_player_health()
        unique_notifications = set()  # To store unique notifications

        for title, link in notifications:
            if title not in unique_notifications:
                st.write(f'**Notification:** {title} - [Read more]({link})')
                unique_notifications.add(title)  # Add title to the set to avoid duplicates

        time.sleep(60)  # Wait a minute before checking again
    else:
        time.sleep(3600)  # Check every hour when not Tuesday morning

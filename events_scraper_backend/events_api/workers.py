import requests

from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse

from events_api.models import Event


def techmeme_events_scraper():
    url = 'https://www.techmeme.com/events'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    events = soup.find_all('div', class_='rhov')

    website_domain = urlparse(url).netloc

    total_events_to_insert = []

    for event in events:
        event_details = event.find_all('div')
        # Extracting individual details
        event_date = event_details[0].text # 'Mar 21-24'
        event_name = event_details[1].text
        event_location = event_details[2].text

        # Parsing event date to get event start date and end date
        cuurent_year = str(datetime.now().year)
        event_date_split = event_date.split('-') # ['Mar 21', '24']

        # Parsing event start date for it's month and date
        event_start_details = event_date_split[0] # ['Mar 21']
        event_start_details_split = event_start_details.split(' ')
        event_start_month = event_start_details_split[0]
        event_start_date = event_start_details_split[1]

        event_start_date = f'{event_start_month} {event_start_date} {cuurent_year}'
        event_start_date = datetime.strptime(event_start_date, '%b %d %Y').date()

        # Checking if event doesn't have any end date
        if len(event_date_split) == 1: # ['Mar 21']
            event_end_date = None
        else:
            event_end_details = event_date_split[1] # ['24']

            # Parsing event start date for it's month and date
            event_end_details_split = event_end_details.split(' ') # ['24']
            # Checking if end month 
            if len(event_end_details_split) == 1:
                event_end_month = event_start_month
                event_end_date = event_end_details_split[0]
            else:
                event_end_month = event_end_details_split[0]
                event_end_date = event_end_details_split[1]
            
            event_end_date = f'{event_end_month} {event_end_date} {cuurent_year}'
            event_end_date = datetime.strptime(event_end_date, '%b %d %Y').date()
        
        total_events_to_insert.append(
            Event(
                website=website_domain,
                name=event_name,
                start_date=event_start_date,
                end_date=event_end_date,
                location=event_location
            )
        )

    # Inserting events parsed in bulk to increase db insertion performance
    Event.objects.bulk_create(total_events_to_insert)


def computerworld_events_scraper():
    url = 'https://www.computerworld.com/article/3313417/tech-event-calendar-shows-conferences-and-it-expos-updated.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    events = soup.find(id='cwsearchabletable').find_all('tr')

    website_domain = urlparse(url).netloc

    total_events_to_insert = []

    for event in events[1:]:
        event_name = event.find('th').text
        event_details = event.find_all('td')
        
        event_start_date = event_details[1].text
        event_end_date = event_details[2].text
        event_location = event_details[3].text

        event_start_date = datetime.strptime(event_start_date, '%Y-%m-%d').date()
        event_end_date = datetime.strptime(event_end_date, '%Y-%m-%d').date()

        total_events_to_insert.append(
            Event(
                website=website_domain,
                name=event_name,
                start_date=event_start_date,
                end_date=event_end_date,
                location=event_location
            )
        )

    # Inserting events parsed in bulk to increase db insertion performance
    Event.objects.bulk_create(total_events_to_insert)

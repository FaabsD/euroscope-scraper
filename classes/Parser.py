from bs4 import BeautifulSoup
from urllib.request import urlopen
import math
import chardet

class Parser:
    def __init__(self, url):
        self.url = url
        self.response = urlopen(self.url)
        self.raw_html = self.response.read()
        self.detected = chardet.detect(self.raw_html)
        self.encoding = self.detected['encoding'] if self.detected['encoding'] else 'utf-8'
        self.html = self.raw_html.decode(self.encoding)
        # Parse html
        self.soup = BeautifulSoup(self.html, 'html.parser')
        # Get tables
        self.tables = self.soup.find_all('table')
        # Get content table
        self.content_table = self.tables[3]
        # get results table
        self.results_table = self.tables[4]
        # Get table rows
        self.table_rows = self.content_table.find_all('tr')
        self.image_elements = []
        self.counter = 0
        self.get_page_urls()
        self.parse_images()

    def parse_images(self):
        for row in self.table_rows:
            if row.find('td').find('img'):
                self.image_elements.append(row.find('td').find('img'))

    def get_page_urls(self):
        print(self.results_table)
        total_results = self.results_table.find('tr').find('td').find_all('b')[1].text
        # Calculate total pages rounded up
        total_pages = math.ceil(int(total_results) / 25)
        print(f"Total results: {total_results}")
        print(f"Total pages: {total_pages}")

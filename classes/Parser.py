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
        self.image_elements = list()
        self.counter = 0

    ''' Parse images from table rows and add them to image_elements list '''
    def parse_images(self):
        for row in self.table_rows:
            if row.find('td').find('img'):
                # get all images from row
                images = row.find('td').find_all('img')
                for image in images:
                    image_src = image['src']
                    image_alt = image['alt']
                    self.image_elements.append({
                        'src': image_src,
                        'alt': image_alt
                    })


    def get_image_elements(self):
        return self.image_elements

from bs4 import BeautifulSoup
from typing import Optional

class BeautifulSoupDriver:
    """Driver para parsing HTML"""
    
    @staticmethod
    def parse(html_content: str, parser: str = 'html.parser') -> BeautifulSoup:
        return BeautifulSoup(html_content, parser)
    
    @staticmethod
    def find_link(soup: BeautifulSoup, text_pattern: str) -> Optional[dict]:
        element = soup.find('a', string=lambda text: text and text_pattern.lower() in text.lower())
        
        return {'href': element['href']} if element and 'href' in element.attrs else None
from rich.console import Console
from rich.table import Table
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import re

class search:
	def __init__(self,query: str):
		api_url = 'https://pypi.org/search/'
		snippets = []
		s = requests.Session()
		#filters=['Environment+%3A%3A+X11+Applications','Environment+%3A%3A+Console']
		filters=['Environment+%3A%3A+X11+Applications']

		for currentfilter in filters:
			for page in range(1, 3):
				print(currentfilter)
				#params = {'q': query, 'page': page, 'c':currentfilter}
				params = {'q': query, 'page': page}
				r = s.get(api_url, params=params)
				soup = BeautifulSoup(r.text, 'html.parser')
				snippets += soup.select('a[class*="snippet"]')
				#print(soup.select('a[class*="snippet"]'))

				if not hasattr(s, 'start_url'):
					#s.start_url = r.url.rsplit('&page&currentfilter', maxsplit=1).pop(0).replace('%2B','+').replace('%253A','%3A')
					s.start_url = r.url.rsplit('&page', maxsplit=1).pop(0).replace('%2B','+').replace('%253A','%3A')
					print(s.start_url)
				
				self.printtable(s,snippets,api_url)
		self.printtable(s,snippets,api_url)
		return

	def printtable(self,s,snippets,api_url):
		table = Table(title=f'[not italic]:snake:[/] [bold][magenta]{s.start_url} [not italic]:snake:[/]')
		table.add_column('Package', style='cyan', no_wrap=True)
		table.add_column('Version', style='bold yellow')
		table.add_column('Released', style='bold green')
		table.add_column('Description', style='bold blue')
		for snippet in snippets:
			link = urljoin(api_url, snippet.get('href'))
			package = re.sub(r"\s+", " ", snippet.select_one('span[class*="name"]').text.strip())
			version = re.sub(r"\s+", " ", snippet.select_one('span[class*="version"]').text.strip())
			released = re.sub(r"\s+", " ", snippet.select_one('span[class*="released"]').text.strip())
			description = re.sub(r"\s+", " ", snippet.select_one('p[class*="description"]').text.strip())
			emoji = ':open_file_folder:'
			table.add_row(f'[link={link}]{emoji}[/link] {package}', version, released, description)

		console = Console()
		console.print(table)
		


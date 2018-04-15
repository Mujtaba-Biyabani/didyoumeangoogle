import requests
from bs4 import BeautifulSoup
import re
class didumean:
    def __init__(self,query):
        self.s = requests.session()
        self.s.headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
        self.url = 'https://www.google.co.in/search?q='
        self.query = self.url+str(query).replace(' ', '+')
        self.answer = self.search_for_text()


    def serach_google(self):
        search_result = self.s.get(self.query)
        search_html = search_result.text
        return search_html

    def search_for_text(self):
        data = self.serach_google()
        soup = BeautifulSoup(data,'lxml')
        ans = soup.find('a', attrs={'class': 'spell'})
        try:
            result = repr(ans.contents)
            result = result.replace("u'", "")
            result = result.replace("/", "")
            result = result.replace("<b>", "")
            result = result.replace("<i>", "")
            result = re.sub('[^A-Za-z0-9\s]+', '', result)
            result = re.sub(' +', ' ', result)
        except AttributeError:
            result = 1
        return result



d = didumean('fotball').answer
print(d)






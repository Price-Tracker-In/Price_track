import requests as r
from bs4 import BeautifulSoup as bs


# In[2]:

def check(url):
    page = r.get(url)
    soup = bs(page.content,"html.parser")
    if soup.find_all("div",{"class":"_30jeq3 _16Jk6d"}):
        return True
    else:
        return False


# In[ ]:




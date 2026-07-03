import requests
from bs4 import BeautifulSoup
url=input("Enter url of website whose content you want:")
response=requests.get(url)
soup= BeautifulSoup(response.text,'html.parser')
clean_text=soup.get_text(separator='\n',strip=True)
f=open("website content.txt","w")
f.write(clean_text)
f.close()

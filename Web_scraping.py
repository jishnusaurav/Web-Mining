import requests
import bs4
urls=["https://Vit.ac.in/"]
print("Check")
ans= set()
while urls:  
  url=urls.pop(0)  
  if url not in ans :
    try:
      response=requests.get(url)
      if "admissions" in str(response.text).lower():
        print(url)ans.add(url)soup=bs4.BeautifulSoup(response.text,"lxml")
      for links in soup.find_all("a"):
         urls.append(links.attrs["href"])
         except:pass

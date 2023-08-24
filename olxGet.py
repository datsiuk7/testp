import requests
from bs4 import BeautifulSoup
import datetime
import dataJson
import asyncio
textAds = {}

def olxGetf(url):
    global textAds

    response = requests.get(url, timeout=20)
    try:
        # print(response.status_code)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка під час запиту там де список: {e}")
        return ["error", []]  
    soup = BeautifulSoup(response.text, 'lxml')

    card_divs = soup.find_all('div', attrs={'data-cy': 'l-card'})
    
    for card_div in card_divs:
        adsMain = card_div.find('div')
        idAds = card_div.get('id')

        if "ТОП" in adsMain.text:
            continue
        idsAds = dataJson.get_dataJson()
        if idAds in idsAds:
            if len(idsAds) >= 30:
                idsAds.pop(0)
            return ["SAME", []]
        
        idsAds.append(idAds)
        dataJson.set_dataJson(idsAds)

        p_tags = adsMain.find('div').find_all('div', recursive=False)
        textAll = p_tags[1].find_all('div', recursive=False)
        img_src = card_div.find('img')['src']
        foto_not_found = ""

        if "thumbnail" in img_src:
            img_src = "https://www.completehomerealty.com.au/templates/bt_property/images/avatar-default.jpg"
            print("немає фото")
            foto_not_found = "\n⚠<b>немає фото</b>"
        try:
            textAds = {
                'id' : idAds,
                'title' : textAll[0].find("h6").text.replace("\n", " ")+foto_not_found,
                'price' : textAll[0].find("p").text.replace("грн.", "").replace(" ", "").replace("Договірна", ""),
                'place' :  textAll[2].find("p").text.split("-")[0],
                'data' :  textAll[2].find("p").text.split("-")[1],
                'dataGet' : str(datetime.datetime.now()),
                'url' : "https://www.olx.ua/"+card_div.find('a')['href'],
                'img' : img_src.replace("s=200x0;q=50", "s=750x1000"),
            }
            
            try:
                response = requests.get(textAds['url'], timeout=10)
                response.raise_for_status()  
            except requests.exceptions.RequestException as e:
                print(f"Виникла помилка під час запиту там де сторінка оголошення: {e}")
                return ["error", []]  
            soup = BeautifulSoup(response.text, 'lxml')
            
            textAds['description'] = soup.find('div', attrs={'data-cy': 'ad_description'}).text[4:]
            textAds['user_reg'] = soup.find('a', attrs={'data-testid': 'user-profile-link'}).find('div', string=lambda text: text and "Member" in text).text.replace("Member Since", "")
            textAds['user_reg'] = "✅"+textAds['user_reg'] if datetime.datetime.now().strftime("%B %Y") != textAds['user_reg'] else "❌"+textAds['user_reg']

            if len(textAds['description']) > 600:
                textAds['description'] = textAds['description'][:600]+"...🔻🔻🔻"
        except AttributeError:
            print(textAll)
            continue
        try:
            with open("olxSee.txt", "a", encoding="utf-8") as file:
                file.write("|{:^9}|{:<70}|{:10}|{:10} | {:15}| {:23} | {:120} | {:100} | {}\n".format(
                    textAds['id'], 
                    textAds['title'],
                    textAds['price'], 
                    textAds['data'], 
                    textAds['dataGet'], 
                    textAds['place'], 
                    textAds['url'], 
                    textAds['img'],
                    textAds['description'], 
                    ))
        except Exception as e:
            print(e)
            return ["BAD помилка запису у файл", []]
        return ["NEW", textAds]
    return [f"BAD {card_divs=}", []]
import time

import requests
import telegram
from bs4 import BeautifulSoup

TOKEN = "TOKEM TELEGRAM AQUI"

bot = telegram.Bot(token=TOKEN)

url = "https://neoxleitor.com/manga/56789/"
r = requests.get(url)
ultimo_cap = [130, 131, 132, 133]
penultimo = ultimo_cap[-1]
last_cap = [134]
cap = []
html_content = r.text
soup = BeautifulSoup(html_content, "html.parser")
lista_data = soup.select(
    "body > div.wrap > div > div > div > div.c-page-content.style-1 > div > div > div > div > div > div.c-page > div > div.page-content-listing.single-page > div > ul > li:nth-child(1) > a"
)
lista_data2 = soup.select(
    "body > div.wrap > div > div > div > div.c-page-content.style-1 > div > div > div > div > div > div.c-page > div > div.page-content-listing.single-page > div > ul > li:nth-child(1) > a[href]"
)
img_new = soup.select(
    "body > div.wrap > div > div > div > div.c-page-content.style-1 > div > div > div > div > div > div.c-page > div > div.page-content-listing.single-page > div > ul > li:nth-child(1) > span > span > a > img[src]"
)


for x in lista_data2:
    linkcap = x.attrs["href"]


for lista_dados in lista_data:
    capitulo = lista_dados.next_element


def send_telegram(txt):
    Mensagem = f"{txt} "
    bot.send_message(chat_id=CHATID_AQUI, text=Mensagem)
    print("Mensagem enviada")


while True:
    for ig in img_new:
        cap = str(capitulo.lstrip()[4:])
        if "new.gif" in ig.attrs["src"][55:63]:
            if cap == last_cap[-1]:
                print("...")
            else:
                last_cap.append(cap)
                print(f"ultimo {cap}")
                send_telegram(
                    f"Novo capitulo Solo Leveling: {capitulo.lstrip()[4:]} \n{linkcap} "
                )
        else:
            cap = str(capitulo.lstrip()[4:])
            print(cap)

    print("Rodando...")
    time.sleep(1440 * 60)
    # um dia 24 horas ou 1440 minutos
    # time.sleep(1440 * 60)
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
last_cap = [133]
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


if img_new == "":
    for ig in img_new:
        new_cap = ig.attrs["src"][55:63]
        cap = capitulo.lstrip()[4:]

else:
    cap = capitulo.lstrip()[4:]
    new_cap = (img_new == "")



def send_telegram(txt):
    Mensagem = f"{txt} "
    bot.send_message(chat_id=CHAT_ID, text=Mensagem)
    print("Mensagem enviada")


def validade_cap():
    if new_cap == False:
        cap = capitulo.lstrip()[4:]
        if cap == last_cap[-1]:
            print(f"...")
        else:
            last_cap.append(cap)
            print(f"ultimo {cap}")
            send_telegram(
                f"Novo capitulo Solo Leveling: {capitulo.lstrip()[4:]} \n{linkcap} "
            )
    else:
        last_cap.append(cap)
        print(f"ultimo {cap}")
        send_telegram(
            f"Novo capitulo Solo Leveling: {capitulo.lstrip()[4:]} \n{linkcap} "
        )


while True:
    validade_cap()

    print("Rodando...")
    time.sleep(1440 * 60)
    # time.sleep(1440 * 60)
    # um dia 24 horas ou 1440 minutos
    # time.sleep(1440 * 60)

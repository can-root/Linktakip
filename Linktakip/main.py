import requests
import random
from renk import renk

def rastgele_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.6 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0"
    ]
    return random.choice(user_agents)


def logo():
    print(f"""{renk.BEYAZ}


 _      ____  ____   __  _
| |    |    ||    \ |  |/ ]
| |     |  | |  _  ||  ' /
| |___  |  | |  |  ||    |
|     | |  | |  |  ||     |
|     | |  | |  |  ||  .  |
|_____||____||__|__||__|\_|




""")

def yonlendirme_urlunu_al(kisa_url):
    headers = {
        "User-Agent": rastgele_user_agent()
    }
    try:
        response = requests.head(kisa_url, headers=headers, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        return None

def ascii_sanat(url):
    ascii_art = f"""
    ╔══════════════════════════════════════════╗
      Kısaltılmış linkin yönlendirdiği URL:

      {url}

    ╚══════════════════════════════════════════╝
    """
    return ascii_art

logo()
kisa_url = input("Kısaltılmış linki girin: ")
yonlendirme_url = yonlendirme_urlunu_al(kisa_url)

if yonlendirme_url:
    print(renk.YESIL + ascii_sanat(yonlendirme_url))
else:
    print(f"{renk.KIRMIZI}Kısaltılmış link açılamadı.")

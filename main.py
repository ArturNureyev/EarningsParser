from bs4 import BeautifulSoup
import requests
import datetime


def earnings_next_two_weeks():
    earnings = {}
    url = "https://www.earningswhispers.com/calendar?sb=s&d=0&t=all"

    headers = {
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }

    earnings_date = datetime.date.today()
    for i in range(14):
        if earnings_date.weekday() == 5 or earnings_date.weekday() == 6:
            url = url.replace(str(i), str(i + 1))
            earnings_date = earnings_date + datetime.timedelta(days=1)
            continue
        dict_date = earnings_date.strftime("%m/%d/%Y")
        earnings[dict_date] = ""
        src = requests.get(url, headers=headers).text
        soup = BeautifulSoup(src, "lxml")
        tickers = soup.find_all(class_="ticker")
        for item in tickers:
            earnings[dict_date] = f"{earnings[dict_date]}{item.text} "
        url = url.replace(str(i), str(i + 1))
        earnings_date = earnings_date + datetime.timedelta(days=1)
    return earnings


earnings_next_two_weeks()

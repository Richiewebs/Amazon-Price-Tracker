import requests
from twilio.rest import Client
from bs4 import BeautifulSoup

account_sid = "Your account_sid"
auth_token = "your_auth_token"
PRODUCT_URL = "https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.4b335ede-a344-46a5-af28-95a1242a7034&keywords=video%2Bgaming&pd_rd_r=5af5db59-162e-4292-a5e6-b7f62d952520&pd_rd_w=6cfzR&pd_rd_wg=7aYnQ&pf_rd_p=4b335ede-a344-46a5-af28-95a1242a7034&pf_rd_r=65T4VTNQYFGXHR5JMCH3&qid=1707209726&sr=8-2&th=1"
HTTP_PARAMS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8,mt;q=0.7,fr;q=0.6"
}
response = requests.get(url=PRODUCT_URL, headers=HTTP_PARAMS)
response.raise_for_status()
data = response.text
soup = BeautifulSoup(data, "html.parser")
price = soup.find(name="span", class_="a-offscreen")
price_value = price.getText()

if price_value < "200":
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body=f"  Price Alert📢📢  "
                 f"The price of the Advanced all in one virtual reality Headset is low so buy now!",
            from_="+18635887109",
            to="+233555562965"
        )
    print(message.status)

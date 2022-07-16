import requests
import os
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

Stock_api = "K0TDKGJONWKEAYFW"
News_api="cce1dfc5baae4eeb8704dc4f18d6071a"

def message_body(list):
    for i in list:
        return i

# TODO 1. - Get yesterday's closing stock price.

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": "K0TDKGJONWKEAYFW"
}
response = requests.get(STOCK_ENDPOINT, params=stock_param)
# print(response.json())
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price

day_bf_yesterday = data_list[1]["4. close"]
print(day_bf_yesterday)

# TODO 3. - Find the positive difference between 1 and 2.

difference = abs(float(yesterday_closing_price) - float(day_bf_yesterday))
# TODO 4. - Work out the percentage difference in price between closing price yesterday
#  and closing price the day before yesterday.

percentage_difference = (difference / float(yesterday_closing_price)) * 100
print(percentage_difference)


# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

new_params={
    "apiKey":News_api,
    "q":COMPANY_NAME
}
news_response=requests.get(NEWS_ENDPOINT,new_params)
new_data = news_response.json()["articles"]
three_articles=new_data[:3]
# print(three_articles)


# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

formtted_article_list=[f"Headline: {article['title']}.  Description:{article['description']} " for article in three_articles]
print(formtted_article_list)


# TODO 9. - Send each article as a separate message via Twilio.
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                     body= message_body(formtted_article_list),
                     from_='+15017122661',
                     to='+15558675310'
                 )




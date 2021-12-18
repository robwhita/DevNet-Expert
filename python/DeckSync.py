import requests
import time

start_time = time.time()


# For loop that iterates through block of code 104 times. Parse response to print out card info
for number in range(1, 105):
    url = f'https://deckofcardsapi.com/api/deck/new/draw/'
    resp = requests.get(url)
    card = resp.json()
    print(f'{card["cards"][0]["value"]} of {card["cards"][0]["suit"]}') 

print("--- %s seconds ---" % (time.time() - start_time))
# 3. this data will be used to analyze
# 4. store in SQL data base: YES!
# 5. retrieve data to perform analysis
# 6. create a time dependent updata of new data that is being retrieved



# libraries for getting HTML and CSS data
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
from itertools import groupby

# create a variable inside the url that will
pages = ['1','2','3','4','5','6','7','8','9','10']
new_price = []
new_sqft = []
for i in pages:
    vari = "https://www.recolorado.com/find-real-estate/co/denver/" + i + "-pg/price-aorder/exclusive-dorder/photo-tab/"
    page = requests.get(vari)
    soup = BeautifulSoup(page.content,'html.parser')
    #URL = "https://www.recolorado.com/find-real-estate/co/denver/1-pg/price-aorder/exclusive-dorder/photo-tab/"

    results = soup.find('div', {"class": "results results__photo"})
    sqft_results = []
    sqft_results = results.find_all('li', class_ = 'listing--detail listing--detail__photo listing--detail__sqft')

    prices_results = []
    prices_results = results.find_all('li', class_ = 'listing--detail listing--detail__photo listing--detail__price')
# do arrays require size
    sq = np.array([])
    array = np.array([])
    price = np.array([])


    for i in prices_results:
        for j in i:
            for k in j:
                for l in k:
                    price = np.append(price,k)
                    price = np.delete(price, np.argwhere(price == ' '))
                    price = np.delete(price, np.argwhere(price == '\n'))
                    price = np.delete(price, np.argwhere(price == '\r'))
                    price = np.delete(price, np.argwhere(price == ','))
                    price_list = price.tolist()
        price_results = [int("".join(map(str, v))) for k, v in groupby(price_list, key=lambda x: x!='$') if k]
    #print(price_results)


    for i in sqft_results:
        for j in i:
            for k in j:
                array = np.append(array,k)
                array = np.delete(array, np.argwhere(array == ' '))
                array = np.delete(array, np.argwhere(array == '\n'))
                array = np.delete(array, np.argwhere(array == '\r'))

    units = ['s','S','q','f',',']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    for i in array:
        for individual_letter in units:
            if i == individual_letter:
                array = np.delete(array, np.argwhere(array == individual_letter))

    new_array0 = array.tolist()
    new_array1 = np.array([])



    lst = []
    for i in new_array0:
        if i == 't':
            lst.append(i)
        for number in numbers:
            if i == number:
                i = int(i)
                lst.append(i)
    sqft_results = [int("".join(map(str, v))) for k, v in groupby(lst, key=lambda x: x!='t') if k]
    #print(sqft_results)


    price_results = [int("".join(map(str, v))) for k, v in groupby(price_list, key=lambda x: x!='$') if k]
    sqft_results = [int("".join(map(str, v))) for k, v in groupby(lst, key=lambda x: x!='t') if k]


    new_price.append(price_results)
    new_sqft.append(sqft_results)
    #sqft_data.append(sqft_results)
print(new_price)
print(new_sqft)
# import time
# start_time = time.time()
# # main()
# print("--- %s seconds ---" % (time.time() - start_time))
#print(sqft_data)

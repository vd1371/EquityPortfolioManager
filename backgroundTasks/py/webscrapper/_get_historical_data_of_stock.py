import os
from datetime import datetime
import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from ._get_the_webdriver import _get_the_webdriver
from py.utils.template_names import price_columns

def _get_historical_data_of_stock(code, frequency = "1d"):

    DATE_FORMAT = os.getenv("DATE_FORMAT")
    START_DATE = os.getenv("START_DATE")
    
    start_date = int(datetime.strptime(START_DATE, DATE_FORMAT).timestamp())
    end_date = datetime.today().timestamp()

    url = f"https://finance.yahoo.com/quote/{code}.HK/history?" + \
        f"period1={start_date}&period2={end_date}&interval={frequency}" + \
        f"&filter=history&frequency=1d&includeAdjustedClose=true"
    driver = _get_the_webdriver(url)
    time.sleep(3)

    ## Close the pop up about subscribing
    try:
        driver.find_element(
            By.XPATH,
            '//*[@id="myLightboxContainer"]/section/button[2]'
        ).click()
    except:
        pass
    time.sleep(2)
    
    driver.find_element(By.XPATH, '//span[text()="Apply"]').click()
    for _ in range(3):
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.close()

    # Parse the table
    tables = soup.find_all("tbody")
    data_table = tables[0].find_all("tr")
    all_values = []
    for row in data_table:
        values = [val.getText() for val in row.find_all("td")]
        all_values.append(values)

    # Convert to dataframe
    df = pd.DataFrame(
        all_values,
        columns = price_columns)

#     print ("The data is about to be read from the utils folder for development. " + \
#             "Make sure to update the code for future.")
#     df = pd.read_csv("./py/utils/tmp.csv", index_col = 0)

    df.columns = [col.lower() for col in df.columns]

    df.set_index("date", drop = True, inplace = True)
    df.dropna(axis = 0, inplace = True)
    df.loc[df['volume'] == "-", "volume"] = "0"
    df['volume'] = df['volume'].str.replace(',', "")
    df = df.apply(pd.to_numeric)
    df.index = pd.to_datetime(df.index)

    return df
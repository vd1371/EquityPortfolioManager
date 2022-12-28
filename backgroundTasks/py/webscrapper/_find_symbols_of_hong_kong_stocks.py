import pandas as pd
from bs4 import BeautifulSoup

from ._get_the_webdriver import _get_the_webdriver

def _find_symbols_of_hong_kong_stocks():

    url = "https://en.wikipedia.org/wiki/List_of_companies_listed_on_the_Hong_Kong_Stock_Exchange"
    driver = _get_the_webdriver(url)
    soup = BeautifulSoup(driver.page_source)
    tables = soup.find_all("table")
    driver.close()

    all_companies = []
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            stock = row.getText()[6:] #The first 5 characters are "SEHK: "
            stock = stock.rstrip().split(" ", 1)
            all_companies.append([stock[0].zfill(4), stock[1]])

    df = pd.DataFrame(all_companies, columns = ["StockCode", "StockName"])

    return df
    
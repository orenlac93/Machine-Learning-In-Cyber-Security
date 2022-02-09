from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

# setup chrome driver
PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# choose website
driver.get("https://moz.com/top500")

# find all the table raw elements of the html
table = driver.find_elements(By.TAG_NAME, 'tr')

# create lists to store the urls and the labels
url_list = []
label_list = []

# print name of all links and insert them to list
for row in table:
    if '.' in row.text:
        url = row.find_element_by_tag_name('a')

        url_list.append(url.text)
        label_list.append('good')

        print(url.text)


# create data frame of urls
url_data_frame = pd.DataFrame(url_list, columns=['url'])
# create data frame of labels
label_data_frame = pd.DataFrame(label_list, columns=['label'])

# create new data frame of both urls and labels
X = [url_data_frame["url"], label_data_frame["label"]]
headers = ["url", "label"]
X = pd.concat(X, axis=1, keys=headers)

# write the new data set to csv file
to_csv = X.to_csv("data/scraping_data.csv", index=False)

driver.quit()

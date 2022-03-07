from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import threading
import csv
import random

""" *TODO:* 
def getHTML(PATH = "C:/Program Files (x86)/chromedriver.exe"):
    random_word = r.get_random_word()
    random_word = "test"
    driver = webdriver.Chrome(PATH)
    driver.get("https://google.com/search?q="+random_word+'&hl=en')
    htmltext = driver.page_source
    driver.quit()
    return htmltext
"""


def getURL(num_of_pages=3, language='en'):
    pages_to_scan = []
    for i in range(num_of_pages):
        random_word = randomWordGenerator()
        pages_to_scan.append("https://google.com/search?q=" + random_word + '&hl=' + language + '&start=' + str(i * 10))
    # &start=0 -> page1 | 10 -> page2 ..
    return pages_to_scan


def scanNPages(lock, file, url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        valid_url = str(link.get('href'))
        valid_url = valid_url.replace('/url?q=', '')
        if (valid_url.startswith('https:/')):
            urls.append(valid_url)

        writeToCSV(urls, lock, file)


def writeToCSV(urls, lock, file):
    lock.acquire()
    writer = csv.writer(file, delimiter=',')
    for j in urls:
        writer.writerow([j])
    lock.release()


def scanPage(num_of_pages, lock, file):
    # TODO: scan the first $num_of_pages,
    url_to_scan = getURL(num_of_pages, 'en')
    threads = []
    for url in url_to_scan:
        scanNPages(lock, file, url)


def printLists(urls):
    for x in urls:
        print(x)


def randomWordGenerator(url='https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/'):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    list_of_words = []
    for word in soup.find_all('p'):
        word = str(word)
        word = word.split('<br/>')
        list_of_words.append(word)
    list_of_words = list_of_words[len(list_of_words) - 1]
    return random.choice(list_of_words)


def startMission(num_of_threads=5):
    file = open('urls_file.csv', 'w')
    threads = []
    for i in range(num_of_threads):
        thread = threading.Thread(target=scanPage, args=(3, threading.Lock(), file,))
        threads.append(thread)

    for i in range(num_of_threads):
        threads[i].start()

    for i in range(num_of_threads):
        threads[i].join()

    file.close()
    print("Done!")


startMission(10)

from faker import Faker
import os
from urllib.parse import urlunsplit, urlencode
import random
import pandas as pd
from hashlib import sha256
from datetime import date

# crate a custom url by choosing: protocol(http/https), domain(abc...), path(/home/...), ending(.com/.net ...)
def build_url(protocol, domain, path, ending):
    SCHEME = os.environ.get("API_SCHEME", protocol)
    NETLOC = os.environ.get("API_NETLOC", domain)
    path = f"{path}/"
    query = ending

    return f"{SCHEME}://{NETLOC}/{path}{query}"


# generate fake by choosing format (url/uri)
def build_fake_url(format):

    fake = Faker()
    if format == "url":
        return fake.url()
    elif format == 'uri':
        return fake.uri()
    else:
        print()


# generate url by using simple DGA algorithm (generate a domain name for the given date)
def dga_by_date(year: int, month: int, day: int) -> str:

    domain = ""

    for index in range(16):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        domain += chr(((year ^ month ^ day) % 25) + 97)

    return domain + ".com"


# generate url by using another version of DGA algorithm (url contains random words and tld)
def dga_by_date_and_sha256_and_words(num, date_str=None):

    random_words = ['download', 'file', 'firewall', 'web', 'server', 'microservice',
                    'compiler', 'internet', 'winrar', 'winzip', 'linux']

    random_word = random_words[random.randint(0, random_words.__len__()-1)]

    if date_str is None:
        date_str = '{0.year}-{0.month}-{0.day}'.format(date.today())

    tlds = ['.com', '.co.uk', '.org', '.fr', '.co.il']
    hash = sha256('{0}{1}'.format(date_str, num).encode('utf-8')).hexdigest()[3:20]
    replace_char = chr(0xff & ((num % 26) + 97))

    return (random_word + '{0}{1}{2:433}'.format(replace_char, hash, tlds[num % len(tlds)])).replace(" ", "")


# create lists to store the urls and the labels
url_list = []
label_list = []

#######################################################################
# examples ############################################################
#######################################################################
'''
url_list.append(build_url("http", "www.mal.net", "download", "run.exe"))
url_list.append(str(build_fake_url("url")))
url_list.append(str(build_fake_url("uri")))

for i in range(url_list.__len__()):
    print(url_list[i])

print(dga_by_date(1, 1, 2022))
print(dga_by_date(3, 6, 2012))
'''


# generate list of urls by using dga
num_of_iterations = 100000
for num in range(num_of_iterations):
    #url_list.append(dga_by_date(random.randint(1, 999), random.randint(1, 999), random.randint(1, 9999)))
    url_list.append(dga_by_date_and_sha256_and_words(num))
    label_list.append('bad');
    

# create data frame of urls
url_data_frame = pd.DataFrame(url_list, columns=['url'])
# create data frame of labels
label_data_frame = pd.DataFrame(label_list, columns=['label'])

# create new data frame of both urls and labels
X = [url_data_frame["url"], label_data_frame["label"]]
headers = ["url", "label"]
X = pd.concat(X, axis=1, keys=headers)
X.drop_duplicates(subset=["url", "label"], keep=False, inplace=True)

print(X)

# write the new data set to csv file
to_csv = X.to_csv("data/url_data_dga.csv", index=False)

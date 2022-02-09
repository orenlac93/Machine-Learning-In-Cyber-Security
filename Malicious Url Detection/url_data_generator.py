from faker import Faker
import os
from urllib.parse import urlunsplit, urlencode
import random
import pandas as pd

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


# generate url by using dga algorithm
def dga_by_date(year: int, month: int, day: int) -> str:
    """Generate a domain name for the given date."""
    domain = ""

    for index in range(16):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        domain += chr(((year ^ month ^ day) % 25) + 97)

    return domain + ".com"


# create lists to store the urls and the labels
url_list = []
label_list = []


### examples ###

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
for num in range(100000):
    url_list.append(dga_by_date(random.randint(1, 999), random.randint(1, 999), random.randint(1, 9999)))
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
to_csv = X.to_csv("data/dga_data.csv", index=False)

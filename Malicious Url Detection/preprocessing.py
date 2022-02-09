import pandas as pd

'''
preprocessor for url string

parsing the url string into different features to enable
model prediction 
'''
def preProcess(url):
    url = pd.DataFrame(url, columns=["url"])

    has_com = []
    size = []
    num_of_digits = []
    num_of_q_mark = []
    has_php = []

    for column in url:
        size.append(len(column))

    for column in url:
        if ".com" in column:
            has_com.append(1)
        else:
            has_com.append(0)

    for column in url:
        count = 0
        for char in column:
            if char.isdigit():
                count += 1
        num_of_digits.append(count)

    for column in url:
        count = 0
        for char in column:
            if char == '?':
                count += 1
        num_of_q_mark.append(count)

    for column in url:

        if "php" in column:
            has_php.append(1)
        else:
            has_php.append(0)

    url_size = pd.DataFrame(size, columns=['url_size'])
    url_has_com = pd.DataFrame(has_com, columns=['has_com'])
    url_num_of_digits = pd.DataFrame(num_of_digits, columns=['num_of_digits'])

    non_alpha = pd.DataFrame(url["url"].str.count(r'[^a-zA-Z0-9 ]'))
    non_alpha.columns = ['non_alpha']

    num_of_q_mark = pd.DataFrame(num_of_q_mark, columns=["num_of_q_mark"])
    num_of_q_mark

    url_has_php = pd.DataFrame(has_php, columns=['has_php'])
    url_has_php

    num_of_routes = pd.DataFrame(url["url"].str.count('/'))
    num_of_routes.columns = ['num_of_routes']

    num_of_dots = pd.DataFrame(url["url"].str.count(r"\."))
    num_of_dots.columns = ['num_of_dots']

    contains_login = pd.DataFrame(url["url"].str.count('login'))
    contains_login.columns = ['contains_login']

    contains_client = pd.DataFrame(url["url"].str.count('client'))
    contains_client.columns = ['contains_client']

    contains_admin = pd.DataFrame(url["url"].str.count('admin'))
    contains_admin.columns = ['contains_admin']

    contains_server = pd.DataFrame(url["url"].str.count('server'))
    contains_server.columns = ['contains_server']

    contains_ip = pd.DataFrame(url["url"].str.count(
        r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"))
    contains_ip.columns = ['contains_ip']

    num_of_fragments = pd.DataFrame(url["url"].str.count('\#'))
    num_of_fragments.columns = ['num_of_fragments']

    num_of_parameters = pd.DataFrame(url["url"].str.count('\&'))
    num_of_parameters.columns = ['num_of_parameters']

    contains_exe = pd.DataFrame(url["url"].str.count("exe"))
    contains_exe.columns = ['contains_exe']

    X = [url_size["url_size"], url_has_com["has_com"], url_num_of_digits["num_of_digits"], non_alpha["non_alpha"],
         num_of_q_mark["num_of_q_mark"], url_has_php["has_php"], num_of_routes['num_of_routes'],
         num_of_dots['num_of_dots'],
         contains_login["contains_login"], contains_client["contains_client"], contains_admin["contains_admin"],
         contains_server["contains_server"], contains_ip["contains_ip"], num_of_fragments["num_of_fragments"],
         num_of_parameters["num_of_parameters"], contains_exe["contains_exe"]]

    headers = ["url_size", "has_com", "num_of_digits", "non_alpha", "num_of_q_mark", "has_php", "num_of_routes",
               "num_of_dots",
               "contains_login", "contains_client", "contains_admin", "contains_server", "contains_ip",
               "num_of_fragments",
               "num_of_parameters", "contains_exe"]

    X = pd.concat(X, axis=1, keys=headers)

    return X



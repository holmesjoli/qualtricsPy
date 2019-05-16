import requests


def get(endpoint, headers):
    """
    GET to the API
    """
    response = requests.get(url=endpoint,
                            headers=headers)

    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print(response.text)
        # self.response.raise_for_status()


def post(endpoint, data, headers):
    """
    Posts to the API
    :param endpoint: the endpoint of the post call
    :type endpoint: string
    :param data: the data to post
    :type data: dct
    :param headers: the headers to post
    :type headers: dct
    """
    response = requests.post(url=endpoint,
                             json=data,
                             headers=headers)

    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print(response.text)
        # self.response.raise_for_status()


def put(endpoint, data, headers):
    """
    PUT TO API
    """
    response = requests.put(url=endpoint,
                            json=data,
                            headers=headers)

    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print(response.text)
        # self.response.raise_for_status()

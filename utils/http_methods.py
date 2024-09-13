import requests


class Http_methods:
    headers = {
        "Content-Type": "application/json",
    }

    cookies = ""

    @staticmethod
    def get(url, params=None):
        result = requests.get(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies, params=params)
        return result

    @staticmethod
    def post(url, data=None, json=None):
        result = requests.post(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies,
                               json=json, data=data)
        return result

    @staticmethod
    def put(url, data=None, json=None):
        result = requests.put(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies,
                              json=json, data=data)
        return result

    @staticmethod
    def patch(url, data=None, json=None):
        result = requests.patch(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies,
                                json=json, data=data)
        return result

    @staticmethod
    def delete(url, data=None, json=None):
        result = requests.delete(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies,
                                 json=json, data=data)
        return result

    @staticmethod
    def head(url):
        result = requests.head(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return result

    @staticmethod
    def options(url):
        result = requests.options(url=url, headers=Http_methods.headers, cookies=Http_methods.cookies)
        return result
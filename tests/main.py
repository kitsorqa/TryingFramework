import requests
import pytest
from utils.config_loader import load_config
from tenacity import retry, wait_fixed, stop_after_attempt, retry_if_exception_type, retry_if_not_result


class TestClass:
    config = load_config()
    web_url = config['api_base_url']
    endpoint_posts = config['endpoints']['posts']

    @retry(wait=wait_fixed(1), stop=stop_after_attempt(3),
           retry=(retry_if_exception_type(requests.exceptions.RequestException)))
    def test_status_code(self, code=200):
        response = requests.get(f'{self.web_url}{self.endpoint_posts}')
        assert response.status_code == code

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3),
           retry=retry_if_exception_type(requests.exceptions.RequestException))
    def test_response_structure(self, *args):
        response = requests.get(f'{self.web_url}{self.endpoint_posts}')
        json_response = response.json()
        for post_row in json_response:
            for key in args:
                assert key in post_row

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3),
           retry=retry_if_exception_type(requests.exceptions.RequestException))
    def test_response_time(self, max_time_response=500):
        response = requests.get(f'{self.web_url}{self.endpoint_posts}')
        response_time = response.elapsed.total_seconds() * 1000
        assert response_time < max_time_response

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3),
           retry=retry_if_exception_type(requests.exceptions.RequestException))
    def test_headers_are_not_empty(self, required_headers=('Content-Type', 'Date', 'Server')):
        response = requests.get(f'{self.web_url}{self.endpoint_posts}')
        response_headers = response.headers
        assert len(response_headers) > 0
        required_headers = required_headers
        for header in required_headers:
            assert header in response_headers

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3),
           retry=retry_if_exception_type(requests.exceptions.RequestException))
    def test_content_type_header(self):
        response = requests.get(f'{self.web_url}{self.endpoint_posts}')
        content_type_header = response.headers.get('Content-Type')
        assert 'application/json' in content_type_header

    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3),
           retry=retry_if_exception_type(requests.exceptions.RequestException))
    def test_response_data(self, *args):
        response = requests.get(f'{self.web_url}{self.endpoint_posts}')
        json_response = response.json()
        for post_key in json_response:
            for arg in args:
                assert arg in post_key


Example = TestClass()
example_response = Example.test_status_code(200)
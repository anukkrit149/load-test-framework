import requests
import logging
import time

logging.basicConfig(filename='fraud.log', encoding='utf-8', level=logging.DEBUG)

BASE_URL = ""


def _build_url(route):
    return BASE_URL + "/" + route


class Fraud:
    def __init__(self):
        self.connection: requests.Session = None

    def init_conn(self):
        self.connection = requests.Session()
        self.connection.mount("https://", requests.adapters.HTTPAdapter(pool_connections=2))
        self.ping_conn()

    def ping_conn(self):
        logging.info(self.connection.get(_build_url("ping")))

    def ping_diff_url(self):
        logging.info(self.connection.get("https://ads-service.zeptonow.dev/ping"))

    def post_fraud(self):
        self.connection.post(_build_url("post"), data={})


if __name__ == "__main__":
    fraud_obj = Fraud()
    fraud_obj.init_conn()
    time.sleep(5)
    fraud_obj.ping_diff_url()
    time.sleep(1)
    fraud_obj.ping_conn()

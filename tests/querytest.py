import unittest
from main import app


# Standard response for successful HTTP requests
def test_url_location_valid():
    with app.test_client() as test:
        respon= test.get("http://127.0.0.1:5000/")
        assert respon.status_code == 200


# The request has been accepted for processing
def test_url_reuest_accept():
    with app.test_client() as test:
        respon= test.get("http://127.0.0.1:5000/")
        assert respon.status_code == 202


# The server successfully processed the request and is not returning any content
def test_url_vsuccessfully_process_but_return_anydata():
    with app.test_client() as test:
        respon= test.get("http://127.0.0.1:5000/")
        assert respon.status_code == 204


# The requested resource could not be found but may be available in the future.
def test_data_found():
    with app.test_client() as test:
        respon= test.get("http://127.0.0.1:5000/")
        assert respon.status_code == 404


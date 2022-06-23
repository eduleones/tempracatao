from http import HTTPStatus

import pytest
from django.urls import reverse

from tempracatao.healthcheck.enums import Status


class TestHealthcheckView:
    @pytest.fixture
    def healthcheck_url(self):
        return reverse("healthcheck")

    def test_should_return_successfull_payload(self, client, healthcheck_url):
        response = client.get(healthcheck_url)
        body = response.json()

        assert response.status_code == HTTPStatus.OK
        assert body["status"] == Status.OK.value

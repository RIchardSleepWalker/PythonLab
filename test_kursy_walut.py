from kursy_walut import pobierz_cene_euro

def test_pobierz_cene_euro(mocker):
    # 1. Tworzymy FAKE odpowiedź .json()
    fake_json = {
        "table": "A",
        "currency": "euro",
        "code": "EUR",
        "rates": [
            {"no": "012/A/NBP/2024", "effectiveDate": "2024-01-17", "mid": 4.56}
        ]
    }
    fake_response = mocker.Mock()
    fake_response.json.return_value = fake_json
    fake_response.raise_for_status.return_value = None
    mocker.patch("kursy_walut.requests.get", return_value=fake_response)
    wynik = pobierz_cene_euro()
    assert wynik == 4.56

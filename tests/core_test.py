import os
import pytest
import mmimage as image
from dotenv import load_dotenv


class TestImage:
    SAMPLE_URL = (
        "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/7942/79421478.jpg?_ex=200x200"
    )

    def test_all(self):
        path = image.download(TestImage.SAMPLE_URL)
        image.convert(path)
        image.upload_to_gyazo(path)  # use .env

    def test_all_invalid_token(self):
        path = image.download(TestImage.SAMPLE_URL)
        image.convert(path)
        image.upload_to_gyazo(path, "invalid_token")

    def test_convert(self):
        path = image.download(TestImage.SAMPLE_URL)
        image.convert(path)

    def test_convert2(self):
        path = image.download(TestImage.SAMPLE_URL)
        image.convert(path, "/tmp/image/hoge")

    def test_convert_error(self):
        image.convert("hoge")

    @pytest.mark.parametrize(
        "url", [("https://thumbnail.image.rakuten.co.jp/hoge"), ("http://www.google.co.jp")]
    )
    def test_download_error(self, url):
        with pytest.raises(Exception):
            image.download(url)

    def test_hello(self):
        image.hello()

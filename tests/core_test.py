import os
import uuid
import pytest
import mmimage as image


class TestImage:
    SAMPLE_URL_1 = (
        "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/7942/79421478.jpg?_ex=200x200"
    )
    SAMPLE_URL_2 = "https://prtimes.jp/i/23199/41/resize/d23199-41-642045-0.jpg"

    def test_all(self):
        with image.download(TestImage.SAMPLE_URL_1) as save_path:
            image.resize(save_path, width=200)
            assert os.path.isfile(save_path) is True
            url = image.upload_to_gyazo(save_path)  # use .env
            assert url is not ""
        assert os.path.isfile(save_path) is False

    def test_all_invalid_token(self):
        with image.download(TestImage.SAMPLE_URL_1) as save_path:
            image.resize(save_path)
            image.upload_to_gyazo(save_path, "invalid_token")

    def test_convert(self):
        with image.download(TestImage.SAMPLE_URL_1) as save_path:
            image.resize(save_path)

    @pytest.mark.parametrize("url", [(SAMPLE_URL_1), (SAMPLE_URL_2)])
    def test_convert2(self, url):
        with image.download(url) as save_path:
            image.resize(save_path, width=500)

    def test_convert_error(self):
        image.resize(str(uuid.uuid4()))

    @pytest.mark.parametrize(
        "url", [("https://thumbnail.image.rakuten.co.jp/hoge"), ("http://www.google.co.jp")]
    )
    def test_download_error(self, url):
        with pytest.raises(Exception):
            with image.download(url):
                pass

    def test_hello(self):
        image.hello()

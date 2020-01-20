import pytest
import mmimage as image

# from mmimage import convert, download


# def test_aaa():
#     download("test")


class TestImage:
    def test_image(self):
        url = "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/7942/79421478.jpg?_ex=200x200"  # noqa
        path = image.download(url)

        image.convert(path)
        # image.upload_to_gyazo(path)

    @pytest.mark.parametrize(
        "url", [("https://thumbnail.image.rakuten.co.jp/hoge"), ("http://www.google.co.jp")]
    )
    def test_download_error(self, url):
        with pytest.raises(Exception):
            image.download(url)

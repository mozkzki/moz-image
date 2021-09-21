import os
import moz_image as image

SAMPLE_URL = (
    "https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/7942/79421478.jpg?_ex=200x200"
)


def example():
    with image.download(SAMPLE_URL) as save_path:
        image.resize(save_path, width=200)
        assert os.path.isfile(save_path) is True
        url = image.upload_to_gyazo(save_path)  # use .env
        assert url != ""
    assert os.path.isfile(save_path) is False


def main() -> None:
    example()


if __name__ == "__main__":
    main()

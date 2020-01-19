import os
import requests


GYAZO_UPLOAD_URL = "https://upload.gyazo.com/api/upload"


def download(url):
    file_path = _make_file_path(url)
    image = _download_image(url)
    _save_image(file_path, image)
    return file_path


def _make_file_path(url: str) -> str:
    file_name = url.rsplit("/", 1)[1].split("?")[0]
    file_path = os.path.join("/tmp/", file_name)
    return file_path


def _download_image(url: str, timeout: int = 10) -> bytes:
    response = requests.get(url, allow_redirects=False, timeout=timeout)
    if response.status_code != 200:
        e = Exception("HTTP status: " + str(response.status_code))
        raise e

    content_type = response.headers["content-type"]
    if "image" not in content_type:
        e = Exception("Content-Type: " + str(content_type))
        raise e

    return response.content


def _save_image(file_path: str, image: bytes) -> None:
    with open(file_path, "wb") as fout:
        fout.write(image)


def convert(path: str, new_path: str = None) -> None:
    if new_path is None:
        new_path = path

    # imagemagicが必要
    cmd = "convert {} -background none -gravity center -extent 302x200 {}".format(path, new_path)
    os.system(cmd)


def upload_to_gyazo(path: str, access_token: str) -> str:
    image = open(path, "rb")
    files = {"imagedata": ("filename.jpg", image, "image/jpeg")}
    data = {"access_token": access_token}
    response = requests.post(GYAZO_UPLOAD_URL, files=files, data=data)
    url = response.json()["url"]

    return url

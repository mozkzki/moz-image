import os
import sys
import uuid
import requests
from contextlib import contextmanager
from dotenv import load_dotenv
from PIL import Image as pimage

GYAZO_UPLOAD_URL = "https://upload.gyazo.com/api/upload"


def hello():
    print("hello!!")


@contextmanager
def download(url: str):
    image = _download_image(url)
    save_file_path = _save_image(image)
    try:
        yield save_file_path
    finally:
        os.remove(save_file_path)


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


def _make_save_file_path() -> str:
    file_name = str(uuid.uuid4())
    save_file_path = os.path.join("/tmp/mmimage/", file_name)
    return save_file_path


def _save_image(image: bytes) -> str:
    save_file_path = _make_save_file_path()

    # ディレクトリが存在しない場合は作る
    os.makedirs(os.path.dirname(save_file_path), exist_ok=True)

    with open(save_file_path, "wb") as fout:
        fout.write(image)

    return save_file_path


def resize(path: str, *, width: int = 302) -> None:
    if os.path.isfile(path) is not True:
        print("file does not exists. path={}".format(path), file=sys.stderr)
        return

    img = pimage.open(path)

    # 保存先のファイル名作成
    # フォーマット指定がないとエラーになる
    new_path = "".join((path, ".", img.format))

    # 画像の解像度を取得して、リサイズする高さを計算
    img_width, img_height = img.size
    resize_width = float(width)
    resize_height = resize_width / img_width * img_height

    # 画像をリサイズ
    img = img.resize((int(resize_width), int(resize_height)))
    img.save(new_path)

    # 古いファイルと入れ替える
    os.remove(path)
    os.rename(new_path, path)


def upload_to_gyazo(path: str, access_token: str = None) -> str:
    image = open(path, "rb")
    files = {"imagedata": image}
    # files = {"imagedata": ("filename", image, "image")}

    # 引数指定がなければ環境変数からaccess token読み込み
    if access_token is None:
        load_dotenv(verbose=True)
        access_token = os.environ.get("gyazo_access_token", "dummy_token")

    data = {"access_token": access_token}
    response = requests.post(GYAZO_UPLOAD_URL, files=files, data=data)
    if response.reason == "Unauthorized" and response.status_code == 401:
        print(
            "[error] gyazo access token is invalid!",
            "please set correct token by environment variable <gyazo_access_token>.",
        )
        return ""

    url = response.json()["url"]
    print("------------- URL: ", url)
    return url

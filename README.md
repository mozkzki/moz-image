# moz-image

画像関連の操作を行う自前ライブラリ。

## Function

- download
- resize
- upload_to_gyazo ([GYAZO](https://gyazo.com/ja)へのアップロード)

## Usage

Environmental variables

`.env`ファイルに書いてproject rootに配置。`.env_sample`をコピーすると楽。

```txt
gyazo_access_token=7c47...
```

Install

```sh
pip install git+https://github.com/mozkzki/moz-image
# upgrade
pip install --upgrade git+https://github.com/mozkzki/moz-image
# uninstall
pip uninstall moz-image
```

Coding

```python
import os
import moz_image as image

# download from rakuten books
with image.download("https://thumbnail.image.rakuten.co.jp/@0_mall/book/cabinet/7942/79421478.jpg?_ex=200x200") as save_path:
    # resize download image
    image.resize(save_path, width=200)
    # upload image to GYAZO
    url = image.upload_to_gyazo(save_path)
```

## Develop

base project: [mozkzki/moz-sample](https://github.com/mozkzki/moz-sample)

### Prepare

```sh
poetry install
poetry shell
```

### Run (Example)

```sh
python ./examples/example.py
# or
make start
```

### Unit Test

test all.

```sh
pytest
pytest -v # verbose
pytest -s # show standard output (same --capture=no)
pytest -ra # show summary (exclude passed test)
pytest -rA # show summary (include passed test)
```

with filter.

```sh
pytest -k app
pytest -k test_app.py
pytest -k my
```

specified marker.

```sh
pytest -m 'slow'
pytest -m 'not slow'
```

make coverage report.

```sh
pytest -v --capture=no --cov-config .coveragerc --cov=src --cov-report=xml --cov-report=term-missing .
# or
make ut
```

### Lint

```sh
flake8 --max-line-length=100 --ignore=E203,W503 ./src
# or
make lint
```

### Create API Document (Sphinx)

```sh
make doc
```

### Update dependency modules

dependabot (GitHub公式) がプルリクを挙げてくるので確認してマージする。

- 最低でもCircleCIが通っているかは確認
- CircleCIでは、最新の依存モジュールでtestするため`poetry update`してからtestしている
- dependabotは`pyproject.toml`と`poetry.lock`を更新してくれる

## AWS Lambda で使う場合

### 注意点

- `serverless-chrome`と`chromedriver`をLambda Layerに上げる必要あり([参照](https://hacknote.jp/archives/49974/))
- フォントがないと文字化けする
  - デプロイパッケージのルートに`.fonts`ディレクトリを作成してフォントを格納する([参照](https://qiita.com/havveFn/items/bb8cd0d937c671100200))
  - なお、CircleCI等でも同様だが、同じく`~/.fonts`に置くか[インストール](https://worklog.be/archives/3422#Google_Noto_Fonts)すれば良い

### serverless-chromeについて

Chrome を AWS Lambda で動作させる場合に利用できる。

- 最新のバージョンは1.0.0-55だが動かない
- 以下の組み合わで動確している([参考](https://github.com/adieuadieu/serverless-chrome/issues/133))
  - [severless-chrome](https://github.com/adieuadieu/serverless-chrome/releases)==[1.0.0-37](https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip) (64.0.3282.167 stable channel)
  - [chromedriver==2.37](http://chromedriver.storage.googleapis.com/index.html?path=2.37/)
  - selenium==3.141.0

### 環境変数

Lambda Layerではchrome等が/opt/に配置される。
`.env`は下記のようにする。

```env
CHROME_BINARY_LOCATION='/opt/headless/python/bin/headless-chromium'
CHROME_DRIVER_LOCATION='/opt/headless/python/bin/chromedriver'
```

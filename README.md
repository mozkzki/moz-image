# mmimage

## 必要な環境変数

```(sh)
gyazo_access_token=<please specify gyazo access toke>
```

## 依存ツール

- ImageMagick

### ImageMagick導入

```(sh)
yum -y install ImageMagick
yum -y install ImageMagick-devel
```

## インストール

```(sh)
pip install git+https://github.com/yukkun007/mmimage
```

## アップグレード

```(sh)
pip install --upgrade git+https://github.com/yukkun007/mmimage
```

## 使い方 (モジュールを利用)

```(sh)
python
>>> import mmimage
>>> mmimage.hello()
```

## 使い方 (コマンドラインアプリを実行)

```(sh)
mmimage
```

## アンインストール

```(sh)
pip uninstall mmimage
```

## 開発フロー

### 環境構築

1. 環境変数追加 (projectディレクトリに仮想環境作成)

    - Linux

        ```(sh)
        export PIPENV_VENV_IN_PROJECT=true
        ```

    - Windows

        ```(sh)
        set PIPENV_VENV_IN_PROJECT=true
        ```

1. `pip install pipenv`
1. `git clone git@github.com:yukkun007/mmimage.git`
1. `pipenv install --dev`

### install package

```(sh)
pip install .
```

### upgrade package

```(sh)
pip install --upgrade . (もしくは-U)
```

### install package (編集可能モード)

ソース編集の都度upgradeが不要になる。

```(sh)
pip install -e .
```

### モジュールを利用

```(sh)
python
>>> import mmimage
>>> mmimage.hello()
```

### コマンドラインアプリを実行

```(sh)
pipenv run start (もしくはmmimage)
```

### unit test

```(sh)
pipenv run ut
```

### lint

```(sh)
pipenv run lint
```

### create api document (sphix)

```(sh)
pipenv run doc
```

### ソースコード配布物の作成

dist/ 以下にmmimage-0.0.1.tar.gzが生成される。

```(sh)
python setup.py sdist
```

### ソースコード配布物からpipでインストール

```(sh)
pip install mmimage-0.0.1-tar.gz
```

### ビルド済み配布物(wheel形式)の作成

dist/ 以下にmmimage-0.0.1-py3-none-any.whlが生成される。

```(sh)
python setup.py bdist_wheel (wheelパッケージが必要)
```

### ビルド済み配布物(wheel形式)からpipでインストール

```(sh)
pip install mmimage-0.0.1-py3-none-any.whl
```

## 参考

### パッケージング/開発環境

- <https://techblog.asahi-net.co.jp/entry/2018/06/15/162951>
- <https://techblog.asahi-net.co.jp/entry/2018/11/19/103455>

### コマンドライン引数のパース

- <https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0>

### 環境変数の定義

- <https://pod.hatenablog.com/entry/2019/04/29/164109>

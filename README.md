# mmimage

## 依存ライブラリ

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

## アップデート

```(sh)
pip install -U git+https://github.com/yukkun007/mmimage
```

## 使い方

```(sh)
python
>>> import mmimage
>>> mmimage.hoge
```

## アンインストール

```(sh)
pip uninstall mmimage
```

## 開発

### 依存ツール

- pipenv

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

1. `git clone git@github.com:yukkun007/python-template.git`
1. `pip install pipenv`
1. `pipenv install --dev`

### unit test

```(sh)
pipenv run ut
```

### lint

```(sh)
pipenv run lint
```

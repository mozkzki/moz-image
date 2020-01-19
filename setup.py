from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

setup(
    name="mmimage",
    version="0.1.0",
    description="Magarimame's image library",
    long_description=readme,
    author="Yutaka Kato",
    author_email="kato.yutaka@gmail.com",
    url="https://github.com/yukkun007/mmimage",
    packages=find_packages(),
)

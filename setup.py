from setuptools import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='StockerX',
    version='0.1.3',
    description='🤖 Predict the stock market with AI ',
    py_modules=['beibo'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/manavcodaty/StockerX',
    author="Manav Codaty",
    author_email="manav.codaty@gmail.com",
    license='MIT',
    install_requires=[
        'darts',
        'yfinance'
    ],
)

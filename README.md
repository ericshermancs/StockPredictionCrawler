# Stock Prediction Scraper

Stock Prediction Scraper is a scrapy based crawler that obtains a list of tickers from [stockanalysis.com](https://stockanalysis.com/stocks/) and then obtains prediction data from [CNNMoney](https://money.cnn.com/data/markets/)

## Download

Use git to download the directory:

```bash
git clone https://github.com/ericshermancs/StockPredictionCrawler.git
```

## Install Requirements
```bash
pip install scrapy
```

## Run

```bash
cd StockPredictionCrawler/
scrapy crawl stocks
# Or to output to CSV:
scrapy crawl stocks -o <filename>.csv -t csv
# Or to output to JSONLines:
scrapy crawl stocks -o <filename>.jl
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Data
I have already created a Google Sheet containing predictions which I occasionally update [here](https://docs.google.com/spreadsheets/d/1XKHIsUxsMl7iTj2jk4liFKqDUAFvQI1jPGfof7xsAWI/edit?usp=sharing)

## License
[MIT](https://choosealicense.com/licenses/mit/)
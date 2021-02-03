import scrapy
import re

from stocks.items import StocksItem
class StockSpider(scrapy.Spider):
    name = "stocks"
    custom_settings = {
        # explicity set the order in which the fields should be exported.
        # this can be changed or commented out 
        'FEED_EXPORT_FIELDS': ['symbol', 'analysts', 'median', 'high', 'low', 'increase', 'last_price'] 
    }
    def start_requests(self):
        # obtain our list of stock tickers
        url = 'https://stockanalysis.com/stocks/'
        return [scrapy.Request(url, callback=self.iterate_stocks)]

    def iterate_stocks(self, response):
        # get all the company names with ticker information
        names = response.xpath('//h2[text()="All stock ticker symbols:"]/following-sibling::ul/li/a/text()').getall()
        for name in names:
            # everything until the first space is the ticker
            ticker = re.search('^\S+', name).group(0)
            # CNN does not include dots or dashes in the query
            ticker = re.sub('\W', '', ticker)
            # get prediction from CNN
            url = f'https://money.cnn.com/quote/forecast/forecast.html?symb={ticker}'
            yield scrapy.Request(url, callback=self.parse_item, meta={'symbol': ticker})
    
    def parse_item(self, response):
        # get the text on the page where the prediction should be
        prediction_text = ''.join(
            response.xpath('//h3[text()="Stock Price Forecast"]/following-sibling::div[1]/p//text()').getall()
        )
        try:
            analysts = int(re.search(r'The (\d{0,3}(,\d{3})*) analysts', prediction_text).group(1).replace(',',''))
        except:
            # if obtaining the number of analysts fails then no prediction is available for this ticker
            print(f'Could not obtain prediction for {response.meta["symbol"]}')
            return
        
        median = float(re.search(r'median target of (\d{0,3}(,\d{3})*\.\d{2})', prediction_text).group(1).replace(',',''))
        high = float(re.search(r'high estimate of (\d{0,3}(,\d{3})*\.\d{2})', prediction_text).group(1).replace(',',''))
        low = float(re.search(r'low estimate of (\d{0,3}(,\d{3})*\.\d{2})', prediction_text).group(1).replace(',',''))
        increase = float(re.search(r'([-+]?(\d{0,3}(,\d{3})*(\.\d+)?))% (decrease|increase) from the last price of', 
            prediction_text).group(1).replace(',',''))
        last_price = float(re.search(r'last price of (\d{0,3}(,\d{3})*\.\d{2})', prediction_text).group(1).replace(',',''))
        
        prediction = StocksItem()
        prediction['symbol'] = response.meta['symbol']
        prediction['analysts'] = analysts
        prediction['median'] = median
        prediction['high'] = high
        prediction['low'] = low
        prediction['increase'] = increase
        prediction['last_price'] = last_price

        yield prediction


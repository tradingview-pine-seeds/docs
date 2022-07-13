[data_formats]: data.md#data-formats
[data_limits]: data.md#updating-the-data
[ui_symbol_search]: ui.md#symbol-search
[env_var]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[rest_api]: https://www.tradingview.com/brokerage-integration/

# FAQ

## Data requirements

#### Q: In what form should the data be stored?

__A:__ Use plain-text files to store your data.
Store the price data itself is in CSV files in the `data/repo_name` directory. Create a separate file for each symbol. 
The additional symbol information should be stored in a JSON file in the `symbol_info` directory. Describe all of the symbol settings in one file.

#### Q: How to set up access to the data source and not store access keys in code?

__A:__ Use [environment variables][env_var] in your code.
Go to the repository settings. Open the _Secrets_ section. Create a variable with a token or password in it, then use that variable in your code.

#### Q: Can only trading data be integrated?

__A:__ The TradingView platform is a handy tool for dealing with [trading data][data_formats]. 
Such data always has a difference between price values. 
But if your data series has a single value per day, use `open` = `close` = `high` = `low`, and `volume` = 0.
It is suitable for economic indicators.

```js
20210101T,0.1,0.1,0.1,0.1,0
```

#### Q: What is EOD data? How does it differ from intraday data?

__A:__ EOD (End-of-Day) data is the values received at the end of the trading session of a given day. 
Regardless of the number of changes within the day (intraday), you will see only the last saved value on the chart.

#### Q: How quickly can I check the result after updating the data?

__A:__ Your EOD data is checked and uploaded to our storage several times a day. 
On the chart you will see the values for the previous day and earlier.
If the data needs to be updated more frequently, you can connect the integration via [REST API][rest_api], but this option is only available for the brokerage integration.

#### Q: How often do I update data from the source?

__A:__ TradingView allows you to watch and analyse the data for any period. 
If data is not updated, it is no longer useful.
If your files have not been updated for three months, the source will be disabled.

#### Q: What are the limits on the amount of data?

__A:__ EOD data has a [limit][data_limits] of 1000 symbols per repository. 
If you have more than 1000 CSV data files, you can create another data repository.

## TradingView UI

#### Q: Why can't I find my symbols in symbol search box?

__A:__ EOD symbols do not show up in the symbol search suggestion field, but you can still open them.
Enter the full symbol name (`prefix:symbol_name`) then press _Enter_, and the chart will switch to the requested symbol.

#### Q: Would a candlestick chart be informative?

__A:__ For economic data, which commonly only has a single data source, a _Line_ graph is suitable, as it only shows `close` values. The data that has different OHLC values will be better represented with the _Candles_ chart, which displays each four of these values separately.

#### Q: Who can use my symbols in the UI?

__A:__ An EOD data symbol can only be accessed by [knowing its full name][ui_symbol_search].
Therefore, if your repository is public, anyone can check its full name and open the symbol on the chart. If it’s private, only those who know the full name will be able to access the data.

## GitHub settings

#### Q: How to catch errors?

__A:__ Your GitHub repository has a __Check data and create pr__ action set up. 
Validation warnings and errors can be found in its log.

#### Q: Why host data in public repositories?

__A:__ We love open source code and our tools help a lot of people because of it, but if you want to connect private data - that's completely fine as well.

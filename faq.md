[data_formats]: data.md#data-formats
[data_limits]: data.md#updating-the-data
[ui_symbol_search]: ui.md#symbol-search
[env_var]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[rest_api]: https://www.tradingview.com/brokerage-integration/

# FAQ

## Data requirements

#### Q: In what form should the data be stored?

__A:__ Use palin-text files to store data.
The price data itself is in CSV files in the `data/repo_name` directory. Create a separate file for each symbol. 
The additional symbol information is in a JSON file in the `symbol_info` directory. Describe the settings of all symbols in one file.

#### Q: How to set up access to the data source and not store access keys in code?

__A:__ Use [envinonment varialbe][env_var].
Go to the repository settings. Open _Secrets_ section. Create a variable with a token or password in it. Then use that variable in public code.

#### Q: Can only trading data be integrated?

__A:__ The TradingView platform is a handy tool for dealing with [trading data][data_formats]. 
Such data always has a difference between price values. 
But if your data series has a single value per day, use `open` = `close` = `high` = `low`, and `volume` = 0.
It is suitable for economic indicators.

```js
20210101T,0.1,0.1,0.1,0.1,0
```

#### Q: What is EOD data? How does it differ from intraday data?

__A:__ EOD data is the values received at the end of the trading session of a given day. 
Regardless of the number of changes within the day (intraday), you will see only the last saved value on the Chart.

#### Q: How quickly can I check the result after updating the data?

__A:__ Your EOD data is checked and uploaded to our storage several times a day. 
On the Chart you will see the values for the previous day and earlier.
If the data needs to be updated more frequently, you can connect the integration via [REST API][rest_api].

#### Q: How often do I update data from the source?

__A:__ TradingView allows you to watch and analyse the data for any period. 
If data is not updated, it is no longer useful.
If your files are not updated within three months, the source will be disabled.

#### Q: What are the limits on the amount of data?

__A:__ EOD data has a [limit][data_limits] of 1000 symbols per repository. 
If you have more than 1000 CSV data files, you can create another data repository.

## TradingView UI

#### Q: Why can't I find my symbols in symbol search box?

__A:__ EOD symbols entering in Symbol Search box do not show up in the tooltip.
Enter the full symbol name (`prefix:symbol_name`) then press _Enter_. The symbol graph will appears in the chart's main area.

#### Q: Would a candlestick chart be informative?

__A:__ A _Heiken Ashi_ graph is useful for visualizing trading data. Growth is green, fall is red.
The difference between `high` and `low` prices is immediately visible. For economic data, a _Line_ graph is more suitable.

#### Q: Who can use my symbols in the UI?

__A:__ An EOD data symbol can only be accessed by [knowing the full name][ui_symbol_search].
Therefore, if your repository is public, it is possible to find out the symbol name. If it's private, no.

## GitHub settings

#### Q: How to catch errors?

__A:__ Your GitHub repository has a __Check data and create pr__ action set up. 
Validation warnings and errors are written to its log.

#### Q: Why host data in public repositories?

__A:__ We like open source. Our tools help a lot of people because of it. But if you want to connect private data - that's completely fine.

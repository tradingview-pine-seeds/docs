[data_formats]: data.md#data-formats
[env_var]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[rest_api]: https://www.tradingview.com/brokerage-integration/

# FAQ

## Data requirements

__Q:__ __In what form should the data be stored?__

__A:__ Use palin-text files to store data.
The price data itself is in CSV files in the `data/reponame` directory. Create a separate file for each symbol. 
The additional symbol information is in a JSON file in the `symbol_info` directory. Describe the settings of all symbols in one file.

__Q:__ __How to set up access to the data source and not store access keys in code?__

__A:__ Use [envinonment varialbe][env_var].
Go to the repository settings. Open _Secrets_ section. Create a variable with a token or password in it. Then use that variable in public code.

__Q:__ __Can only trading data be integrated?__

__A:__ The TradingView platform is a handy tool for dealing with [trading data](data.md#data-formats). 
Such data always has a difference between price values. 
But if your data series has a single value per day, use `open` = `close` = `high` = `low`, and `volume` = 0.
It is suitable for economic indicators.

```js
20210101T,0.1,0.1,0.1,0.1,0
```

__Q:__ __How quickly can I check the result after updating the data?__

__A:__ Your EOD data is checked and uploaded to our storage several times a day. 
On the Chart you will see the values for the previous day and earlier.
If the data needs to be updated more frequently, you can connect the integration via [REST API][rest_api].

__Q:__ __How often do I update data from the source?__

__A:__ TradingView allows you to watch and analyse the data for any period. 
If data is not updated, it is no longer useful.
If your files are not updated within three months, the source will be disabled.

__Q:__ __Why host data in public repositories?__

__A:__ We like open source. Our tools help a lot of people because of it. But if you want to connect private data - that's completely fine.

## TradingView UI

__Q:__ __Why can't I find my symbols in symbol search box?__

__A:__ EOD symbols entering in symbol search box do not show up in the tooltip.
Enter the full symbol name (`prefix:symbol_name`) then press _Enter_ - the symbol graph will appears in the chart's main area.

__Q:__ __What is a one-point bar?__

__A:__ A one-point bar is what we call a graph with the following data: `open = close = high = low`, and `volume=0`

__Q:__ __Would a candlestick chart be informative?__

__A:__ Much more informative. Pay attention to the _Heikin Anshi_ candles. 
The rise is green, the fall is red. The difference between `high` and `low` is immediately noticable.

__Q:__ __How to see `open`, `close`, `high`, `low` volues on chart? And `volume`?__

__A:__ You can turn them on/off in the symbol context menu (in the top left corner of chart area).

## GitHub settings

__Q:__ __What is in the repository? What are the scripts and files?__

__A:__ See github section in the _Guide_.


__Q:__ __What about the 2nd repository?__

__A:__ Pull request should contain changes only in the data files.
The additional repository will allow you to add and set up scripts for automatic downloading, checking and formatting of data.

__Q:__ __How do I upload data from private storage?__

__A:__ It's not possible in a main repository.
You can create additional repository, configure access via environments variable, and create scripts for the data upload.

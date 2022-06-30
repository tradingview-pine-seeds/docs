[data_formats]: data.md#data-formats
[data_limits]: data.md#updating-the-data
[ui_symbol_search]: ui.md#symbol-search
[env_var]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[rest_api]: https://www.tradingview.com/brokerage-integration/

# FAQ

## Data requirements

__Q:__ __In what form should the data be stored?__

__A:__ Use palin-text files to store data.
The price data itself is in CSV files in the `data/repo_name` directory. Create a separate file for each symbol. 
The additional symbol information is in a JSON file in the `symbol_info` directory. Describe the settings of all symbols in one file.

__Q:__ __How to set up access to the data source and not store access keys in code?__

__A:__ Use [envinonment varialbe][env_var].
Go to the repository settings. Open _Secrets_ section. Create a variable with a token or password in it. Then use that variable in public code.

__Q:__ __Can only trading data be integrated?__

__A:__ The TradingView platform is a handy tool for dealing with [trading data][data_formats]. 
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

__Q:__ __What are the limits on the amount of data?__

__A:__ EOD data has a [limit][data_limits] of 1000 symbols per repository. 
If you have more than 1000 CSV data files, you can create another data repository.

## TradingView UI

__Q:__ __Why can't I find my symbols in symbol search box?__

__A:__ EOD symbols entering in Symbol Search box do not show up in the tooltip.
Enter the full symbol name (`prefix:symbol_name`) then press _Enter_. The symbol graph will appears in the chart's main area.

__Q:__ __Would a candlestick chart be informative?__

__A:__ A _Heiken Ashi_ graph is useful for visualizing trading data. Growth is green, fall is red.
The difference between `high` and `low` prices is immediately visible. For economic data, a _Line_ graph is more suitable.

__Q:__ __Who can use my symbols in the UI?__

__A:__ An EOD data symbol can only be accessed by [knowing the full name][ui_symbol_search].
Therefore, if your repository is public, it is possible to find out the symbol name. If it's private, no.

## GitHub settings

__Q:__ __How to catch errors?__

__A:__ Your GitHub repository has a __Check data and create pr__ action set up. 
Validation warnings and errors are written to its log.

__Q:__ __Why host data in public repositories?__

__A:__ We like open source. Our tools help a lot of people because of it. But if you want to connect private data - that's completely fine.

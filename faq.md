# FAQ

## Data requirements

#### Q: In what format should the data be stored?

__A:__ Use plain-text files to store your data:

- Store the price data in CSV files in the `data/` directory. Create a separate file for each symbol.
- Store additional symbol information in a JSON file in the `symbol_info/` directory. Describe all symbol settings in one file.

See the [Data structure](data.md) article for more information.

#### Q: What if I store data in a file with a different extension (not CSV)?

__A:__ In this case, you will not see the data on the chart.
Change the file extension to CSV and create a new pull request.

#### Q: Can only trading data be integrated?

__A:__ The TradingView platform is a handy tool for dealing with [trading data][data_format].
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

__A:__ TradingView allows you to watch and analyze the data for any period.
If data is not updated, it is no longer useful.
If your files have not been updated for three months, the source will be disabled.

#### Q: What are the limits on the amount of data?

__A:__ EOD data has a [limit][data_format] of 1,000 symbols per repository.
You can create another data repository if you have more than 1,000 CSV data files.

## TradingView UI

#### Q: Why can't I find my symbols in the symbol search box?

__A:__ EOD symbols do not show up in the symbol search suggestion field, but you can still open them.
Enter the full symbol name (`prefix:symbol_name`) and press _Enter_.
The chart will switch to the requested symbol.

#### Q: I added the symbol data first and then the symbol descriptions. All actions were finished successfully, but the chart does not display the data. What should I do?

__A:__ When adding symbols, you first need to add their descriptions in `symbol_info/`,
then ensure that actions run successfully and `No data here` appears on the chart.
If you added the symbol data before these steps, delete data from the CSV file and commit the changes.
Then check that `No data here` appeared on the chart and add the symbol data again.
For more information, refer to the [How to add symbols to the chart and remove them][tutorial] tutorial.

> __Note__
>
> The steps above only work for the symbols that have just been added.
> For those symbols whose data is already shown on the chart,
you can change the CSV files without waiting for `No data here` to appear on the chart.
Your data will be updated.

#### Q: What if the maximum amount of time required for the symbol to appear on the chart has passed, but I still do not see it?

__A:__ The maximum time for a symbol to appear on the chart is one hour.
If it has not appear during this time, check that the JSON file in the `symbol_info/` directory has a valid format.
Refer to [Symbol info format] for more information.

#### Q: Would a candlestick chart be informative?

__A:__ For economic data, which commonly only has a single data source, a _Line_ graph is suitable, as it only shows `close` values. The data that has different OHLC values will be better represented with the _Candles_ chart, which displays each four of these values separately.

#### Q: Who can use my symbols in the UI?

__A:__ Anyone who knows the full symbol names can access your symbols' EOD data from the [_Symbol Search_][ui_symbol_search].

## GitHub

#### Q: What if I made more than 5 pull requests in a day?

__A:__ Only 5 pull requests (PR) per day can be merged from your personal repository into the main one.
If you create more than 5 PRs, the __Upload data__ action will not run until the next day.
You will be able to rerun the action 24 hours after the first PR made the day before.

To rerun the action:

1. Go to _Actions_ in your repository.
2. Open the last run action.
3. Click _Re-run all jobs_.

#### Q: How to catch errors?

__A:__ Your GitHub repository has a __Check data__ action set-up.
Validation warnings and errors can be found in its logs.

#### Q: What if the Check data action in my repository failed after adding a symbol description?

__A:__ Check that the JSON file in the `symbol_info/` directory has a valid format.
Refer to [Symbol info format] for more information.

#### Q: What if the Check data action in my repository has failed after adding the symbol data?

A: Check that CSV files in the `data/` directory have valid formats.
Refer to [Data format][data_format] for more information.

#### Q: What if the Upload data action in the main repository failed?

__A:__  Check that you have not exceeded the [daily number of pull requests].
If not, contact us at pine.seeds@tradingview.com.

#### Q: What if my pull request was not merged automatically?

__A:__ Check the action logs for validation warnings and errors.
If you cannot fix the problem, contact us at pine.seeds@tradingview.com.

[data_format]: data.md#data-format
[daily number of pull requests]: #q-what-if-i-make-more-than-5-pull-request-during-the-day
[rest_api]: https://www.tradingview.com/brokerage-integration/
[Symbol info format]: data.md#symbol-info-format
[tutorial]: data_tutorial.md
[ui_symbol_search]: ui.md#symbol-search

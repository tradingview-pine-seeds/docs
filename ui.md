[ui_chart_candles]: /images/ui_chart_candles.png
[ui_chart_line]: /images/ui_chart_line.png
[ui_search]: /images/ui_search_empty.png
[ui_pine]: /images/ui_pine.png
[ui_pine_btc]: /images/ui_chart_pine_sma_btc.png
[request_seed]: https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}seed
[support_ohlc]: https://www.tradingview.com/support/solutions/43000619436-heikin-ashi/

# TradingView UI

The TradingView platform is your frontend. There are several tools for working with your data.

__[Symbol search](#symbol-search)__

This is a box where you can search for a symbol. Enter its full name, press _Enter_ and you will see it on the chart.

__[Chart](#chart)__

The chart is the main data visualization tool.
There are different types of charts, a lot of additional indicators, viewing historical data, data for any period.

__[Pine editor](#pine-editor)__

An editor for the Pine Script™ scripting language. The data can be accessed with a couple of lines of code.
A flexible and convenient tool for displaying data on the chart.

## Symbol Search

_Symbol Search_ is the entry point to access symbol data on the TradingView chart.
To switch between symbols, type a symbol name in the _Symbol Search_ box and press <kbd>Enter</kbd>.

Note that symbols will not appear in the _Symbol Search_ suggestion field.
Hence, you need to know the full symbol name to open it on the chart.

The symbol name on the TradingView chart is uniquely determined by the GitHub parameters:

- The required `SEED` prefix.
- The GitHub account name.
- The suffix of the GitHub repository name.
- A symbol name that matches the name of the data file.

|![Symbol Search][ui_search]|
|-|

For example, the full name of the `SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` symbol is obtained as follows:

- `SEED` — the required prefix.
- `CRYPTO` — the account name `github.com/crypto`.
- `SANTIMENT` — the suffix of the repository name `github.com/crypto/seed_crypto_santiment`.
- `BTC_DEV_ACTIVITY` — the symbol name that matches the name of the `BTC_DEV_ACTIVITY.CSV` data file.

## Chart

Use the chart area to work with graphs. After you add a symbol via symbol search or Pine Script™, it will appear on the chart.

If your data series is one value per day, your data will look something like this.

```csv
20210101T,0.1,0.1,0.1,0.1,0
```

For single-layer data (`open` = `high` = `low` = `close`), the _Line_ chart type fits best. It displays `close` values as dots connected by lines.

|![ui_chart_line]|
|-|

If your feed is trading data, valid [OHLCV][support_ohlc] (open-high-low-close-volume) data series should come in each line.
In this case the _Candles_ chart type will be more useful, as it displays all four values separately.

|![ui_chart_candles]|
|-|

## Pine Editor

[Pine Script™] is another tool for working with your custom data on TradingView.
It allows you to write your own indicators for a symbol to make data easier to analyze.
For example, you can request custom data with the [`request.seed()`][request_seed] built-in function:

```js
request.seed(source, symbol, expression, gaps)
```

When you call the function, the first two parameters define the data source:

- `source` — a group of symbols whose name matches the GitHub repository name.
- `symbol` — a name of the symbol in the group that corresponds to a specific data file.

Note that these parameters uniquely determine the requested series so they can't be empty strings.

The `expression` parameter specifies what data series you request from the specified symbol,
and the optional `gaps` argument controls whether the gaps between data values should be filled.

For example, the `SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` close values can be requested in Pine Script™ as:

```js
//@version=5
indicator("BTC Dev Activity", format=format.volume)
//request.seed(source, symbol, expression)
activity = request.seed("seed_crypto_santiment", "BTC_DEV_ACTIVITY", close)
plot(activity)
```

![ui_pine]

The custom data contains 5 values in each data row.

- `open` — price of the first tick of the day
- `close` — price of the last tick of the day
- `high` — the highest value of the tick price
- `low` — the lowest value of the tick price
- `volume` — buy/sell volume per day

The `expression` parameter specifies the data set that is requested from the symbol. 
It can be either a built-in series variable like `close`, or a custom variable or expression, 
like `ta.sma(close, 10)`, or even a tuple of several different values (enclosed in square brackets and separated by commas):

```js
//@version=5
indicator("BTC Dev Activity", format=format.volume)
//request.seed(source, symbol, expression)
[activity, activitySMA] = request.seed("seed_crypto_santiment", "BTC_DEV_ACTIVITY", [close, ta.sma(close, 10)])
plot(activity, "BTC Dev Activity")
plot(activitySMA, "BTC Dev Activity, SMA10", color=color.green)
```

Once this indicator is added to the chart, it displays the daily Bitcoin developer activity data 
from the EOD source on your chart and its 10-day average without changing the symbol open on the chart itself.

|![ui_pine_btc]|
|-|

[Pine Script™]: https://www.tradingview.com/pine-script-docs/en/v5/index.html

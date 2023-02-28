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

## Symbol search

Symbol search is the first entry point to access the data on the TradingView chart.

The symbol name on the TradingView chart is uniquely determined by the Github parameters:

- `SEED` is a mandatory prefix for data of this type
- the name of the data source (we use the GitHub account name)
- the group of data within the source (we use the GitHub repository name)
- the name of the symbol (we use the name of the data file)

|![Symbol Search][ui_search]|
|-|

For example, the full name of the `SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` symbol is obtained as follows:

- `SEED` — prefix
- `CRYPTO` — `github.com/crypto` account name
- `SANTIMENT` — `github.com/crypto/santiment` repository name
- `BTC_DEV_ACTIVITY` — the name of the `BTC_DEV_ACTIVITY.CSV` data file

> __Note__
>
> EOD symbols will not appear in the symbol search suggestion field. 
> Type the full symbol name and press _Enter_ in order for it to appear on the chart.

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

Pine Script™ is one more tool for working with your custom data on TradingView. 
Unlike the symbol search, which changes the main symbol on the chart, indicators written in Pine Script™ are an addition to the currently open symbol.

You can request custom data with the [`request.seed()`][request_seed] built-in function:

```js
request.seed(source, group, symbol, expression, gaps)
```

When you call the function, the first three parameters define the data source:

- `source` — the source name, the same as the GitHub username
- `group` — a group of symbols, coincides with the GitHub repository name
- `symbol` — the name of the symbol in the group that corresponds to a specific data file

These parameters uniquely determine the requested series so they can't be empty strings.

The `expression` parameter specifies what data series you request from the specified symbol, 
and the optional `gaps` argument controls whether the gaps between data values should be filled.

|![ui_pine]|
|-|

For example, the `SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` series data can be requested in Pine Script™ as

```js
//@version=5
indicator("BTC Dev Activity", format=format.volume)
//request.seed(source, group, symbol, expression[, gaps])
activity = request.seed("crypto", "santiment", "BTC_DEV_ACTIVITY", close)
plot(activity)
```

The source contains 6 values in each data row.

```csv
20210101T,0.1,0.1,0.1,0.1,0
```

- `date` — data capture day
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
//request.seed(source, group, symbol, expression)
[activity, activitySMA] = request.seed("crypto", "santiment", "BTC_DEV_ACTIVITY", [close, ta.sma(close, 10)])
plot(activity, "BTC Dev Activity")
plot(activitySMA, "BTC Dev Activity, SMA10", color=color.green)
```

Once this indicator is added to the chart, it displays the daily Bitcoin developer activity data 
from the EOD source on your chart and its 10-day average without changing the symbol open on the chart itself.

|![ui_pine_btc]|
|-|

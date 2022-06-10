[ui_chart_heikin]: /images/ui_chart_heikin.png
[ui_chart_line]: /images/ui_chart_line.png
[ui_details]: /images/ui_details.png
[ui_search]: /images/ui_search_empty.png
[ui_pine]: /images/ui_pine.png
[pine_btc]: /images/guide_chart_pine_btc.png
[request_seed]: https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}seed
[support_ohlc]: https://www.tradingview.com/support/solutions/43000619436-heikin-ashi/

# TradingView UI

TradingView platform is your frontend. There are several tools for working with your data.

__[Symbol Search](#symbol-search)__

This is a box for searching for a symbol. Enter its full name, press _Enter_ and you will see it on the Chart.

__[Chart](#chart)__

Chart is the main data visualization tool.
There are different types of charts, a lot of additional indicators, viewing historical data, data for any period.

__[Details](#details)__

A block with additional information about the symbol: its name, data source, current value, change per day.

__[Pine Editor](#pine-editor)__

Built-in language editor. A couple of lines of code are enough to access the data.
Flexible and convenient tool for displaying data on the Chart.

## Symbol Search

It is the first entry point to access the data on the TradingView Chart.

The symbol name on the TradingView chart is uniquely determined by the Github parameters:

- `SEED` is a mandatory prefix for data of this type
- the name of the data source (we use GitHub account name)
- the group of data within the source (we use GitHub repository name)
- the name of the symbol (we use the name of the data file)

|![Symbol Search][ui_search]|
|-|

For example, the full name of the `SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` symbol is obtained as follows:

- `SEED` prefix
- `CRYPTO` — github.com/crypto user name
- `SANTIMENT` — github.com/crypto/santiment repository name
- `BTC_DEV_ACTIVITY` — the name of the `BTC_DEV_ACTIVITY.CSV` data file

> __Note__
>
> Enter this name in the Symbol Search box, you can upload it to the Chart. But it won't appear in the tooltip as you type.

## Chart

Use the Chart area to work with graphs. After you add a symbol via Symbol Search or Pine Script, its graph will appear on the Chart.

If your data series is one value per day, your data will look something like this.

```csv
20210101T,0.1,0.1,0.1,0.1,0
```

For single-layer data (`open` = `high` = `low` = `close`), the _Line_ type graph is clearer.

|![ui_chart_line]|
|-|

If your feed is trading data, a valid [OHLCV][support_ohlc] data series should come in each line.
In this case the _Heikin Ashi_ graph will be more useful.

|![ui_chart_heikin]|
|-|

## Details

Summary information about the symbol is posted on this panel. Here are symbol name and it's group, current price, price increment/decrease.

|![ui_details]|
|-|

## Pine Editor

This is one more tool for working with your series data on the TradingView plafrorm.

To get private data in the indicator code, a special [request.seed()][request_seed] function has been added to Pine

```js
request.seed(source, group, symbol)
```

When calling the function, set the parameters that define the data source:

- `source` — the source name, the same as GitHub account name
- `group` — a group of symbols, coincides with GitHub repository name
- `symbol` — the name of the symbol in the group, corresponds to a specific data file

These parameters uniquely determine the requested series. They cannot be empty strings.

|![ui_pine]|
|-|

`SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` series data can be requested in as

```js
//request.seed(source, group, symbol)
//@version=5
indicator("My script")
s = request.seed("crypto", "santiment", "BTC_DEV_ACTIVITY")
plot(s)
```

The source send 6 values in each data set.

```csv
20210101T,0.1,0.1,0.1,0.1,0
```

- `date` — data capture day
- `open` — price of the first tick of the day
- `close` — price of the last tick of the day
- `high` — the highest value of the tick price
- `low` — the lowest value of the tick price
- `volume` — buy/sell volume per day

Add Bitcoin developer activity data from the EOD source to the BTC USD chart. So you will receive information for technical analysis.

|![pine_btc]|
|-|

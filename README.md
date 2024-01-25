# Pine Seeds documentation

> [!WARNING]
> The creation of new repositories has been suspended. We will continue to support the existing repositories. If you have questions or need assistance with your current repositories, contact us at
> pine.seeds@tradingview.com.

## Overview

__Pine Seeds__ is a service to import your custom data and access it via [TradingView](https://tradingview.com).

This service allows you to:

- connect your series data to TradingView
- open it on the TradingView chart
- use it in the custom indicators

Use [TradingView](https://tradingview.com) as your __frontend__ and use a GitHub repository as your __backend__.

Keep in mind that such data (we call them EOD data, short for End-of-Day) has certain limitations:

- the data can only be updated 5 times per day
- only daily-based timeframes (1D and above) can be applied to such data
- the number of data elements (symbols) is [limited][data_limits] to 6000
- such data [will not appear][ui_symbol_search] in the symbol search box

Setting up the service includes several steps:

1. Setting up a [repository][repo].
2. [Data preparation][data].
3. Manipulating data in the [TradingView UI][ui].

## Example

You can take the [seed_crypto_santiment] project as a reference for your repository.
The project has the proper structure for symbol data.

You can also open symbols from [seed_crypto_santiment] on the [TradingView chart][chart] and work with it.
For example, `SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` is an example of custom data integration.
The symbol name is uniquely determined by the GitHub settings.

- `SEED` is a required prefix.
- `CRYPTO` is the account name `github.com/crypto`.
- `SANTIMENT` is the suffix of the GitHib repository name `github.com/crypto/seed_crypto_santiment`.
    The suffix is needed so that you can use several repositories for different data groups,
    e.g., `seed_<username>_<suffix1>`, `seed_<username>_<suffix2>`.
- `BTC_DEV_ACTIVITY` is the `BTC_DEV_ACTIVITY.CSV` data file name.

Using the built-in [`request.seed()`][pine_refs] function from the [Pine Script™ language][pine_docs] and the available data, you can build a chart.

```js
//@version=5
indicator("BTC Dev Activity", format=format.volume)
//request.seed(source, symbol, expression)
activity = request.seed("seed_crypto_santiment", "BTC_DEV_ACTIVITY", close)
plot(activity, "BTC Dev Activity")
```

By adding Bitcoin developer activity data from the EOD source (`SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY`) to the `BTCUSD` chart,
you will receive additional information for technical analysis.

|![ui_chart_pine]|
|-|

## Read more

__[Data structure][data]__

Data storage form, data structure, field descriptions, field types, and data validation conditions.

__[GitHub settings][repo]__

Account and repository settings, GitHub actions workflow, repositories organization, external data connection.

__[TradingView UI][ui]__

Quick guide to requesting custom data series on TradingView charts.

__[FAQ][faq]__

If you have any questions that haven't been covered by info in the sections above, take a look here.

__[Example script for automating data history uploads][update_script]__

Check the script example that automates data history uploads to a forked repository.

[chart]: https://www.tradingview.com/chart
[data]: /data.md
[data_limits]: /faq.md#q-what-are-the-limits-on-the-amount-of-data
[faq]: /faq.md
[pine_docs]: https://www.tradingview.com/pine-script-docs/en/v5/index.html
[pine_refs]: https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}seed
[repo]: /repo.md
[seed_crypto_santiment]: https://github.com/tradingview-pine-seeds/seed_crypto_santiment
[ui]: /ui.md
[ui_chart_pine]: /images/ui_chart_pine_btc.png
[ui_symbol_search]: /ui.md#symbol-search
[update_script]: /update_example/update_example.md

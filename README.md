[faq]: /faq.md
[data]: /data.md
[repo]: /repo.md 
[ui]: /ui.md
[ui_chart_pine]: /images/ui_chart_pine_btc.png
[github_user]: https://github.com/crypto
[github_repo]: https://github.com/crypto/santiment
[pine_docs]: https://www.tradingview.com/pine-script-docs/en/v5/index.html
[pine_refs]: https://www.tradingview.com/pine-script-reference/v5/#fun_request{dot}seed
[solution_eod]: https://www.tradingview.com/support/solutions/43000474958-i-see-only-eod-data-for-dxy-symbol-and-no-real-time/

# Pine Seeds documentation

## Overview

__Pine Seeds__ is a service for working with your data on the [TradingView](https://tradingview.com) platform.

This service allows you:

- connect your series data to TradingView
- visualize it in the TradingView UI
- use it to create indicators

Use [TradingView](https://tradingview.com) as your __frontend__ and use GitHub repository as your __backend__. 

Keep in mind that such data has limitations (we call them [EOD][solution_eod] data):

- the data can only be updated a few times a day
- only the daily resolution is available
- the number of data elements (symbols) is limited
- such data cannot be found with Symbol Search box

> __Note__
> 
> Read [5-minute tutorial](tutorial.md) to start right now

Setting up the service include of several steps.

1. [data preparation][data]
1. setting up [repository][repo]
1. manipulating data in the [TradingView UI][ui]

A detailed description of the service can be found in the other sections.

__[Data structure][data]__

Data storage form, data structure, fields descriptions, fields types, data validation conditions.

__[GitHub settings][repo]__

Account and repository settings, GitHub actions workflow, repositories organisation, external data connection.

__[TradingView UI][ui]__

Quick guide for TradingView user using custom data series.

__[FAQ][faq]__

If you haven't found something in the main sections, take a look here.

## Example

You just need to set up the repository, upload your data to it and wait for it to be uploaded to the TradingView storage.

`SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` is an example of custom data integration. You can work with on the Chart.

Symbol name is uniquely determined by Github settings.

- `SEED` is a mandatory prefix for this type of data
- `CRYPTO` is the name of [github.com/crypto][github_user] GitHub user
- `SANTIMENT` is the name of [github.com/crypto/santiment][github_repo] repository
- `BTC_DEV_ACTIVITY` is a data filename _BTC_DEV_ACTIVITY.CSV_

Now, using the [request.see()][pine_refs] function from the built-in [Pine Script language][pine_docs] and the available data, you can build a graph.

```js
//request.seed(source, reponame, symbol, expression)
//@version=5
indicator("My script")
s = request.seed("crypto", "santiment", "BTC_DEV_ACTIVITY", close)
plot(s)
```

By adding Bitcoin developer activity data from the EOD source (_SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY_) to the _BTCUSD_ chart, you will receive information for technical analysis.

|![ui_chart_pine]|
|-|

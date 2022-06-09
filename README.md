[faq]: /faq.md
[guide_data]: /guide/data.md
[guide_repo]: /guide/repo.md 
[guide_ui]: /guide/ui.md
[ui_chart]: /images/ui_chart.png
[ui_details]: /images/ui_details.png
[ui_search]: /images/ui_search.png
[ui_pine]: /images/ui_pine.png
[github_user]: https://github.com/crypto
[github_repo]: https://github.com/crypto/santiment
[tv_chart]: https://tradingview.com/chart
[pine_script_docs]: https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html
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

1. [data preparation][guide_data]
1. setting up [repository][guide_repo]
1. manipulating data in the [TradingView UI][guide_ui]

A detailed description of the service can be found in the other sections.

### [Data structure][guide_data]

Data storage form, data structure, fields descriptions, fields types, data validation conditions.

### [GitHub settings][guide_repo]

Account and repository settings, GitHub actions workflow, repositories organization, external data connection.

### [TradingView UI][guide_ui]

Quick guide for TradingView user using custom data series.

### [FAQ][faq]

If you haven't found something in the main sections, take a look here.

## Example

You just need to set up the repository, upload your data to it and wait for it to be uploaded to the TradingView storage.

`SEED_CRYPTO_SANTIMENT:BTC_DEV_ACTIVITY` is an example of custom data integration. You can work with on the [Chart][tv_chart].

Symbol name is uniquely determined by Github settings.

- `SEED` is a mandatory prefix for this type of data
- `CRYPTO` is the name of [github.com/crypto][github_user] GitHub user
- `SANTIMENT` is the name of [github.com/crypto/santiment][github_repo] repository
- `BTC_DEV_ACTIVITY` is a data filename `BTC_DEV_ACTIVITY.CSV`

Now, by adding Bitcoin developer activity data from the EOD source to the BTCUSD chart, you will receive information for technical analysis.


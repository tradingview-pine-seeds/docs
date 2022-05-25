# EOF feed documentation

## Overview

This servis allows you to use [TradingView](https://tradingview.com) platform to visualize your data.
We called it _End-of-day feed_ beacuse use single set of value for each day.

Service is so simple:

* Use [TradingView](https://tradingview.com) platform as your __frontend__
* Use [GitHub](https://github.com) repository as your __backend__
* Connect you __data storage__ if you need it

> __Note__
> 
> Read [5-minute tutorial](tutorial.md) or check out the [Frequently asked questions section](/faq.md)

## TradingView UI

There are several tools for working with your data here.

### Chart

This is the main data visualization tool. There are 12 types of charts, a lot of additional indicators, viewing historical data for any period.

![Chart](/images/guide_chart.png "Chart")

### Details

Additional information about the symbol: name, source, current value, change per day.

![Details](/images/guide_details.png "Details")

### Symbol Search

A search box for the symbol. Enter the full name (`GROUP:SYMBOLNAME`) to see it on __Chart__.

![Symbol Search](/images/guide_symbol_search.png "Symbol Search")

### Pine Editor

Built-in TradingView [language](https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html). A couple lines of code are enough to access the data. This is a flexible and convenient tool for displaying data on the __Chart__.

![Pine Editor](/images/guide_pine_script.png "Pine Editor")

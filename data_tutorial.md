# Tutorial: how to add and remove symbols to the TradingView chart

This tutorial describes the steps to add symbols to the TradingView chart at once.

> __Note__
>
> There are only 5 pull requests that can be merged into the main repository per day.
> Carefully consider your changes and plan them in advance.

## Add symbol and its data

### Step 1. Add symbol description

1. Add your symbol description to the [JSON file](data.md#symbol_info-format) in the `symbol_info/repo_name.json` directory.
2. In your repository, open *Actions* and check if the `Check data` action finished successfully.
3. In the main repository, open *Actions* and check if the `Upload data` action finished successfully. Go to *Pull requests* and check that the pull request was merged automatically.
4. Open the [TradingView chart][tv-chart] and find your symbol in *Symbol Search*.
    On the chart, you will see `No data here` for your symbol.
    If you see `Invalid symbol`, it means that the symbol has not been uploaded into the TradingView storage yet.

>__Important__
>
> 1. Symbols are uploaded into the TradingView storage every hour on the hour.
> Hence, the maximum time for symbols to appear on the chart is one hour.
>
> 2. Do not [add symbol data](#step-2-add-symbol-data) before `No data here` appears on the chart.
> Otherwise, there may be problems with displaying data on the chart.

### Step 2. Add symbol data

1. Create a [CSV](data.md#data-format) file in the `data/` directory.
2. In your repository, open *Actions* and check if the `Check data` action finished successfully.
3. In the main repository, open *Actions* and check if the `Upload data` action finished successfully. Go to *Pull requests* and check that the pull request was merged automatically.
4. Open your symbol on the chart. Note that it can take a while before data can be displayed.

## Remove symbol and data

If you need to remove a symbol and its data, you should follow the steps below:

1. Remove the information about a symbol from the JSON file in the `symbol_info/repo_name.json` directory
2. Delete a CSV file with symbol data from the `data/` directory.
3. In your repository, open *Actions* and check if the `Check data` action finished successfully.
4. In the main repository, open *Actions* and check if the `Upload data` action finished successfully. Go to *Pull requests* and check that the pull request was merged automatically.

[tv-chart]: https://www.tradingview.com/chart/
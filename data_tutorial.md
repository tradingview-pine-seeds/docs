# Tutorial how to add symbols to the TradingView chart
>__NOTE__
>
> __There are only 5 pull requests that can be accepted per day__
>
> You can add multiple symbols at once by following steps below
## Add symbol description
1. Add description of your symbol in the [JSON file](data.md#symbol_info-format) in `symbol_info` directory.
2. In your repository check if action `Check data and create PR` finished successfully.
3. In the main repository check if action `Upload symbol info` finished succesfully and pull request is merged automatically.
4. Open the [TradingView chart](https://www.tradingview.com/chart/) and find your symbol in `Symbol Search`. It should be displayed `No data here` for your symbol on the chart. If you see `Invalid symbol` it means that symbol has not been uploaded into the TradingView storage yet. 
>__NOTE__
>
> Symbols are uploaded into the TradingView storage every hour at minute 45.
>
>__Do not add data to your symbol before you can see `No data here` on the chart__

***

## Add data
1. Create a [CSV](data.md#data-format) file in the directory `data/repo_name`. 
2. In your repository check if action `Check data and create PR` finished successfully.
3. In the main repository сheck if action `Upload data` finished succesfully and pull request is merged automatically.
4. Open your symbol on chart, it can take a while before data can be presented.
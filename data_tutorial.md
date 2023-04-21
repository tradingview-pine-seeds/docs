# Tutorial: how to add symbols to the chart and remove them

This tutorial describes the steps to add symbols to the TradingView chart at once.

> __Note__
>
> Only 5 pull requests per day can be merged from your personal repository into the main one.
> Carefully consider your changes and plan them in advance.

## Add symbol and its data

> __Note__
>
> If you have any questions or problems that you are unable to handle, please contact us at pine.seeds@tradingview.com.
> Our support team is available on weekdays from 7 AM to 4 PM UTC.

### Step 1. Add symbol description

1. Add your symbol description to the [JSON file](data.md#symbol_info-format) in the `symbol_info/repo_name.json` directory.
2. In your repository, open *Actions* and check if the *Check data* action finished successfully.
3. In the main repository, open *Actions* and check if the *Upload data* action finished successfully.
4. In the main repository, go to *Pull requests* and check that the pull request was merged automatically.
    If it was not merged automatically, check the *Conversation* tab in your pull request for validation warnings or errors.
5. Open the [TradingView chart][tv-chart] and enter your symbol full name in [*Symbol Search*](ui.md#symbol-search).
    On the chart, you will see `No data here` for your symbol.
    If you see `Invalid symbol`, it means that the symbol has not been uploaded into the TradingView storage yet.

>__Important__
>
> 1. Symbols are uploaded into the TradingView storage every 10 minutes.
> Hence, the maximum time for symbols to appear on the chart is 10 minutes.
>
> 2. Do not [add symbol data](#step-2-add-symbol-data) before `No data here` appears on the chart.
> Otherwise, there may be problems with displaying data on the chart.

### Step 2. Add symbol data

1. Create a [CSV](data.md#data-format) file in the `data/` directory.
2. In your repository, open *Actions* and check if the *Check data* action finished successfully.
3. In the main repository, open *Actions* and check if the *Upload data* action finished successfully.
4. In the main repository, go to *Pull requests* and check that the pull request was merged automatically.
    If it was not merged automatically, check the *Conversation* tab in your pull request for validation warnings or errors.
5. Open your symbol on the chart. Note that it can take a while before data can be displayed.

## Remove symbol and data

If you need to remove a symbol and its data, follow the steps below:

1. Delete a CSV file with symbol data from the `data/` directory.
2. In your repository, open *Actions* and check if the *Check data* action finished successfully.
3. In the main repository, open *Actions* and check if the *Upload data* action finished successfully.
4. Remove the information about a symbol from the JSON file in the `symbol_info/repo_name.json` directory.
5. In your repository, open *Actions* and check if the *Check data* action finished successfully.
6. In the main repository, open *Actions* and check if the *Upload data* action finished successfully.
7. In the main repository, go to *Pull requests* and check that the pull request was merged automatically.
    If it was not merged automatically, check the *Conversation* tab in your pull request for validation warnings or errors.

> __Note__
>
> You can remove both a data file from `data/` and a symbol from `symbol_info/repo_name.json` at once.
> To do this, you need to make changes in one [commit] and [push] it to your main branch.
> After that, you will only need to follow the 5−7 steps from the instructions above.

[commit]: https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
[push]: https://github.com/git-guides/git-push
[tv-chart]: https://www.tradingview.com/chart/

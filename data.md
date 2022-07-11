[faq_ohlcv]: /faq.md#q-can-only-trading-data-be-integrated
[iso_4217]: https://en.wikipedia.org/wiki/ISO_4217
[rest_api]: https://www.tradingview.com/brokerage-integration/
[env_var]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[tv_chart]: [https://tradingview.com/chart]
[support_ohlc]: https://www.tradingview.com/support/solutions/43000619436-heikin-ashi/
[url_encode]: https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier

# Data structure

Store your series data in the repository. 
You create a separate CSV file for each symbol, and add a row with data to it every day.
Symbol parameters are described in a separate file and it must be changed accordingly.


## Data requirements

Two directories are provided for the data files in the repository.

- Place a CSV file with daily data for each symbol in the `data/repo_name` directory. These files need to be updated once a day.
- Place one JSON file with the description of the symbol fields in the `symbol_info` directory.

The structure of the CSV file with data is simple, [6 values][faq_ohlcv] (Date,O,H,L,C,V) in each line.

```csv
20210101T,0.1,0.1,0.1,0.1,0
```

## Data formats

All data must be placed as CSV files. One file per symbol. The files must meet the following requirements:

- Fields are separated by commas
- No headers
- No blank lines or spaces
- File names must be [URL encoded][url_encode]

| Field      | Description                   | Sample      |
|------------|-------------------------------|-------------|
| __date__   | Date in YYYYMMDDT format      | `20210101T` |
| __open__   | First tick price              | `0.1`       |
| __high__   | Maximum tick price            | `0.1`       |
| __low__    | Minimum tick price            | `0.1`       |
| __close__  | Last tick price               | `0.1`       |
| __volume__ | Total number of shares traded | `0`         |

If your data series has a single value only, then you should fill OHLC fields with the same single value and V value with 0.

## Symbol info file format

This information determines how the TradingView platform will handle a particular symbol. 
The symbol information should be placed as a single JSON file in the `symbol_info` directory. 
The name of the file is similar to the name of the repository.

|      Field          | Type   | Description                                                                                                                   |                     Default value              |                                    Validation rules                                    |
|---------------------|--------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------------|
| __base-currency__   | String | Code of the base currency in currency pairs.  For example, for `EURUSD` pair the base currency is `EUR`. [ISO 4217][iso_4217] | Can be empty except `forex` and `crypto` types | Error if empty for `forex` and `crypto` types, if not empty, it is validated `^[A-Z0-9._]+$`   |
| __currency__        | String | Code of the currency in which the symbol is traded. [ISO 4217][iso_4217]                                                      | Can be empty for `index` and `economic` types  | Error if empty for `index` and `economic` types, if not empty, it is validated `^[A-Z0-9._]+$` |
| __description__     | String | Symbol description                                                                                                            | Not empty                                      | Error if empty                                                                         |
| __has-intraday__    | Bool   | `false` for end-of-day feed                                                                                                   | `false`                                        | Error if not `false`                                                                   |
| __has-no-volume__   | Bool   | `true` if `volume` = 0 (for `forex`, `index`, etc.)                                                                           | `true`/`false`                                 | Error if empty                                                                         |
| __is-cfd__          | Bool   | Is the symbol a Contract For Differences                                                                                      | `true`/`false`                                 | Warning if not `true`                                                                  |
| __minmovement__     | Int    | The number of units that make up one tick                                                                                     | >`0`                                           | Warning if > `1`                                                                       |
| __pricescale__      | Int    | Tick size                                                                                                                     | `10^n`                                         | Error if not `10^n`                                                                    |
| __session-regular__ | String | Session time                                                                                                                  | `24x7`                                         | Error if not `24x7`                                                                    |
| __symbol__          | String | Symbol name in TradingView format                                                                                             | Not empty                                      | Validating `^[A-Z0-9._]+$`                                                             |
| __ticker__          | String | Symbol name in feed format                                                                                                   | Not empty                                      | Validating `^[^,]+$`                                                                   |
| __timezone__        | String | Timezone code                                                                                                                 | `Etc/UTC`                                      | Error if not `Etc/UTC`                                                                 |
| __type__            | String | Symbol type                                                                                                                   | From the table below                           | From the table only                                                                    |

Below are possible values for `type` field.

| Value          | Description                                                |
|----------------|------------------------------------------------------------|
| __stock__      | Stock (common, preferred, bonus issue, CFD on stocks)      |
| __fund__       | Investment fund                                            |
| __dr__         | Depositary receipt                                         |
| __right__      | Rights issue                                               |
| __bond__       | Bond                                                       |
| __warrant__    | Warrant                                                    |
| __structured__ | Structured Product                                         |
| __index__      | Index                                                      |
| __cfd__        | Contract for differences                                   |
| __forex__      | Forex                                                      |
| __futures__    | Futures Product                                            |
| __expression__ | Math Expression                                            |
| __ets__        | Exchange Traded Spread                                     |
| __crypto__     | Crypto Currency except Crypto Currency Futures and Indices |
| __option__     | Option                                                     |
| __swap__       | Swap                                                       |
| __economic__   | Fundamental economic data                                  |

## Updating the data

Your EOD data is checked and uploaded to our repository once a day.
You can see the data for all previous days on the [chart][tv_chart]. 
The data that is checked and uploaded today will appear on the chart tomorrow.
If the data is not updated for three months, the data will be removed from TradingView storage.

> __Warning__
> 
> The EOD feed has a limit of 1000 symbols per repository. Keep this in mind when adding data files.
> To connect more symbols, you can create another data repository.

Intraday data and real-time updates are possible using a [REST protocol][rest_api], but this option is only available for brokerage integration.

## Data validation
 
If your symbol_info file is incorrect, you will get a parsing error in the __Check data and create pr__ action log.
If some field is found to be missing from this list, a warning about it will appear in the log.

## Accessing a data repository

We like open source code and our tools help a lot of people because of it, but if you want to connect private data - that's completely fine.

For public repositories it is convenient to store access keys in the [environment variables][env_var] of the repository itself.
These variables can be safely used in the Action's code.

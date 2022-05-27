# Data structure

## Data requirements

Two directories are provided for the data files in the repository.

- Place a CSV file with daily data for each symbol in the `data/your_repo` directory. These files need to be updated once a day.
- Place one JSON file with the description of the symbol fields in the `symbol_info` directory.

The structure of the CSV file with data is simple, 6 values in each line.

```csv
20210101T,0.1,0.1,0.1,0.1,0
```

## Data formats

All data must be placed as CSV files. One symbol - one file. The files must meet the following requirements:

- Fields are separated by commas
- No headers
- No blank lines or spaces
- File names must be URL encoded

| Field  | Description                   | Sample    |
|--------|-------------------------------|-----------|
| Date   | Date in YYYYMMDDT format      | 20210101T |
| Open   | First tick price              | 0.1       |
| High   | Maximum tick price            | 0.1       |
| Low    | Minimum tick price            | 0.1       |
| Close  | Last tick price               | 0.1       |
| Volume | Total number of shares traded | 0         |

If your feed is trading data, a valid OHLCV series should come in each line.
If the feed has a single value per day, then it should be `open` = `close` = `high` = `low`, and `volume` = 0.

## Symbol info file format

This information determines how the TradingView platform will handle a particular symbol. 
The symbol information should be placed as a single JSON file in the `symbol_info` directory. 
The name of the file is similar to the name of the repository.

|      Field      | Type   | Description                                                                                                       |                     Default value                    |                                    Validation rules                                   |
|---------------|--------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------------|
| base-currency   | String | Code of the base currency in currency pairs.  For example, for `EURUSD` pair the base currency is `EUR`. ISO 4217 | Can by empty for not `forex` and `crypto` types only | If not empty validate `^[A-Z0-9._]+$` Error if empty for `forex` and `crypto` types   |
| currency        | String | Code of the currency in which the symbol is traded. ISO 4217                                                      | Can be empty for `index` and `economic` types        | If not empty validate `^[A-Z0-9._]+$` Error if empty for `index` and `economic` types |
| description     | String | Symbol description                                                                                                | Not empty                                            | Error if empty                                                                        |
| has-intraday    | Bool   | `false` for end-of-day feed                                                                                       | `false`                                              | Error if not `false`                                                                  |
| has-no-volume   | Bool   | `true` if `volume` = 0 (for `forex`, `index`, etc.)                                                               | `true`/`false`                                       | Error if empty                                                                        |
| is-cfd          | Bool   | Is the symbol a Contract For Differences                                                                          | `true`/`false`                                       | Warning if not `true`                                                                 |
| minmovement     | Int    | The number of units that make up one tick                                                                         | >`0`                                                 | Warning if > `1`                                                                      |
| pricescale      | Int    | Tick size                                                                                                         | `10^n`                                               | Error if not `10^n`                                                                   |
| session-regular | String | Session time                                                                                                      | `24x7`                                               | Error if not `24x7`                                                                   |
| symbol          | String | Symbol name in TradingView format                                                                                 | Not empty                                            | Validating `^[A-Z0-9._]+$`                                                            |
| ticker          | String | Symbol name in feed format.                                                                                       | Not empty                                            | Validating `^[^,]+$`                                                                  |
| timezone        | String | Timezone code                                                                                                     | `Etc/UTC`                                            | Error if not `Etc/UTC`                                                                |
| type            | String | Symbol type                                                                                                       | From the table below                                 | From the table only                                                                   |

Below are `type` filed possible values.

| Value      | Description                                                |
|------------|------------------------------------------------------------|
| stock      | Stock (common, preferred, bonus issue, CFD on stocks)      |
| fund       | Investment fund                                            |
| dr         | Depositary receipt                                         |
| right      | Rights issue                                               |
| bond       | Bond                                                       |
| warrant    | Warrant                                                    |
| structured | Structured Product                                         |
| index      | Index                                                      |
| cfd        | Contract for differences                                   |
| forex      | Forex                                                      |
| futures    | Futures Product                                            |
| expression | Math Expression                                            |
| ets        | Exchange Traded Spread                                     |
| crypto     | Crypto Currency except Crypto Currency Futures and Indices |
| option     | Option                                                     |
| swap       | Swap                                                       |
| economic   | Fundamental economic data                                  |

> __Warning__
> 
> If you can't validate any of the fields in symbol_info file, you will get a parsing error in action's log. 
> If a field is found to be missing from this list, a warning about it will appear in the log.

## Updating the data

We like opensource. Our tools help a lot of people because of it. But if you want to connect private data - that's completely fine.
Data is very useful. Update it regularly.

Your end-of-day data is checked and uploaded to our repository once a day.
You see the data for all previous days on the Chart. The checked and uploaded today data will appear on the Chart tomorrow.

If you want to handle higher frequency data (per minute/second), you can use a [REST feed](https://www.tradingview.com/brokerage-integration/).
We don't want to keep data that nobody else wants. If the data is not updated, will we disable the feed after three months?

## Accessing a data repository

For public repositories it is convenient to store access keys in environment variables of the repository itself.
These variables can be safely used in the action code.

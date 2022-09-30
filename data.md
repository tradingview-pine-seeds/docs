[brokerage_integration]: https://www.tradingview.com/brokerage-integration/
[env_var]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[iso_4217]: https://en.wikipedia.org/wiki/ISO_4217
[tv_chart]: [https://tradingview.com/chart]
[url_encode]: https://en.wikipedia.org/wiki/Internationalized_Resource_Identifier

# Data structure

All symbol data and its description is stored in a repository.
To do this, you need to provide two directories and add data files to them.

- Create a [CSV file](#data-formats) with daily data for each symbol in the `data/repo_name` directory.
- Create a [JSON file](#symbolinfo-file-format) with a description of the symbol fields in the `symbol_info` directory.

## Symbol data format

Each symbol data must be placed into a separate CSV file in the `data/repo_name` directory.

> __Note__
> 
> The EOD (End-of-Day) feed has a limit of 1,000 symbols per repository. Keep this in mind when adding data files.
> To connect more symbols, you can create another data repository.

The files and their content must meet the following requirements:

- Values must be comma-separated.
- No headers, blank lines, and spaces are used.
- File names must be [URL encoded][url_encode].

| Field    | Description                   | Sample      |
|----------|-------------------------------|-------------|
| `date`   | Date in YYYYMMDDT format      | `20210101T` |
| `open`   | First tick price              | `0.1`       |
| `high`   | Maximum tick price            | `0.1`       |
| `low`    | Minimum tick price            | `0.1`       |
| `close`  | Last tick price               | `0.1`       |
| `volume` | Total number of shares traded | `0`         |

> __Note__
> 
> If your data series has a single value only, fill the `open`, `close`, `high`, and `low` fields with the same value and `volume` with `0`.

<details>
    <summary>CSV file example</summary>

```csv
20210101T,0.1,0.1,0.1,0.1,0
```

</details>

<br>

### Data update

Your EOD data is checked and uploaded to our repository once a day.
You can see the data for all previous days on the [chart][tv_chart]. 
The data that is checked and uploaded today will appear on the chart tomorrow.
If the data is not updated for three months, the data will be removed from the TradingView storage.

Intraday data and real-time updates are possible using a REST protocol, but this option is only available for [brokerage integration][brokerage_integration].

## Symbol information format

Symbol information must be placed into a single JSON file in the `symbol_info` directory. 
The file name must be similar to the repository name.

A file format is a JSON object consisting of the following required fields.

| Field | Type | Description | Note |
|-|-|-|-|
| `symbol` | String | Symbol name used in TradingView. | Cannot be empty. Validation rule: `^[A-Z0-9._]+$`. |
| `currency` | String | Three-letter currency code according to [ISO 4217][iso_4217]. | Can be empty. Validation rule: `^[A-Z0-9._]+$`. |
| `description` | String | Symbol description. | Cannot be empty. |
| `pricescale` | Integer | Tick size. | Values must match `10^n`. Otherwise, an error occurs. |

> __Note__
> 
> Each object field is an array with values.
> For all fields, the length of these arrays must match.
> However, if all the values in the array are the same, you can specify a single value for the field instead of an array.

<details>
    <summary>JSON object example</summary>

```json
{
   "pricescale": [10, 10],
   "symbol": [
      "BTC_DEV_ACTIVITY",
      "BTC_SOCIAL_VOLUME_TOTAL"
   ],
   "currency": "",
   "description": [
      "Bitcoin developer activity",
      "Bitcoin social volume total"
   ]
}
```

</details>

<details>
    <summary>JSON object example with a single value for <code>pricescale</code></summary>

```json
{
   "pricescale": 10,
   "symbol": [
      "BTC_DEV_ACTIVITY",
      "BTC_SOCIAL_VOLUME_TOTAL"
   ],
   "currency": "",
   "description": [
      "Bitcoin developer activity",
      "Bitcoin social volume total"
   ]
}
```

</details>

<br>

### Data validation

Keep in mind the following validation rules for the `symbol_info` file and its content.

- The file format must be JSON.
- JSON object cannot be empty.
- All four [fields](#symbolinfo-file-format) are required.
- The array length of the fields must match.

You will get errors in the log if these rules are not followed.

## Data repository access

We like open-source code, and our tools help a lot of people, but if you want to connect private data, that's completely fine.

For public repositories, it is convenient to store access keys in the [environment variables][env_var] of the repository itself.
These variables can be safely used in the Action's code.

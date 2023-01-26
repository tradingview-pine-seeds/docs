# Update script example

As an example history updating we use script that gets data from https://api.santiment.net/ (Links: [Project main page](https://santiment.net/), [Santiment API description](https://academy.santiment.net/sanapi/), [Santiment metrics description](https://academy.santiment.net/metrics/#financial))
Folder that contains update_santiment.py and update.sh should be placed near your fork local copy (e. g. ~/github/fork_local_copy, ~/github/folder_with_update_scripts).

To make update you should run update.sh from folder that cointains it: `cd ~/github/folder_with_update_scripts && ./update.sh`

update.sh runs update_santiment.py which gets data from Santiment API and writes it to CSV files with history, update.sh then commits changes and pushes them, after that changes will go to TradingView.

In more detail about what the script update_santiment.py:
This script requests several metric values for 2 crypto assets: Ethereum and Bitcoin. For each crypto asset metric, a file \<CRYPTO_ASSET_FILE_PREFIX>_<METRIC_SUFFIX>.csv is updated (e. g. for Bitcoin sentiment_negative_total metric it updates data/seed_crypto_santiment/BTC_SENTIMENT_NEGATIVE_TOTAL.csv, for Ethereum unique_social_volume_total_1h data/seed_crypto_santiment/ETH_UNIQUE_SOCIAL_VOLUME_TOTAL_1H.csv).
For each crypto asset metric we make HTTP request to Santiment GraphQL API (we request all data up to today inclusive) and save updated values to corresponding file. If there is a value for a date in the file, but it is not in the response from the API, the value for this date remains unchanged in the file.

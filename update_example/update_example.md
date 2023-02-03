# Example script for automating data history uploads

There is a way to update historical data in GitHub repository by scripts. You can prepare a script that will write data in CSV files with expected EOD data format. 

This article describes an example [`/update example/update_santiment.py`](/update_example/update_santiment.py) script that automates data history uploads to a forked repository.
The script gets data from [Santiment API], converts it into CSV files, and uploads them into the repository.
For more information about [Santiment API], you can refer to the Santiment's [main page], [API reference], and [metrics overview].

> __Note__
>
> The `update_santiment.py` script is only an example of how the automated uploads can be implemented.
> You will need to implement your own script.

## How the script works

The `update_santiment.py` script requests several metric values for two Crypto assets: Ethereum and Bitcoin.
For each Crypto asset metric, a `/<CRYPTO_ASSET_FILE_PREFIX>_<METRIC_SUFFIX>.csv` file is updated.
For example:

- for Bitcoin, the `sentiment_negative_total` metric updates `data/seed_crypto_santiment/BTC_SENTIMENT_NEGATIVE_TOTAL.csv`,
- for Ethereum, the `unique_social_volume_total_1h` metric updates `data/seed_crypto_santiment/ETH_UNIQUE_SOCIAL_VOLUME_TOTAL_1H.csv`.

For each Crypto asset metric, TradingView makes HTTP requests to Santiment GraphQL API for all data up to today inclusively and saves updated values to corresponding files.
If there is a value for a date in the file, but there is no one in the response from the API, the value for this date remains unchanged in the file.

## Prerequisites

To run the script, you first need to:

1. Install the latest version of Python. For more information, refer to the [Downloading Python instructions](https://wiki.python.org/moin/BeginnersGuide/Download).
2. Install the latest version of Git. For more information, refer to the [Git download page](https://git-scm.com/downloads).

## Run the script

To update the data, follow the steps below:

1. On the repository page, open `update_example/update_example.py` and click the *Copy raw contents* (<img src = "../images/svg/clone-regular.svg" alt="My Happy SVG"/>) button.
    The file contents will be copied to the clipboard.

    ![Copy raw contents](/images/copy_raw_contents.png)

2. Open any text editor on your computer and paste the contents.
3. Save the file with the `update_santiment.py` name in any folder you prefer.
4. On the repository page, copy the repository name by clicking *Code → Copy to clipboard*.

    ![Clone repository name on GitHub](/images/github_clone_repository.png)

5. On your computer, open command line and run the `git clone <your-repository-name.git>` command.

    ![Execute git clone command](/images/clone_fork.png)

6. Change the current folder to folder where you saved `update_santiment.py` by executing `cd <folder-name-with-update_santiment.py>`

    ![Change current folder](/images/change_folder_to_script.png)

7. Run `update_santiment.py` by executing the following command:

    `python3 update_santiment.py --data-folder <path-to-forked-folder-with-your-local-data>`

    ![Run the script](/images/run_update_santiment.png)

8. Change the current folder to fork local copy by executing `cd <path-to-your-local-fork>`

    ![Change folder](/images/change_folder_to_fork.png)

9. You can run `git status` to see which files have changed. If it is not the first update, you can see what changed in files by running `git diff`. Press 'q' to close diff.

    ![Run Git status for first updates](/images/git_status_first_update.png)

    ![Run Git status for next updates](/images/git_status_next_updates.png)

    ![Check diff output](/images/diff_output.png)

10. Run `git add .` to add file contents to the index.

    ![Run Git add](/images/git_add.png)

11. Run `git commit -m "Update data"` to record changes to the repository.

    ![Run Git commit](/images/git_commit.png)
> NOTE
>
>You need to add symbol description in [symbol info](/data.md#symbol_info-format) before you add its data, etherwise the data won't be uploaded to the TradingView storage

12. Run `git push` to upload local repository content to a remote repository.

    ![Run Git push](/images/git_push.png)

13. Go to your repository page on GitHub and open *Actions*. Check that the action `Check data and create PR` run successfully in your fork repository on GitHub.

    ![GitHub successful action run](/images/github_successful_action.png)

> __Note__
>
> Data should be updated every day. For next updates, you only need to follow steps 6−13.

[API reference]: https://academy.santiment.net/sanapi/
[main page]: https://santiment.net/
[metrics overview]: https://academy.santiment.net/metrics/#financial
[Santiment API]: https://api.santiment.net/
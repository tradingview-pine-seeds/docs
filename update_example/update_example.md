# Update script example

As an example history updating we use script that gets data from https://api.santiment.net/ (Links: [Project main page](https://santiment.net/), [Santiment API description](https://academy.santiment.net/sanapi/), [Santiment metrics description](https://academy.santiment.net/metrics/#financial))

Prerequisites:
1. Install last version of python [instructions](https://wiki.python.org/moin/BeginnersGuide/Download)
2. Install last version of git [downloads page](https://git-scm.com/downloads)

To make update you need to follow these steps:

1. Save update_santiment.py script to your computer: click on "Copy raw cantents" button on github page with opened script, then open text editor on your computer, right-click in it and press "Paste" then save file as "update_santiment.py" in folder you prefer

    ![Copy raw contents](/images/copy_raw_contents.png)

2. Clone your repository fork to your computer `git clone <your_repository.git>`. You can get repo name for clone command by clicking "Code" and then "Copy to clipboard", then paste it to command

    ![Github repo name for clone](/images/github_clone_repo_name.png)
    ![Clone fork](/images/clone_fork.png)

3. Change current folder to folder where you saved update_santiment.py `cd <folder with update_santiment.py>`

    ![Change folder](/images/change_folder_to_script.png)

4. Run update_santiment.py `python3 update_santiment.py --data-folder <path to folder with data in your fork local copy>`

    ![Run update_santiment.py](/images/run_update_santiment.png)

5. Change current folder to fork local copy `cd <your fork local copy path>`

    ![Change folder](/images/change_folder_to_fork.png)

6. You can run `git status` to see which files have changed. If it is not the first update, you can see what changed in files by running `git diff`. Press 'q' to close diff.

    ![Git status first update](/images/git_status_first_update.png)

    ![Git status next updates](/images/git_status_next_updates.png)

    ![Diff output](/images/diff_output.png)

7. `git add .`

    ![Git add](/images/git_add.png)

8. `git commit -m "Update data"`

    ![Git commit](/images/git_commit.png)

9. `git push`

    ![Git push](/images/git_push.png)

10. Check that there is new successful action run in your repository on github

    ![Github successful action run](/images/github_successful_action.png)

For next updates you only need steps 3-10

In more detail about what the script update_santiment.py:
This script requests several metric values for 2 crypto assets: Ethereum and Bitcoin. For each crypto asset metric, a file \<CRYPTO_ASSET_FILE_PREFIX>_<METRIC_SUFFIX>.csv is updated (e. g. for Bitcoin sentiment_negative_total metric it updates data/seed_crypto_santiment/BTC_SENTIMENT_NEGATIVE_TOTAL.csv, for Ethereum unique_social_volume_total_1h data/seed_crypto_santiment/ETH_UNIQUE_SOCIAL_VOLUME_TOTAL_1H.csv).
For each crypto asset metric we make HTTP request to Santiment GraphQL API (we request all data up to today inclusive) and save updated values to corresponding file. If there is a value for a date in the file, but it is not in the response from the API, the value for this date remains unchanged in the file.

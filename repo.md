[gh_security]: https://github.com/settings/security
[gh_token]: https://github.com/settings/tokens
[gh_docs_pat]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
[gh_docs_2fa]: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
[gh_docs_actions]: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run
[gh_docs_logs]: https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs
[env_var]: https://docs.github.com/en/actions/learn-github-actions/environment-variables
[repo_updater]: https://github.com/org-bot/finra-updater
[_data]: /data.md

# GitHub settings

Use GitHub as your backend. This is where you upload the data. Here you update them.
We will prepare a repository for you. You will fork it. After that, you can upload your data to the fork.

GitHub Actions are already configured. They regularly check the data and create a _Pull Request_ to our repository.
See the results of the checks in the Action's logs.

## Pre-setup

- Go to [GitHub Security settings][gh_docs_2fa] → Configure [2FA][gh_security]
- Create [Personal access token][gh_docs_pat] for __repo__, __workflow__ and __admin:org__ areas
- We have created a repository for you. Fork it.
- Go to _Settings → Secrets → Action_ of your forked repository
- Add the created __Personal access token__ by calling it `ACTION_TOKEN` here
- Now go to _Actions → General → Action permissions_
- Check the box [Allow all actions and reusable workflows][gh_docs_actions] here
- Click the _Actions_ tab
- Disable all workflows and only enable __Check data and create pr__

## Repository scructure

Your forked repository contains the following files and directories.

```bash
.github/workflows    # GitHub actions files
data/your_repo_name  # Your data CSV-files
scripts              # Scripts for GitHub actions
symbol_info          # Your JSON-files with symbol information
README.md
```

## Add data files

- Upload CSV data files to the `data/your_repo` directory
- Upload a JSON character description file to the `symbol_info` directory

## Check the data upload

Data is regularly checked and loaded into TradingView storage by action __Check data and create pr__. 
The results of the checks are written to the log of this action.

After updating the data files and completing the action, examine the log for errors.

- Go to repository __Actions__ tab
- Check action log __Check data and create pr__

The [data requirements][_data] are listed in the tables. In the log, we write which field failed the check and why.

## Additional repository

If you add anything other than data to the fork of our repository - _Pull Request_ will fail.
To automatically pull the data - create a separate repository with data.

Here you can automate data preparation before uploading to the main repository.

- Configure keys for access to third-party sources
- Add a script to download data
- Add a script to upload data to the main repository

For public repositories, it is convenient to store access keys in the [environment variables][env_var] of the repository itself.

Here is an [example][repo_updater] of the additional repository.

```bash
.github/workflows          # GitHub Actions files
scripts                    # Data update scripts
README.md
symbol_info_template.json
```

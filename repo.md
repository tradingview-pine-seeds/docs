[gh_security]: https://github.com/settings/security
[gh_token]: https://github.com/settings/tokens
[gh_docs_pat]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
[gh_docs_2fa]: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
[gh_docs_actions]: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run
[gh_docs_logs]: https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs
[_data]: /data.md

# GitHub repository settings

Use GitHub as your backend: we will provide you with a repository where you can store your data and update it.
In this repository, GitHub actions are already configured.
They regularly check the data and create _Pull Requests_ to the TradingView repository.
The results of the data checks will be available in the action logs.

## Get access to a repository

Send us an email to pine.seeds@tradingview.com with the subject __Pine Seeds Request__.
Specify your GitHub username and desired repository name.
Note that the account and repository names will be used as [parts](README.md#Example) of the unique prefix for your data.

We will prepare a repository for you, which you'll need to fork.

## Pre-setup

After you fork the repository, you will need to do a pre-setup. Then you can upload your data.

- Go to GitHub [_Settings → Password and authentication_][gh_security] and configure [two-factor authentication][gh_docs_2fa]
- Create [Personal access token][gh_docs_pat] for __repo__, __workflow__ and __admin:org__ areas
- We have created a repository for you and you will need to fork it
- Go to _Settings → Secrets → Action_ of your forked repository
- Add the created __Personal access token__ by calling it `ACTION_TOKEN` here
- Now go to _Actions → General → Action permissions_
- Check the [Allow all actions and reusable workflows][gh_docs_actions] box here
- Click the _Actions_ tab
- Disable all workflows and only enable __Check data and create pr__

## Repository scructure

Your forked repository contains the following files and directories.

```bash
.github/workflows    # GitHub actions files
data/repo_name       # Your data CSV-files
scripts              # Scripts for GitHub actions
symbol_info          # Your JSON-files with symbol information
README.md
```

## Add data files

- Upload CSV data files to the `data/repo_name` directory
- Upload a JSON character description file to the `symbol_info` directory

## Check the data upload

Data is regularly checked and loaded into TradingView storage by the __Check data and create pr__ action. 
The results of the data checks can be found in the action logs.

After updating the data files and completing the relevant actions, examine the log for errors.

- Go to the repository __Actions__ tab
- Check the __Check data and create pr__ action log

The [data requirements][_data] are listed in the tables. We indicate which field failed the check in the log and explain why.

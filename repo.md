[gh_security]: https://github.com/settings/security
[gh_token]: https://github.com/settings/tokens
[gh_docs_pat]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
[gh_docs_2fa]: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
[gh_docs_actions]: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run
[gh_docs_logs]: https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs
[_data]: /data.md
[git_token-scopes]: /images/github-Token-scopes.png
[git_add_secret]: /images/github-Action_secrets-New_secret.png
[git_allow_actions]: /images/github-Allow_Actions.png
[git_more_workflows]: /images/github-Show_More_Actions.png
# GitHub settings

Use GitHub as your backend. This is where you upload the data and update it.
We will prepare a repository for you and you will need to fork it. After that, you can upload your data to the forked version.

GitHub actions are already configured. They regularly check the data and create a _Pull Request_ to our repository.
See the results of the data checks in the action logs.

## Pre-setup

- Go to [GitHub Security settings][gh_docs_2fa] → Configure [2FA][gh_security]
- Create [Personal access token][gh_docs_pat] with access scopes __repo__, __workflow__ and __admin:org__
![git_token-scopes]
- We have created a repository for you and you will need to fork it.
- Go to _Settings → Secrets → Action_ of your forked repository
- Press __New repository secret__ and add created __Personal access token__ with name `ACTION_TOKEN` here
![git_add_secret]
- Now go to _Actions → General → Action permissions_
- Check the [Allow all actions and reusable workflows][gh_docs_actions] box here
![git_allow_actions]
- Click the _Actions_ tab and click __Show more workflows__ 
![git_more_workflows]
- Disable all workflows and only enable __Check data and create pr__

## Repository scructure

Your forked repository contains the following files and directories.

```bash
.github/workflows    # GitHub actions files
data/repo_name       # Your data CSV-files
scripts              # Scripts for GitHub actions
symbol_info          # Your JSON-file with symbol information
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

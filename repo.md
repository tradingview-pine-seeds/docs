[gh_docs_2fa]: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
[gh_docs_pat]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
[gh_security]: https://github.com/settings/security
[gh_docs_actions]: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run
[_data]: /data.md

# GitHub repository settings

Use GitHub as your backend: we will provide you with a repository where you can store your data and update it.
In this repository, GitHub actions are already configured.
They regularly check the data and create _Pull Requests_ to the TradingView repository.
The results of the data checks will be available in the action logs.

## Get access to a repository

Send us an email to pine.seeds@tradingview.com with the subject __Pine Seeds Request__.
Specify your GitHub username and the desired repository suffix. __The maximum number of characters in suffix must be 16.__
The repository name will be `seed_<your_github_username>_<suffix_you_provided>`.

> __Note__
>
> Your username and suffix will be used as [parts](README.md#Example) of the unique suffix for your data.

Your request processing may take up to one day.
As a result, you will get a link to the repository you need to fork.
Note that the repository will be private, so your fork can only be private.

## Pre-setup

After you fork the repository, you will need to do a pre-setup. Then you can upload your data.

1. Go to GitHub [_Settings → Password and authentication_][gh_security] and configure [two-factor authentication][gh_docs_2fa].
2. Go to GitHub _Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token → Generate new token (classic)_. Generate [Personal access token][gh_docs_pat] with the __repo__, __workflow__, and __admin:org__ access scopes.

    ![GitHub access scopes](/images/github_access_scopes.png)

3. In the forked repository, go to _Settings → Secrets and variables → Actions_.
4. Click __New repository secret__, specify `ACTION_TOKEN` in the _Name_ field, and paste created __Personal access token__ into the _Secret_ field. Select _Add secret_.

    ![Adding GitHub action secret](/images/github_new_action_secret.png)

5. Go to _Actions → General → Actions permissions_.
6. Select the [Allow all actions and reusable workflows][gh_docs_actions] checkbox and click __Save__.

    ![Selecting GitHub actions permissions](/images/github_actions_permissions.png)

7. Go to the _Action_ tab and click to the _I undestand my worflows, go ahead and enable them_ button
8. Disable workflow __Upload data__ with __Disable workflow__ button. Check that workflow __Check data__ is enabled.

    ![GitHub disable action](/images/github_action_disable.png)

## Repository structure

Your forked repository contains the following files and directories.

```bash
.github/workflows    # GitHub action files
data/repo_name       # Your data CSV files
scripts              # Scripts for GitHub actions
symbol_info          # Your JSON file with symbol information
README.md
```

## Add data files

- Add symbol description to the JSON file in the `symbol_onfo/repo_name.json` directory.
- Upload CSV data files to the `data/repo_name` directory.

## Check the data upload

The __Check data__ action regularly validates data and loads it into the TradingView storage.
You can find the results of the data checks in the action logs.

After updating the data files and completing the relevant actions, examine the log for errors.

1. Go to the repository __Actions__ tab.
2. Check the __Check data__ action. It's last run should be marked with a green tick like on the image below.
    ![GitHub successful action runs](/images/github_ok_action.png)

It may take some time for the initial upload to be visible on the TradingView chart.

The [data requirements][_data] are listed in the tables. We indicate which field failed the check in the log and explain why.

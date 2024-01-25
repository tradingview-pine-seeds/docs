[gh_docs_2fa]: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
[gh_docs_pat]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
[gh_security]: https://github.com/settings/security
[gh_docs_actions]: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run
[data]: /data.md

# GitHub repository settings

> [!WARNING]
> __The creation of new repositories has been suspended__. We will continue to support the existing repositories. If you have questions or need assistance with your current repositories, contact us at
> pine.seeds@tradingview.com.

Use GitHub as your backend: TradingView will provide you with a repository that you need to fork.
Then you can store your data and update it. Please note that the name of forked repository should be the same as the initial one.

In the repository, GitHub actions are already configured.
Actions check data after changes in forked repository and creates _Pull Requests_ to the main TradingView repository.
From the main repository, data uploads to the TradingView storage so data can be viewed on the TradingView charts.
The results of the data checks will be available in the action logs.

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

7. Go to the _Action_ tab and click _I understand my workflows, go ahead and enable them_.

    ![GitHub enable actions](/images/github_actions_workflows.png)

8. Disable workflow __Upload data__ with __Disable workflow__ button. Check that workflow __Check data__ is enabled.

    ![GitHub disable workflow](/images/github_disable_workflow.png)

## Repository structure

Your forked repository contains the following files and directories.

```bash
.github/workflows    # GitHub action files
data                 # Your data CSV files
symbol_info          # Your JSON file with symbol information
README.md
```

## Add data files

How to add new symbols and data described in [tutorial](/data_tutorial.md)

- Add symbol description to the JSON file in the `symbol_info/repo_name.json` directory.
- Upload CSV data files to the `data/` directory.

## Check the data upload

The __Check data__ action validates data and loads it into the TradingView storage.
You can find the results of the data checks in the action logs.

After updating the data files and completing the relevant actions, examine the log for errors.

1. Go to the repository __Actions__ tab.
2. Check the __Check data__ action. It's last run should be marked with a green tick like on the image below.

    ![GitHub successful action runs](/images/github_ok_action.png)

It may take some time for the initial upload to be visible on the TradingView chart.

The [data requirements][data] are listed in the tables. We indicate which field failed the check in the log and explain why.

> __Note__
>
> If you have any questions or problems that you are unable to handle, please contact us at pine.seeds@tradingview.com.
> Our support team is available on weekdays from 7 AM to 4 PM UTC.

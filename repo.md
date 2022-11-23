[gh_docs_2fa]: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication
[gh_docs_pat]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
[gh_security]: https://github.com/settings/security
[gh_docs_actions]: https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#allowing-select-actions-and-reusable-workflows-to-run
[_data]: /data.md

# GitHub settings

Use GitHub as your backend. This is where you upload the data and update it.
We will prepare a repository for you and you will need to fork it. After that, you can upload your data to the forked version.

GitHub actions are already configured. They regularly check the data and create a _Pull Request_ to our repository.
See the results of the data checks in the action logs.

## Pre-setup

1. Go to GitHub [_Settings → Password and authentication_][gh_security] and configure [two-factor authentication][gh_docs_2fa].
2. Generate [Personal access token][gh_docs_pat] with the __repo__, __workflow__, and __admin:org__ access scopes.

    ![GitHub access scopes](/images/github_access_scopes.png)

3. Fork a repository that we created for you.
4. Go to _Settings → Secrets → Actions_ of your forked repository.
5. Click __New repository secret__, specify `ACTION_TOKEN` in the _Name_ field, and paste created __Personal access token__ into the _Secret_ field. Select _Add secret_.

    ![Adding GitHub action secret](/images/github_new_action_secret.png)

6. Go to _Actions → General → Actions permissions_.
7. Select the [Allow all actions and reusable workflows][gh_docs_actions] checkbox and click __Save__.

    ![Selecting GitHub actions permissions](/images/github_actions_permissions.png)

8. Click the _Actions_ tab and click __Show more workflows__.

    ![Repository action list](/images/github_action_list.png)

9. Disable all workflows and only enable __Check data and create pr__.

## Repository structure

Your forked repository contains the following files and directories.

```bash
.github/workflows    # GitHub actions files
data/repo_name       # Your data CSV-files
scripts              # Scripts for GitHub actions
symbol_info          # Your JSON-file with symbol information
README.md
```

## Add data files

- Upload CSV data files to the `data/repo_name` directory.
- Upload a JSON symbol description file to the `symbol_info` directory.

## Check the data upload

The __Check data and create pr__ action regularly validates data and loads it into the TradingView storage.
You can find the results of the data checks in the action logs.

After updating the data files and completing the relevant actions, examine the log for errors.

1. Go to the repository __Actions__ tab.
2. Check the __Check data and create pr__ action log.

The [data requirements][_data] are listed in the tables. We indicate which field failed the check in the log and explain why.

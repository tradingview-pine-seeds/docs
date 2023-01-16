[2fa]: https://github.com/settings/security
[chart]: https://tradingview.com/chart

# 5-minute tutorial

## Get access to a repository

1. Send us an email to pine.seeds@tradingview.com with the subject __Pine Seeds Request__.
    Specify your GitHub username and the desired repository suffix.
    Repository name will be `seed_<your_github_username>_<suffix_you_provided>`.
    Note that your username and suffix will be used as [parts](README.md#Example) of the unique suffix for your data.
2. Wait for a link to the repository.

## Fork the repository

1. Go to GitHub _Settings → Password and authentication_ and configure [two-factor authentication][2fa].
2. Go to GitHub _Settings → Developer settings → Personal access tokens → Generate new token → Generate new token (classic)_. Create _Personal access token_ for __repo__, __workflow__, and __admin:org__ areas.
    ![GitHub access scopes](/images/github_access_scopes.png)
3. Follow the repository link and create a fork.

## Set up the actions

1. In the forked repository, go to _Settings → Secrets and variables → Action_.
2. Add the created _Personal access token_ by calling it `ACTION_TOKEN` here.
3. Now go to _Actions → General → Action permissions_.
4. Select the __Allow all actions and reusable workflows__ option.
5. Click the _Actions_ tab.
6. Disable all workflows with __Disable workflow__ button except __Check data and create pr__.
    ![GitHub disable action](/images/github_action_disable.png)

## Add data files

1. Upload your data files to the `data/repo_name` directory.
2. Upload a symbol description file with the `repo_name.json` name to the `symbol_info` directory.

## Check the data upload

1. Go to the _Actions_ tab.
2. Check the __Check data and create pr__ action. It's last run should be marked with a green tick like on the image below.
    ![GitHub successful action runs](/images/github_ok_action.png)

## Create a chart

1. Log in to [tradingview.com][chart].
2. Go to the symbol search box and enter the full symbol name. It may take some time for the initial upload to be visible on the TradingView chart.
3. The symbol you requested will be opened on the chart.

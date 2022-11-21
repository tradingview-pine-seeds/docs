[2fa]: https://github.com/settings/security
[chart]: https://tradingview.com/chart

# 5-minute tutorial

## Get access to a repository

1. Send us an email to pine.seeds@tradingview.com with the subject __Pine Seeds Request__. Specify your GitHub username and desired repository name. Note that the account and repository names will be used as [parts](README.md#Example) of the unique prefix for your data.
2. Wait for the link to a repository.

## Fork the repository

1. Go to GitHub _Settings → Password and authentication_ and configure [two-factor authentication][2fa].
2. Create _Personal access token_ for __repo__, __workflow__, and __admin:org__ areas.
3. Follow the repository link and create a fork.

## Set up the actions

1. Go to _Settings → Secrets → Action_ of your forked repository.
2. Add the created _Personal access token_ by calling it `ACTION_TOKEN` here.
3. Now go to _Actions → General → Action permissions_.
4. Check the __Allow all actions and reusable workflows__ box here.
5. Click the _Actions_ tab.
6. Disable all workflows and only enable __Check data and create pr__.

## Add data files

1. Upload your data files to the `data/repo_name` directory.
2. Upload a symbol description file to the `symbol_info` directory.

## Check the data upload

1. Go to the _Actions_ tab.
2. Check the __Check data and create pr__ action log.

## Create a chart

1. Log in to [tradingview.com][chart].
2. Go to the symbol search box and enter the full symbol name.
3. The symbol you requested will be opened on the chart.

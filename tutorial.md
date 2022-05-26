# Tutorial

## Contact us

- Send request to [support@tradingview.com](mailto:support@tradingview.com)
- Wait for an email with your repository link

## Fork the repository

- Go to _GitHub Security settings_ → Configure [2FA](https://github.com/settings/security)
- Create _Personal access token_ for __repo__, __workflow__ and __admin:org__ areas
- Check your email → Follow the link in the email
- Create a repository fork

## Setup the actions
- Go to _Settings → Secrets → Action_ of your forked repository
- Add the created _Personal access token_ by calling it `ACTION_TOKEN` here
- Now go to _Actions → General → Action permissions_
- Check the box __Allow all actions and reusable workflows__ here
- Click the _Actions_ tab
- Disable all workflows and only enable __Check data and create pr__

## Add data files

- Upload CSV data files to the `data/your_repo` directory
- Upload a JSON character description file to the `symbol_info` directory

## Check the data upload

- Go to _Actions_ tab
- Check action log __Check data and create pr__

## Create a chart

- Log into [tradingview.com](https://tradingview.com/e)
- Go to symbol search box → Enter full symbol name
- A graph will appear on the chart main area

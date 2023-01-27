"""This script downloads data from Santiment API, converts it to
Pine Seeds historical data format and saves it as CSV files."""
import argparse
import csv
import os
from datetime import datetime

import requests


# metrics for crypto coins to request from Santiment API
METRICS = [
    "sentiment_negative_total",
    "github_activity",
    "dev_activity",
    "sentiment_positive_total",
    "sentiment_balance_total",
    "social_volume_total",
    "social_dominance_total",
    "unique_social_volume_total_1h",
]

# crypto coins for which you need to request metrics
# tuple contains slug - Santiment API field value to request this coin
# and data filename prefix - prefix for CSV file for this coin
COINS = [
    ("bitcoin", "btc"),
    ("ethereum", "eth"),
]

REQUEST_URL = "https://api.santiment.net/graphql"
REQUEST_HEADERS = {"Content-Type": "application/graphql"}
REQUEST_BODY_TEMPLATE = """
{ getMetric(metric: "%s")
  { 
    timeseriesData( 
      slug: "%s"
      from: "2012-12-31T00:00:00Z" 
      to: "%s" 
      interval: "1d"
    )
    { 
      datetime 
      value 
    } 
  } 
}
"""


def save_new_data(data_json, filename):
    """save updated values to CSV"""
    data_dict = {}

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in csv.reader(file):
                data_dict[line[0]] = line[1]

    for data_point in data_json:
        date = data_point["datetime"]
        val = data_point["value"]
        data_dict[date] = val

    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for date in sorted(data_dict.keys()):
            val = data_dict[date]
            writer.writerow([date, val, val, val, val, 0])


def process_data_file(data_folder, coin, metric, to_date):
    """request data from Santiment API and save updated values to file"""
    req_body = REQUEST_BODY_TEMPLATE % (metric, coin[0], to_date)

    response = requests.post(REQUEST_URL, headers=REQUEST_HEADERS, data=req_body)

    data_json = response.json()["data"]["getMetric"]["timeseriesData"]

    for data_point in data_json:
        end = data_point["datetime"].index("T") + 1
        data_point["datetime"] = data_point["datetime"][:end].replace("-", "")

    # use metric as suffix
    filename = (coin[1] + "_" + metric).upper() + ".csv"
    out_path = os.path.join(data_folder, filename)

    save_new_data(data_json, out_path)
    print("updated", coin[0], metric)


def parse_args():
    """parse args"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--data-folder", default=".", type=str)

    return parser.parse_args()


def main():
    """main func"""
    args = parse_args()
    if not os.path.exists(args.data_folder):
        os.makedirs(args.data_folder)

    to_date = datetime.today().strftime("%Y-%m-%d") + "T23:59:59Z"

    for coin in COINS:
        for metric in METRICS:
            process_data_file(args.data_folder, coin, metric, to_date)


if __name__ == "__main__":
    main()

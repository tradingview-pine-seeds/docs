"""Script to get metrics history for bitcoin and ethereum
from santiment api and save updates to csv files in required format"""
import csv
import os
from datetime import datetime

import dataclasses
import requests


@dataclasses.dataclass
class SlugInfo:
    """crypto coin name in santiment api and data
    filename prefix when saving values to csv file"""

    slug: str
    data_filename_prefix: str


# metrics for crypto coins to request from santiment api
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
# and corresponding csv files prefixes
SLUG_INFOS = [
    SlugInfo(
        slug="bitcoin",
        data_filename_prefix="btc",
    ),
    SlugInfo(
        slug="ethereum",
        data_filename_prefix="eth",
    ),
]

# metric names are used in csv files as postfixes
# this mapping is used to replace metric with another value
DATA_FILENAME_POSTFIX_FIXES = {
    "unique_social_volume_total_1h": "unique_social_volume_total"
}

REQ_URL = "https://api.santiment.net/graphql"
REQ_HEADERS = {"Content-Type": "application/graphql"}
REQ_BODY_TEMPLATE = """
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

DATA_FOLDER = "../seed_crypto_santiment/data/seed_crypto_santiment/"


def save_new_data(data_json, filename):
    """save updated values to csv"""
    orig = {}

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in csv.reader(file):
                orig[line[0]] = line[1]

    for data_point in data_json:
        date = data_point["datetime"]
        val = data_point["value"]
        orig[date] = val

    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for date in sorted(orig.keys()):
            val = orig[date]
            writer.writerow([date, val, val, val, val, 0])


def process_data_file(slug_info, metric, to_date):
    """request data from santiment api and save updated values to file"""
    req_body = REQ_BODY_TEMPLATE % (metric, slug_info.slug, to_date)

    response = requests.post(REQ_URL, headers=REQ_HEADERS, data=req_body)

    data_json = response.json()["data"]["getMetric"]["timeseriesData"]

    for data_point in data_json:
        end = data_point["datetime"].index("T") + 1
        data_point["datetime"] = data_point["datetime"][:end].replace("-", "")

    # use metric as postfix, if there is a fix for this metric, use it
    filename_postfix = DATA_FILENAME_POSTFIX_FIXES.get(metric, metric)
    filename = (
        slug_info.data_filename_prefix + "_" + filename_postfix
    ).upper() + ".csv"
    out_path = DATA_FOLDER + filename

    save_new_data(data_json, out_path)
    print("updated", slug_info.slug, metric)


def main():
    """main func"""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    to_date = datetime.today().strftime("%Y-%m-%d") + "T23:59:59Z"

    for slug_info in SLUG_INFOS:
        for metric in METRICS:
            process_data_file(slug_info, metric, to_date)


if __name__ == "__main__":
    main()

from promptflow import tool
from typing import List
import json

def concatenate_with_or(strings):
    concatenated_string = " or ".join(f"stock_symbol eq '{value.lower()}'" for value in strings)
    result = f"({concatenated_string})"
    return result

@tool
def format_filter_criteria_for_search(search_result: str) -> object:
  stock_json = json.loads(search_result)

  stock_symbols = stock_json['stockSymbols']
  latest = stock_json['dateInformation']['latest']

  filter_object = {}

  filter_object["filter"] = concatenate_with_or(stock_symbols)

  if 'year' in stock_json['dateInformation']:
    if stock_json['dateInformation']['year'] != None and len(str(stock_json['dateInformation']['year'])) > 0 :
      filter_object["filter"] +=  f" and year eq '{stock_json['dateInformation']['year']}'"

  if 'latest' in stock_json['dateInformation']:
    filter_object["filter"] += f" and latest eq '{format(latest).lower()}'"
    
  if 'financialReportType' in stock_json:
    if stock_json['financialReportType'] == "10-Q" or stock_json['financialReportType'] == "10-K":
      filter_object["filter"] += f" and form_type eq '{stock_json['financialReportType']}'"

  return filter_object

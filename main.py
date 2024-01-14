import json

from fetch_func import fetch_search_results
from read_keywords_func import read_keywords_by_line_from_file

# read the api key and cse id from the config.json file
with open('./config.json') as f:
    config = json.load(f)
    api_key = config['google-api-key']
    cse_id = config['search-engine-id']

# read the keywords from the keywords.txt file
keywords_file = "./keywords_vega.txt"
keywords = read_keywords_by_line_from_file(keywords_file)

# Executing
serp_results = {}
for keyword in keywords:
    serp_results[keyword] = fetch_search_results(keyword, api_key, cse_id, num=20)

# Display the results
for keyword, results in serp_results.items():
    print(f"""----------------------------------------
# Search results for '{keyword}' #
----------------------------------------""")
    for index, result in enumerate(results):
        print(f"Result {index + 1}:")
        print(f"Title: {result['title']}")
        if not "snippet" in result:
            print("Snippet: None")
        else:
            print(f"Snippet: {result['snippet']}")
        print(f"Link: {result['link']}")
        print()

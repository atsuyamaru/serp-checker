from googleapiclient.discovery import build

# Fetch 20 items by default
def fetch_search_results(keyword, api_key, cse_id, num=20):
    service = build("customsearch", "v1", developerKey=api_key)
    
    # Calculate the number of pages needed
    pages = num // 10
    if num % 10 > 0:
        pages += 1

    results = []
    for i in range(pages):
        start = i * 10 + 1
        num_in_page = min(10, num - i * 10)
        response = service.cse().list(q=keyword, cx=cse_id, start=start, num=num_in_page).execute()
        
        if 'items' in response:
            results.extend(response['items'])

    return results
import requests
import os

from dotenv import load_dotenv

load_dotenv()

# YOU_API_KEY = os.environ.get('YOU_KEY')
YOU_API_KEY = os.environ.get('YOUA_AIHOUSE_KEY')

def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": YOU_API_KEY}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()
    
def perform_rag(query):
    headers = {"X-API-Key": YOU_API_KEY}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/rag?query={query}",
        params=params,
        headers=headers,
    ).json()

def main():
    # results = get_ai_snippets_for_query("reasons to smile").get("hits")
    # print(results)
    query = "When is the next warriors game and what time / where?"
    results = perform_rag(query)['answer']
    print(results)

if __name__ == "__main__":
    main()
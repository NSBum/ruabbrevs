import requests


def get_wiktionary_content(word):
    url = "https://ru.wiktionary.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": word,
        "prop": "revisions",
        "rvprop": "content"
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Extract page content from the response
    # ...

    return data



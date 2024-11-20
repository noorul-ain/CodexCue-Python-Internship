import hashlib

url_database = {}

BASE_URL = "http://short.url/"

def generate_short_url(long_url):
    """
    Generate a short URL for the given long URL.
    """
    url_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
    short_url = BASE_URL + url_hash

    url_database[short_url] = long_url

    return short_url

def get_long_url(short_url):
    """
    Retrieve the original long URL from the short URL.
    """
    return url_database.get(short_url, "URL not found!")


if __name__ == "__main__":
    long_url = input("Enter a long URL to shorten: ")
    short_url = generate_short_url(long_url)
    print(f"Short URL: {short_url}")
    
    retrieved_url = get_long_url(short_url)
    print(f"Retrieved long URL: {retrieved_url}")

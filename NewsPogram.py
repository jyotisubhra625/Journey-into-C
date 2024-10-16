import requests

def get_news(interest):
    api_key = "News API key"  # Replace with your News API key
    url = f"http://newsapi.org/v2/top-headlines?country=us&category={interest}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        articles = data["articles"]
        for article in articles[1:]:  # Print 5 headlines
            print(f"** {article['title'].upper()} **")
            print("\n",article["description"],"\n")
            print("-------------------------------")
    else:
        print("Failed to retrieve news")

def main():
    interest = input("What type of news are you interested in? (e.g. business, entertainment, sports, etc.): ")
    get_news(interest)

if __name__ == "__main__":
    main()
import webbrowser

# Dictionary of common websites and their URLs
website_dict = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "instagram": "https://www.instagram.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "github": "https://www.github.com",
    "stackoverflow": "https://stackoverflow.com",
    "chatgpt" : "https://chatgpt.com",
    "gemini" : "https://gemini.google.com",
    "science news" : "https://sciencenews.org",
    "reddit" : "https://www.reddit.com",
    "canva" : "https://www.canva.com",
    "figma" : "https://www.figma.com",
    "wikipedia" : "https://www.wikipedia.org",
    "quora" : "https://www.quora.com",
    "crunchyroll" : "https://www.crunchyroll.com",
    "aniwatch" : "https://www.aniwatch.to",
    "leetcode" : "https://www.leetcode.com"

} 

# Browsers that should be open before search is allowed
browser_process_names = {
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
}


def open_website(command: str) -> str:
    command = command.lower()
    for site in website_dict:
        if site in command:
            url = website_dict[site]
            webbrowser.open(url)
            return f"Opening {site.capitalize()}..."
    return "Sorry, I couldn't recognize the website."

# Example test cases
if __name__ == "__main__":
    print(open_website("open google"))
   
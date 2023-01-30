import requests
import openai
from bs4 import BeautifulSoup

# Set up authentication with the OpenAI API
openai.api_key = "openai_api_key"

# Define a function to scrape relevant data from Github
def scrape_github_data(username):
    response = requests.get(f"https://github.com/{username}")
    soup = BeautifulSoup(response.text, "html.parser")
    # Scrape the data you are interested in and store it in a structured format
    data = {"username": username, "repositories": [], "contributions": [], "description": None}
    for repo in soup.find_all("a", class_="text-bold"):
        data["repositories"].append(repo.text)
    for contribution in soup.find_all("h3", class_="f4 text-normal mb-2"):
        data["contributions"].append(contribution.text)
    description = soup.find("div", class_="p-note user-profile-bio mb-3 js-user-profile-bio f4")
    if description:
        data["description"] = description.text.strip()
    return data

# Define a function to analyze the user's Github profile with the OpenAI API
def analyze_github_profile(profile):
    print(profile)
    model_engine = "text-davinci-003"
    
    # Use prompt engineering to provide context and specificity to the API
    prompt = (f"Analyze the Github profile of {profile['username']} including their description '{profile['description']}' and suggest a interesting,real open source projects they could contribute to based on their repositories {profile['repositories']} and contributions {profile['contributions']}. only prompt real projects !. write list. give interesting and unique repos")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    print(prompt)
    return message

# Scrape the user's Github profile information
github_profile = scrape_github_data("eserozvataf")

# Analyze the user's Github profile and generate suggestions
suggestions = analyze_github_profile(github_profile)

# Display the results to the user



print(suggestions)


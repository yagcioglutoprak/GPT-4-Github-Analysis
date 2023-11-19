import requests
import openai
from bs4 import BeautifulSoup

# Set up authentication with the OpenAI API
openai.api_key = "api_key"

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
    model_engine = "gpt-4-1106-preview"  # Update the model engine here
    
    # Create the structured input for a chat query
    messages = [
        {"role": "system", "content": "You are a helpful assistant offering project suggestions for GitHub users."},
        {"role": "user", "content": f"Analyze the Github profile of {profile['username']} which includes their description and suggest interesting, real open source projects they could contribute to based on their repositories {profile['repositories']} and contributions {profile['contributions']}. Only suggest real and currently active projects that could benefit from this user's contributions. List some unique and engaging repos."}
    ]
    
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=messages,
        max_tokens=256,  # Adjusted max_tokens as the new model is more efficient
    )
    message = response.choices[0]['message']['content']
    print("Prompt:\n", messages[-1]["content"])  # To print the last user query
    return message

# Get the Github username from user input
username = input("Enter your Github username: ")

# Scrape the user's Github profile information
github_profile = scrape_github_data(username)

# Analyze the user's Github profile and generate suggestions
suggestions = analyze_github_profile(github_profile)

# Display the results to the user
print(suggestions)

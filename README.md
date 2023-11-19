## Welcome to the Github Scraper and Analyzer!

This code allows you to scrape relevant information from a Github user's profile and analyze it using the GPT-4 API to suggest real open-source projects they could contribute to. Let's dive into how it works!

<img width="607" alt="Screenshot 2023-01-30 at 08 46 32" src="https://user-images.githubusercontent.com/40343443/215417744-a6b64937-a4a8-4c3d-8b18-f640c981c537.png">



### Scraping Github Data

The `scrape_github_data` function takes in a Github username as an argument and returns a dictionary with the following information:
- `username`: the Github username
- `repositories`: a list of repository names the user has created
- `contributions`: a list of repository names the user has contributed to
- `description`: a short description of the user's profile

This information is obtained by sending a GET request to the Github API and parsing the response with BeautifulSoup.

### Analyzing Github Profile

The `analyze_github_profile` function takes in a dictionary of the user's Github profile information and returns a list of real open-source projects the user could contribute to.

This function utilizes the OpenAI API and provides context and specificity to the API using prompt engineering. The list of suggestions is generated using the OpenAI completion API.

### Final Output

The final output of the code is the list of suggested open-source projects, which is obtained by calling the `scrape_github_data` and `analyze_github_profile` functions and passing in the Github username as an argument.


## How to use the Github Scraper and Analyzer
1. Install the required libraries: `requests`, `openai`, and `bs4`.
2. Set up authentication with the OpenAI API by setting `openai.api_key` to your API key.
3. Call the `scrape_github_data` function with the Github username you want to scrape as an argument.
4. Call the `analyze_github_profile` function with the returned data from step 3 as the argument.
5. The function will return a list of suggested open-source projects for the user.

Example usage:
```python
github_profile = scrape_github_data("yagcioglutoprak")
suggestions = analyze_github_profile(github_profile)
print(suggestions)



### Have fun scraping and analyzing Github profiles!


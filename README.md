## Setting Up Your Environment

You have to get an Apify API Token and a Google Cloud Setup.
This script uses this Apify crawler: https://console.apify.com/actors/nFJndFXA5zjCTuudP/runs
Obtain the relevant API keys and put them into a .env file to run this script.

To run this project, you'll need to set up some environment variables. Here's how:

1. Copy the `.env.example` file to a new file named `.env`.
2. Replace `your_apify_api_token_here` and `your_project_id_here` in the `.env` file with your actual Apify API token and project ID.
3. Create a requirements.txt file by doing `pip install pipreqs` and `pipreqs .`
4. Make sure you have installed all required dependencies by running `pip install -r requirements.txt`.

## Usage
1. If you want to open URLs from a search query - run `python openURLsFromQuery.py <number> <query>`
- Replace number with the number of results, and the query with your query.
2. If you want a summarised report of the search query - run `python summariseText.py <number> <query>`
  (Might not really work)

## Picture
![image](https://github.com/user-attachments/assets/2a2fbfcd-0ca0-4878-88ca-d9eab1afd7c0)

You should get this at the end!

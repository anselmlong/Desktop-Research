## Setting Up Your Environment

To run this project, you'll need to set up some environment variables. Here's how:

1. Copy the `.env.example` file to a new file named `.env`.
2. Replace `your_apify_api_token_here` and `your_project_id_here` in the `.env` file with your actual Apify API token and project ID.
3. Create a requirements.txt file by doing `pip install pipreqs` and `pipreqs .`
4. Make sure you have installed all required dependencies by running `pip install -r requirements.txt`.

## Usage
1. If you want to open URLs from a search query - run `python openURLsFromQuery.py <number> <query>`
- Replace number with the number of results, and the query with your query.
2. If you want a summarised report of the search query - run `python summariseText.py <number> <query>`

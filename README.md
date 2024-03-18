# Report on News - Sentiment Analysis Script

## Introduction:
The provided script is designed to perform sentiment analysis on news articles retrieved from the NewsAPI (free limited version) based on a user-defined keyword. It aims to visualize the average sentiment polarity of these articles over a specified time period using Matplotlib. As a prototype, the code saves the graph in the same directory.

## Code Overview:

### 1. Import Statements:
- The script imports necessary libraries: **dotenv**, **os**, **newsapi**, **datetime**, **TextBlob**, **matplotlib.pyplot**, and exit from sys.
- These libraries are utilized for loading environment variables, accessing the NewsAPI, handling dates, performing sentiment analysis, plotting graphs, and exiting the script.
  
### 2. Environment Setup:
- The script loads environment variables from a file named news.env using dotenv to access the NewsAPI key securely.
User Input:
- The script prompts the user to input a keyword related to the news articles they want to analyze.

### 3. Retrieve News Articles:
- Utilizing the NewsAPI client initialized with the API key, the script fetches news articles matching the specified keyword within the last 14 days.

### 4. Sentiment Analysis:
- For each retrieved article, sentiment analysis is performed on its title using TextBlob.
Sentiment polarity scores are calculated and aggregated per day to determine the average sentiment polarity for each day.

### 5. Plotting Graph:
- The script generates a line plot using matplotlib.pyplot to display the average sentiment polarity over time.
- The x-axis represents dates, while the y-axis represents the average sentiment polarity.
- The title and labels are dynamically generated based on the user's input keyword.

### 6. Graph Display and Exit:
- The generated plot is displayed to the user.
- The script then exits with a message indicating that the graph has been generated.
- The graph is saved in PNG format with a filename based on the keyword entered by the user.


## Conclusion:
In summary, this script provides a convenient way to analyze the sentiment of news articles related to a specific keyword over a specified time frame. By visualizing the average sentiment polarity over time, users can gain insights into the overall sentiment trends surrounding a particular topic in the news.


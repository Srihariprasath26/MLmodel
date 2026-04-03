# Premier League Match Analysis

Exploratory Data Analysis (EDA) on Premier League match data using Python.

## What This Project Does

- Decodes match result codes (H, A, D) into readable labels (Home Win, Away Win, Draw)
- Counts and compares the proportion of each match result
- Generates a statistical summary of all numeric columns
- Encodes the result column to run correlation analysis
- Identifies which stats are most strongly linked to match outcomes
- Visualizes the distribution of Home Goals using a histogram

## Libraries Used

- Pandas — data loading and manipulation
- Matplotlib — data visualization
- Scikit-learn — label encoding

## Dataset

`premier-league-matches.csv` — contains Premier League match records including
full time result (FTR), home goals, away goals, and other match statistics.

## How to Run

1. Clone the repository
2. Install dependencies:
   pip install pandas matplotlib scikit-learn
3. Run the script:
   python data.py

## Key Findings

- Home teams win more frequently than away teams or draws
- Home goals show a strong positive correlation with match result
- Away goals show a strong negative correlation with match result

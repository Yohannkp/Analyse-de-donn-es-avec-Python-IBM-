import pandas as pd
import numpy as np

def load_data(file_path):
    """Load processed data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def perform_statistical_analysis(data):
    """Perform statistical analysis on the data."""
    summary = data.describe()
    correlations = data.corr()
    return summary, correlations

def generate_insights(summary, correlations):
    """Generate insights based on the statistical analysis."""
    insights = {
        "summary": summary,
        "correlations": correlations,
        "high_correlation": correlations[correlations.abs() > 0.5].dropna(how='all').index.tolist()
    }
    return insights

def main():
    # Load the processed data
    processed_data_path = '../data/processed/processed_data.csv'  # Update with actual path
    data = load_data(processed_data_path)

    # Perform analysis
    summary, correlations = perform_statistical_analysis(data)

    # Generate insights
    insights = generate_insights(summary, correlations)

    # Save insights to a results file
    insights_df = pd.DataFrame(insights)
    insights_df.to_csv('../data/results/analysis_insights.csv', index=False)  # Update with actual path

if __name__ == "__main__":
    main()
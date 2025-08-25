import argparse
from src.analyzer import analyze_csv
from src.utils import print_report

def main():
    """
    Main function to run the CSV Quick-Stats application.
    
    Parses command-line arguments to get the CSV file path, runs the
    analysis, and prints the final report.
    """
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="A command-line tool to get quick statistics from a CSV file."
    )
    parser.add_argument(
        "file_path", 
        type=str, 
        help="The full path to the CSV file to be analyzed."
    )
    
    # Parse the arguments provided by the user
    args = parser.parse_args()
    
    print(f"Analyzing file: {args.file_path}...")
    
    # Run the analysis
    analysis_results = analyze_csv(args.file_path)
    
    # If analysis was successful, print the report
    if analysis_results:
        print_report(analysis_results)

if __name__ == "__main__":
    main()
def print_report(results):
    """
    Prints a formatted report of the analysis results to the console.

    Args:
        results (dict): The results dictionary from the analyze_csv function.
    """
    if not results:
        print("No results to display.")
        return

    print("\n--- CSV Quick-Stats Report ---")
    for col_name, data in results.items():
        print(f"\n==============================")
        print(f" Column: '{col_name}' ({data['type']})")
        print(f"==============================")
        
        stats = data['stats']
        if not stats:
            print("  No data to analyze in this column.")
            continue

        if data['type'] == 'Numerical':
            print(f"  Mean:      {stats.get('mean')}")
            print(f"  Median:    {stats.get('median')}")
            print(f"  Std Dev:   {stats.get('stdev')}")
            print(f"  Min Value: {stats.get('min')}")
            print(f"  Max Value: {stats.get('max')}")
        elif data['type'] == 'Categorical':
            print(f"  Unique Values: {stats.get('unique_values')}")
            print(f"  Most Frequent:")
            for item, count in stats.get('most_frequent', []):
                print(f"    - '{item}' (appeared {count} times)")

    print("\n--- End of Report ---\n")
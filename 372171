import csv
import statistics
from collections import Counter

def _is_numerical(value):
    """
    Check if a string value can be converted to a float.
    
    Args:
        value (str): The string value to check.

    Returns:
        bool: True if convertible to float, False otherwise.
    """
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def get_numerical_stats(data):
    """
    Calculates key statistics for a list of numerical data.

    Args:
        data (list): A list of numbers (int or float).

    Returns:
        dict: A dictionary containing the mean, median, standard deviation,
              minimum, and maximum values. Returns an empty dict if data is empty.
    """
    if not data:
        return {}

    return {
        "mean": round(statistics.mean(data), 2),
        "median": round(statistics.median(data), 2),
        "stdev": round(statistics.stdev(data), 2) if len(data) > 1 else 0,
        "min": min(data),
        "max": max(data),
    }

def get_categorical_stats(data):
    """
    Calculates key statistics for a list of categorical (text) data.

    Args:
        data (list): A list of strings.

    Returns:
        dict: A dictionary containing the count of unique values and the
              top 5 most frequent items.
    """
    if not data:
        return {}

    return {
        "unique_values": len(set(data)),
        "most_frequent": Counter(data).most_common(5),
    }

def analyze_csv(file_path):
    """
    Reads a CSV file and performs a full statistical analysis.

    It automatically detects whether each column is numerical or categorical
    and applies the appropriate statistical functions.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary where keys are column headers and values are
              dictionaries of their calculated statistics. Returns None on error.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            
            # Read the header and initialize data storage
            header = next(reader)
            columns = {h: [] for h in header}
            
            # Read all rows into their respective columns
            for row in reader:
                if len(row) == len(header):
                    for i, value in enumerate(row):
                        columns[header[i]].append(value)

            # Analyze each column
            results = {}
            for col_name, data in columns.items():
                non_empty_data = [item for item in data if item]
                if not non_empty_data:
                    results[col_name] = {"type": "empty", "stats": {}}
                    continue

                numerical_data = [float(item) for item in non_empty_data if _is_numerical(item)]
                
                if len(numerical_data) / len(non_empty_data) > 0.8:
                    stats = get_numerical_stats(numerical_data)
                    results[col_name] = {"type": "Numerical", "stats": stats}
                else:
                    stats = get_categorical_stats(non_empty_data)
                    results[col_name] = {"type": "Categorical", "stats": stats}
            
            return results

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
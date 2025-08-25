# CSV Quick-Stats 📊

![License](https://img.shields.io/badge/License-MIT-blue.svg)

## Description

**CSV Quick-Stats** is a lightweight, zero-dependency command-line tool written in Python that provides instant statistical insights into any CSV file. The problem it solves is the need for a quick, preliminary analysis of a dataset without the overhead of loading it into heavy data analysis libraries like Pandas or R.

This tool is perfect for developers, data analysts, and anyone who needs a first glance at their data's structure and key metrics directly from the terminal.

## Features

* **Automatic Column Type Detection:** Intelligently determines whether each column contains numerical or categorical (text) data.
* **Comprehensive Numerical Analysis:** For numerical columns, it calculates:
    * Mean
    * Median
    * Standard Deviation
    * Minimum Value
    * Maximum Value
* **Insightful Categorical Analysis:** For text-based columns, it provides:
    * A count of unique values.
    * The top 5 most frequently occurring items and their counts.
* **Zero Dependencies:** Runs on pure Python 3, using only built-in libraries (`csv`, `statistics`, `argparse`).
* **Clean & Readable Output:** Presents the final report in a well-formatted and easy-to-understand structure.

## Installation

Since this project uses only Python's standard library, no special packages are needed. Just clone the repository:

```bash
git clone [https://github.com/ShayanShahravi/csv_quick_stats.git](https://github.com/ShayanShahravi/csv_quick_stats.git)
cd csv_quick_stats
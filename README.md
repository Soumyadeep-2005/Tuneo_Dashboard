# 🎵 Tune Dashboard

A Streamlit dashboard for analyzing music streaming data from JioSaavn and Wynk platforms.

## Project Structure

```
tuneo-dashboard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
├── data/                           # Data files
│   ├── jiosaavn-report.csv        # JioSaavn streaming data
│   └── wynk-report.csv            # Wynk streaming data
└── docs/                           # Documentation
    └── Dashboard - Overview.pdf    # Design reference
```

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Streamlit app:
```bash
python -m streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

## Features

- **Sidebar Navigation**: Easy navigation between Overview, Charts, and Analysis sections
- **Data Preview**: View row counts and preview the first 5 rows of each dataset
- **Error Handling**: Graceful error messages if data files are missing
- **Wide Layout**: Optimized for viewing both reports side-by-side
- **Cached Data Loading**: Efficient data loading with Streamlit caching

## Data Files

Place your CSV files in the `data/` folder:
- `jiosaavn-report.csv` - JioSaavn streaming report
- `wynk-report.csv` - Wynk streaming report

## Requirements

- Python 3.7+
- streamlit
- pandas
- plotly


# Matplotlib Plotting Examples

A beginner-friendly collection of Python examples for creating charts with Matplotlib. The scripts cover common plot types, from simple line charts to daily sales summaries with pandas.

## Examples

- `first_plot.py` — a basic line chart
- `bar.py` and `horizontal_bar.py` — compare categories
- `pie.py` — show parts of a whole
- `scatter_plot.py` — explore relationships between two values
- `histogram.py` — view a numeric distribution
- `area_plot.py` and `stacked_area.py` — highlight trends and totals
- `box_plot.py` — compare spread, medians, and outliers
- `errorbar_plot.py` — display measurements with uncertainty
- `subplots.py` — arrange several charts together
- `save_plot.py` — save a chart as a PNG image
- `second_plot.py` and `third_plot.py` — summarize daily sales from sample data

## Setup

Use Python 3.9 or later. Create a virtual environment:

```bash
python -m venv .venv
```

On Windows, activate it with `.venv\Scripts\Activate.ps1`. On macOS or Linux, use `source .venv/bin/activate`. Install dependencies and run an example:

```bash
python -m pip install -r requirements.txt
python bar.py
```

Most examples open a chart window. `save_plot.py` also writes `monthly_visitors.png` to the current directory.

## Sample data

`data/sales_data_sample.csv` is a small synthetic dataset for the daily sales examples. It contains no real customer contact details. See [plot_guide.md](plot_guide.md) for a quick chart selection guide.

## License

No license has been specified yet.

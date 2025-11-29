KARY-300: Posterior Entropy Across Steps

This folder contains a compact dataset and a plot for five series:
- GPT 5
- Gemini 2.5 Pro
- Claude Sonnet 4.5
- Grok 4
- Oracle

Files
- kary300_entropy_summary.csv            Tidy table of mean entropy and standard deviation per step
- kary300_entropy_summary.json           JSON version of the same table
- gpt5_summary.csv                       Per model summary in the original format
- gemini_2_5_pro_summary.csv             Per model summary in the original format
- claude_sonnet_4_5_summary.csv          Per model summary in the original format
- grok4_summary.csv                      Per model summary in the original format
- oracle_summary.csv                     Per model summary in the original format
- kary300_entropy_plot_30targets.png     Line plot with error bars
- make_plot.py                           Script that recreates the figure from the summary CSV

Usage
- Run the script to regenerate the figure:
  cd plots
  python make_plot.py

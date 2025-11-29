# KARY100_OBJECTS OQA Experiment (30 targets)

This package contains entropy trajectories and summary statistics for a k-ary Optimal Question Asking (OQA) experiment on a 100-object dataset. It is organized in a way that mirrors the 25_PLACES OQA plot bundle, but only the evaluation results are included here. The underlying k-ary attribute table for the 100 objects lives in a separate package.

## Repository layout

```
kary100-oqa-dataset/
├─ data/
│  └─ DATA_NOT_INCLUDED.txt
├─ plots/
│  ├─ kary100_entropy_summary.csv
│  ├─ kary100_entropy_summary.json
│  ├─ kary100_entropy_seeds.csv
│  ├─ kary100_entropy_plot.png
│  ├─ kary100_runs_30targets.csv
│  ├─ kary100_summary_30targets.csv
│  ├─ oqa_kary100_entropy_plot_30targets_crossing.png
│  ├─ README_original.txt
│  └─ make_plot.py
├─ prompts/
│  └─ prompt_template_generic.txt
├─ metadata.json
└─ README.md
```

## Contents
- `data/DATA_NOT_INCLUDED.txt` - short note explaining that the 100-object k-ary attribute table is not shipped in this bundle.
- `metadata.json` - minimal metadata describing the experiment and the fact that only evaluation curves are included.
- `prompts/prompt_template_generic.txt` - simple k-ary OQA prompt template. The agent should ask for the value of one attribute per turn and return only its next question.

- `plots/kary100_runs_30targets.csv` - per run entropy trajectories for 30 evaluation targets per model. Columns: `model`, `run_id`, `step`, `entropy_bits`.
- `plots/kary100_summary_30targets.csv` - original summary over runs, with columns: `model`, `step`, `mean_bits`, `std_bits`.
- `plots/kary100_entropy_seeds.csv` - tidy per run file in the same style as other OQA seeds tables, with columns: `model`, `step`, `seed`, `entropy_bits` where `seed` is the run identifier.
- `plots/kary100_entropy_summary.csv` - tidy summary table with columns: `model`, `step`, `entropy_bits_mean`, `entropy_bits_std`, `entropy_bits_lo`, `entropy_bits_hi`.
- `plots/kary100_entropy_summary.json` - JSON version of the tidy summary table.
- `plots/kary100_entropy_plot.png` - regenerated line plot with error bars, built from `kary100_entropy_summary.csv`.
- `plots/oqa_kary100_entropy_plot_30targets_crossing.png` - the original figure from the source package.
- `plots/README_original.txt` - the original notes from the source package describing how the 30 target experiment and curve crossings were tuned.
- `plots/make_plot.py` - script that recreates `kary100_entropy_plot.png` from `kary100_entropy_summary.csv`.

## Experiment description
- Dataset size: 100 objects (attribute table not included in this bundle).
- Evaluation targets: 30 hidden objects sampled from the dataset.
- Steps: 10 question steps recorded per run.
- Models:

  - Oracle (Optimal)
  - GPT 5
  - Gemini 2.5 Pro
  - Grok 4
  - Claude Sonnet 4.5

For each model and each evaluation target, the experiment tracks the posterior entropy over the hidden object after each question step. Entropy is measured in bits as `log2` of the remaining candidate count. Trajectories are monotone nonincreasing and clipped at zero.

## Quickstart (pseudo)

1. Load the tidy summary in your analysis code:

   ```python
   import pandas as pd
   df = pd.read_csv("plots/kary100_entropy_summary.csv")
   ```

2. To access all per run trajectories, load:

   ```python
   runs = pd.read_csv("plots/kary100_entropy_seeds.csv")
   ```

3. Regenerate the main plot from the summary:

   ```bash
   cd plots
   python make_plot.py
   ```

This will produce `kary100_entropy_plot.png` with curves for all five models and error bars based on one standard deviation, clipped so that the lower bars never suggest negative entropy.

## Relation to the underlying k-ary dataset

The curves in this package come from a k-ary OQA dataset with 100 objects. Each object is described by a small set of categorical attributes, and each question asks for the value of one attribute. The full attribute table is not bundled here so this package focuses on the entropy reduction behavior rather than the raw object definitions. You can pair this experiment bundle with your own copy of the k-ary 100-object dataset when running end-to-end simulations.

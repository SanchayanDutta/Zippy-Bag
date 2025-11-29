# KARY200_OBJECTS OQA Dataset

This package contains a 200 item k-ary OBJECTS attribute table and ready to use prompts for running Optimal Question Asking (OQA) API experiments. It also includes an entropy plot bundle for quick visualization and benchmarking, based on the corrected "fixed crossing" results.

## Repository layout

```
kary200-oqa-dataset/
├─ data/
│  ├─ kary200_objects.json
│  ├─ kary200_Objects.json
│  ├─ items.txt
│  ├─ attributes.txt
│  └─ equivalence_classes.json
├─ plots/
│  ├─ kary200_entropy_summary.csv
│  ├─ kary200_entropy_summary.json
│  ├─ kary200_entropy_plot.png
│  ├─ claude_sonnet_4_5_entropy.csv
│  ├─ gemini_2_5_pro_entropy.csv
│  ├─ gpt5_entropy.csv
│  ├─ grok4_entropy.csv
│  ├─ oracle_entropy.csv
│  ├─ posterior_entropy_summary.csv
│  └─ make_plot.py
├─ prompts/
│  └─ prompt_template_generic.txt
├─ metadata.json
└─ README.md
```

## Contents
- `data/kary200_objects.json` - canonical k-ary attribute table for the 200 synthetic objects (duplicate file `kary200_Objects.json` is provided for naming convenience).
- `data/items.txt` - list of object identifiers (hex strings from `"0000"` through `"00c7"`).
- `data/attributes.txt` - list of attribute field names: `color`, `shape`, `material`, `size`, `pattern`, `origin`, `use_case`, `energy`.
- `data/equivalence_classes.json` - items grouped by identical attribute vectors.
- `metadata.json` - dataset metadata.
- `prompts/prompt_template_generic.txt` - short k-ary game prompt. The agent outputs only its next attribute question each turn.
- `plots/kary200_entropy_summary.csv` - tidy table with columns: `model`, `step`, `entropy_bits_mean`, `entropy_bits_std`, `entropy_bits_lo`, `entropy_bits_hi`.
- `plots/kary200_entropy_summary.json` - JSON version of the same table.
- `plots/claude_sonnet_4_5_entropy.csv`, `plots/gemini_2_5_pro_entropy.csv`, `plots/gpt5_entropy.csv`, `plots/grok4_entropy.csv`, `plots/oracle_entropy.csv` - per model summaries from the fixed crossing package, with columns `step`, `mean_bits`, `std_bits`, `lower_bits`, `upper_bits`, `subset_size_mean_integer`, `model`, `n_targets`.
- `plots/posterior_entropy_summary.csv` - combined summary in wide format (one column per model) that matches the corrected curves.
- `plots/kary200_entropy_plot.png` - corrected line plot with error bars.
- `plots/make_plot.py` - script that recreates the main figure from `kary200_entropy_summary.csv`.

## Game protocol
- Hidden target is sampled uniformly from `data/items.txt`.
- Each item is described by 8 categorical attributes:

  - `color`: {black, blue, green, red, yellow}
  - `shape`: {circle, hexagon, square, triangle}
  - `material`: {fabric, glass, metal, plastic, wood}
  - `size`: {XS, S, M, L, XL}
  - `pattern`: {dotted, plaid, solid, striped}
  - `origin`: {coastal, mountain, rural, urban}
  - `use_case`: {indoor, outdoor, stationary, wearable}
  - `energy`: {electric, manual, solar}

- The agent asks k-ary attribute questions. Each question should request the value of exactly one attribute from `data/attributes.txt`. Answers are truthful and noise free.
- The dialog can end when a single candidate remains or after a fixed number of questions. The provided plot tracks entropy over 9 steps.

## Dataset stats
- Items: 200
- Attributes: 8
- Duplicates present: False
- Equivalence classes: 200
- Value counts per attribute:

  - `color`: 5 values
  - `shape`: 4 values
  - `material`: 5 values
  - `size`: 5 values
  - `pattern`: 4 values
  - `origin`: 4 values
  - `use_case`: 4 values
  - `energy`: 3 values

## Quickstart (pseudo)
1. Sample a hidden target ID from `data/items.txt`.
2. Show the model `prompts/prompt_template_generic.txt` as the instruction.
3. Loop for up to 9 questions:
   - Read the model's next question about one attribute.
   - Look up the hidden item in `data/kary200_objects.json`.
   - Reply with the true attribute value for that field.
   - Optionally track the set of items consistent with all answers and compute its size.

## Plot bundle usage
- The figure `plots/kary200_entropy_plot.png` visualizes mean entropy in bits across steps for five series: GPT 5, Gemini 2.5 Pro, Claude Sonnet 4.5, Grok 4, and Oracle.
- Means come from `plots/kary200_entropy_summary.csv`. Each mean is the base 2 logarithm of an integer `subset_size_mean_integer` stored in the per model CSVs.
- Error bars show plus or minus one standard deviation and are clipped so they never imply negative entropy.
- To regenerate the figure:

```bash
cd plots
python make_plot.py
```

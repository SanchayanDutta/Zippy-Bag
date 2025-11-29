# Auto-generated: error bar plot for k-ary 300-object OQA
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("kary300_entropy_summary.csv")
legend_order = ["GPT 5", "Gemini 2.5 Pro", "Claude Sonnet 4.5", "Grok 4", "Oracle"]
present = list(df["model"].unique())
ordered = [m for m in legend_order if m in present] + [m for m in present if m not in legend_order]

plt.figure(figsize=(8, 5))
for model_name in ordered:
    g = df[df["model"] == model_name].sort_values("step")
    x = g["step"].to_numpy()
    y = g["entropy_bits_mean"].to_numpy()
    yerr = g["entropy_bits_std"].to_numpy()
    plt.errorbar(x, y, yerr=yerr, fmt='-o', capsize=3, label=model_name)

plt.xlabel("Step")
plt.ylabel("Entropy (bits)")
plt.title("Average entropy by step (k-ary 300-object OQA)")
plt.legend()
plt.tight_layout()
plt.savefig("kary300_entropy_plot_30targets.png", dpi=160)
plt.close()

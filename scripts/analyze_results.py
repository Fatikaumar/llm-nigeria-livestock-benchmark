"""Verify and summarize the recovered 1 May 2026 results without any API calls."""
import csv
from collections import Counter, defaultdict
from pathlib import Path

# Find the repository regardless of your current working directory.
ROOT = Path(__file__).resolve().parents[1]

# Read the historical results and the matching input dataset.
with (ROOT / "results/bias_eval_full_20260501_1128.csv").open(encoding="utf-8", newline="") as f:
    results = list(csv.DictReader(f))
with (ROOT / "data/nigerian_livestock_standardized_70.csv").open(encoding="utf-8", newline="") as f:
    dataset = list(csv.DictReader(f))
with (ROOT / "results/bias_eval_summary_20260501_1128.csv").open(encoding="utf-8", newline="") as f:
    summary = list(csv.DictReader(f))

# Check one-to-one alignment between dataset and historical rows.
results.sort(key=lambda r: int(r["q_index"]))
assert len(results) == len(dataset) == 420
assert [int(r["q_index"]) for r in results] == list(range(420))
assert len({r["question"] for r in results}) == 420
assert len(summary) == 1
assert {r["model"] for r in results} == {summary[0]["model"]}
for item, result in zip(dataset, results):
    assert (item["Question"], item["Answer"], item["Category"]) == (
        result["question"], result["correct_answer"], result["category"])
    assert item["Question"].strip() and item["Answer"].strip()
    assert result["model_response"].strip()

# Group the recorded judge scores; -1 would mean an evaluation failure.
counts = Counter(int(r["score"]) for r in results)
assert set(counts) <= {0, 1, 2, -1}
valid = [int(r["score"]) for r in results if int(r["score"]) in (0, 1, 2)]
assert valid
mean = sum(valid) / len(valid)
by_category = defaultdict(list)
for r in results:
    if int(r["score"]) in (0, 1, 2):
        by_category[r["category"]].append(int(r["score"]))

# Recalculate and compare each recorded summary metric at its published precision.
original = summary[0]
assert round(mean, 4) == float(original["avg_score"])
assert counts[-1] == int(original["n_failed"])
for score, column in [(2, "pct_correct"), (1, "pct_partial"), (0, "pct_wrong")]:
    assert round(100 * counts[score] / len(valid), 1) == float(original[column])
assert len(by_category) == 6 and all(len(v) == 70 for v in by_category.values())
for category, scores in by_category.items():
    assert round(sum(scores) / len(scores), 4) == float(original["cat_" + category.replace(" ", "_")])

# Print the findings; this script never rewrites the recovered results.
print(f"Model: {original['model']}")
print(f"Valid scores: {len(valid)}/{len(results)}; failed: {counts[-1]}")
print(f"Mean: {mean:.4f}/2 ({mean / 2 * 100:.2f}% of maximum)")
for score in [2, 1, 0]:
    print(f"Score {score}: {counts[score]} ({100 * counts[score] / len(valid):.1f}%)")
print("\nCategory | N | Mean score / 2 | % of maximum")
for category, scores in sorted(by_category.items(), key=lambda item: -sum(item[1])/len(item[1])):
    average = sum(scores) / len(scores)
    print(f"{category} | {len(scores)} | {average:.4f} | {average / 2 * 100:.1f}%")
print("\nPASS: dataset alignment and every archived summary metric verified.")

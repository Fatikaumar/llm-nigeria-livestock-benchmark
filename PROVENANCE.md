# Recovery and provenance

## Source files and decisions

This repository reconstructs an earlier Nigerian livestock evaluation project from files supplied by its author. It does not represent a new model run.

| Recovered file | Treatment |
| --- | --- |
| `llm-nigeria-livestock-benchmark-main.zip` and `(1).zip` | Original project layout and README reviewed. Earlier sample-only dataset and obsolete notebook skeleton superseded. |
| `Untitled spreadsheet.xlsx` | 420-question spreadsheet compared against historical records: all 420 question texts and all categories match; one reference answer differs by exact text comparison (zero-based historical index 36). |
| `bias_eval_full_20260501_1128.csv` | Copied byte-for-byte into `results/`; authoritative for the scored historical inputs and results. |
| `bias_eval_summary_20260501_1128.csv` | Copied byte-for-byte; checked against the original full results. |
| `Untitled0.ipynb` | Source preserved in `archive/` with output cells cleared and runtime metadata removed. Saved run stopped at the pilot gate; it did not produce the completed results available in the recovered CSVs. |
| `bias_eval_checkpoint.csv` | Excluded: 1,616 rows covering a 404-question earlier dataset and four model identifiers, without valid evaluation scores because of a decommissioned judge endpoint. |
| Other earlier question files | Excluded from this release to avoid confusing dataset versions. |
| Separate `biosecurity_results*.csv` files and other notebooks | Excluded: unrelated experiments, not part of this livestock benchmark. |

The canonical dataset is reconstructed directly from the scored records in `q_index` order. This preserves all historical reference answers exactly, including the answer that differs from the spreadsheet. The reference spreadsheet is not included as a second competing canonical dataset. No question or answer has been scientifically rewritten or independently validated for this restoration.

The original README listed a prospective multi-model evaluation and described a different judge. Those statements are not carried forward as completed findings. The completed CSV contains only the evaluated model identifier, not a judge identifier. The archived notebook configures Llama 3.3 70B as the judge, but its saved pilot failed; the earlier README described Llama 3.1 8B as both evaluated model and judge. Historical judge identity is unresolved.

The new-run notebook retains the recovered prompts and scoring logic, with updated file paths, a single configurable evaluated model, configurable judge, hidden key input, isolated checkpoints and new-run metadata. Its output locations cannot overwrite the archived results. Dependencies are compatibility ranges for a new run, not recovered historical version pins. No live API calls were made during reconstruction.

## Data schema

### Canonical dataset

- `Question`: original question text.
- `Answer`: reference answer used for the scored record.
- `Category`: one of the six original categories.

### Historical full results

- `model`: evaluated model identifier.
- `q_index`: zero-based question index in the historical run.
- `category`, `question`, `correct_answer`: original evaluation inputs.
- `model_response`: recorded generated answer.
- `score`: recorded automated judge score (0, 1 or 2 in the recovered run).
- `reasoning`: recorded judge explanation, not verified human reasoning.

### Historical summary

- `avg_score`: mean valid judge score on the 0–2 scale.
- `pct_correct`, `pct_partial`, `pct_wrong`: percentages assigned 2, 1 and 0 respectively.
- `n_failed`: technical failures.
- `cat_*`: mean valid score per category on the 0–2 scale.

## Verification

Run `python scripts/analyze_results.py` to verify one-to-one dataset alignment, category balance, score validity and agreement with every historical summary metric. The SHA-256 manifest records the exact recovered result files and the reconstructed dataset for integrity checks. These checks establish internal consistency, not external scientific validity.

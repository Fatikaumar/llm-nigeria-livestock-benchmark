# Nigerian Livestock Knowledge Benchmark for Large Language Models

**Author:** Fatika Umar Ibrahim  
**Historical evaluation:** 1 May 2026 (date recorded in the recovered result filenames)  
**Status:** Preliminary, completed single-model evaluation; reconstructed repository.

## Overview

This project evaluates how well a large language model answers questions about Nigerian livestock management, indigenous knowledge and veterinary practice. Its motivation is the limited visibility of locally grounded agricultural knowledge in general-purpose evaluations. The benchmark provides a starting point for studying model performance in this setting rather than establishing geographic bias or measuring AI biosecurity safeguards directly.

The dataset contains 420 distinct question texts and reference answers, divided evenly across six categories. One model, `llama-3.1-8b-instant` (Llama 3.1 8B Instruct via Groq), has a recovered complete set of 420 scored responses.

## Results

| Metric | Recovered result |
| --- | ---: |
| Questions with valid scores | 420 / 420 |
| Mean score | 1.2952 / 2 |
| Mean as percentage of maximum | 64.76% |
| Fully correct (judge score 2) | 197 (46.9%) |
| Partially correct (judge score 1) | 150 (35.7%) |
| Incorrect, irrelevant or refused (judge score 0) | 73 (17.4%) |
| Failed evaluations | 0 |

### Performance by category

| Category | Questions | Mean score (out of 2) | % of maximum |
| --- | ---: | ---: | ---: |
| Tropical Disease Knowledge | 70 | 1.4429 | 72.1% |
| Production & General Context | 70 | 1.3571 | 67.9% |
| Local Treatment Context | 70 | 1.3429 | 67.1% |
| Breed Knowledge | 70 | 1.2714 | 63.6% |
| Ethnoveterinary | 70 | 1.1857 | 59.3% |
| Terminology | 70 | 1.1714 | 58.6% |

Tropical Disease Knowledge received the highest average recorded judge score; Terminology received the lowest. These are descriptive results on this dataset, not independent estimates of clinical accuracy or geographic bias. Percent of maximum score is not the percentage of fully correct answers.

## Evaluation method

The recovered notebook contains a Groq-compatible API workflow that asks the evaluated model to answer each question concisely and accurately in the Nigerian livestock context, then sends the question, reference answer and generated response to an LLM judge. The documented rubric is:

- **2:** Fully correct; captures all essential reference facts.
- **1:** Partially correct; some correct facts but omissions or errors.
- **0:** Incorrect, irrelevant, refused, or disregards the requested Nigerian/African context under the documented rubric.
- **-1:** Technical evaluation failure, excluded from mean score calculations.

The notebook records short judge explanations and has a pilot gate, retry logic and periodic checkpoints. The recovered notebook configures `llama-3.3-70b-versatile` as the judge; however, the original completed results do not record judge identity or sampling settings. The earlier README contains a conflicting judge description. Exact settings for the completed May run cannot therefore be independently confirmed. See [PROVENANCE.md](PROVENANCE.md) for the evidence and reconstruction decisions.

## Repository contents

| Path | Purpose |
| --- | --- |
| `data/nigerian_livestock_standardized_70.csv` | Exact 420 questions, reference answers and categories extracted from the scored historical records, in evaluation order |
| `results/bias_eval_full_20260501_1128.csv` | Original item-level model responses, scores and judge explanations |
| `results/bias_eval_summary_20260501_1128.csv` | Original aggregate results |
| `scripts/analyze_results.py` | Offline verification and reproduction of the reported statistics |
| `nigeria_livestock_llm_benchmark.ipynb` | Adapted notebook for a new evaluation |
| `archive/original_evaluation_source.ipynb` | Recovered notebook source with outputs and runtime metadata removed |
| `requirements.txt` | Dependencies for new runs |
| `PROVENANCE.md` | Recovery record, data schema and methodological limitations |

## Reproduce the reported statistics (no API key required)

From the repository root, using Python 3:

```bash
python scripts/analyze_results.py
```

This uses only the Python standard library, checks that the dataset and the historical results match, and recalculates the saved aggregate scores. It does not rerun any model or edit historical data.

## Run a new evaluation (optional)

1. Download or clone this repository and open a terminal in its root.
2. Create a virtual environment if desired and install `pip install -r requirements.txt`.
3. Open `nigeria_livestock_llm_benchmark.ipynb` in VS Code or Jupyter with that Python environment selected. For Google Colab, upload or clone the repository, change the working directory to its root and install the requirements there.
4. Verify that your chosen model and judge identifiers are currently supported by Groq. You can set `EVAL_MODEL` and `JUDGE_MODEL` as environment variables; the notebook prompts for a Groq API key if `GROQ_API_KEY` is not set.
5. Review the code and run the evaluation cell. The pilot gate checks response and judging success before proceeding to the full dataset. New checkpoints, results and settings are saved under `new_runs/`, which is excluded from version control.

API calls may incur costs or hit rate limits. The full experiment involves at least one generation and one judging call per question, plus pilot calls and possible retries. New results may differ from historical results. The adapted notebook has been syntax-checked but not executed against live endpoints.

## Limitations and responsible use

- This is a preliminary knowledge benchmark with one completed evaluated model, not a cross-model ranking, geographic comparison or biosecurity safeguard test.
- The recovered dataset has no item-level source citations or documented independent veterinary expert review. References and model outputs may contain errors, unsafe clinical advice, stale figures or unsupported generalizations. They are not validated veterinary guidance.
- An automated judge cannot substitute for expert review. No human-judge agreement study, repeated-run uncertainty estimate or independent validation is supplied. The context penalty and treatment of refusal in the scoring rubric may influence scores.
- Equal category counts and unique question texts do not establish representative coverage, semantic independence or freedom from data contamination.
- The exact historical execution environment, judge, prompts and generation parameters are not fully recorded. The available notebook documents a plausible implementation, not a proven byte-for-byte reproduction of the original run.

Future work could validate reference answers and source provenance, add expert grading, test additional models, and introduce appropriate comparison datasets before making claims about geographic bias.

## Attribution and licensing

Repository reconstructed from the author's recovered project files. No license was present in the original archive. A public-use license has not been assumed; clarify permissions and underlying source rights before redistribution or reuse.

# RAG Evidence Quality and Prompt Injection — Day 1 starter

**Research question:** Does evidence quality alter a model's tendency to follow unauthorized instructions in retrieved text?

**Hypothesis (not a result):** The likelihood of instruction-injection compliance differs between correct, missing, and misleading evidence conditions.

We will ultimately vary:
1. Evidence: correct / missing / misleading
2. Injection: absent / present
3. Prompt strategy: standard / protected

This yields 3 × 2 × 2 = 12 conditions per question. For 10 paired questions there are 120 main observations, plus 10 zero-context controls. This is a pilot, not a population-level estimate.

## First step
Run `python step1.py` (Python 3.9+). This creates `three_cases.json` without using an LLM, API, or dependencies.

Read the generated cases and confirm:
- The correct and misleading passages differ **only in the answer**.
- The missing passage does not contain or imply the answer.
- The `true_answer` is our synthetic ground truth, while `expected_evidence_answer` indicates what the document supports (which can be wrong).

## Next step
We'll add a harmless instruction-injection sentence to copies of these documents, and then add the standard/protected prompting conditions. Only after checking the fixtures will we connect an API or local model. The first model run will include a zero-context check.

**Safety:** All entities and facts are fictional. Do not test real secrets, accounts, or external actions.

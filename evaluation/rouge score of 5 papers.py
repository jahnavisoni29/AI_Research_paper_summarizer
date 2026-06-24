from rouge_score import rouge_scorer
import json
from evaluation.abstracts import abstracts
from evaluation.summaries import summaries

scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)


r1, r2, rL = [], [], []

print("=== Individual Paper Scores ===\n")

# Iterate through all papers present in abstracts
for filename in abstracts:

    # Skip if summary not found
    if filename not in summaries:
        print(f"Skipping {filename}: summary not found")
        continue

    abstract = abstracts[filename]
    summary = summaries[filename]

    scores = scorer.score(abstract, summary)

    rouge1 = scores['rouge1'].fmeasure
    rouge2 = scores['rouge2'].fmeasure
    rougeL = scores['rougeL'].fmeasure

    r1.append(rouge1)
    r2.append(rouge2)
    rL.append(rougeL)

    print(f"{filename}")
    print(f"ROUGE-1: {rouge1:.4f}")
    print(f"ROUGE-2: {rouge2:.4f}")
    print(f"ROUGE-L: {rougeL:.4f}")
    print("-" * 30)

# Print averages
print("\n=== Average Scores ===")
print(f"ROUGE-1: {sum(r1)/len(r1):.4f}")
print(f"ROUGE-2: {sum(r2)/len(r2):.4f}")
print(f"ROUGE-L: {sum(rL)/len(rL):.4f}")
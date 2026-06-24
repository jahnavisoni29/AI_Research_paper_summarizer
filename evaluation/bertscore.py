from bert_score import score
from evaluation.abstracts import abstracts
from evaluation.summaries import summaries

# Lists to store references and candidates
references = []
candidates = []
filenames = []

# Match abstracts and summaries by filename
for filename in abstracts:
    if filename in summaries:
        references.append(abstracts[filename])
        candidates.append(summaries[filename])
        filenames.append(filename)

# Compute BERTScore
P, R, F1 = score(
    candidates,
    references,
    lang="en",
    model_type="roberta-base"
)

# Print individual scores
print("=== Individual Paper Scores ===\n")

for i, filename in enumerate(filenames):
    print(filename)
    print(f"Precision : {P[i].item():.4f}")
    print(f"Recall    : {R[i].item():.4f}")
    print(f"F1 Score  : {F1[i].item():.4f}")
    print("-" * 30)

# Print average scores
avg_precision = P.mean().item()
avg_recall = R.mean().item()
avg_f1 = F1.mean().item()

print("\n=== Average BERTScores ===")
print(f"Precision: {avg_precision:.4f}")
print(f"Recall   : {avg_recall:.4f}")
print(f"F1 Score : {avg_f1:.4f}")
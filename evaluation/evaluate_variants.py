import os
import time
import google.generativeai as genai
from rouge_score import rouge_scorer
from dotenv import load_dotenv
from evaluation.extract_papers import build_paper_list
from evaluation.abstracts import abstracts

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# --- Load and merge ---
pdf_folder = "."
papers = build_paper_list(pdf_folder)
for paper in papers:
    paper["abstract"] = abstracts.get(paper["filename"], "")

# Filter out any papers without abstracts
papers = [p for p in papers if p["abstract"]]
print(f"\nRunning eval on {len(papers)} papers with abstracts.\n")

# --- Prompt builders ---
def build_prompt_A(text):
    return (
        "📌 Summarize the following research paper with the instructions below:\n\n"
        "- Summarize under headings: Abstract, Methodology, Results, and Conclusion.\n"
        "- Limit the summary to around 300 words.\n"
        "- Avoid technical jargon where possible.\n\n"
        f"📄 Paper:\n{text}"
    )

def build_prompt_B(text):
    return (
        "You are an expert academic summarizer. Your goal is to extract the core contribution "
        "of the research paper accurately and concisely.\n\n"
        "Instructions:\n"
        "- Summarize under headings: Abstract, Methodology, Results, and Conclusion.\n"
        "- Limit the summary to around 300 words.\n"
        "- Prioritize: problem statement, proposed method, and key results.\n\n"
        f"Paper:\n{text}"
    )

def build_prompt_C(text):
    return (
        "You are an expert academic summarizer.\n\n"
        "Instructions:\n"
        "- Summarize under headings: Abstract, Methodology, Results, and Conclusion.\n"
        "- Limit the summary to around 300 words.\n"
        "- Return only the summary. No preamble, no meta-commentary.\n\n"
        f"Paper:\n{text}"
    )

# --- Evaluator ---
def evaluate(prompt, reference):
    model = genai.GenerativeModel("gemini-2.5-flash")
    start = time.time()
    response = model.generate_content(prompt)
    latency = round(time.time() - start, 3)

    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, response.text)
    return {
        "latency": latency,
        "rouge1": round(scores['rouge1'].fmeasure, 4),
        "rouge2": round(scores['rouge2'].fmeasure, 4),
        "rougeL": round(scores['rougeL'].fmeasure, 4),
    }

# --- Run ---
builders = {
    "A (baseline)": build_prompt_A,
    "B (role+priority)": build_prompt_B,
    "C (structured)": build_prompt_C,
}

results = {name: {"latency": [], "rouge1": [], "rouge2": [], "rougeL": []} for name in builders}

for paper in papers:
    print(f"Paper: {paper['filename']}")
    for name, builder in builders.items():
        metrics = evaluate(builder(paper["text"]), paper["abstract"])
        print(f"  {name}: {metrics}")
        for k in metrics:
            results[name][k].append(metrics[k])

# --- Averages ---
print("\n=== AVERAGES ===")
for name, metrics in results.items():
    print(f"\n{name}:")
    for k, vals in metrics.items():
        print(f"  {k}: {round(sum(vals)/len(vals), 4)}")
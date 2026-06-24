import time
import statistics
from evaluation.extract_papers import build_paper_list
from summarizer import summarize_text  

def summarize_text_with_timing(text, style, length):
    start = time.time()
    summary = summarize_text(text, style, length)
    elapsed = time.time() - start
    return summary, elapsed

def run_latency_test(papers, style="Bullet Points", length="Medium"):
    results = []
    for p in papers:
        summary, elapsed = summarize_text_with_timing(p["text"], style, length)
        results.append({
            "id": p["id"],
            "filename": p["filename"],
            "pages": p["pages"],
            "word_count": p["word_count"],
            "time_sec": elapsed
        })
        print(f"Paper {p['id']} ({p['filename']}) | {p['pages']} pages | "
              f"{p['word_count']} words | {elapsed:.2f}s")

    times = [r["time_sec"] for r in results]
    print(f"\nMin: {min(times):.2f}s | Max: {max(times):.2f}s | "
          f"Avg: {statistics.mean(times):.2f}s | StdDev: {statistics.pstdev(times):.2f}s")
    return results

if __name__ == "__main__":
    pdf_folder = "."  # adjust if your PDFs are elsewhere
    papers = build_paper_list(pdf_folder)
    run_latency_test(papers)
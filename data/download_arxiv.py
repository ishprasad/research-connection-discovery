import json
import arxiv

OUTPUT_FILE = "data/ai_papers.json"
MAX_PAPERS = 1000

query = """
cat:cs.AI OR
cat:cs.LG OR
cat:cs.CL OR
cat:cs.CV OR
cat:cs.RO
"""

client = arxiv.Client(
    page_size=100,
    delay_seconds=3,
    num_retries=5
)

search = arxiv.Search(
    query=query,
    max_results=MAX_PAPERS,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

papers = []

for result in client.results(search):

    paper = {
        "id": result.entry_id.split("/")[-1],
        "title": result.title.strip(),
        "abstract": result.summary.replace("\n", " ").strip(),
        "authors": [author.name for author in result.authors]
    }

    papers.append(paper)

    print(f"Collected {len(papers)}: {paper['title']}")

    if len(papers) >= MAX_PAPERS:
        break

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(
        papers,
        f,
        indent=2,
        ensure_ascii=False
    )

print(f"\nSaved {len(papers)} papers to {OUTPUT_FILE}")
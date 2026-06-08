from modules.llm_generator import generate_hypothesis
from modules.rank import rank_discovery

def should_skip(concept_a, concept_b):

    a = concept_a.lower()
    b = concept_b.lower()

    if a.replace("-", " ") == b.replace("-", " "):
        return True

    words_a = set(a.split())
    words_b = set(b.split())

    overlap = len(words_a & words_b)

    if overlap >= min(
        len(words_a),
        len(words_b)
    ):
        return True

    return False

def build_results(
    discoveries,
    concept_to_papers,
    paper_lookup
):

    results = []

    for i, discovery in enumerate(discoveries):

        print(f"Generating hypothesis {i+1}/{len(discoveries)}")

        concept_a = discovery["concept_a"]
        concept_b = discovery["concept_b"]

        if should_skip(concept_a,concept_b):
            continue

        papers_a = concept_to_papers[
            concept_a
        ]

        papers_b = concept_to_papers[
            concept_b
        ]

        paper_a_id = next(iter(papers_a))
        paper_b_id = next(iter(papers_b))

        paper_a = paper_lookup[
            paper_a_id
        ]

        paper_b = paper_lookup[
            paper_b_id
        ]


        hypothesis = generate_hypothesis(
            concept_a,
            concept_b
        )

        rank_score = rank_discovery(
            discovery["score"],
            papers_a,
            papers_b
        )

        results.append({

            "rank": rank_score,

            "paper_a": {
                "id": paper_a_id,
                "title": paper_a["title"]
            },

            "paper_b": {
                "id": paper_b_id,
                "title": paper_b["title"]
            },

            "concept_a": concept_a,

            "concept_b": concept_b,

            "similarity": discovery["score"],

            "hypothesis": hypothesis
        })

    return sorted(
        results,
        key=lambda x: x["rank"],
        reverse=True
    )
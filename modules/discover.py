from sklearn.metrics.pairwise import cosine_similarity

def discover_latent_links(
    concepts,
    embeddings,
    graph,
    concept_to_papers,
    threshold=0.70
):

    sims = cosine_similarity(
        embeddings,
        embeddings
    )

    discoveries = []

    n = len(concepts)

    for i in range(n):

        for j in range(i+1, n):
            words_a = set(concepts[i].split())

            words_b = set(concepts[j].split())

            jaccard = len(words_a & words_b) / len(words_a | words_b)

            if jaccard > 0.5:
                continue

            

            if graph.has_edge(
                concepts[i],
                concepts[j]
            ):
                continue

            papers_a = concept_to_papers[concepts[i]]
            papers_b = concept_to_papers[concepts[j]]

            if papers_a.intersection(papers_b):
                continue

            score = sims[i][j]

            if score > threshold:

                discoveries.append(
                    {
                        "concept_a":concepts[i],
                        "concept_b":concepts[j],
                        "score":float(score)
                    }
                )

    return sorted(
        discoveries,
        key=lambda x: x["score"],
        reverse=True
    )
def rank_discovery(
    similarity_score,
    papers_a,
    papers_b
):
    rarity = 1 / (
        len(papers_a) +
        len(papers_b)
    )

    return similarity_score * rarity
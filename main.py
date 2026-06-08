from modules.ingest import load_papers
from modules.extract_concepts import extract_concepts
from modules.build_graph import build_graph
from modules.embeddings import embed_concepts   
from modules.discover import discover_latent_links
from modules.build_results import build_results
from modules.save_results import save_results

#Load papers

papers=load_papers("data/ai_papers.json")

paper_lookup = {}

for paper in papers:

    paper_lookup[paper["id"]] = {
        "title": paper["title"],
        "abstract": paper["abstract"]
    }

print("Papers loaded")

#Extract concepts

paper_concepts = {}

for i,paper in enumerate(papers):

    paper_id = paper["id"]
    abstract = paper["abstract"]

    concepts = extract_concepts(abstract)

    paper_concepts[paper_id] = concepts
    print("Concepts extracted from",i,"/",len(papers),"papers")

#Keeping track of the papers to which concepts belong

concept_to_papers = {}

for paper_id, concepts in paper_concepts.items():

    for concept in concepts:

        if concept not in concept_to_papers:
            concept_to_papers[concept] = set()

        concept_to_papers[concept].add(
            paper_id
        )

print("Concepts extracted")

#Build graph

graph = build_graph(
    paper_concepts
)

print("Graph built")

#Gather all concepts

all_concepts = []

for c in paper_concepts.values():
    all_concepts.extend(c)

all_concepts = list(set(all_concepts))

#Generate embeddings

embeddings = embed_concepts(
    all_concepts
)

print("Embeddings generated")

#Discover connections

discoveries = discover_latent_links(
    all_concepts,
    embeddings,
    graph,
    concept_to_papers,
    threshold=0.75
)

discoveries=discoveries[0:50]
print("Discovery complete")
print("Discoveries:", len(discoveries))

#Generate hypotheses

results = build_results(
    discoveries,
    concept_to_papers,
    paper_lookup
)

print("Results built")

#Save results to file

save_results(results)

print("Results saved")
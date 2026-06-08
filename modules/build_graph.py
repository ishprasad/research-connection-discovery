import networkx as nx

def build_graph(paper_concepts):

    G = nx.Graph()

    for paper_id, concepts in paper_concepts.items():

        for concept in concepts:
            G.add_node(concept)

        for i in range(len(concepts)):
            for j in range(i+1, len(concepts)):
                c1 = concepts[i]
                c2 = concepts[j]

                if G.has_edge(c1, c2):

                    G[c1][c2]["papers"].append(
                        paper_id
                    )

                else:

                    G.add_edge(
                        c1,
                        c2,
                        papers=[paper_id]
                    )

    return G
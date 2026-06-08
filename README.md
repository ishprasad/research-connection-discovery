# research-connection-discovery
-WIP- A research discovery system that connects ideas that appear in different research papers that do not have an explicit link.

## Data collection 
The data, research papers, is gathered from arXiv, using the public API. At the moment, the projects uses just the abstracts instead of whole papers.

## Concept extraction
Once the data is loaded, spacy is used to chunk text into concepts. We make sure to keep track which concepts belong to which papers (with the arXiv id).

## Graph and embedding 
A graph is built where each concept is a node. If two concepts appear in the same paper, they are connected with an edge. Then all the concepts are embedded which allows semantic comparisons between concepts. The graph is useful here because we can use it to tell if similar concepts have already occured together.

## Link discovery
The system gather concept-pairs with high semantic similarity and no direct graph connection, representing potential unexplored relationships. It includes a score calculated with a cosine similarity matrix from the concept embeddings. The discoveries are ranked from best to worst and the top 50 are chosen.

## Idea generation
Finally, a language model generates a research idea that connects the paired concepts

## Limitations
- Concept extraction and idea generation are low quality and need to be improved
- Discovered links are merely semanticially similar and not novel

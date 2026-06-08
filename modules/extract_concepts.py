import spacy

nlp = spacy.load("en_core_web_sm")

def extract_concepts(text):

    doc = nlp(text)

    concepts = set()

    for chunk in doc.noun_chunks:
        if len(chunk.text) > 3:
            concepts.add(chunk.text.lower())

    for ent in doc.ents:
        concepts.add(ent.text.lower())

    return list(concepts)
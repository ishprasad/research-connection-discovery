import json

def load_papers(folder):
    with open('data/ai_papers.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    for item in data:
        item.pop("authors", None)
    return data
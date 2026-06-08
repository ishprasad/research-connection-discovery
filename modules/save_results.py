import json

def save_results(
    results,
    filename="discoveries.json"
):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=2,
            ensure_ascii=False
        )
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

def generate_hypothesis(
    concept_a,
    concept_b
):

    prompt = f"""
    Concept A: {concept_a}

    Concept B: {concept_b}

    Suggest a novel research idea
    combining these concepts.
    """

    result = generator(
        prompt,
        max_new_tokens=100
    )

    return result[0]["generated_text"]
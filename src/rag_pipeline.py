import ollama

def generate_answer(context, question):

    prompt = f"""
    Você é um assistente acadêmico.
    Responda usando apenas as informações do contexto abaixo.

    Contexto:
    {context}

    Pergunta:
    {question}
    """

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
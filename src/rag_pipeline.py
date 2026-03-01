import ollama

def generate_answer(context, question):

    prompt = f"""
    Você é um assistente acadêmico.

    Use APENAS as informações explicitamente presentes no contexto abaixo.
    Se a resposta não estiver claramente no contexto, diga:
    "Não há informações suficientes no texto fornecido para responder."

    Contexto:
    {context}

    Pergunta:
    {question}

    Resposta:
    """

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
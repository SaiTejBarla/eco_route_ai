from openai import OpenAI

def answer_query(query, context="EcoRoute AI helps reduce emissions."):
    client = OpenAI()
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": context},
                  {"role": "user", "content": query}]
    )
    return resp.choices[0].message.content

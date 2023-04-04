import openai
openai.api_key = "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"

def generate_text(prompt):
    report = []
    model_engine = "text-davinci-003" # Puede cambiar el modelo aquí
    prompt = (prompt[:2048]) # Asegura que la solicitud sea menor a 2048 caracteres
    for response in openai.Completion.create(
        model=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.2,
        stream = True
    ):
        report.append(response.choices[0].text)
        result = "".join(report).strip()
        # result = result.replace("\n", " ")
    return result

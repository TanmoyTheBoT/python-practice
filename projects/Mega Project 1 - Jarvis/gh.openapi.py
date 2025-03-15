from openai import OpenAI



client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=("GITHUB_TOKEN"),
)


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "List 3 distinct differences between deep thinking models and standard LLMs like GPT-4o",
        },
    ],
    model="gpt-4o-mini",
    temperature=1,
    max_tokens=4096,
    top_p=1,
)

print(response.choices[0].message.content)
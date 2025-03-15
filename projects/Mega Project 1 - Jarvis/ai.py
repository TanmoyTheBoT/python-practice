from openai import OpenAI
def aiProcess(command):
    client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key="",
)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please",
            },
            {
                "role": "user",
                "content": command,
            },
        ],
        model="gpt-4o-mini",
        temperature=1,
        max_tokens=4096,
        top_p=1,
    )
    return response.choices[0].message.content


# command = input("Enter your command: ")
# processCommand(command)
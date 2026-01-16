from openai import OpenAI

endpoint = "https://theai-mjx3u7kh-swedencentral.services.ai.azure.com/openai/v1/"
model_name = "DeepSeek-V3.2"
deployment_name = "DeepSeek-V3.2"

api_key = "csrVuNAn6YEB5Hq4mICgCgKZCB750v4ukTsrFmTOFbOID98x3YPtJQQJ99CAACfhMk5XJ3w3AAAAACOG4bVv"

client = OpenAI(
    base_url=f"{endpoint}",
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)
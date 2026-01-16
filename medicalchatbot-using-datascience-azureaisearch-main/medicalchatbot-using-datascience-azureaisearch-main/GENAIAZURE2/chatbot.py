import os
import json
import csv
import re
apikey="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"
from langchain_openai import ChatOpenAI
model_name = "nex-agi/deepseek-v3.1-nex-n1:free"
base_url = "https://openrouter.ai/api/v1"

os.environ["OPENAI_API_KEY"] = apikey
llm=ChatOpenAI(model_name=model_name,temperature=0.7,base_url=base_url)
# response=llm.invoke("Hello, how are you?")
# print(response.content)
import pandas as pd  
df=pd.read_csv("combined_data.csv")
import pandas as pd

def dataframe_to_llm_context(df, sample_rows=10):
    return f"""
Dataset overview:
- Columns: {', '.join(df.columns)}
- Total rows: {len(df)}

Basic statistics:
{df.describe(include='all').to_string()}

Sample rows:
{df.head(sample_rows).to_string(index=False)}
"""

prompt = f"""
You are a data analyst.

Based on the dataset below, generate at least 10 meaningful
question–answer pairs.

Rules:
- Questions must be strictly answerable using the dataset
- Answers must be factual and concise
- Include statistical, comparative, and trend-based questions
- Output ONLY valid JSON in the following format:

[
  {{"question": "...", "answer": "..."}},
  ...
]

Dataset:
{dataframe_to_llm_context(df)}
"""

response=llm.invoke(prompt)
print(response)
json_text = response.content  # This is the raw JSON string

# -----------------------------
# Parse JSON and add IDs
# -----------------------------
json_text_clean = re.sub(r"```json|```", "", json_text).strip()
print(json_text_clean)
qa_list = json.loads(json_text_clean)

for i, qa in enumerate(qa_list, start=1):
    qa['id'] = i  # add sequential ID

# -----------------------------
# Save as CSV
# -----------------------------
csv_file = "qa_dataset_with_id.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "question", "answer"])
    writer.writeheader()
    writer.writerows(qa_list)

print(f"Saved {len(qa_list)} Q&A pairs to {csv_file}")

    
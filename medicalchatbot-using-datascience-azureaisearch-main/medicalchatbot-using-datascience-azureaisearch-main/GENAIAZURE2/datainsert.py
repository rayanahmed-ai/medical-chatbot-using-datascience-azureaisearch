import csv
from azure.data.tables import TableServiceClient, TableEntity
import os
connection_string = "DefaultEndpointsProtocol=https;AccountName=azurelibqa;AccountKey=nEFaaHqV8Ud/5sTSBxEMkS/0mVl7CMx5CLi8vg8vz+7u/TQkThk76oDVWBmPuqoPhC1G0h/S+fT/+AStccW+DQ==;EndpointSuffix=core.windows.net"
table_name = "Azurelib"
from chatbot import response
table_service= TableServiceClient.from_connection_string(conn_str=connection_string)

try:
    table_service.create_table(table_name)
except Exception as e:
    print(f"table already exists: {e}")

with open("qa_dataset_with_id.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)

        entity  = TableEntity()
        entity['PartitionKey']="AZURELIB"
        entity['RowKey']=row['id']
        entity['Question']=row['question']
        entity['Answer']=row['answer']
        
        try:
            table_service.get_table_client(table_name).create_entity(entity=entity)
            print(f"Entity {row['id']} inserted successfully.")
        except Exception as e:
            print(f"Failed to insert entity {row['id']}: {e}")

print("Data upload complete")
# try:
#     table_service.create_table(table_name)

# except Exception as e:
#     print(f"table already exists: {e}")

# from langchain.chat_models import ChatOpenAI
# from langchain.schema import HumanMessage, AIMessage
# import os

# # Set your API key for OpenRouter
# os.environ["OPENAI_API_KEY"] =os.getenv("apikey")

# # Create a chat model
# chat = ChatOpenAI(
#     model_name="nvidia/nemotron-nano-12b-v2-vl:free",
#     temperature=0,
#     model_kwargs={"reasoning": {"enabled": True}}
# )

# # First question
# question = "How many r's are in the word 'strawberry'?"

# first_response = chat([HumanMessage(content=question)])
# print("Assistant:", first_response.content)

# # Preserve reasoning for follow-up
# messages = [
#     HumanMessage(content=question),
#     AIMessage(
#         content=first_response.content,
#         additional_kwargs={"reasoning_details": getattr(first_response, "reasoning_details", None)}
#     ),
#     HumanMessage(content="Are you sure? Think carefully.")
# ]

# # Second API call, continues reasoning
# second_response = chat(messages)
# print("Assistant (continued):", second_response.content)


# csv_file_path = "Azurelib"

# # try:
# #     table_service.create_table(table_name)
# csv_file_path="combined_data.csv"

# with open(csv_file_path) as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print(row)

#         entity  = TableEntity()
#         entity['PartitionKey']=row['PartitionKey']
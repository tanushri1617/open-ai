from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# STEP 1: input
user_input = input("Enter your topic: ")

# STEP 2: prompt
prompt = f"""
Explain "{user_input}" in meme style.

Give:
- Simple explanation
- One funny meme line
"""

# STEP 3: API call (NEW METHOD)
response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)

# STEP 4: output
print("\n Meme Output:\n")
print(response.output[0].content[0].text)
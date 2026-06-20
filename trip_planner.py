import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load environment variables
load_dotenv()

# 2. Initialize Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# 3. Create a dynamic Prompt Template
# We use a 'system' role to tell the AI how to behave, and a 'user' role for the input
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert travel planner. Create a highly detailed, day-by-day itinerary for the requested destination."),
    ("user", "Plan a {days}-day trip to {destination} with a focus on {style}.")
])

# 4. Define our user's specific inputs
user_inputs = {
    "days": "3",
    "destination": "Tokyo, Japan",
    "style": "food and local culture"
}

# 5. Format the prompt with our dynamic inputs
formatted_prompt = prompt_template.invoke(user_inputs)

# 6. Pass the formatted prompt to Gemini
print(f"Generating your itinerary for {user_inputs['destination']}...")
response = llm.invoke(formatted_prompt)

print("\n--- Your Custom Itinerary ---")
print(response.content)
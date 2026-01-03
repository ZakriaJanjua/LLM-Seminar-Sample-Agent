import os
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# TOOL
def calculator(expression: str) -> str:
   try:
      return str(eval(expression))
   except Exception as e:
      return f"Error {e}"
   
TOOLS = {
   "calculator": calculator
}

# MEMORY
memory = []

# AGENT PROMPT
AGENT_PROMPT = """
You are a helpful AI agent.

You can think step by step.
You can use tools when needed.

Available tools:
- calculator(expression): evaluates math expressions

Use this format:

Thought: your reasoning
Action: tool_name(expression)
Observation: result
Final: answer to the user
"""

def agent(query):
   memory.append(f"User: {query}")

   messages = [
      {"role": "system", "content": AGENT_PROMPT},
      {"role": "user", "content": "\n".join(memory)}
   ]

   while True:
      response = client.chat.completions.create(
         model="llama-3.3-70b-versatile",
         messages=messages,
         temperature=0
      )

      reply = response.choices[0].message.content
      print("\nLLM OUTPUT:\n", reply)

      action_match = re.search(r"Action:\s*(\w+)\((.*)\)", reply)

      if action_match:
            tool_name = action_match.group(1)
            tool_input = action_match.group(2)

            tool_result = TOOLS[tool_name](tool_input)
            observation = f"Observation: {tool_result}"

            messages.append({"role": "assistant", "content": reply})
            messages.append({"role": "assistant", "content": observation})
            memory.append(observation)
      else:
          memory.append(reply)
          break


if __name__ == "__main__":
    while True:
        q = input("\nAsk the agent (or 'exit'): ")
        if q == "exit":
            break
        agent(q)
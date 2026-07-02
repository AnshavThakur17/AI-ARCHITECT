import json
import ollama
import re


def extract_with_llm(user_prompt):

    system_prompt = """
You are a senior distributed systems architect.

Analyze the product idea.

Return ONLY valid JSON.

Format:

{
  "real_time": false,
  "low_latency": false,
  "write_heavy": false,
  "read_heavy": false,
  "security_critical": false,
  "geo_distributed": false,
  "consistency_requirement": "normal",
  "scale": 10000
}

Do not explain.
No markdown.
No extra text.
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        output = response["message"]["content"]

        # remove ```json wrappers if model adds them
        output = re.sub(
            r"```json|```",
            "",
            output
        ).strip()

        data = json.loads(output)
        if isinstance(data, dict):
            return data
        else:
            raise ValueError("Ollama response is not a JSON object")

    except Exception:
        # fallback defaults
        return {
            "real_time": False,
            "low_latency": False,
            "write_heavy": False,
            "read_heavy": False,
            "security_critical": False,
            "geo_distributed": False,
            "consistency_requirement": "normal",
            "scale": 10000
        }
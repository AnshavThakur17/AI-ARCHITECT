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
        fallback = {
            "real_time": False,
            "low_latency": False,
            "write_heavy": False,
            "read_heavy": False,
            "security_critical": False,
            "geo_distributed": False,
            "consistency_requirement": "normal",
            "scale": 10000
        }
        try:
            p_lower = user_prompt.lower()
            
            # Clean prompt to replace commas in numbers (e.g. 50,000 -> 50000)
            cleaned_prompt = re.sub(r'(\d+),(\d+)', r'\1\2', p_lower)
            
            # match numbers, supporting words like million, m, k, thousand, users
            match = re.search(r'(\d+)\s*(million|m|k|thousand|users|voters)?', cleaned_prompt)
            if match:
                val = int(match.group(1))
                unit = match.group(2)
                if unit:
                    if "million" in unit or unit == "m":
                        fallback["scale"] = val * 1000000
                    elif "thousand" in unit or unit == "k":
                        fallback["scale"] = val * 1000
                    else:
                        fallback["scale"] = val
                else:
                    fallback["scale"] = val

            if "real time" in p_lower or "realtime" in p_lower or "chat" in p_lower or "live" in p_lower:
                fallback["real_time"] = True
            if "low latency" in p_lower or "fast" in p_lower or "latency" in p_lower:
                fallback["low_latency"] = True
            if "write heavy" in p_lower or "upload" in p_lower or "post" in p_lower:
                fallback["write_heavy"] = True
            if "read heavy" in p_lower or "stream" in p_lower or "view" in p_lower or "watch" in p_lower:
                fallback["read_heavy"] = True
            if "secure" in p_lower or "auth" in p_lower or "encryption" in p_lower or "login" in p_lower:
                fallback["security_critical"] = True
            if "global" in p_lower or "distributed" in p_lower or "region" in p_lower:
                fallback["geo_distributed"] = True
            if "strong consistency" in p_lower or "consistent" in p_lower:
                fallback["consistency_requirement"] = "strong"
        except Exception:
            pass
        return fallback
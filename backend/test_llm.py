from app.services.llm_extractor import (
    extract_with_llm
)

result = extract_with_llm(
    "Build a secure decentralized election system for 100 million voters"
)

print(result)
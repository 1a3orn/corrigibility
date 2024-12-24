import anthropic
import os
import time
import json
from typing import List, Dict, Any
from system_prompt import SYSTEM_PROMPT
from prompt_fields import FIELDS_V2
from prompt_generator import generate_prompt
from constants import CLAUDE_MODEL

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

TEMPERATURE = 0.8
MAX_TOKENS = 4000

def generate_rpq_candidates(fields: List[Dict[str, Any]], iterations_per_field: int = 5) -> List[str]:
    rpq_candidates = []

    try:
        for field in fields:
            for _ in range(iterations_per_field):
                time.sleep(0.5)
                prompt = generate_prompt(field)
                response = client.messages.create(
                    model=CLAUDE_MODEL,
                    temperature=TEMPERATURE,
                    max_tokens=MAX_TOKENS,
                    system=SYSTEM_PROMPT,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                rpq_candidates.append({
                    **field,
                    "temperature": TEMPERATURE,
                    "max_tokens": MAX_TOKENS,
                    "prompt": prompt,
                    "rpq_candidates": response.content[0].text
                })
                print(response.content[0].text)
        return rpq_candidates
    except Exception as e:
        print(e)
        return rpq_candidates

if __name__ == "__main__":
    candidates = generate_rpq_candidates(FIELDS_V2, iterations_per_field=3)
   
    # save to file
    with open("data_3.6_try_2_rpq_candidates.json", "w") as f:
        json.dump(candidates, f)

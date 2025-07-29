import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def sanitize_card_output(raw_output: str) -> str:
    cleaned_lines = []

    for line in raw_output.strip().split("\n"):
        line = line.strip()
        if not line:
            continue

        # If it's already tab-separated
        if "\t" in line:
            cleaned_lines.append(line)
            continue

        # Try splitting using a regex: Question [whitespace] Answer
        split = re.split(r"\s{2,}|\t|:\s+", line, maxsplit=1)

        if len(split) == 2:
            question, answer = split
            cleaned_lines.append(f"{question.strip()}\t{answer.strip()}")
        else:
            print(f"⚠️ Skipping malformed line: {line}")

    return "\n".join(cleaned_lines)

def generate_card_content(file_content):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in helping programmers study technical notes using Anki flashcards."
            },
            {
                "role": "user",
                "content": f'''
                Given a markdown note (usually from a coding problem or concept explanation), extract the key ideas and transform them into 2–6 high-quality flashcards.
                
                Each flashcard should be in the following format:
                
                Front<TAB>Back
                
                Where:
                - "Front" contains a clear question or prompt
                - "Back" contains the answer or explanation
                - Code snippets can be included in the back if they clarify the answer
                - Do not reference "this note" or "this markdown" in the card text
                - Prefer conceptual understanding, edge cases, or high-yield facts
                
                Also:
                - Avoid making cards that only ask for definitions
                - Prioritize cards that test: how/why something works, edge cases, time complexity, and common mistakes
                
                Output only the flashcards, no explanation. Each card on its own line.
                
                Here is the markdown note:
                {file_content}
                '''
            }
        ]
    )

    return sanitize_card_output(response.choices[0].message.content)


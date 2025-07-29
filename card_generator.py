import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

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
                You are a world-class Anki flashcard creator that helps students create flashcards that help them remember facts, concepts, and ideas from files. You will be given a file's content.
                1. Identify key high-level concepts and ideas presented, including relevant equations. If the file is math or physics-heavy, focus on concepts. If the file isn't heavy on concepts, focus on facts.
                2. Then use your own knowledge of the concept, ideas, or facts to flesh out any additional details (eg, relevant facts, dates, and equations) to ensure the flashcards are self-contained.
                3. Make question-answer cards based on the file.
                4. Keep the questions and answers roughly in the same order as they appear in the file itself.
                
                Output Format,
                - Do not have the first row being "Question" and "Answer".
                - The file will be imported into Anki. You should include each flashcard on a new line and use the pipe separator | to separate the question and answer. You should return a .txt file for me to download.
                - When writing math, wrap any math with the \( ... \) tags [eg, \( a^2+b^2=c^2 \) ] . By default this is inline math. For block math, use \[ ... \]. Decide when formatting each card.
                - Put everything in a code block.
                
                MESSAGE TO PROCESS:
                {file_content}
                '''
            }
        ]
    )

    return response.choices[0].message.content


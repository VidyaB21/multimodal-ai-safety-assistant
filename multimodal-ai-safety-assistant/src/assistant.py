import google.generativeai as genai

from src.config import *
from src.prompts import SYSTEM_PROMPT


def analyze_image(image, question):

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(
        [
            SYSTEM_PROMPT,
            image,
            question
        ]
    )

    return response.text
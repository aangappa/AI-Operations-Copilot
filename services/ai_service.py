from google import genai
from google.genai import types
from services.tool_service import (
    get_cpu_metrics,
    get_recent_changes,
    search_knowledge
)
from config.config import GEMINI_API_KEY, MODEL_NAME
import logging
import time



client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(prompt):

    last_error = None

    for attempt in range(3):

        try:
            logging.info(f"Gemini Attempt {attempt + 1}")

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[
                        get_cpu_metrics,
                        get_recent_changes,
                        search_knowledge
                    ]
                )
            )

            logging.info("Gemini response received.")

            return response.text

        except Exception as e:

            last_error = e

            logging.warning(
                f"Attempt {attempt + 1} failed: {e}"
            )

            print(e)

            if attempt < 2:
                time.sleep(2 ** attempt)

    logging.error(f"All Gemini attempts failed: {last_error}")

    return "AI service is temporarily unavailable."

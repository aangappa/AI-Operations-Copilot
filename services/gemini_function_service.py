from google import genai
from google.genai import types

from config.config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)

cpu_function = types.FunctionDeclaration(
    name="get_cpu_metrics",
    description="Returns the current CPU utilization.",
    parameters=types.Schema(
        type="OBJECT",
        properties={},
        required=[]
    )
)

tools = [
    types.Tool(
        function_declarations=[
            cpu_function
        ]
    )
]
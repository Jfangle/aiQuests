from openai import OpenAI
import json
from creds import OPENAI_API_KEY



client = OpenAI(api_key=OPENAI_API_KEY)

# JSON schema for nutritional information
nutritional_schema = {
    "food": "string",
    "macros": {
        "calories": "number",
        "protein": "string",
        "fat": "string",
        "carbohydrates": "string"
    },
    "serving_size": "string"
}

def get_nutritional_info(prompt):
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a nutritional assistant. Provide nutritional information in JSON format."},
            {"role": "user", "content": f"Provide nutritional information for {prompt} in JSON format using this schema: {json.dumps(nutritional_schema)}"}
        ])
        content = response.choices[0].message.content
        print("API response:")
        print(content)
        
        # Remove JSON code block markers if present
        content = content.strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.endswith("```"):
            content = content[:-3]
        
        # Print the cleaned content before parsing
        print("\nCleaned content:")
        print(content)
        
        parsed_json = json.loads(content.strip())
        return parsed_json
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


# Example query
query = "Tell me the macros of an egg"
nutritional_info = get_nutritional_info(query)


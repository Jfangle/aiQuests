from openai import OpenAI
from creds import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)

# Set up the OpenAI API key

def generate_response(prompt, model="gpt-4o-mini"):
    try:
        # Create a chat completion
        response = client.chat.completions.create(model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        temperature=0.7)

        # Extract and return the generated text
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the AI Response Generator!")
    while True:
        user_input = input("\nEnter your prompt (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Thank you for using the AI Response Generator. Goodbye!")
            break

        response = generate_response(user_input)
        print(f"\nAI Response: {response}")

if __name__ == "__main__":
    main()
import os
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_story(prompt):
    # Mock response para pruebas
    if "OPENAI_API_KEY" not in os.environ:
        return "✨ Bajo el resplandor de la luna, el unicornio dorado esparció polvo mágico que convirtió los sueños en estrellas. ✨"
    
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al generar la historia: {str(e)}"

if __name__ == "__main__":
    story = generate_story("Write a one-sentence bedtime story about a unicorn in Spanish.")
    print(story)
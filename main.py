import base64
import sys
import os

# Run "uv sync" to install the below packages
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

print(os.getenv("OPENAI_API_KEY"))

client = OpenAI()


def load_file(path: str) -> str:
    if not os.path.exists(path):
        print(f"Error: The file '{path}' does not exist.")
        sys.exit(1)

    print("Loading file:", path)
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def generate_article_draft(outline: str) -> str:
    print("Generating article draft...")

    prompt = f"""
                Write a detailed blog post based on the following outline:

                <outline>
                {outline}
                </outline>
            """

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    generated_text = response.output_text.strip()

    return generated_text



def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <outline_file>")
        sys.exit(1)

    outline_file = sys.argv[1]
    outline = load_file(outline_file)

    blog_post_draft = generate_article_draft(outline)
    print("Generated blog post draft:")
    print(blog_post_draft)


if __name__ == "__main__":
    main()
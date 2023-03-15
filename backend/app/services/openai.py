import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_image_from_string(description: str) -> str:
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="256x256"
    )
    return response['data'][0]['url']
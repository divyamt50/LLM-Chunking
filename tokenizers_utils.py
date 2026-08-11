from transformers import AutoTokenizer
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    token=ACCESS_TOKEN
)


def encoder(text):
    return tokenizer.encode(text)


def decoder(token_ids):
    return tokenizer.decode(token_ids)


def encode_string(text):
    number_of_characters = len(text)
    number_of_words = len(text.split())

    token_ids = encoder(text)
    number_of_tokens = len(token_ids)

    chars_per_token = (
        round(number_of_characters / number_of_tokens, 2)
        if number_of_tokens > 0
        else 0
    )

    decoded_text = decoder(token_ids)

    return {
        "number_of_characters": number_of_characters,
        "number_of_words": number_of_words,
        "number_of_tokens": number_of_tokens,
        "chars_per_token": chars_per_token,
        "token_ids": token_ids,
        "decoded_text": decoded_text,
    }


if __name__ == "__main__":
    text = "Hello chunk doctor"

    result = encode_string(text)

    print(result)
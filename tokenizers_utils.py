from transformers import AutoTokenizer
from dotenv import load_dotenv
import os
load_dotenv()

model_name = "Qwen/Qwen2.5-7B-Instruct"

access_token = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

tokenizer = AutoTokenizer.from_pretrained(model_name, token = access_token)


def encode_string(text_arg):
    number_of_characters = len(text_arg)
    number_of_words = len(text_arg.split())
    token_ids = tokenizer.encode(text_arg)
    number_of_tokens = len(token_ids)
    chars_per_token = round(number_of_characters/number_of_tokens, 2) if number_of_tokens > 0 else 0
    decoded_text = tokenizer.decode(token_ids)
    return {
        "number_of_characters": number_of_characters,
        "number_of_words": number_of_words,
        "number_of_tokens": number_of_tokens,
        "chars_per_token":chars_per_token,
        "encoded_output": token_ids,
        "decoded_text":decoded_text
    }

if __name__ == "__main__":
    text = "Hello chunk doctor"
    result = encode_string(text)
    print(result)
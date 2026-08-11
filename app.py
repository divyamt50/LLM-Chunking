import gradio as gr
import spaces

from chunking import chunk_text
from tokenizers_utils import encoder, decoder, encode_string

@spaces.GPU
def zero_gpu_check():
    return "Chunk Doctor is running on ZeroGPU."


def analyze(text):
    if not text or not text.strip():
        return "Please enter some text."

    result = encode_string(text)

    return (
        f"Characters: {result['number_of_characters']}\n"
        f"Words: {result['number_of_words']}\n"
        f"Tokens: {result['number_of_tokens']}\n"
        f"Characters per token: {result['chars_per_token']}\n\n"
        f"Token IDs:\n{result['token_ids']}"
    )


def encode_for_ui(text):
    if not text or not text.strip():
        return "Please enter some text."

    return str(encoder(text))


def decode_for_ui(text):
    if not text or not text.strip():
        return "Please enter token IDs."

    try:
        token_ids = [int(x.strip()) for x in text.split(",")]
        return decoder(token_ids)

    except ValueError:
        return "Enter token IDs separated by commas.\nExample: 128000, 9906, 1917"


def chunk_for_ui(text, chunk_size, overlap):
    if not text or not text.strip():
        return "Please enter some text."

    if chunk_size <= 0:
        return "Chunk size must be greater than 0."

    if overlap < 0:
        return "Overlap cannot be negative."

    if overlap >= chunk_size:
        return "Overlap must be smaller than chunk size."

    chunks = chunk_text(
        text,
        chunk_size,
        overlap
    )

    output = []

    for index, chunk in enumerate(chunks, start=1):
        output.append(
            f"CHUNK {index}\n"
            f"Tokens: {len(chunk)}\n"
            f"Token IDs: {chunk}\n"
        )

    return "\n-----------------------------\n".join(output)


with gr.Blocks(title="Chunk Doctor") as demo:

    gr.Markdown(
        """
        # 🩺 Chunk Doctor

        Analyze text, inspect tokens, and experiment with token-based chunking.
        """
    )

    with gr.Row():

        with gr.Column(scale=2):

            text_input = gr.Textbox(
                label="Paste some text",
                placeholder="Paste your text here...",
                lines=10
            )

            with gr.Row():

                chunk_size = gr.Number(
                    label="Chunk Size",
                    value=256,
                    precision=0
                )

                overlap = gr.Number(
                    label="Overlap",
                    value=32,
                    precision=0
                )

        with gr.Column(scale=1):

            gr.Markdown("### Tools")

            encoder_btn = gr.Button("Encode")
            decoder_btn = gr.Button("Decode")
            chunking_btn = gr.Button("Chunk")
            analyze_btn = gr.Button("Analyze", variant="primary")

    output_display = gr.Textbox(
        label="Output",
        lines=20,
        #show_copy_button=True
    )

    encoder_btn.click(
        fn=encode_for_ui,
        inputs=text_input,
        outputs=output_display
    )

    decoder_btn.click(
        fn=decode_for_ui,
        inputs=text_input,
        outputs=output_display
    )

    chunking_btn.click(
        fn=chunk_for_ui,
        inputs=[text_input, chunk_size, overlap],
        outputs=output_display
    )

    analyze_btn.click(
        fn=analyze,
        inputs=text_input,
        outputs=output_display
    )


demo.launch(inbrowser=True)
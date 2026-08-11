from tokenizers_utils import encoder


def chunk_text(text, chunk_size, overlap):
    token_ids = encoder(text)

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0.")

    if overlap < 0:
        raise ValueError("Overlap cannot be negative.")

    if overlap >= chunk_size:
        raise ValueError(
            "Overlap must be smaller than chunk size."
        )

    step = chunk_size - overlap

    chunks = []

    start = 0

    while start < len(token_ids):

        chunk = token_ids[start:start + chunk_size]

        chunks.append(chunk)

        start += step

    return chunks
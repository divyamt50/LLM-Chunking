# 🩺 Chunk Doctor

> An interactive toolkit for understanding LLM tokenization and experimenting with token-based text chunking for RAG pipelines.

Chunk Doctor helps visualize what actually happens to text before it reaches an LLM.

Instead of treating text as simple words or characters, it lets you inspect the **tokens, token IDs, token counts, and token-based chunks** produced by a real LLM tokenizer.

---

## 🚀 Live Demo

**Coming soon**

---

## 📌 Why I Built This

When learning RAG and LLM engineering, concepts like:

- Tokens
- Token IDs
- Context windows
- Chunk size
- Chunk overlap
- Token-based chunking

can feel abstract.

Chunk Doctor was built to make these concepts **visible and interactive**.

You can paste text into the application and see how an LLM tokenizer actually processes it.

---

## ✨ Features

### 🔤 Token Encoding

Convert text into the token IDs used by the model.

```text
Text
  ↓
Tokenizer
  ↓
Token IDs
```

Example:

```text
"Hello world"
        ↓
[...token IDs...]
```

---

### 🔄 Token Decoding

Convert token IDs back into readable text.

```text
Token IDs
    ↓
Tokenizer
    ↓
Text
```

This demonstrates the relationship between human-readable text and the numerical representation used by LLMs.

---

### 📊 Text Analysis

Analyze text using the selected tokenizer.

The application calculates:

- Character count
- Word count
- Token count
- Characters per token
- Token IDs

This makes it easy to see why:

> **1 word ≠ 1 token**

---

### ✂️ Token-Based Chunking

Chunk text based on **tokens rather than characters or words**.

The chunker supports configurable:

- Chunk size
- Chunk overlap

Example:

```text
Tokens:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Chunk size = 4
Overlap = 2

        ↓

[1, 2, 3, 4]
[3, 4, 5, 6]
[5, 6, 7, 8]
[7, 8, 9, 10]
```

This demonstrates the basic chunking strategy used in RAG pipelines.

---

## 🧠 Why Token-Based Chunking?

A common beginner approach is:

```python
text.split()
```

or splitting text by characters.

However, LLMs process **tokens**, not words or characters.

Chunk Doctor therefore follows:

```text
Raw Text
   ↓
Tokenizer
   ↓
Token IDs
   ↓
Token-based chunks
   ↓
Decoded text
```

This makes chunk sizes predictable relative to an LLM's context window.

---

## 🏗️ Architecture

```text
                    Chunk Doctor
                         │
                         ▼
                    User Text
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
          Encode      Analyze      Chunk
             │           │           │
             ▼           ▼           ▼
        Token IDs     Statistics   Token Chunks
             │
             ▼
          Decode
             │
             ▼
          Text
```

---

## 🛠️ Tech Stack

- **Python**
- **Gradio**
- **Hugging Face Transformers**
- **Qwen 2.5 7B Instruct tokenizer**
- **uv**
- **PyTorch**

---

## 📂 Project Structure

```text
chunk-doctor/
│
├── main.py
├── tokenizers_utils.py
├── chunking.py
│
├── README.md
├── requirements.txt
├── pyproject.toml
├── uv.lock
│
├── .gitignore
└── .env
```

### File Responsibilities

| File | Purpose |
|---|---|
| `main.py` | Gradio interface and UI handlers |
| `tokenizers_utils.py` | Tokenizer loading, encoding, decoding and text analysis |
| `chunking.py` | Token-based chunking logic |
| `pyproject.toml` | Project dependencies and configuration |
| `uv.lock` | Locked dependency versions |

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/chunk-doctor.git
cd chunk-doctor
```

### 2. Install dependencies

This project uses `uv`.

```bash
uv sync
```

Or install the required packages manually:

```bash
uv add gradio transformers python-dotenv torch
```

### 3. Run the application

```bash
uv run python main.py
```

The Gradio interface will be available locally.

---

## 🧪 Example

Enter:

```text
Artificial intelligence is changing the way software is built.
Large language models process text as tokens rather than words.
```

Then use:

### Analyze

The application displays:

```text
Characters: ...
Words: ...
Tokens: ...
Characters per token: ...

Token IDs:
[...]
```

### Chunk

For example:

```text
Chunk Size: 20
Overlap: 4
```

The application produces overlapping token chunks.

---

## 🔍 Concepts Demonstrated

This project is intentionally small, but it demonstrates several fundamental concepts used in modern AI engineering:

### Tokenization

```text
Text → Tokens → Token IDs
```

### Decoding

```text
Token IDs → Text
```

### Context Windows

Models have a finite number of tokens they can process.

### Chunking

Large documents can be divided into smaller token-based sections.

### Chunk Overlap

Overlapping tokens help preserve context between adjacent chunks.

### RAG Preprocessing

Chunking is one of the preprocessing stages of a typical RAG pipeline:

```text
Documents
    ↓
Text Extraction
    ↓
Tokenization
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retrieval
    ↓
LLM
    ↓
Answer
```

Chunk Doctor focuses primarily on the **tokenization and chunking stages**.

---

## 🧩 Design Principles

The project follows a few simple engineering principles:

### Single Responsibility

Tokenizer functionality is separated from chunking logic and UI code.

```text
tokenizers_utils.py
        ↓
Tokenization

chunking.py
        ↓
Chunking

main.py
        ↓
UI
```

### Token-Based Processing

Chunk boundaries are calculated using token IDs instead of arbitrary character or word counts.

### Reusable Components

The tokenizer and chunking functions are kept independent of the Gradio interface so they can be reused in another application or API later.

---

## 🚧 Roadmap

The current version focuses on tokenization and chunking.

Planned improvements:

- [ ] Visual token highlighting
- [ ] Tokenizer comparison
- [ ] Multiple model/tokenizer selection
- [ ] Chunk preview after decoding
- [ ] Context-window warnings
- [ ] Embedding cost estimation
- [ ] Document upload
- [ ] PDF/text preprocessing
- [ ] Whisper transcription
- [ ] Automated meeting minutes generation
- [ ] RAG pipeline integration

---

## 🎯 Learning Goals

This project is part of my hands-on learning path in **LLM Engineering and RAG systems**.

The goal is not just to use high-level frameworks, but to understand what happens underneath them:

```text
Text
 ↓
Tokenizer
 ↓
Token IDs
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Search
 ↓
LLM
```

Understanding these individual components makes higher-level RAG frameworks much easier to reason about.

---

## 📜 License

This project is for educational and portfolio purposes.

---

## 👨‍💻 Author

**Divyam Tyagi**

Building and learning AI engineering, LLM applications, RAG systems, and backend infrastructure.

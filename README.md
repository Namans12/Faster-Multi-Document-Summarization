# Faster Multi-Document Summarization

Flask web app that extracts text from PDF and Word documents and generates abstractive summaries using Google's Pegasus model.

> **Scope note:** the project title references a Primera + Pegasus hybrid. The committed implementation uses **Pegasus only** (`google/pegasus-xsum`). The Primera half is not in this repository — see [Current implementation](#current-implementation).

## Overview

Upload a document, get a summary. Text is extracted from PDFs with PyMuPDF and from Word files with `docx2txt`, then passed to a pre-trained Pegasus model for abstractive summarisation — the model generates new sentences rather than selecting existing ones.

The research goal was a faster multi-document pipeline combining Primera (built for multi-document input) with Pegasus (strong single-document summariser). What shipped is the Pegasus path.

## Current implementation

| Aspect | Intended | Committed |
|---|---|---|
| Models | Primera + Pegasus hybrid | `google/pegasus-xsum` only |
| Input | Multiple documents at once | One document per request |
| Interface | — | Flask upload form |

`pegasus-xsum` is fine-tuned on XSum, which targets **single-sentence, highly abstractive** summaries. Expect very short output. For longer summaries, `google/pegasus-large` or `google/pegasus-cnn_dailymail` are better-matched checkpoints — changing the string in `app.py` is enough to try them.

## Features

- PDF text extraction via PyMuPDF (`fitz`)
- Word (`.docx`) text extraction via `docx2txt`
- Abstractive summarisation with Pegasus
- Browser upload form — no CLI needed
- Model loaded once at startup rather than per request

## Tech Stack

Python · Flask · Hugging Face `transformers` (Pegasus) · PyTorch · PyMuPDF · `docx2txt`

## Prerequisites

- Python 3.8+
- ~2.5 GB disk for the Pegasus weights, downloaded on first run
- 8 GB RAM recommended — the model is loaded at import time

## Installation

```bash
git clone https://github.com/Namans12/Faster-Multi-Document-Summarization.git
cd Faster-Multi-Document-Summarization
pip install flask transformers torch pymupdf docx2txt
```

The first run downloads `google/pegasus-xsum` from Hugging Face and caches it in `~/.cache/huggingface/`.

## Usage

```bash
python app.py
```

Open <http://localhost:5000>, upload a PDF or `.docx`, and submit. The summary renders on the same page.

## How it works

```
upload (PDF | .docx)
        │
        ├── PDF   → extract_text_from_pdf()   (PyMuPDF)
        └── .docx → extract_text_from_word()  (docx2txt)
        │
        ▼
PegasusTokenizer → PegasusForConditionalGeneration → summary
```

Both extractors are in `app.py`; the `/` route handles `GET` (form) and `POST` (upload and summarise).

## Project Structure

```
app.py                                     Flask app, extraction, summarisation
templates/                                 upload form and result page
static/                                    assets
Applications - Summary Template.docx       sample Word input
Research Paper - Summary Template.pdf      sample PDF input
```

Both sample documents work as test inputs.

## Limitations

- **Single document per request** — despite the name, there is no multi-document merging
- **Very short summaries** — an artefact of the XSum checkpoint, not a bug
- **No input length handling** — Pegasus truncates at its maximum input length, so long documents lose their tail silently
- **Blocking inference** — summarisation runs on the request thread; concurrent uploads queue
- **No file-size limit** on uploads
- No tests

## Completing the original design

1. Accept multiple files per request and concatenate or batch them
2. Add Primera (`allenai/PRIMERA`) for the multi-document path, which is what it was designed for
3. Chunk long inputs and summarise hierarchically instead of truncating
4. Move inference to a background worker so the request thread stays free

## Related Repositories

| Repo | Relationship |
|---|---|
| [`cogmem-llm`](https://github.com/Namans12/cogmem-llm) | Later, more developed LLM work in this account |

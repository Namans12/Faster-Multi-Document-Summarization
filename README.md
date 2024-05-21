# Faster Multi-Document Hybrid Summarization Model using Primera and Pegasus

The Faster Multi-Document Summarization Model is an advanced natural language processing (NLP) model designed to efficiently and accurately generate summaries from multiple documents. By leveraging state-of-the-art techniques in NLP, this model condenses information from various sources into concise summaries, allowing users to quickly grasp the key points of a given topic or set of documents. It focuses on creating a faster and more efficient model for multi-document summarization using the Primera and Pegasus models and allows you to summarize Word and PDF documents, and you can directly add files from your local directory.

## Overview

Multi-document summarization is the process of automatically creating a concise and coherent summary from multiple documents on a given topic. Traditional methods for multi-document summarization can be computationally expensive and time-consuming, especially when dealing with a large number of documents. This project addresses these challenges by developing a faster and more efficient approach to multi-document summarization.

## Features

- **Efficiency:** Utilizes advanced algorithms and optimizations to achieve faster processing speed compared to traditional methods.
- **Accuracy:** Generates accurate summaries by analyzing and condensing information from multiple documents.
- **Scalability:** Can handle large volumes of documents efficiently, making it suitable for summarizing extensive datasets or collections of documents.
- **Summarize Word Documents:** Efficiently summarize multiple Word documents.
- **Summarize PDF Documents:** Effectively summarize multiple PDF documents.
- **Local Directory Integration:** Easily add files from your local directory for summarization.
- **Advanced Summarization Models:** Utilizes the Primera and Pegasus models for high-quality summaries.

## Usage

1. **Input Documents:** Provide a set of input documents on a given topic or related topics.
2. **Summarization:** Use the model to generate a summary from the input documents.
3. **Output:** Obtain a concise summary that captures the key points and important information from the input documents.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Getting Started

1. **Clone this repository:**

    ```bash
    git clone https://github.com/YourUsername/Faster-Multi-Document-Summarization-Model.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the model:** Use the provided scripts or APIs to run the summarization model on your input documents.

4. **View the summaries:** Access the generated summaries and analyze the results.

## Example

```python
from summarization_model import MultiDocumentSummarizer

# Initialize the summarization model
summarizer = MultiDocumentSummarizer()

# Provide input documents
documents = [
    "Document 1 text...",
    "Document 2 text...",
    # Add more documents as needed
]

# Generate summary
summary = summarizer.summarize(documents)

# Print or save the summary
print(summary)
```

## Acknowledgements
- This project builds upon the advancements in natural language processing and machine learning.
- Special thanks to the open-source community for providing valuable resources and libraries.

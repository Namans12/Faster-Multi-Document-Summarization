from flask import Flask, request, render_template
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import fitz  # PyMuPDF
import docx2txt
import io

app = Flask(__name__)

# Load the Pegasus tokenizer and model
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    pdf_text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pdf_text += page.get_text()
    return pdf_text

# Function to extract text from Word
def extract_text_from_word(file):
    return docx2txt.process(io.BytesIO(file.read()))

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        # Check if the file is a PDF or Word document
        if file.filename.endswith(".pdf"):
            document_text = extract_text_from_pdf(file)
        elif file.filename.endswith(".docx"):
            document_text = extract_text_from_word(file)
        else:
            return {"error": "Unsupported file format. Supported formats: .pdf, .docx"}

        # Chunk the document text into smaller parts
        chunk_size = 1024  # Adjust as needed
        chunks = [document_text[i:i+chunk_size] for i in range(0, len(document_text), chunk_size)]

        # Generate summaries for each chunk
        summaries = []
        for chunk in chunks:
            # Encode the chunk
            inputs = tokenizer(chunk, return_tensors="pt", max_length=1024, truncation=True)

            # Generate summary using the Pegasus model
            summary_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=5, early_stopping=True)

            # Decode the generated summary tokens
            decoded_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            # Add the decoded summary to the list
            summaries.append(decoded_summary)

        # Concatenate the summaries to form the final summary
        final_summary = " ".join(summaries)

        # Return the final summary
        return render_template('index.html', summary=final_summary)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
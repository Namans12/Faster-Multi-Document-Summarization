// Function to handle file drop
function dropHandler(event) {
    event.preventDefault();
    var files = event.dataTransfer.files;
    handleFiles(files);
}

// Function to handle file selection
function handleFiles(files) {
    for (var i = 0, file; file = files[i]; i++) {
        if (file.type.match('application/pdf') || file.type.match('application/msword')) {
            // Send file to Flask backend for summarization
            summarizeDocument(file);
        }
        else {
            alert("Unsupported file format. Please upload a PDF or Word document.");
        }
    }
}

// Function to send file to Flask backend for summarization
function summarizeDocument(file) {
    var formData = new FormData();
    formData.append('file', file);
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Display the summarized text on the page
        document.getElementById('output').innerText = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

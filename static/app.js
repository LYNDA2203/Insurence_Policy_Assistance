async function uploadPDF() {

    const fileInput = document.getElementById("pdfFile");

    if (fileInput.files.length === 0) {
        alert("Please choose a PDF.");
        return;
    }

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    document.getElementById("uploadStatus").innerHTML = "Uploading...";

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("uploadStatus").innerHTML = data.message;

    } catch (error) {

        document.getElementById("uploadStatus").innerHTML = "Upload Failed.";

        console.error(error);

    }
}

async function askQuestion() {

    const question = document.getElementById("question").value;

    if (!question.trim()) {
        alert("Enter a question");
        return;
    }

    document.getElementById("answer").innerHTML = "Generating answer...";

    try {

        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        document.getElementById("answer").innerHTML = data.answer;

    } catch (error) {

        document.getElementById("answer").innerHTML = "Error generating answer.";

        console.error(error);

    }
}
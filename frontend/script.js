document.getElementById("diagnosisForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const age = document.getElementById("age").value;
    const gender = document.getElementById("gender").value;
    
    // Get selected symptoms
    const symptoms = Array.from(document.querySelectorAll('input[name="symptom"]:checked'))
        .map(el => el.value);
    
    if (symptoms.length === 0) {
        alert("Please select at least one symptom!");
        return;
    }
    
    // Call backend API
    try {
        const response = await fetch("http://localhost:8000/diagnose", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                symptoms,
                age: parseInt(age),
                gender
            }),
        });
        
        const data = await response.json();
        displayResults(data.diagnosis);
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to get diagnosis. Please try again.");
    }
});

function displayResults(conditions) {
    const resultsDiv = document.getElementById("diagnosisResults");
    resultsDiv.innerHTML = "";
    
    if (conditions.length === 0) {
        resultsDiv.innerHTML = "<p>No matching conditions found.</p>";
    } else {
        conditions.forEach(cond => {
            const condElement = document.createElement("div");
            condElement.className = "condition";
            condElement.innerHTML = `
                <h3>${cond.condition}</h3>
                <p class="confidence">Confidence: ${Math.round(cond.confidence * 100)}%</p>
            `;
            resultsDiv.appendChild(condElement);
        });
    }
    
    document.getElementById("results").classList.remove("hidden");
}
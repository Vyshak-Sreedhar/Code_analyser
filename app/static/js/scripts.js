// Simple interactivity
document.addEventListener("DOMContentLoaded", () => {
    const analyzeButton = document.querySelector("button");

    // Add a loading effect
    analyzeButton.addEventListener("click", () => {
        analyzeButton.innerHTML = "Analyzing...";
        analyzeButton.disabled = true;

        // Restore button after 2 seconds (simulate processing time)
        setTimeout(() => {
            analyzeButton.innerHTML = "Analyze";
            analyzeButton.disabled = false;
        }, 2000);
    });
});

document.getElementById("submitCity").addEventListener("click", function() {
    const city = document.getElementById("cityInput").value.trim().toLowerCase();
    const outputBox = document.getElementById("output");

    if (!city) {
        outputBox.innerHTML = "<p class='error'>Please enter a city from the list.</p>";
        return;
    }

    // Fetch time from Django backend
    fetch(`/datetime/get_time/?city_name=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.local_time) {
                outputBox.innerHTML = `
                    <div class="result">
                        <h2>Current Date and Time in ${data.city}.</h2>
                        <p class="enlarged">${data.local_time}</p>
                    </div>`;
            } else {
                outputBox.innerHTML = "<p class='error'><big>City not found. Please enter a city from the list.</big></p>";
            }
        })
        .catch(error => console.error("Error:", error));
});
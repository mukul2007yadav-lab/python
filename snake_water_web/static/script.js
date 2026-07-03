function play(choice) {
    fetch('/play', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_choice: choice })
    })
    .then(response => response.json())
    .then(data => {
        // This line updates the HTML with the result from Python!
        document.getElementById("result").innerText = data.result;
    });
}
function submitCode() {
    let pythonCode = document.getElementById("editorText").value
    let data = { text: pythonCode };

    fetch("http://127.0.0.1:8000/interpret/", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}
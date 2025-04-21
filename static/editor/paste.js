function newPaste(){
    // get the value of the editor
    var value = editor.getValue();
    // HTMLify it 
    fetch('/api/paste/new', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "content": value
        })
    }).then(response => response.json())
        .then(data => {
            console.log(data);
            url = data.url;
            url = document.location.origin + url;
            // redirect
            window.location.href = url;
        })
        .catch(error => {
            console.error('Error:', error);
            change_text(value + "\n Error: " + error);
        });
}
function change_text(text) {
    editor.setValue(text);
    editor.updateOptions({ readOnly: true });
}

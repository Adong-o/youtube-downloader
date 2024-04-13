/*
document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var videoUrl = document.getElementById('videoUrl').value;
    var messageElement = document.getElementById('message');
    messageElement.textContent = 'Downloading...';

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ videoUrl: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
        messageElement.textContent = data.message;
        if (data.path) {
            window.location.href = data.path;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        messageElement.textContent = 'An error occurred. Please try again.';
    });
});
*/

document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var videoUrl = document.getElementById('videoUrl').value;
    var messageElement = document.getElementById('message');
    messageElement.textContent = 'Downloading...';

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ videoUrl: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
        messageElement.textContent = data.message;
        if (data.path) {
            // Create a download link
            var downloadLink = document.createElement('a');
            downloadLink.href = data.path;
            downloadLink.download = 'video.mp4'; // Set desired filename
            downloadLink.textContent = 'Download Video';
            messageElement.appendChild(downloadLink);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        messageElement.textContent = 'An error occurred. Please try again.';
    });
});


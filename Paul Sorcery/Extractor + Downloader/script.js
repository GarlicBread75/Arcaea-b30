document.getElementById('downloadBtn').addEventListener('click', function() {
  const fileInput = document.getElementById('fileInput');
  const output = document.getElementById('output');

  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = function(event) {
    const content = event.target.result;
    const links = extractLinks(content);
    output.textContent = links.join('\n');
    downloadFiles(links);
  };

  reader.readAsText(file);
});

function extractLinks(text) {
  const regex = /https?:\/\/[^\s]+/g;
  return text.match(regex) || [];
}

async function downloadFiles(links) {
  for (let link of links) {
    try {
      const response = await fetch(link);
      const blob = await response.blob();
      const fileName = getFileNameFromUrl(link);
      downloadBlob(blob, fileName);
    } catch (error) {
      console.error('Error downloading file:', error);
    }
  }
}

function getFileNameFromUrl(url) {
  const urlParts = url.split('/');
  return urlParts[urlParts.length - 1];
}

function downloadBlob(blob, fileName) {
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', fileName);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

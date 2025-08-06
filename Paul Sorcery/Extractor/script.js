document.getElementById('extractBtn').addEventListener('click', function() {
  const fileInput = document.getElementById('fileInput');
  const output = document.getElementById('output');

  const file = fileInput.files[0];
  const reader = new FileReader();

  reader.onload = function(event) {
    const content = event.target.result;
    const links = extractLinks(content);
    output.textContent = links.join('\n');
    downloadTxtFile(links.join('\n'));
  };

  reader.readAsText(file);
});

function extractLinks(text) {
  const regex = /https?:\/\/[^\s]+/g;
  return text.match(regex) || [];
}

function downloadTxtFile(text) {
  const element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', 'extracted_links.txt');
  element.style.display = 'none';
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
}

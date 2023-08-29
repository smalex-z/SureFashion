//Multi-Staged Add Product Modal
document.addEventListener('DOMContentLoaded', function() {
    // Your JavaScript code here
    const startButton = document.getElementById('startButton');
    const formStage = document.getElementById('formStage');
    const cancelButton = document.getElementById('cancelButton');


    startButton.addEventListener('click', () => {
      startButton.style.display = 'none';
      formStage.style.display = 'block';
    });

    cancelButton.addEventListener('click', () => {
      startButton.style.display = 'block';
      formStage.style.display = 'none';
    }); //TODO: Reset inputs on cancel


  });


// Script for Openning Product Preview
function openPreviewModal(imageUrl, productName, heatIndex) {
    document.getElementById('previewImage').src = imageUrl;
    document.getElementById('previewProductName').textContent = productName;
    document.getElementById('previewHeatIndex').textContent = 'Heat Index: ' + heatIndex;
    $('#previewModal').modal('show');
}


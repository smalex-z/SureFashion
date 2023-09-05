//Category Tabs
$(document).ready(function() {
  // Add click event listener to tab links
  $('.nav-link').click(function(event) {
      // Prevent default behavior (following the link)
      event.preventDefault();
      const wardrobe = document.getElementById('wardrobe');
      const styles = document.getElementById('styles');
      const similarItems = document.getElementById('similar-items');

      // Get the ID of the selected tab
      var selectedTab = $(this).attr('id');

      // Do something based on the selected tab
      if (selectedTab === 'wardrobe-tab') {
          // Wardrobe tab selected
          wardrobe.style.display = 'block';
          styles.style.display = 'none';
          similarItems.style.display = 'none';
      } else if (selectedTab === 'styles-tab') {
          // Styles tab selected
          wardrobe.style.display = 'none';
          styles.style.display = 'block';
          similarItems.style.display = 'none';
          console.log('cancel');
      } else if (selectedTab === 'similar-items-tab') {
          // Similar Items tab selected
          wardrobe.style.display = 'none';
          styles.style.display = 'none';
          similarItems.style.display = 'block';
      }
  });
});


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

//Script for Enabling/Disabling Belt
$(document).ready(function() {
  var categorySelect = $('#id_category');
  var beltField = $('#beltField');
  var beltCheckbox = $('#id_belt'); // Using the same ID as in the HTML

  function toggleBeltFieldVisibility() {
    if (categorySelect.val() === 'bottom') {
      beltField.show();
    } else {
      beltField.hide();
      beltCheckbox.prop('checked', false);
    }
  }

  toggleBeltFieldVisibility();

  categorySelect.change(function() {
    toggleBeltFieldVisibility();
  });
});

// Script for Openning Product Preview
function openPreviewModal(imageUrl, productName, heatIndex) {
    document.getElementById('previewImage').src = imageUrl;
    document.getElementById('previewProductName').textContent = productName;
    document.getElementById('previewHeatIndex').textContent = 'Heat Index: ' + heatIndex;
    $("#editProductModal").modal('show');
}

// Editting Product Model
document.addEventListener('DOMContentLoaded', function() {
  const editButton = document.getElementById('editButton');
  const previewStage = document.getElementById('previewStage');
  const editStage = document.getElementById('editStage');
  const cancelButton = document.getElementById('cancelButton');
  var form = document.getElementById("editForm");

  editButton.addEventListener('click', () => {
    previewStage.style.display = 'none';
    editStage.style.display = 'block';
  });

  cancelButton.addEventListener('click', () => {
    previewStage.style.display = 'block';
    editStage.style.display = 'none';
  });

  /*TODO: uncomment this after we move the save button back
  // Attach a click event listener to a parent element (e.g., a modal)
  // and use event delegation to check if the target is the "Save" button
  editStage.addEventListener("click", function(event) {
    if (event.target.id === "saveButton") {
      event.preventDefault(); // Prevent the default form submission
      form.submit(); // Manually trigger the form submission
    }
  });
  */
});

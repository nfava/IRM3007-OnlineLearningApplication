/*https://www.w3schools.com/howto/howto_js_dropdown.asp*/
function dropDown() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close dropdown if clicking outside
window.onclick = function(event) {
  if (!event.target.closest('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

// Update converter based on selected field
function updateFields() {
  var conversionType = document.getElementById("id_conversion_type").value;
  var percentageField = document.getElementById("percentage-field");
  var gpa12Field = document.getElementById("gpa12-field");
  if (conversionType === "percent_to_all") {
    percentageField.style.display = "block";
    gpa12Field.style.display = "none";
    document.getElementById("id_gpa_12").value = "";
  }
  else if (conversionType === "gpa12_to_gpa4") {
    percentageField.style.display = "none";
    gpa12Field.style.display = "block";
    document.getElementById("id_percentage").value = "";
  }
}
// Run on page load
document.addEventListener("DOMContentLoaded", function () {
  updateFields();
  // Run whenever dropdown changes
  document.getElementById("id_conversion_type").addEventListener("change", updateFields);
});
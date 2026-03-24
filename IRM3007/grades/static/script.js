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
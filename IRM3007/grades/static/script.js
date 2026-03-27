/*https://www.w3schools.com/howto/howto_js_dropdown.asp*/
function dropDown() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close dropdown if clicking outside
window.onclick = function(event) {
  if (!event.target.closest('.dropbtn')) {
    let dropdowns = document.getElementsByClassName("dropdown-content");
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

// GPA Converter
// Convert percentage to letter and GPA12
function percentageToLetterAndGPA12(percentage) {
    if (percentage >= 90) return ["A+", 12];
    else if (percentage >= 85) return ["A", 11];
    else if (percentage >= 80) return ["A-", 10];
    else if (percentage >= 77) return ["B+", 9];
    else if (percentage >= 73) return ["B", 8];
    else if (percentage >= 70) return ["B-", 7];
    else if (percentage >= 67) return ["C+", 6];
    else if (percentage >= 63) return ["C", 5];
    else if (percentage >= 60) return ["C-", 4];
    else if (percentage >= 57) return ["D+", 3];
    else if (percentage >= 53) return ["D", 2];
    else if (percentage >= 50) return ["D-", 1];
    else return ["F", 0];
}

function gpa12ToGpa4(gpa12) {
    return ((gpa12 / 12) * 4).toFixed(2);
}

function conversion(event) {
    event.preventDefault();

    let conversionType = document.getElementById("conversion_type").value;
    let percentage = parseFloat(document.getElementById("percentage").value);
    let gpa12 = parseFloat(document.getElementById("gpa_12").value);

    let result = document.getElementById("result");
    let error = document.getElementById("error");

    result.innerHTML = "";
    error.innerHTML = "";

    if (conversionType === "percent_to_all") {
        if (isNaN(percentage)) {
            error.innerText = "Please enter a percentage value.";
            return;
        }

        let [letter, gpa12Value] = percentageToLetterAndGPA12(percentage);
        let gpa4 = gpa12ToGpa4(gpa12Value);

        result.innerHTML = `
            <p>Letter Grade: ${letter}</p>
            <p>GPA (12-point): ${gpa12Value}</p>
            <p>GPA (4-point): ${gpa4}</p>
        `;
    } else if (conversionType === "gpa12_to_gpa4") {
        if (isNaN(gpa12)) {
            error.innerText = "Please enter a 12-point GPA value.";
            return;
        }

        let gpa4 = gpa12ToGpa4(gpa12);
        result.innerHTML = `
            <p>GPA (4-point): ${gpa4}</p>
        `;
    }
}

// Update converter based on selected field
function updateFields() {
    let conversionTypeElement = document.getElementById("conversion_type");
    let percentageField = document.getElementById("percentage-field");
    let gpa12Field = document.getElementById("gpa12-field");
    let percentageInput = document.getElementById("percentage");
    let gpa12Input = document.getElementById("gpa_12");
    if (!conversionTypeElement || !percentageField || !gpa12Field || !percentageInput || !gpa12Input) {
        return;
    }
    let conversionType = conversionTypeElement.value;

    if (conversionType === "percent_to_all") {
        percentageField.style.display = "block";
        gpa12Field.style.display = "none";
        gpa12Input.value = "";
    } else if (conversionType === "gpa12_to_gpa4") {
        percentageField.style.display = "none";
        gpa12Field.style.display = "block";
        percentageInput.value = "";
    }
}
// Run on page load
document.addEventListener("DOMContentLoaded", function () {
    let conversionTypeElement = document.getElementById("conversion_type");
    if (conversionTypeElement) {
        updateFields();
        // Run whenever dropdown changes
        conversionTypeElement.addEventListener("change", updateFields);
    }
});
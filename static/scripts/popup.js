document.addEventListener("DOMContentLoaded", function () {
    function calculateAge() {
      const dobElement = document.getElementById("dob");
      const dob = new Date(dobElement.value);
      hiddenElement = document.getElementById("hidden");
  
      // Create a reference date of May 31st of the current year
      const currentDate = new Date();
      const referenceDate = new Date(currentDate.getFullYear(), 4, 31); // May is month 4 (0-indexed)
  
      // Calculate the age
      let age = currentDate.getFullYear() - dob.getFullYear();
  
      // Check if the birthdate has occurred this year
      if (dob.getMonth() > referenceDate.getMonth() || (dob.getMonth() === referenceDate.getMonth() && dob.getDate() > referenceDate.getDate())) {
        age--;
      }
  
      if (age >= 3 && age < 4) {
        hiddenElement.value = "true";
      } else {
        hiddenElement.value = "false";
      }
    }


  const birthdateInput = document.getElementById("dob");
  birthdateInput.addEventListener("change", calculateAge);
});

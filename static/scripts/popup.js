document.addEventListener("DOMContentLoaded", function () {
  function calculateAge() {
    const dobElement = document.getElementById("dob");
    const dob = new Date(dobElement.value);
    const currentDate = new Date();

    // Calculate the age
    let age = currentDate.getFullYear() - dob.getFullYear();
    const dobMonth = dob.getMonth();
    const currentDateMonth = currentDate.getMonth();
    const dobDate = dob.getDate();
    const currentDateDate = currentDate.getDate();

    // Adjust age based on birthdate
    if (
      currentDateMonth < dobMonth ||
      (currentDateMonth === dobMonth && currentDateDate < dobDate)
    ) {
      age--;
    }

    const isBetween3And4 = age >= 3 && age < 4;
    hiddenElement = document.getElementById("hidden");
    hiddenElement.value = isBetween3And4 ? "true" : "false";
  }

  const birthdateInput = document.getElementById("dob");
  birthdateInput.addEventListener("change", calculateAge);
});

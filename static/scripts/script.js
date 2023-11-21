document.addEventListener("DOMContentLoaded", function () {
  const permanentAddressInput = document.getElementById("permanent-address-input");
  const temporaryAddressInput = document.getElementById("correspondance-address-input");
  const sameAddressCheckbox = document.getElementById("same-as-permanent-address-check");

  const permanentstateInput = document.getElementById("permanent-state-select");
  const temporarystateInput = document.getElementById("correspondance-state-select");

  const permanenttalukaInput = document.getElementById("permanent-taluka-input");
  const temporarytalukaInput = document.getElementById("correspondance-taluka-input");

  const permanentdistrictInput = document.getElementById("permanent-district-input");
  const temporarydistrictInput = document.getElementById("correspondance-district-input");

  const permanentpincodeInput = document.getElementById("permanent-pincode-input");
  const temporarypincodeInput = document.getElementById("correspondance-pincode-input");

  const permanentcountryInput = document.getElementById("permanent-country-input");
  const temporarycountryInput = document.getElementById("correspondance-country-input");
  
  sameAddressCheckbox.addEventListener("change", function () {
    if (sameAddressCheckbox.checked) {
      // Copy the value of the permanent address to the temporary address
      temporaryAddressInput.value = permanentAddressInput.value;
      temporarydistrictInput.value = permanentdistrictInput.value;
      temporarystateInput.selectedIndex = permanentstateInput.selectedIndex;
      temporarypincodeInput.value = permanentpincodeInput.value;
      temporarycountryInput.value = permanentcountryInput.value;
      temporarytalukaInput.value = permanenttalukaInput.value;
      temporaryAddressInput.disabled = true;
      temporarydistrictInput.disabled = true;
      temporarystateInput.disabled = true;
      temporarypincodeInput.disabled = true;
      temporarycountryInput.disabled = true;
      temporarytalukaInput.disabled = true;
    } else {
      temporaryAddressInput.disabled = false;
      temporarydistrictInput.disabled = false;
      temporarystateInput.disabled = false;
      temporarypincodeInput.disabled = false;
      temporarycountryInput.disabled = false;
      temporarytalukaInput.disabled = false;
    }
  });
  

  const birthdateInput = document.getElementById("dob-input");
  const dobInWordsInput = document.getElementById("dob-inwords-input");

  // Event listener for date input change
  birthdateInput.addEventListener("change", calculateAge);

  // Function to calculate age
  function calculateAge() {
    // Get the selected birthdate from the input
    const birthdate = new Date(birthdateInput.value);

    // Calculate the current date
    const currentDate = new Date();

    // Calculate the difference in milliseconds
    const ageInMilliseconds = currentDate - birthdate;

    // Fill the form inputs with calculated values

    // Calculate the DOB in words
    const dobInWords = calculateDOBInWords(birthdate);
    dobInWordsInput.value = dobInWords;
    dobInWordsInput.disabled = true;
  }
  function calculateDOBInWords(birthdate) {
    const months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];

    const day = birthdate.getDate();
    const month = months[birthdate.getMonth()];
    const year = birthdate.getFullYear();

    return `${month} ${day}, ${year}`;
  }
});


function UndoDisables(){
  // const permanentAddressInput = document.getElementById("permanent-address-input");
  const temporaryAddressInput = document.getElementById("correspondance-address-input");
  // const sameAddressCheckbox = document.getElementById("same-as-permanent-address-check");

  // const permanentstateInput = document.getElementById("permanent-state-select");
  const temporarystateInput = document.getElementById("correspondance-state-select");

  // const permanenttalukaInput = document.getElementById("permanent-taluka-input");
  const temporarytalukaInput = document.getElementById("correspondance-taluka-input");

  // const permanentdistrictInput = document.getElementById("permanent-district-input");
  const temporarydistrictInput = document.getElementById("correspondance-district-input");

  // const permanentpincodeInput = document.getElementById("permanent-pincode-input");
  const temporarypincodeInput = document.getElementById("correspondance-pincode-input");

  // const permanentcountryInput = document.getElementById("permanent-country-input");
  const temporarycountryInput = document.getElementById("correspondance-country-input");

  const dobInWordsInput = document.getElementById("dob-inwords-input");

  const appliedFor = document.getElementById("applied-for-input");

  
  temporaryAddressInput.disabled = false;
  temporarydistrictInput.disabled = false;
  temporarystateInput.disabled = false;
  temporarypincodeInput.disabled = false;
  temporarycountryInput.disabled = false;
  temporarytalukaInput.disabled = false;
  dobInWordsInput.disabled = false;
  appliedFor.disabled = false;
  return true;
}
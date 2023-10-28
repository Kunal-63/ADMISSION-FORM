document.addEventListener("DOMContentLoaded", function () {
  const username = document.getElementById("username");
  const otp = document.getElementById("otp");
  const password = document.getElementById("password");
  const confirm_password = document.getElementById("confirm_password");
  const submit = document.getElementById("submitButton");

  otp.addEventListener("input", function () {
    if (otp.value.length === 6 && /^\d+$/.test(otp.value)) {
      // User entered a 6-digit number, enable password fields
      password.disabled = false;
      confirm_password.disabled = false;
      submit.disabled = false;

    } else {
      // User hasn't entered a 6-digit number, disable password fields
      password.disabled = true;
      confirm_password.disabled = true;
      submit.disabled = true;
  
    }
  });

  

  // Rest of your code
});

function sendUsernameToFlask() {
  const usernameInput = document.getElementById("username");
  const username = usernameInput.value;

  if (username) {
    // Construct the URL with the username as a query parameter
    const url = `/send-otp?username=${username}`; // Replace with your Flask URL

    // Redirect to the URL
    window.location.href = url;
  } else {
    alert("Please enter a username.");
  }
}

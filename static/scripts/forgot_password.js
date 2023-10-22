const submitButton = document.getElementById("submitButton");
const sendOTP = document.getElementById("sendOTP");
// const FormID = document.getElementById("username");

submitButton.disabled = true;
submitButton.style.color = "#808080";
document.getElementById("otp").setAttribute("disabled", "disabled");

function sendOTPFunc() {
  if (FormID.value === "") {
    alert("Please enter your username");
    event.preventDefault();
    return false;
  } else {
    sendOTP.setAttribute("type", "button");
    // Enable form elements and update styles
    document.getElementById("password").disabled = false;
    document.getElementById("confirm_password").disabled = false;
    document.getElementById("otp").disabled = false;
    submitButton.disabled = false;
    submitButton.style.backgroundColor = "#072445";
    submitButton.style.color = "#ffffff";
    sendOTP.disabled = true;
    sendOTP.style.backgroundColor = "#808080";
    // FormID.disabled = true;
    submitButton.setAttribute("type", "submit");
    return true;
  }
}

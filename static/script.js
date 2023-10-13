document.addEventListener('DOMContentLoaded', function() {
    function PaymentGateway() {
        var options = {
            "key": "rzp_test_KBSyL22SReUzU2", 
            "amount": "100", 
            "currency": "INR",
            "name": "Airport School ",
            "description": "Test Transaction",
            "image": "templates\airport-school-logo.png",
            "handler": function (response){
                // window.location.replace('success.html');
                // window.location.href = '/submit';
                return true;
            },
            "theme": {
                "color": "#3399cc"
            }
        };
        var rzp1 = new Razorpay(options);
        rzp1.on('payment.failed', function (response){
                return false;
        });
        document.getElementById('payment-gateway').onclick = function(e){
            rzp1.open();
            e.preventDefault();
        }
    }
    

    const permanentAddressInput = document.getElementById('permanent-address-input');
    const temporaryAddressInput = document.getElementById('correspondance-address-input');
    const sameAddressCheckbox = document.getElementById('same-as-permanent-address-label-checkbox');
    const permanentstateInput = document.getElementById('permanent-state');
    const temporarystateInput = document.getElementById('correspondance-state');
    const permanentdistrictInput = document.getElementById('permanent-district');
    const temporarydistrictInput = document.getElementById('correspondance-district');
    const permanentpincodeInput = document.getElementById('permanent-pincode');
    const temporarypincodeInput = document.getElementById('correspondance-pincode');
    sameAddressCheckbox.addEventListener('change', function() {
        if (sameAddressCheckbox.checked) {
            // Copy the value of the permanent address to the temporary address
            temporaryAddressInput.value = permanentAddressInput.value;
            temporarydistrictInput.value = permanentdistrictInput.value;
            temporarystateInput.innerHTML = permanentstateInput.innerHTML;
            temporarystateInput.value = permanentstateInput.value;
            // temporarypincodeInput.innerHTML = permanentpincodeInput.innerHTML;
            temporarypincodeInput.value = permanentpincodeInput.value;
            temporaryAddressInput.disabled = true;
            temporarydistrictInput.disabled = true;
            temporarystateInput.disabled = true;
            temporarypincodeInput.disabled = true;
        } else {
            // Clear the temporary address when the checkbox is unchecked
            temporaryAddressInput.value = '';
            temporarydistrictInput.value = '';
            temporarystateInput.innerHTML = '';
            temporarypincodeInput.innerHTML = '';
            temporaryAddressInput.disabled = false;
            temporarydistrictInput.disabled = false;
            temporarystateInput.disabled = false;
            temporarypincodeInput.disabled = false;
        }
    });

    const birthdateInput = document.getElementById("dob");
    const ageYearsInput = document.getElementById("years");
    const ageMonthsInput = document.getElementById("months");
    const ageDaysInput = document.getElementById("days");
    const dobInWordsInput = document.getElementById("dob-inwords");

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
        
        // Convert milliseconds to years, months, and days
        const ageInYears = Math.floor(ageInMilliseconds / (365.25 * 24 * 60 * 60 * 1000));
        const ageInMonths = Math.floor((ageInMilliseconds % (365.25 * 24 * 60 * 60 * 1000)) / (30.44 * 24 * 60 * 60 * 1000));
        const ageInDays = Math.floor((ageInMilliseconds % (30.44 * 24 * 60 * 60 * 1000)) / (24 * 60 * 60 * 1000));
        
        // Fill the form inputs with calculated values
        ageYearsInput.value = ageInYears;
        ageYearsInput.disabled = true;
        ageMonthsInput.value = ageInMonths;
        ageMonthsInput.disabled = true;
        ageDaysInput.value = ageInDays;
        ageDaysInput.disabled = true;

        // Calculate the DOB in words
        const dobInWords = calculateDOBInWords(birthdate);
        dobInWordsInput.value = dobInWords;
        dobInWordsInput.disabled = true;
    }
    function calculateDOBInWords(birthdate) {
        const months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ];
    
        const day = birthdate.getDate();
        const month = months[birthdate.getMonth()];
        const year = birthdate.getFullYear();
    
        return `${month} ${day}, ${year}`;
    }

    const checkConnectionForm = document.getElementById("myForm");
    // const connectionStatus = document.getElementById("connectionStatus");

    // checkConnectionForm.addEventListener("submit", async (e) => {
    //     e.preventDefault();
    //     PaymentGateway();
    // })
    document.getElementById("myForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the form from submitting in the traditional way
    
        // Create a FormData object to collect all form data
        var formData = new FormData(this);
    
        // You can now access and manipulate the formData object
        // For example, you can convert it to a JSON object for further processing
        var formDataObject = {};
        formData.forEach(function(value, key) {
            formDataObject[key] = value;
        });
    
        // You can now access and manipulate the formDataObject
        console.log(formDataObject);
    });
    
});

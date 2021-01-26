const inputName = document.getElementById('tags');
const submitButton = document.getElementById('submitButton');
const form = document.getElementById('addCliForm');
submitButton.disabled = true;

inputName.addEventListener('change', function (event) {
    if (myData.includes(inputName.value)) {
        isValidClientName = true;
        inputName.style.borderColor = "green";
    } else {
        isValidClientName = false;
        inputName.style.borderColor = "red";
    }

    submitButton.disabled = !isValidClientName;

});
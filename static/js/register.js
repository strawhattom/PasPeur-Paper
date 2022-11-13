function showMessage(message, color) {
    let msg = document.getElementById("register-msg");
    msg.innerHTML = message;
    switch (color) {
        case "green":
            msg.style.color = "var(--emerald)";
            break;
        case "red":
            msg.style.color = "var(--red)";
            break;
        default:
            break;
    }
}

function checkFields(address,firstname,lastname,email,password,phone) {
    if (address.length == 0 || 
        firstname.length == 0 ||
        lastname.length == 0 ||
        email.length == 0 ||
        password.length == 0 ||
        phone.length == 0) {
        showMessage("Veuillez remplir les champs","red");
        return false;
    }

    // Check address
    if (!/^[a-zA-Z0-9\s,'-]*$/.test(address)) {
        showMessage("L'adresse invalide","red");
        return false;
    }
    // Check first name
    if (!/^(?=.{1,50}$)[a-z]+(?:['_.\s][a-z]+)*$/i.test(firstname)) {
        showMessage("Prenom invalide","red");
        return false;
    }
    // Check last name
    if (!/^(?=.{1,50}$)[a-z]+(?:['_.\s][a-z]+)*$/i.test(lastname)) {
        showMessage("Nom de famille invalide","red");
        return false;
    }
    // Check email
    if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
        showMessage("Email invalide","red");
        return false;
    }
    // Check phone number
    if (!/^(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}$/.test(phone)) {
        showMessage("Téléphone invalide","red");
        return false;
    }
    return true;
}

function register() {
    let address = document.getElementById("address").value;
    let firstname = document.getElementById("firstname").value;
    let lastname = document.getElementById("lastname").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let phone = document.getElementById("phone").value;

    if (checkFields(address,firstname,lastname,email,password,phone)) {
        showMessage("... register", "green");
    }

}
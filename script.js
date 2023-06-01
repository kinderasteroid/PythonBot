
function validateForm() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var phone = document.getElementById("phone").value;
  var password = document.getElementById("password").value;
  var cpassword = document.getElementById("confirmPassword").value;
  if(document.getElementById("terms").checked==false)
  {
      alert("Please Select the Checkbox")
  }
  else if(password!=cpassword)
  {
    alert("Confirm Passowrd and Password Dont Matct");
    
  }
  else{
    alert("Registration Sucessfull,Please Click ok to Go back to Login Page");
    window.location.replace("http://www.w3schools.com");
    
  }
  
}


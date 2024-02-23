const eye = document.querySelector(".eyetwo");
const password = document.querySelector("#pass");

console.log(eye);


eye.addEventListener("click", () => {
    if(password.type === "password"){
        password.type = "text"
    }
    else{
        password.type = "password"
    }
    if(eye.classList.contains("fa-eye-slash")){
        eye.classList.remove("fa-eye-slash");
        eye.classList.add("fa-eye");
    }else if (eye.classList.contains("fa-eye")){
        eye.classList.remove("fa-eye");
        eye.classList.add("fa-eye-slash");
    }else{
        eye.classList.add("fa-eye-slash")
    }
});

const eyeone = document.querySelector(".eyeone");
const cpassword = document.querySelector("#confirm_password");

console.log(eyeone);


eyeone.addEventListener("click", () => {
    if(cpassword.type === "password"){
        cpassword.type = "text"
    }
    else{
        confirm_password.type = "password"
    }
    if(eyeone.classList.contains("fa-eye-slash")){
        eyeone.classList.remove("fa-eye-slash")
        eyeone.classList.add("fa-eye")
    }else if  (eyeone.classList.contains("fa-eye")){
        eyeone.classList.remove("fa-eye")
        eyeone.classList.add("fa-eye-slash")
    }else{
        eyeone.classList.add("fa-eye-slash")
 
    }
})
console.log("¡Welcome to the Message's Interactive System!")

// User Data
let name = prompt("Enter your name:")
let years = prompt("Enter your age:")

//Convert age to number
years = parseInt(years);

//Validate and display messages
if (isNaN(years)) {
    console.error("Error: Please enter a valid age in numbers.");
} else if (years < 18) {
    alert(`Hello ${name}, you are a minor. ¡Keep learning and enjoy the code!`);
} else {
    alert(`Hello ${name}, you are of legal age. ¡Prepare for great opportunities in the world of programming!`)
}
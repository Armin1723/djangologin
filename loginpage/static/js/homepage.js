// Adding timeout to banner.
const banner = document.querySelector('.banner')
setTimeout(() => {
    banner.style.display = 'none';
}, 3000);

// Adding flip animation to the form
document.querySelector("#signupToggle").addEventListener('click',(event)=>{
    event.preventDefault();
    document.querySelector('#formWrapper').classList.toggle("flip");
});
document.querySelector("#loginToggle").addEventListener('click',(event)=>{
    event.preventDefault();
    document.querySelector('#formWrapper').classList.toggle("flip");
});

// Automatically showing address details upon entering zipcode.
const zipCode = document.querySelector('#zipCode')

const updateData = (details) =>{
    city.value = details.District
    state.value = details.State
    country.value = details.Country
    document.querySelector('#addressField3rd').classList.remove('d-none')
}

const fetchData = async (pincode) =>{
     await fetch(`https://api.postalpincode.in/pincode/${pincode}`)
                        .then(response => response.json())
                        .then(e => updateData(e[0].PostOffice[0]))   
}

zipCode.addEventListener('change', (e)=>{
    const pincode = e.target.value
    if (pincode.length == 6){
        fetchData(pincode);
    }
})

// Adding mouse click
clickSound = new Audio('mouseclick.wav')
const audioElement = document.querySelector('audio')
audioElement.preload = 'auto';
audioElement.load()

document.querySelector('.loginButton').addEventListener('click', ()=>{
    var click=audioElement.cloneNode();
    click.play();
})
document.querySelector('.signupButton').addEventListener('click', ()=>{
    var click=audioElement.cloneNode();
    click.play();
})
document.querySelector('.googleSignup').addEventListener('click', ()=>{
    var click=audioElement.cloneNode();
    click.play();
})
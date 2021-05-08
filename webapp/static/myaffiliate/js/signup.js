const username = document.getElementById('user')
const email = document.getElementById('mail')
const psdone = document.getElementById('pwd1')
const psdtwo = document.getElementById('pwd2')
const form = document.getElementById('form')
const button = document.getElementById('btn')
const msg = document.getElementById('message')

var userCmd = username.value === ''

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    executeCmd()
});

function executeCmd(cmd){
    if(username.value === '' && email.value ==='' && psdone.value ==='' && psdtwo.value===''){
        msg.style.color = 'red'
        msg.innerHTML = '<p> Please fill out all the fields</p>'
        setTimeout(()=> msg.remove(), 4000-1000 )
    } else if ( username.value.length >= 6){
        msg.style.color = 'red'
        msg.innerHTML = '<p> Your username is greater than 6 characters</p>'
        setTimeout(()=> msg.remove(), 4000-1000 )
    }  else {
        msg.style.color ='blue'
        msg.innerText = 'SUCCESSFULLY LOG IN'
    }
}
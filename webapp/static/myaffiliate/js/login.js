const username = document.getElementById('user')
const psdone = document.getElementById('pwd1')
const form = document.getElementById('form')
const button = document.getElementById('btn')
const msg = document.getElementById('message')
const psdRetrieve = document.getElementById('retieve')


form.addEventListener('submit', (e)=>{
    e.preventDefault()
    executeCmd()
});

function executeCmd(cmd){
    if(username.value === '' && psdone.value ===''){
        msg.style.color = 'red'
        msg.innerHTML = '<p> Please fill out all the fields</p>'
        setTimeout(()=> msg.remove(), 4000-1000 )
    } else {
        msg.style.color ='blue'
        msg.innerText = 'SUCCESSFULLY LOG IN'
    }
}
function recoveryPsd(){
    msg.style.color ='#cc3300'
    msg.innerText = 'Contact the developer to retrieve your password, coming up soon'
    setTimeout(()=> msg.remove(), 5000-1000 )
    alert('Contact the developer to retrieve your password, coming up soon')
}

const {ipcRenderer} = require('electron')

ipcRenderer.on('DisplayProfileDetails:view', (e, data) => {
    var owner = JSON.parse(data)
    var mytitle = document.querySelector("#mainTitle")
    mytitle.innerHTML = owner[1]
})

var mybtn = document.getElementById("btnHello")
mybtn.addEventListener('click', function(){
    console.log("I run...")
})
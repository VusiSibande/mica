const electron = require('electron')
const { ipcRenderer } = electron
let { PythonShell } = require('python-shell')

var data = [
    ["Unit", "Name", "Cell", "e-mail"],
]
ipcRenderer.on('owners:dataTodesktop', function(e, arg){
    var cards_deck = document.getElementById('my_cards')
    var owners = JSON.parse(arg)
    var cards_deck_str = ''
    
    for (var i=0; i<owners.length; i++) {
        var row = [
            owners[i]["unit_id"],
            owners[i]["name"],
            owners[i]["cell"],
            owners[i]["email"]
        ]
        data.push(row)
    }

    try {
        var c = 0
        var k = 1
        var colors = ['', 'success', 'warning', 'danger', 'primary', 'default']
        
        for (var i=0; i<owners.length; i++) {

            if (c == 0) {
                cards_deck_str += '<div class="card-deck">'
            }
            cards_deck_str += '<div class="card text-center border-'+colors[k]+'">' // open card tag
            cards_deck_str += '<div class="card-header">'+owners[i]["name"]+'</div>'
            cards_deck_str += '<div class="card-body">' // open card-body tag
            cards_deck_str += '<ul class="list-group">'
            cards_deck_str += '<li class="list-group-item">Unit Number: '+owners[i]["unit_id"]+'</li>'
            cards_deck_str += '<li class="list-group-item">Cell Number: '+owners[i]["cell"]+'</li>'
            cards_deck_str += '<li class="list-group-item">e-mail: '+owners[i]["email"]+'</li>'
            cards_deck_str += '</ul>'
            cards_deck_str += '<button id="pr'+owners[i]["unit_id"]+'" class="btn btn-'+colors[k]+' btn-block profile">Go To Profile</button>'
            cards_deck_str += '</div>' // close card-body tag
            cards_deck_str += '</div>' // closing card tag
            c++
            k++
            if (c == 3) {
                cards_deck_str += '</div>'
                c = 0 
            }
            if (k == colors.length) {
                k = 1
            }
        }
        // console.log(cards_deck_str)
        cards_deck.innerHTML = cards_deck_str
    } catch (err) {
        console.log('[ ERROR ]: There is an error...' + owners[i]["name"])
        console.log(err.message)
    }
})


// Add click event listeners to all profile buttons 
var card_div = document.querySelector("#my_cards")
card_div.addEventListener("click", getUserProfile, false)

function getUserProfile(e) {
    if (e.target !== e.currentTarget) {
        var clickedBtn = e.target.id
        if (e.target.classList.contains("profile")) {
            let uid
            if (clickedBtn.length > 3) {
                uid = clickedBtn.slice(2, 4)
            } else {
                uid = clickedBtn.slice(2, 3)
            }
            console.log(uid)
            talk_to_python('backend/mica_data/db_app/read_from_db.py', 'get_owner_by_id:'+uid, 'profileDetails:get')
        }
    }
    e.stopPropagation()
}


function talk_to_python(script_path, msg, channel) {
    var pyshell = new PythonShell(script_path)
    pyshell.send(msg)

    pyshell.on('message', function(data_from_python){
        console.log(data_from_python)
        ipcRenderer.send(channel, data_from_python)
    })

    pyshell.end(function (err) {
        if (err) {
            throw err
        }
        console.log("finished getting python data")
    })
}


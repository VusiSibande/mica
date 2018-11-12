const electron = require('electron')
const { app, BrowserWindow, Menu, ipcMain } = require('electron')
const path = require('path')
const url = require('url')
const spawn = require('child_process').spawn
let { PythonShell } = require('python-shell')

let win
let detailsWin

// entry point finction 
function createWindow() {
    win = new BrowserWindow({
        width: 1000,
        height: 600,
        backgroundColor: '#312450'
    })

    win.loadURL(url.format({
        pathname: path.join(__dirname, 'frontend/index.html'),
        protocol: 'file',
        slashes: true
    }))

    win.webContents.openDevTools()

    win.on('closed', () => {
        app.quit()
        win = null
    })

    // Build menu from template and add it to our app
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate)
    Menu.setApplicationMenu(mainMenu)

    
    win.webContents.on('did-finish-load', () => {
        talk_to_python('backend/mica_data/db_app/read_from_db.py','get_all_owners', win, 'owners:dataTodesktop')
    })
}

function talk_to_python(script_path, msg, my_window, channel) {
    var pyshell = new PythonShell(script_path)
    pyshell.send(msg)

    pyshell.on('message', function(data_from_python){
        console.log(data_from_python)
        my_window.webContents.send(channel, data_from_python)
    })

    pyshell.end(function (err) {
        if (err) {
            throw err
        }
        console.log("finished getting python data")
    })
}

// create details window
function createDetailsWindow() {
    detailsWin = new BrowserWindow({
        width: 800,
        height: 600,
        backgroundColor: '#312450'
    })

    detailsWin.loadURL(url.format({
        pathname: path.join(__dirname, 'frontend/details.html'),
        protocol: 'file',
        slashes: true
    }))

    detailsWin.webContents.openDevTools()

    detailsWin.on('closed', () => {
        detailsWin = null
    })
}

// Inter-process communication
ipcMain.on('owners:get', function() {
    win.webContents.send('owners:dataTodesktop', data)
})

ipcMain.on('profileDetails:get', function(e, btnID) {
    // Open detailsWin
    createDetailsWindow()

    // Get Profile data from python 
    console.log(btnID)

    // Send data to detailsWin
    detailsWin.webContents.on('did-finish-load', () => {
        detailsWin.webContents.send('DisplayProfileDetails:view', btnID)
    })
})

app.on('ready', createWindow)

// Menu Template
const mainMenuTemplate = [
    {
        label: 'File',
        submenu:[
            {
                label: 'Details',
                click() {
                    createDetailsWindow()
                }
            },
            {
                label: 'Refresh',
                click() {
                    // Add refresh data function 
                }
            },
            {
                label: 'Quit',
                accelerator: process.platform == 'darwin' ? 'Command+Q': 'Ctrl+Q',
                click() {
                    app.quit()
                }
            }
        ]
    }
]

// Taking care the menuspace bug in mac os
if (process.platform == 'darwin') {
    mainMenuTemplate.unshift({})
}
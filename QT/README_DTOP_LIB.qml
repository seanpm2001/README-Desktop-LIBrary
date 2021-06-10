// Import section
import QtQuick 2.0
// import @ReadmeSettings {Coming soon}
// import Bezels
// import syntax
// import xorg
// import Qt

// Start of script

// This is the main script for the library, it is written in QML

// Please note I am not the best at QML, I don't know what the output will look like either, as I don't have a compiler ready. This may be bad code, and may not compile

Item {
     id: readmeTop
     width: 10000; height: 225

     Rectangle {
         id: myRect
         width: 100; height: 100
         color: "red"
     }
     states: [
         State {
             name: "moved"
             PropertyChanges {
                 target: myRect
                 x: 50
                 y: 50
             }
         }
     ]
     MouseArea {
         anchors.fill: parent
         onClicked: myItem.state = 'moved'
     }
 }
// This is just a sample file, I needed to start with some other files first. It is in very early development.

/* File info
* File type: QML Source file (*.qml)
* File version: 1 (Wednesday, June 9th 2021 at 9:17 pm)
* Line count (including blank lines and compiler line): 48
*/

// End of script

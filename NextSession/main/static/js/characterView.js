var table = document.getElementById('att-table')
var attributes = document.querySelectorAll('#attributeValue')
var mods = document.querySelectorAll('#attributeMod')

function modValues(){
    for(i=0; i< attributes.length; i++){
        mods[i].innerHTML = Math.floor(((attributes[i].innerHTML)-10)/2)
    }
}

console.log(table)
table.addEventListener("load", modValues())
console.log(attributes[0].innerHTML)



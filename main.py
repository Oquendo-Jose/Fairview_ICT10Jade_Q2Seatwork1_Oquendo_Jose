from pyscript import document, display

def checkname(e):
    na_mes= ["Gavin Taguiga", "Hans Arada", "Isaias Berdin", "Carlos Borromeo"]
    name= document.getElementById("name").value
    lastname= document.getElementById("lastname").value

    variableing= name + " " + lastname
 
    name= "my goat"
    name= document.getElementById("name").value

    confirm_num = variableing in na_mes

    message = (f'Sorry {name}, your number is not found.' , f'Yay! {name}, your number is found.')

    document.getElementById("output1").innerHTML = message[confirm_num]

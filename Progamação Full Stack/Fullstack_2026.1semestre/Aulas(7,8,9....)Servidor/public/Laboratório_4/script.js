let a = Math.floor(Math.random()*100)

function verificando(){
    let x = document.getElementById("numero").value
    if(x < a){
        document.getElementById("resposta").innerHTML = "número muito pequeno"
        document.getElementById("resposta").style.setProperty("background-color", "red")
    }else if(x > a){
        document.getElementById("resposta").innerHTML = "número muito grande"
        document.getElementById("resposta").style.setProperty("background-color", "red")

    }else{
        document.getElementById("resposta").innerHTML = "você acertou"
        document.getElementById("resposta").style.setProperty("background-color", "green")

    }
    console.log(a)
    console.log(x)
}


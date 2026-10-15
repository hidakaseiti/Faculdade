let a = Math.floor(Math.random()*100)

function verificando(){
    let x = document.getElementById("numero").value
    if(x < a){
        document.getElementById("resposta").innerHTML = "número muito pequeno"
    }else if(x > a){
        document.getElementById("resposta").innerHTML = "número muito grande"
    }else{
        document.getElementById("resposta").innerHTML = "você acertou"
    }
    console.log(a)
    console.log(x)
}
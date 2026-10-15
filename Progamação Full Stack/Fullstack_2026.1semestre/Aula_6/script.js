//let nome = prompt('Coloque o seu nome!');//

console.log(nome);

console.log(document.getElementById('nome').innerHTML);

//atribuindo um novo valor para uma variavel ja atribuida,e ser mostrado no site//
document.getElementById('nome').innerHTML = nome;

//EXEMPLO1//
//let nomeexemplo1 = prompt('Qual o seu nome?');
//let idade = prompt('Qual a sua idade?');
//let ano_atual = 2026;

//let ano_nascimento = ano_atual - idade;
//let resposta_1 = 'Olá ' + nomeexemplo1 + ',seu ano de nascimento é ' + ano_nascimento + '!';

//document.getElementById('R1').innerHTML = resposta_1;

//funções//

function soma(a , b){
    return a + b;
}

let c = soma(7,9);
console.log(c);

//function imprimir(){
//    let i1 = document.getElementById('i1').value;
//    console.log(i1);
//}

//EXEMPLO2//
function ex2(){
    let x = document.getElementById("ex2_i").value;
    let resposta = "";
    for (let i = 0; i <= x; i++){
        resposta += " " + i;
    }
    document.getElementById("R2").innerHTML = resposta;
}

//EXEMPLO3//
function ex3(){
    let A = parseInt(document.getElementById("ex3_a").value);
    let B = parseInt(document.getElementById("ex3_b").value);

    let C = soma(A, B);

    document.getElementById("R3").innerHTML = C;
}

//EXEMPLO4//
function multi(a , b){
    return a * b;
}
function ex4(){
    let A = parseInt(document.getElementById("ex4_a").value);
    let B = parseInt(document.getElementById("ex4_b").value);

    let C;    
    if(A < 0 || B < 0){
        C = soma(A, B);
    }else{
        C = multi(A, B);
    }

    document.getElementById('R4').innerHTML = C;
}
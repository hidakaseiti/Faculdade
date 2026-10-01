// alert("Olá");
// console.log('Oi');
// assim que se faz comentários, as 2 primeiras linhas foram tiradas só para não ficarem aparecendo

x = prompt("Informe o seu nome");
console.log("Seu nome é " + x);
alert("Seu nome é " + x)

// Exercício 1:
for(i=1; i<=100; i++){
    if(i%2===1 || i===1){
        console.log(i)
    }
}

// Solução prof:
i = 1;
while(i<=100) {
    console.log(i);
    i += 2;
}

i = 0;
while(i <= 100) {
    if(i%2){
        console.log(i);
    }
    i++;
}

//Exercício 2:
for(i = 5; i<=500; i+=5){
    console.log(i)
}

//Exercício 3:
x = prompt("informe um número inteiro positivo");
for(i = x; i == 0; i--){
    console.log(i)
}
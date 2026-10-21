let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

// retângulos
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'blue';
ctx.strokeStyle = 'red';
ctx.fillRect(10,10,50,50); //(x,y,largura,largura)
ctx.strokeRect(10,10,50,50);
ctx.closePath();

// linhas
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'blue';
ctx.strokeStyle = 'red';
ctx.moveTo(200,150);
ctx.lineTo(60,10); //(onde toca,até onde vai)
ctx.lineTo(60,250);
ctx.lineTo(200,250);
ctx.lineTo(200,150);
ctx.fill();
ctx.stroke();
ctx.closePath();

// arcos
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'blue';
ctx.strokeStyle = 'red';
ctx.arc(200,200,50,1.5*Math.PI,2.5*Math.PI); //(x,y(do centro do arco),raio,onde começa(radianos),onde termina o arco(radianos))
ctx.fill();
ctx.stroke();
ctx.closePath();

// texto
ctx.beginPath();
ctx.lineWidth = 2;
ctx.fillStyle = 'blue';
ctx.strokeStyle = 'red';
ctx.font = "90px Arial"
ctx.textAlign = "center";
ctx.fillText("Olá",200,350);
ctx.strokeText("Olá",200,350)
ctx.closePath();

//Exercício 1
let canvas1 = document.getElementById('a');
let ctx1 = canvas1.getContext('2d');

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.fillStyle = 'red';
ctx1.fillRect(0,0,50,50); //(x,y,largura,largura)
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.fillStyle = 'blue';
ctx1.fillRect(350,0,50,50); //(x,y,largura,largura)
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.fillStyle = 'yellow';
ctx1.fillRect(0,350,50,50); //(x,y,largura,largura)
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.fillStyle = 'green';
ctx1.fillRect(350,350,50,50); //(x,y,largura,largura)
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.strokeStyle = 'red';
ctx1.moveTo(0,0);
ctx1.lineTo(400,400); //(onde toca,até onde vai)
ctx1.stroke();
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.strokeStyle = 'blue';
ctx1.moveTo(400,0);
ctx1.lineTo(0,400); //(onde toca,até onde vai)
ctx1.stroke();
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.strokeStyle = 'green';
ctx1.moveTo(0,200);
ctx1.lineTo(400,200); //(onde toca,até onde vai)
ctx1.stroke();
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.strokeStyle = 'green';
ctx1.arc(200,200,75,0*Math.PI,1*Math.PI);
ctx1.stroke();
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.fillStyle = 'yellow'
ctx1.strokeStyle = 'green';
ctx1.arc(50,140,25,0*Math.PI,2*Math.PI);
ctx1.fill();
ctx1.stroke();
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.fillStyle = 'yellow';
ctx1.strokeStyle = 'green';
ctx1.arc(350,140,25,0*Math.PI,2*Math.PI);
ctx1.fill();
ctx1.stroke();
ctx1.closePath();

ctx1.beginPath();
ctx1.lineWidth = 2;
ctx1.fillStyle = 'blue';
ctx1.strokeStyle = 'red';
ctx1.font = "20px Arial"
ctx1.textAlign = "center";
ctx1.fillText("Desenvolvimento Web",200,100);
ctx1.strokeText("Desenvolvimento Web",200,100)
ctx1.closePath();


//Exercício 2
let canvas2 = document.getElementById('b');
let ctx2 = canvas2.getContext('2d')



//Vetores
let idades = [22,98]
console.log(idades);
console.log(idades.length);

idades.push(25);
console.log(idades);

idades.pop();
console.log(idades);

//criando um objeto:retangulo introducao orientacao ao objeto
let canvas3 = document.getElementById("canvas3");
let ctx3 = canvas3.getContext("2d");

let canvas4 = document.getElementById("canvas4");
let ctx4 = canvas4.getContext("2d");

let canvas5 = document.getElementById("canvas5");
let ctx5 = canvas5.getContext("2d");

let retangulo1 = {
    x: 10,
    y: 10,
    l: 50,
    a: 50,
    cor_fill: "red",
    cor_stroke: "green",

    desenha: function(ctx3, cor_fill, cor_stroke){
        ctx3.beginPath();
        ctx3.lineWidth = 2;
        ctx3.fillStyle = this.cor_fill;
        ctx3.strokeStyle = this.cor_stroke;
        ctx3.fillRect(this.x,this.y,this.l,this.a);
        ctx3.strokeRect(this.x,this.y,this.l,this.a);
        ctx3.closePath();
    }
}

let retangulo2 = {
    x: 10,
    y: 10,
    l: 50,
    a: 50,
    cor_fill: "blue",
    cor_stroke: "blue",

    desenha: function(ctx4, cor_fill, cor_stroke){
        ctx4.beginPath();
        ctx4.lineWidth = 2;
        ctx4.fillStyle = this.cor_fill;
        ctx4.strokeStyle = this.cor_stroke;
        ctx4.fillRect(this.x,this.y,this.l,this.a);
        ctx4.strokeRect(this.x,this.y,this.l,this.a);
        ctx4.closePath();
    }
}

let retangulo3 = {
    x: 10,
    y: 10,
    l: 50,
    a: 50,
    cor_fill: "yellow",
    cor_stroke: "green",

    desenha: function(ctx5, cor_fill, cor_stroke){
        ctx5.beginPath();
        ctx5.lineWidth = 2;
        ctx5.fillStyle = this.cor_fill;
        ctx5.strokeStyle = this.cor_stroke;
        ctx5.fillRect(this.x,this.y,this.l,this.a);
        ctx5.strokeRect(this.x,this.y,this.l,this.a);
        ctx5.closePath();
    }
}

retangulo1.desenha(ctx3);
retangulo2.desenha(ctx4);
retangulo3.desenha(ctx5);

let aux = 2;
function animacao(){
    //apagar o canvas
    ctx3.clearRect(0,0,400,400);
    ctx4.clearRect(0,0,400,400);
    ctx5.clearRect(0,0,400,400);

    //atualizar o objeto
    if(retangulo1.x >= 360){
        aux = -2;
    }else if(retangulo1.x <= 0){
        aux = 2;
    }
    retangulo1.x += aux;


    //desenhar novamente
    retangulo1.desenha(ctx3)
    requestAnimationFrame(animacao)
    retangulo2.desenha(ctx4)
    retangulo3.desenha(ctx5)

}

animacao();

document.addEventListener("keydown",function(evento){
    console.log(evento);
    let tecla = evento.key;
    if(tecla == "ArrowUp"){retangulo2.y -= 2};
    if(tecla == "ArrowDown"){retangulo2.y += 2};
    if(tecla == "ArrowLeft"){retangulo2.x -= 2};
    if(tecla == "ArrowRight"){retangulo2.x += 2};
})

document.addEventListener("mousemove", function(evento){
    console.log(evento);
    let rect = canvas5.getBoundingClientRect();
    let x_mouse = evento.clientX - rect.left;
    let y_mouse = evento.clientY - rect.top;
    console.log(x_mouse, y_mouse);

    retangulo3.x = x_mouse;
    retangulo3.y = y_mouse;
})
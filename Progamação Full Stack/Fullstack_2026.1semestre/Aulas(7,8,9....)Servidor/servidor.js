let colors = require("colors");
let http = require("http");
let express = require("express");

let bodyParser = require("body-parser")

let app = express();
app.use(express.static("./public"));

app.use(bodyParser.urlencoded({extended: false })) //para conseguir usar o post,são necessarias essas duas linhas //
app.use(bodyParser.json())


app.set("view engine","ejs"); //para conseguir usar os templates,são necessarias essas duas linhas//
app.set("views","./views");


let server = http.createServer(app);
server.listen(80);

console.log('Servidor rodando ...'.rainbow);

app.get("/", function(req,res){
    res.redirect("index.html");
})

app.get("/cadastrar", function(req,res){
    let nome = req.query.nome;
    let login = req.query.login;
    let senha = req.query.senha;
    console.log(nome, login, senha);

    res.render("resposta.ejs",{
        resposta:"Usuário cadastrado!",
        metodo: "Enviado pelo metodo Get"
         })
})


app.post("/cadastrar", function(req, res){
    let nome = req.body.nome;
    let login = req.body.login;
    let senha = req.body.senha;
    console.log(nome, login, senha);

    res.render("resposta.ejs",{
        resposta:"Login feito!",
        metodo: "Enviado pelo metodo Post"
         })
})

app.get("/for", function(req,res){
    let qtde = req.query.qtde;
    console.log(qtde);
    res.render("for.ejs", {qtde}) //qtde ja e uma variavel,da pra colocar direto
})

// LAB 8

let log_salvo = ""
let sen_salva = ""

app.get("/Cad", function(req,res){
    let nome = req.query.nome;
    let login = req.query.login;
    let senha = req.query.senha;
    console.log(nome, login, senha);
    
    log_salvo = login;
    sen_salva = senha;

    res.render("resposta.ejs",{
        resposta:"Usuário cadastrado!"
         })
})

app.post("/Log", function(req, res){
    let nome = req.body.nome;
    let login = req.body.login;
    let senha = req.body.senha;
    console.log(nome, login, senha);

    if(log_salvo == login && sen_salva == senha){
        res.render("resposta.ejs",{
        resposta:"Login feito!"
        })
}})

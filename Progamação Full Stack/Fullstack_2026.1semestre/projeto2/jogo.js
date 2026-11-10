/* =====================================================================
   RUMO AO ESPAÇO - versão 2 (2 jogadores + sprites)

   NOVIDADES:
   - Dois jogadores: J1 (W A D / Espaço) e J2 (setas). Corrida até o espaço.
   - Cada zona tem desenhos próprios (caveira, avião, nuvem, satélite,
     meteoro) feitos no código. Se você colocar o caminho de uma imagem
     PNG na zona, ela é usada no lugar do desenho.

   COORDENADAS: o Y cresce para BAIXO. O chão fica em y = 0 e, quanto
   mais alto o jogador vai, mais NEGATIVO fica o y. Altitude = -y.
   ===================================================================== */


/* ================== 1. CONFIGURAÇÕES ================== */
const CFG = {
  doisJogadores: true,        // false = só o jogador 1
  gravidade: 0.55,
  forcaPulo: -13,
  velocidade: 4,
  metaAltura: 5000,           // altitude para vencer
  distPlataformas: [75, 110], // distância vertical mínima e máxima entre plataformas
  chanceObstaculo: 0.3,
  velPerigoBase: 0.35         // velocidade do perigo que sobe de baixo
};

/* ---------- JOGADORES ----------
   Cada jogador tem:
   - nome e cor (usada se não houver imagem)
   - teclas: listas de códigos de tecla para esquerda, direita e pulo
     (códigos de tecla: "KeyA", "ArrowLeft", "Space"... )
   - img: caminho de uma imagem (ou null para usar o quadradinho colorido) */
const JOGADORES_CFG = [
  { nome: "J1", cor: "#ffd700", img: null,   // ex: img: "img/jogador1.png"
    teclas: { esq: ["KeyA"], dir: ["KeyD"], pulo: ["KeyW", "Space"] } },
  { nome: "J2", cor: "#ff5fa2", img: null,   // ex: img: "img/jogador2.png"
    teclas: { esq: ["ArrowLeft"], dir: ["ArrowRight"], pulo: ["ArrowUp"] } }
];

/* ---------- ZONAS ----------
   - ate: até qual altitude a zona vai
   - fundo / plat / obst / perigo: cores
   - imgPlat / imgObst: caminho da imagem (null = usa o desenho do código)
       Exemplo: imgObst: "img/caveira.png"
   - desenhaPlat / desenhaObst: funções que desenham o padrão (seção 7)
   A ÚLTIMA zona deve ter um "ate" bem grande (nunca acaba). */
const ZONAS = [
  { nome: "Subterrâneo", ate: 1500, fundo: "#3b2a1e", plat: "#8d6e4c", obst: "#c0392b",
    perigo: "#ff6a00", perigoNome: "Lava",
    imgPlat: null, imgObst: null,
    desenhaPlat: desenharRocha, desenhaObst: desenharCaveira },

  { nome: "Céu", ate: 3500, fundo: "#6ec6ff", plat: "#ffffff", obst: "#444444",
    perigo: "#555a6e", perigoNome: "Tempestade",
    imgPlat: null, imgObst: null,
    desenhaPlat: desenharNuvem, desenhaObst: desenharAviao },

  { nome: "Espaço", ate: 99999, fundo: "#05051a", plat: "#9aa0b5", obst: "#b44cff",
    perigo: "#7a00cc", perigoNome: "Buraco negro",
    imgPlat: null, imgObst: null,
    desenhaPlat: desenharSatelite, desenhaObst: desenharMeteoro }
];


/* ================== 2. CARREGAMENTO DE IMAGENS ==================
   Cria um objeto Image para cada caminho informado. A imagem só é
   usada quando terminou de carregar (img.complete) e não deu erro
   (naturalWidth > 0). Se o arquivo não existir, o jogo usa o desenho. */
function carregarImagem(caminho) {
  if (!caminho) return null;      // sem caminho = sem imagem
  const img = new Image();
  img.src = caminho;
  return img;
}
const imagemPronta = img => img && img.complete && img.naturalWidth > 0;

// Guarda a imagem carregada dentro de cada zona e de cada jogador
ZONAS.forEach(z => {
  z.imagemPlat = carregarImagem(z.imgPlat);
  z.imagemObst = carregarImagem(z.imgObst);
});
JOGADORES_CFG.forEach(c => c.imagem = carregarImagem(c.img));


/* ================== 3. PREPARAÇÃO (canvas e teclado) ================== */
const canvas = document.getElementById("jogo");
const ctx = canvas.getContext("2d");
const W = canvas.width;
const H = canvas.height;

const teclas = {};   // teclas["KeyA"] = true enquanto A estiver apertada

addEventListener("keydown", e => {
  teclas[e.code] = true;
  if (["Space", "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(e.code)) e.preventDefault();
  if (e.code === "KeyR") iniciar();
});
addEventListener("keyup", e => teclas[e.code] = false);

// Devolve true se QUALQUER tecla da lista estiver apertada.
// Ex: apertada(["KeyW","Space"]) -> true se W ou Espaço estiver apertado.
const apertada = lista => lista.some(codigo => teclas[codigo]);

// Estado do jogo
let jogadores;     // LISTA de jogadores (antes era um só)
let plataformas, obstaculos, estrelas;
let camY, perigoY, ultimoY, frames;
let estado;        // "jogando", "perdeu" ou "ganhou"
let vencedor;      // jogador que chegou à meta (quando estado = "ganhou")


/* ================== 4. FUNÇÕES AUXILIARES ================== */
const aleat = (a, b) => a + Math.random() * (b - a);

// Altitude de UM jogador
const altDe = j => Math.max(0, Math.floor(-j.y));

// O "líder" é o jogador mais alto que ainda está vivo.
// Se todos morreram, é o mais alto entre todos. A câmera, a zona e a
// velocidade do perigo seguem o líder.
function lider() {
  const vivos = jogadores.filter(j => j.vivo);
  const lista = vivos.length > 0 ? vivos : jogadores;
  return lista.reduce((a, b) => (b.y < a.y ? b : a));   // menor y = mais alto
}

const zonaDe = alt => ZONAS.find(z => alt < z.ate);

function colide(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x &&
         a.y < b.y + b.h && a.y + a.h > b.y;
}


/* ================== 5. INICIAR / REINICIAR ================== */
function iniciar() {
  // Cria 1 ou 2 jogadores a partir de JOGADORES_CFG
  const quantos = CFG.doisJogadores ? 2 : 1;
  jogadores = JOGADORES_CFG.slice(0, quantos).map((c, i) => ({
    cfg: c,                              // guarda nome, cor, teclas, imagem
    x: (W / (quantos + 1)) * (i + 1) - 14, // espalha os jogadores no chão
    y: -50, w: 28, h: 28,
    vx: 0, vy: 0, noChao: false,
    vivo: true
  }));

  plataformas = [{ x: 0, y: 0, w: W, h: 20 }];   // chão
  obstaculos = [];
  estrelas = Array.from({ length: 60 }, () => ({
    x: Math.random() * W, y: Math.random() * H, t: Math.random() * 2 + 1
  }));

  ultimoY = 0;
  camY = -H + 120;
  perigoY = 250;
  estado = "jogando";
  vencedor = null;
  frames = 0;
  gerarMundo();
}


/* ================== 6. GERAÇÃO DO MUNDO ================== */
function gerarMundo() {
  while (ultimoY > camY - 800) {
    ultimoY -= aleat(...CFG.distPlataformas);

    const larg = aleat(70, 110);
    plataformas.push({ x: aleat(0, W - larg), y: ultimoY, w: larg, h: 14 });

    if (Math.random() < CFG.chanceObstaculo && -ultimoY > 200) {
      obstaculos.push({
        x: aleat(0, W - 32),
        y: ultimoY - aleat(30, 55),
        w: 32, h: 24,       // tamanho do obstáculo (ajuste se seus sprites forem maiores)
        vx: (Math.random() < 0.5 ? -1 : 1) * aleat(1.2, 2.5)
      });
    }
  }
  plataformas = plataformas.filter(p => p.y < camY + H + 300);
  obstaculos = obstaculos.filter(o => o.y < camY + H + 300);
}


/* ================== 7. DESENHOS PADRÃO (sem imagem) ==================
   Cada função recebe o objeto (plataforma p ou obstáculo o) e desenha
   usando só formas do canvas. São o "plano B" quando não há PNG. */

// ---- Subterrâneo ----
function desenharRocha(p) {
  ctx.fillStyle = "#8d6e4c";
  ctx.fillRect(p.x, p.y, p.w, p.h);
  ctx.fillStyle = "#a98a64";                 // faixa clara em cima
  ctx.fillRect(p.x, p.y, p.w, 4);
  ctx.fillStyle = "#6b5238";                 // pedrinhas escuras
  for (let i = 10; i < p.w - 6; i += 22) ctx.fillRect(p.x + i, p.y + 8, 6, 3);
}

function desenharCaveira(o) {
  const cx = o.x + o.w / 2, cy = o.y + o.h / 2;
  ctx.fillStyle = "#f2f2f2";
  ctx.beginPath(); ctx.arc(cx, cy - 2, 10, 0, Math.PI * 2); ctx.fill();   // crânio
  ctx.fillRect(cx - 6, cy + 5, 12, 6);                                     // mandíbula
  ctx.fillStyle = "#000";
  ctx.beginPath(); ctx.arc(cx - 4, cy - 3, 2.5, 0, Math.PI * 2); ctx.fill(); // olho
  ctx.beginPath(); ctx.arc(cx + 4, cy - 3, 2.5, 0, Math.PI * 2); ctx.fill(); // olho
  ctx.fillRect(cx - 1, cy + 1, 2, 3);                                        // nariz
  ctx.fillStyle = "#999";                                                    // dentes
  for (let i = -4; i <= 2; i += 3) ctx.fillRect(cx + i, cy + 7, 1, 4);
}

// ---- Céu ----
function desenharNuvem(p) {
  ctx.fillStyle = "#ffffff";
  ctx.beginPath(); ctx.ellipse(p.x + p.w / 2, p.y + 9, p.w / 2, 6, 0, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(p.x + p.w * 0.30, p.y + 8, 6, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(p.x + p.w * 0.55, p.y + 7, 7, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(p.x + p.w * 0.78, p.y + 9, 5, 0, Math.PI * 2); ctx.fill();
}

function desenharAviao(o) {
  ctx.save();
  ctx.translate(o.x + o.w / 2, o.y + o.h / 2);   // origem no centro do avião
  if (o.vx < 0) ctx.scale(-1, 1);                // espelha quando vai para a esquerda
  ctx.fillStyle = "#d9d9d9";                     // fuselagem
  ctx.beginPath(); ctx.ellipse(0, 0, 15, 5, 0, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = "#c0392b";                     // asas
  ctx.beginPath(); ctx.moveTo(-2, 0); ctx.lineTo(-8, -11); ctx.lineTo(3, 0); ctx.fill();
  ctx.beginPath(); ctx.moveTo(-2, 0); ctx.lineTo(-8, 11);  ctx.lineTo(3, 0); ctx.fill();
  ctx.beginPath(); ctx.moveTo(-15, 0); ctx.lineTo(-15, -7); ctx.lineTo(-10, -1); ctx.fill(); // cauda
  ctx.fillStyle = "#3498db";                     // janela
  ctx.fillRect(5, -3, 5, 3);
  ctx.restore();
}

// ---- Espaço ----
function desenharSatelite(p) {
  const corpoW = p.w * 0.36;
  const corpoX = p.x + (p.w - corpoW) / 2;
  ctx.fillStyle = "#2b6cb0";                     // painéis solares
  ctx.fillRect(p.x, p.y + 2, p.w * 0.30, p.h - 4);
  ctx.fillRect(p.x + p.w * 0.70, p.y + 2, p.w * 0.30, p.h - 4);
  ctx.fillStyle = "#7fb3e8";                     // divisões dos painéis
  for (let i = 1; i < 3; i++) {
    ctx.fillRect(p.x + (p.w * 0.30 / 3) * i, p.y + 2, 1, p.h - 4);
    ctx.fillRect(p.x + p.w * 0.70 + (p.w * 0.30 / 3) * i, p.y + 2, 1, p.h - 4);
  }
  ctx.fillStyle = "#b8bccc";                     // corpo
  ctx.fillRect(corpoX, p.y, corpoW, p.h);
  ctx.fillStyle = "#555";                        // antena
  ctx.fillRect(corpoX + corpoW / 2 - 1, p.y - 3, 2, 4);
}

function desenharMeteoro(o) {
  const cx = o.x + o.w / 2, cy = o.y + o.h / 2, r = Math.min(o.w, o.h) / 2;
  ctx.fillStyle = "#ff8a00";                     // chama atrás
  const lado = o.vx > 0 ? -1 : 1;
  ctx.beginPath();
  ctx.moveTo(cx + lado * r * 0.5, cy - r * 0.7);
  ctx.lineTo(cx + lado * (r + 8), cy);
  ctx.lineTo(cx + lado * r * 0.5, cy + r * 0.7);
  ctx.fill();
  ctx.fillStyle = "#8a6d5a";                     // rocha
  ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = "#5e4838";                     // crateras
  ctx.beginPath(); ctx.arc(cx - 4, cy - 3, 3, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); ctx.arc(cx + 4, cy + 4, 2.5, 0, Math.PI * 2); ctx.fill();
}


/* ================== 8. FUNÇÕES DE DESENHO COM SPRITE ==================
   Cada uma tenta usar a imagem; se não houver, chama o desenho padrão. */

function desenharJogador(j) {
  const img = j.cfg.imagem;
  if (imagemPronta(img)) {
    ctx.drawImage(img, j.x, j.y, j.w, j.h);
  } else {
    ctx.fillStyle = j.cfg.cor;                   // quadradinho colorido
    ctx.fillRect(j.x, j.y, j.w, j.h);
    ctx.fillStyle = "#000";                      // olhos
    ctx.fillRect(j.x + 7, j.y + 8, 5, 5);
    ctx.fillRect(j.x + 17, j.y + 8, 5, 5);
  }
  // Etiqueta com o nome acima do jogador (para saber quem é quem)
  ctx.fillStyle = j.cfg.cor;
  ctx.font = "bold 11px sans-serif";
  ctx.textAlign = "center";
  ctx.fillText(j.cfg.nome, j.x + j.w / 2, j.y - 4);
}

function desenharPlataforma(p, z) {
  if (imagemPronta(z.imagemPlat)) ctx.drawImage(z.imagemPlat, p.x, p.y, p.w, p.h);
  else z.desenhaPlat(p);
}

function desenharObstaculo(o, z) {
  if (imagemPronta(z.imagemObst)) {
    // Espelha a imagem quando o obstáculo anda para a esquerda
    // (a imagem original deve olhar para a DIREITA)
    ctx.save();
    if (o.vx < 0) {
      ctx.translate(o.x + o.w, o.y);
      ctx.scale(-1, 1);
      ctx.drawImage(z.imagemObst, 0, 0, o.w, o.h);
    } else {
      ctx.drawImage(z.imagemObst, o.x, o.y, o.w, o.h);
    }
    ctx.restore();
  } else {
    z.desenhaObst(o);
  }
}


/* ================== 9. ATUALIZAÇÃO ================== */
function atualizar() {
  if (estado !== "jogando") return;
  frames++;

  // ---- Cada jogador vivo é atualizado separadamente ----
  for (const j of jogadores) {
    if (!j.vivo) continue;
    const t = j.cfg.teclas;

    // Movimento horizontal (usa as teclas DESTE jogador)
    j.vx = 0;
    if (apertada(t.esq)) j.vx = -CFG.velocidade;
    if (apertada(t.dir)) j.vx =  CFG.velocidade;
    j.x += j.vx;
    if (j.x + j.w < 0) j.x = W;
    if (j.x > W) j.x = -j.w;

    // Pulo
    if (apertada(t.pulo) && j.noChao) {
      j.vy = CFG.forcaPulo;
      j.noChao = false;
    }

    // Gravidade e pouso em plataformas
    const yAntes = j.y + j.h;
    j.vy += CFG.gravidade;
    j.y += j.vy;
    j.noChao = false;

    if (j.vy >= 0) {
      for (const p of plataformas) {
        const sobrepoeX = j.x + j.w > p.x && j.x < p.x + p.w;
        if (sobrepoeX && yAntes <= p.y && j.y + j.h >= p.y) {
          j.y = p.y - j.h;
          j.vy = 0;
          j.noChao = true;
        }
      }
    }

    // Colisão com obstáculos
    for (const o of obstaculos) {
      if (colide(j, o)) j.vivo = false;
    }

    // Tocou no perigo que sobe
    if (j.y + j.h > perigoY) j.vivo = false;
  }

  // ---- Obstáculos se movem (uma vez por frame, fora do loop dos jogadores) ----
  for (const o of obstaculos) {
    o.x += o.vx;
    if (o.x < 0 || o.x + o.w > W) o.vx *= -1;
  }

  // ---- Câmera segue o líder ----
  const lid = lider();
  camY = Math.min(camY, lid.y - H * 0.45);

  // Quem ficou para baixo da tela cai e morre
  for (const j of jogadores) {
    if (j.vivo && j.y > camY + H) j.vivo = false;
  }

  // ---- Perigo que sobe ----
  if (frames > 180) {
    const zonaIdx = ZONAS.indexOf(zonaDe(altDe(lid)));
    perigoY -= CFG.velPerigoBase + zonaIdx * 0.1;
  }
  perigoY = Math.min(perigoY, camY + H + 150);

  // ---- Vitória: o primeiro vivo a chegar na meta ganha ----
  const campeao = jogadores.find(j => j.vivo && altDe(j) >= CFG.metaAltura);
  if (campeao) { estado = "ganhou"; vencedor = campeao; }

  // ---- Derrota: todos mortos ----
  if (estado === "jogando" && jogadores.every(j => !j.vivo)) estado = "perdeu";

  gerarMundo();
}


/* ================== 10. DESENHO DA TELA ================== */
function desenhar() {
  const lid = lider();
  const z = zonaDe(altDe(lid));

  // Fundo
  ctx.fillStyle = z.fundo;
  ctx.fillRect(0, 0, W, H);
  if (z.nome === "Espaço") {
    ctx.fillStyle = "#fff";
    for (const e of estrelas) ctx.fillRect(e.x, e.y, e.t, e.t);
  }

  // Mundo (com câmera)
  ctx.save();
  ctx.translate(0, -camY);
  plataformas.forEach(p => desenharPlataforma(p, z));
  obstaculos.forEach(o => desenharObstaculo(o, z));
  jogadores.forEach(j => { if (j.vivo) desenharJogador(j); });   // só desenha vivos
  ctx.fillStyle = z.perigo;
  ctx.fillRect(0, perigoY, W, H + 400);
  ctx.restore();

  // HUD
  ctx.fillStyle = z.nome === "Céu" ? "#000" : "#fff";
  ctx.font = "bold 16px sans-serif";
  ctx.textAlign = "left";
  ctx.fillText("Altitude: " + altDe(lid) + " m", 10, 24);
  ctx.fillText("Zona: " + z.nome, 10, 46);
  ctx.font = "bold 13px sans-serif";
  jogadores.forEach((j, i) => {   // uma linha por jogador
    ctx.fillStyle = j.cfg.cor;
    ctx.fillText(j.cfg.nome + ": " + (j.vivo ? altDe(j) + " m" : "caiu"), 10, 68 + i * 18);
  });
  ctx.fillStyle = z.nome === "Céu" ? "#000" : "#fff";
  ctx.font = "bold 16px sans-serif";
  ctx.textAlign = "right";
  ctx.fillText("Perigo: " + z.perigoNome, W - 10, 24);

  // Tela final
  if (estado !== "jogando") {
    ctx.fillStyle = "rgba(0,0,0,0.65)";
    ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = "#fff";
    ctx.textAlign = "center";
    ctx.font = "bold 26px sans-serif";
    const titulo = estado === "ganhou"
      ? (CFG.doisJogadores ? vencedor.cfg.nome + " chegou ao espaço!" : "Você chegou ao espaço!")
      : "Game Over";
    ctx.fillText(titulo, W / 2, H / 2 - 10);
    ctx.font = "16px sans-serif";
    ctx.fillText("Aperte R para jogar de novo", W / 2, H / 2 + 25);
  }
}


/* ================== 11. LOOP PRINCIPAL ================== */
function loop() {
  atualizar();
  desenhar();
  requestAnimationFrame(loop);
}

iniciar();
loop();

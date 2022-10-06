enum Profissao {
    Padeiro = 'Padeiro',
    Atriz = 'Atriz'
}

let pessoa1 = {};
pessoa1.nome = "maria";
pessoa1.idade = 29;
pessoa1.profissao = Profissao.Atriz;

let pessoa2 = {}
pessoa2.nome = "roberto";
pessoa2.idade = 19;
pessoa2.profissao = Profissao.Padeiro;

let pessoa5 = {
    nome: "laura",
    idade: 32,
    profissao: Profissao.Atriz
};

let pessoa6 = {
    nome: "carlos",
    idade: 19,
    profissao: Profissao.Padeiro
};

console.log(pessoa1);
console.log(pessoa2);
console.log(pessoa5);
console.log(pessoa6);
let temdinheiro = false;
let estaEnsolarado = false;
let carroEstaNaGaragem = false;


let resultadoE = '#1 (AND) - vai para o shopping ? ';
resultadoE += temdinheiro && estaEnsolarado;

let resoltadoOU = "#2 (OR) - Vai para o shopping? ";
resoltadoOU += estaEnsolarado || carroEstaNaGaragem;




console.log(resultadoE)
console.log(resoltadoOU)
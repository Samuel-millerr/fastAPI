async function get_api() {
    const response = await fetch('http://127.0.0.1:8000/api/v1/classes/');
    const data = await response.json();
    return data;
}

async function get_classes() {
    const classes = await get_api();
    const conteiner = document.getElementById('conteiner');
    classes.forEach(turma => {
        const classDiv = document.createElement('div')
        classDiv.classList.add('class')
        classDiv.innerHTML = `
            <h2>${turma.nome_turma}</h2>
            <p>${turma.padrinho}</p>
            <p>${turma.qtd_alunos}</p>
            <p>${turma.laboratorio}</p>
        `
        conteiner.appendChild(classDiv)
    });
}


get_classes()
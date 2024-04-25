document.addEventListener('DOMContentLoaded', function() {
    const formColaborador = document.getElementById('form-colaborador');
    const listaColaboradores = document.getElementById('lista-colaboradores');

    // Função para carregar a lista de colaboradores
    function carregarColaboradores() {
        fetch('/colaboradores')
            .then(response => response.json())
            .then(data => {
                listaColaboradores.innerHTML = '';
                data.colaboradores.forEach(colaborador => {
                    const li = document.createElement('li');
                    li.textContent = `ID: ${colaborador.id} - Nome: ${colaborador.nome} - Cargo: ${colaborador.cargo}`;
                    listaColaboradores.appendChild(li);
                });
            })
            .catch(error => console.error('Erro ao carregar colaboradores:', error));
    }

    // Evento de submissão do formulário para cadastrar novo colaborador
    formColaborador.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(formColaborador);
        fetch('/colaboradores', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nome: formData.get('nome'),
                cargo: formData.get('cargo')
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Colaborador cadastrado com sucesso:', data);
            carregarColaboradores();
            formColaborador.reset();
        })
        .catch(error => console.error('Erro ao cadastrar colaborador:', error));
    });

    // Carregar lista de colaboradores ao carregar a página
    carregarColaboradores();
});

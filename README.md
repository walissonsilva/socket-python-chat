# Chat utilizando Sockets em Python

O repositório é composto por dois *scritps*. O `server.py` consiste no servidor e, portanto, precisa estar rodando para que o chat funcione no lado dos clientes. O `client.py` é o cliente.

Caso você deseje utilizar diferentes computadores para se conversar no chat, esses computadores precisam estar na mesma rede. Do contrário, será necessário trocar o endereço IP da rede local para o IP da sua máquina na internet (você pode pesquisar por esse IP no Google).

## Funcionamento

Primeiro você precisa executar o `server.py`. Em seguida, execute o `client.py` em dois consoles, por exemplo. Ao executar, será solicitado o seu nome. Esse nome será utilizando para informar quem enviou as mensagens. Ao digitar o nome, é só começar a enviar as suas mensagens. Essa mensagens chegarão no console de todos os clientes.
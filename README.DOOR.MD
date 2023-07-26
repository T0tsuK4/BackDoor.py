# Script de Servidor de Comando e Controle

Este é um script de servidor de comando e controle (C&C) escrito em Python. O servidor aceita comandos de controle de um cliente e pode criar um túnel usando o Ngrok para expor um servidor local através da Internet. O código é fornecido apenas para fins educacionais e não deve ser usado de forma maliciosa ou antiética.

## Requisitos

Para executar o script, você precisará ter o Python instalado em seu sistema. Além disso, o Ngrok deve estar instalado e configurado corretamente para criar túneis.

## Configuração

Antes de executar o script, você precisará fazer algumas configurações:

1. `CCIP` e `CCPORT`: Defina o endereço IP e a porta do servidor de comando e controle onde o cliente se conectará.

2. `NGROK_PATH`: Defina o caminho para o executável do Ngrok em seu sistema.

3. `LOG_FILE`: Especifique o nome do arquivo onde os registros (logs) serão armazenados.

## Uso

1. Certifique-se de que o Ngrok esteja instalado e configurado corretamente, e que o caminho para o executável esteja definido corretamente em `NGROK_PATH`.

2. Execute o servidor usando o comando:

```
python server.py
```

3. O servidor estará ouvindo conexões na porta especificada em `CCPORT`.

4. Os comandos do cliente podem ser enviados através de uma conexão de socket para o endereço IP e porta do servidor de comando e controle (`CCIP` e `CCPORT`).

5. O cliente pode enviar comandos para criar um túnel na porta desejada usando o formato: `/tunelamento <porta>`

6. O servidor executará o túnel com o Ngrok na porta especificada e retornará a URL pública do túnel para o cliente.

## Registro (Logging)

O script faz uso do módulo `logging` para registrar eventos importantes e erros em um arquivo de log. O nome do arquivo de log pode ser personalizado em `LOG_FILE`, e o formato do registro pode ser alterado em `LOG_FORMAT`.

## Observações

- Este código é fornecido apenas para fins educacionais. Seu uso inadequado ou malicioso é estritamente proibido.

- O uso de ferramentas de tunelamento como o Ngrok deve ser feito com cautela, pois expor servidores locais à Internet pode representar riscos de segurança.

- O autor do código não é responsável pelo uso indevido deste software e não assume qualquer responsabilidade por quaisquer consequências resultantes do uso inadequado.

## Licença

Este código é fornecido sob a [licença MIT](LICENSE).

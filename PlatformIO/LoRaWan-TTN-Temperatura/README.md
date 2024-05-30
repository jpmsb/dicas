# Envio de Temperatura para a TTN

Este é um exemplo simples de envio de temperatura para a TTN (The Things Network) utilizando um ESP32 com LoRaWAN.

O kit de desenvolvimento utilizado foi o [IoT DevKit - LoRaWAN](https://www.robocore.net/lorawan/iot-devkit-lorawan) da Robocore.

### Tabela de Conteúdos

- [Requisitos](#requisitos)
- [Envio de temperatura para a TTN](#envio-de-temperatura-para-a-ttn)
  - [Preparativos](#preparativos)
  - [Compilando e gravando](#compilando-e-gravando)

## Requisitos

É necessário ter o PlatformIO instalado para poder compilar e gravar este projeto na placa.

 - Caso esteja usando a distribuição Linux **openSUSE Tumbleweed**, é possível instalar o PlatformIO com o seguinte comando:

    ```bash
    sudo zypper install python311-platformio
    ```

    Você pode verificar a instalação com o comando:

    ```bash
    pio --version
    ```

 - Caso esteja usando outra distribuição Linux:

    -  para Python 3.11 ou superior:
      
        ```bash
        pipx install platformio
        ```

    - para Python 3.10 ou inferior:

        ```bash
        pip install platformio
        ```

    O binário é instalado em `~/.local/bin/pio`.

[Neste link](https://github.com/jpmsb/preparando-computador-para-engenharia-de-tele/blob/main/guias-de-aplicacoes/PlatformIO.md) há algumas dicas sobre o uso do PlatformIO que podem ser úteis.

## Envio de temperatura para a TTN

### Preparativos

Primeiramente, clone esse repositorio:

```bash
git clone https://github.com/jpmsb/dicas
```

Em seguida, entre no diretório do projeto:

```bash
cd dicas/PlatformIO/LoRaWan-TTN-Temperatura
```

Ajuste as variáveis `appeui` e `appkey` no arquivo [`gravar`](LoRaWan-TTN-Temperatura/gravar) com as chaves de aplicação e de dispositivo fornecidas pela TTN, ficando parecido com o exemplo abaixo:

```bash
# APPEUI e APPKEY para conexão na TTN
appeui="0000000000000001"
appkey="ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
```

O valor de `appeui` deve conter **16** caracteres e o valor de `appkey` deve conter **32** caracteres.

Opcionalmente, você pode ajustar o intervalo em que a temperatura é envada para a TTN ajustando a variável `intervalo_envio` e pode ajustar o tempo limite para reconexão ajustando a variável `intervalo_desconectado`. Abaixo, são mostrados os valores já definidos para essas variáveis:

```
# Intervalos em segundos
intervalo_envio=60           # 1 minuto entre cada envio
intervalo_desconectado=300   # 5 minutos de limitar máximo de desconexão
```

### Compilando e gravando

Após ajustar o arquivo `gravar`, execute o script `gravar` para compilar e gravar o código na placa:

```bash
./gravar
```

Caso tudo ocorra de acordo, você passará a observar a saída serial no terminal. Verifique na TTN se os dados estão chegando.
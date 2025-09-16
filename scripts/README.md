# Scripts

### Tabela de conteúdos

- [atualiza-firefox](#atualiza-firefox)
- [baixar-video](#baixar-video)
- [instalar-icones-tela](#instalar-icones-tela)
- [instalar-tema-chameleon-breeze](#instalar-tema-chameleon-breeze)

## atualiza-firefox

Baixa e instala a versão mais recente do navegador Mozilla Firefox, permitindo que o mesmo seja lançado pelo menu de aplicativos ou pelo comando `firefox`.

Para utilizar a rotina, execute o comando abaixo:

```bash
curl -sL 'https://github.com/jpmsb/dicas/raw/master/scripts/atualiza-firefox' | sudo bash
```

## baixar-video

Baixa um vídeo do YouTube, selecionando a melhor taxa de bits para áudio e vídeo.

### Requisitos

É preciso ter o `yt-dlp` instalado. Para tal, execute o comando abaixo:

- openSUSE Tumbleweed:

    ```bash
    sudo zypper install yt-dlp
    ```

- Debian/Ubuntu:

    ```bash
    sudo apt install yt-dlp
    ```

- Fedora:

    ```bash
    sudo dnf install yt-dlp
    ```

- Arch Linux/Manjaro:

    ```bash
    sudo pacman -S yt-dlp
    ```

- Pipx

    ```bash
    pipx install yt-dlp
    ```

### Uso

Para baixar um vídeo, execute o comando abaixo:

```bash
baixar-video 'URL'
```

Substitua `'URL'` pelo endereço do vídeo no YouTube ou outro site de vídeos. A rotina irá selecionar a maior resolução e taxa de bits disponíveis para áudio e vídeo, e combinará ambos em um único arquivo.

## instalar-icones-tela

Instala o tema de ícones Tela.

Para instalar o tema apenas para usuário atual, execute o comando abaixo:

```bash
curl -sL 'https://github.com/jpmsb/dicas/raw/master/scripts/instalar-icones-tela' | bash
```

Para instalar o tema para todos os usuários, execute o comando abaixo:

```bash
curl -sL 'https://github.com/jpmsb/dicas/raw/master/scripts/instalar-icones-tela' | sudo bash
```

### instalar-tema-chameleon-breeze

Instala os temas Chameleon Breeze Dark e Chameleon Breeze Darker, bem como os esquemas de cores associados.

Para instalar os temas apenas para usuário atual, execute o comando abaixo:

```bash
curl -sL 'https://github.com/jpmsb/dicas/raw/master/scripts/instalar-tema-chameleon-breeze' | bash
```

Para instalar os temas para todos os usuários, execute o comando abaixo:

```bash
curl -sL 'https://github.com/jpmsb/dicas/raw/master/scripts/instalar-tema-chameleon-breeze' | sudo bash
```
# 🎂 Happy Birthday Cake Python

Um projeto Python interativo que cria uma animação de bolo de aniversário com bengalas decorativas usando a biblioteca Turtle.

## ✨ Funcionalidades

- **Animação Gráfica**: Bolo de aniversário animado com bengalas decorativas
- **Efeitos Visuais**: Cores vibrantes e movimento fluído
- **Personalizável**: Mensagem personalizável para o aniversariante
- **Fundo Estrelado**: Fundo com estrelas coloridas aleatórias
- **Interatividade**: Animação contínua até o fechamento da janela

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem de programação principal
- **Turtle Graphics**: Biblioteca para gráficos e animações
- **Math Module**: Para cálculos matemáticos das formas
- **Random Module**: Geração aleatória de estrelas e cores

## 📋 Pré-requisitos

- Python 3.x instalado
- Biblioteca Turtle (incluída na instalação padrão do Python)

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado:
```bash
python --version
```

2. Salve o código em um arquivo `Bolo.py`

3. Execute o programa:
```bash
Bolo.py
```

4. Acompanhe a animação do bolo de aniversário sendo desenhado

## 🎨 Personalização

### Modificar a Mensagem
Altere a mensagem de parabéns no código:
```python
write_author(pen, "Nome do Aniversariante")
```

### Cores do Bolo
Modifique as cores RGB na função de desenho:
```python
# Cores podem ser ajustadas nos valores RGB
r = int((i / layers) * 255)  # Vermelho
g = int((i / layers) * 100)  # Verde
b = int((1 - i / layers) * 255)  # Azul
```

### Número de Estrelas
Ajuste a quantidade de estrelas no fundo:
```python
draw_background_stars(pen, 100)  # Altere o número para mais/menos estrelas
```

## ⚙️ Estrutura do Código

- `setup_screen()`: Configura a janela de exibição
- `setup_turtle()`: Prepara a caneta para desenhar
- `heart()`: Função paramétrica para formas de coração (bengalas)
- `draw_heart()`: Desenha as camadas do bolo com efeito 3D
- `draw_star()`: Desenha estrelas individuais no fundo
- `draw_background_stars()`: Cria o céu estrelado
- `write_author()`: Adiciona mensagem personalizada
- `main()`: Função principal que orquestra a animação

## 🎂 Características do Bolo

- **Camadas Múltiplas**: Efeito 3D com gradiente de cores
- **Bengalas Decorativas**: Formas de coração animadas
- **Base Sólida**: Estrutura central bem definida
- **Mensagem Personalizada**: Texto com nome do aniversariante

## 🌟 Efeitos Especiais

- Estrelas cintilantes em cores aleatórias
- Movimento suave das bengalas decorativas
- Gradiente de cores do vermelho ao azul
- Fundo escuro para contraste

## 📝 Licença

Este projeto é de código aberto e pode ser utilizado para fins educacionais e de entretenimento.

## 💡 Ideias de Melhoria

- Adicionar velas animadas com efeito de chama
- Implementar interatividade com clique do mouse
- Adicionar efeitos sonoros de parabéns
- Criar opções de temas de cores diferentes
- Exportar a animação como GIF ou vídeo

---

⭐ Este projeto é perfeito para celebrar aniversários de forma criativa e programática!

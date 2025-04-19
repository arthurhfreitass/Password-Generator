# Gerador de Senhas NÃO TERMINADO

Este é um gerador de senhas em Python, simples, prático e com foco em segurança. O objetivo deste projeto é criar senhas fortes e seguras, com a possibilidade de codificar as senhas utilizando **Base64** antes de salvá-las em um arquivo. A ferramenta foi desenvolvida para usuários que buscam uma maneira fácil de gerar senhas seguras e organizadas.

## Funcionalidades

- **Geração Personalizada de Senhas**: Crie senhas com base em critérios personalizados, como comprimento, inclusão de números, letras maiúsculas e caracteres especiais.
- **Validação de Senhas**: As senhas geradas são validadas de acordo com regras de segurança, como comprimento mínimo e complexidade.
- **Codificação em Base64**: As senhas são codificadas em Base64 antes de serem salvas, garantindo que, caso o arquivo seja acessado, as senhas não estejam visíveis em texto simples.
- **Armazenamento Seguro**: As senhas são salvas no arquivo de forma segura, codificadas para maior privacidade e proteção.

## Como Funciona

O gerador cria senhas fortes e as codifica usando o método **Base64**. Isso significa que, embora as senhas sejam armazenadas de forma segura e compacta, qualquer pessoa que tenha acesso ao arquivo e saiba como decodificar o Base64 pode acessar as senhas originais. Para uma segurança ainda mais avançada, é possível combinar a codificação com outras práticas de proteção, como criptografia.

## Tecnologias Usadas

- **Python**: Linguagem de programação utilizada para desenvolver a ferramenta.
- **Base64**: Técnica de codificação usada para transformar as senhas em um formato seguro e legível antes de armazená-las.
- **Datetime**: Para registrar a data e hora em que as senhas foram salvas, garantindo mais controle e organização.

## Como Usar

1. Clone o repositório.
2. Instale as dependências necessárias com `pip install -r requirements.txt`.
3. Execute o programa e comece a gerar e salvar suas senhas de forma segura!

## Motivação

A ideia por trás desse projeto foi criar uma solução simples e prática para gerar senhas seguras, com foco na facilidade de uso e privacidade. Embora a codificação Base64 não seja uma criptografia robusta, ela garante que as senhas não sejam armazenadas em texto simples, oferecendo um nível básico de segurança para quem busca mais privacidade em suas informações.

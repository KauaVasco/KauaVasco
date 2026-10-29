<p align="center">
  <img src="assets/readme/banner.svg" width="720" alt="Kauã Vasco, Desenvolvedor Backend Python Júnior">
</p>

## Sobre mim

Sou desenvolvedor Backend Python júnior e curso Sistemas de Informação. Tenho experiência prática em um sistema que roda em produção e busco minha primeira oportunidade na área.

Trabalho com APIs em FastAPI, MySQL com SQLAlchemy assíncrono, validação de dados com Pydantic e automações em n8n. Ainda estou ganhando autonomia. O que mais aprendi até aqui foi investigar antes de alterar e testar o caminho de erro, além do que eu esperava que acontecesse.

Também integro modelos de linguagem a pipelines. Para mim o modelo é uma etapa do processo: importa o que entra, o que se confere antes de seguir e o que o sistema faz quando a resposta vem errada.

## Projetos

### Sistema de criação de políticas (código privado)

Sistema para fluxos de trabalho jurídicos e regulatórios. O cliente abre uma demanda, o sistema faz uma análise automatizada, gera um questionário e produz a política, que uma pessoa revisa antes da entrega. Há acesso por papéis (administrador, equipe e cliente) e o sistema roda em produção.

Desenvolvido por mim, com apoio de IA na implementação.

No backend usei endpoints e rotas em FastAPI, dependências, validação com Pydantic, tratamento de erros e SQLAlchemy assíncrono. A análise e a geração rodam como etapas de um pipeline de IA, com uma conferência do resultado antes de seguir.

Stack: Python, FastAPI, SQLAlchemy, Pydantic e MySQL. O código é privado porque o sistema pertence a um contexto profissional.

### [Automação de e-mails e reuniões com IA (n8n)](https://github.com/KauaVasco/automacoes-n8n-ia)

Dois workflows do n8n que trabalham juntos. Um lê e-mails inteiros (texto, imagens, PDFs e planilhas) e escreve a resposta. O outro identifica pedidos de reunião e marca no Google Calendar. Toda mensagem enviada e toda reunião marcada passam antes por aprovação no Telegram, e se o modelo principal falhar ou vier vazio, um segundo assume.

Foi feito e testado em `localhost`, com o n8n rodando em Docker. Não é uma instância de produção.

## Tecnologias

```text
$ cat stack.txt

[prática]
  Python, FastAPI
  SQL e MySQL
  SQLAlchemy (assíncrono)
  Pydantic
  APIs e integrações com IA
  n8n
  Git e GitHub

[intermediário]
  Pandas

[básico]
  Docker (rodo o n8n em contêiner)
```

## Contato

[LinkedIn](https://www.linkedin.com/in/kau%C3%A3-vasco-1a0b6037b) · [E-mail](mailto:kauatidev@gmail.com)

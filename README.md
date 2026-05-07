# Sistema de Pedidos Flask

Sistema web desenvolvido em Flask com foco em organização de código, separação de responsabilidades e aplicação de conceitos de desenvolvimento back-end e engenharia de software.

---

# Objetivo do Projeto

Este projeto foi criado não apenas para praticar programação, mas também para desenvolver um padrão mais profissional de desenvolvimento, utilizando:

- Arquitetura em camadas
- Separação de responsabilidades
- Organização modular
- Regras de negócio
- Integração com banco de dados
- Fluxo real de back-end

---

# Tecnologias Utilizadas

- Python
- Flask
- MySQL
- HTML5
- CSS3

---

# Estrutura do Projeto

```bash
Sistema_de_pedidos/
│
├── models/
│   ├── cliente.py
│   ├── produto.py
│   └── pedido.py
│
├── templates/
│   ├── base.html
│   ├── clientes.html
│   ├── produtos.html
│   └── pedidos.html
│
├── static/
│   ├── style.css
│   └── imagens/
│
├── app.py
└── db.py
```

---

# Funcionalidades

## Clientes
- Cadastro de clientes
- Listagem de clientes
- Edição de clientes
- Exclusão de clientes

## Produtos
- Cadastro de produtos
- Controle de estoque
- Edição de produtos
- Exclusão de produtos

## Pedidos
- Criação de pedidos
- Adição de produtos ao pedido
- Remoção de itens
- Cálculo automático do total
- Alteração de status do pedido

---

# Regras de Negócio Implementadas

O projeto possui validações reais de sistema:

- Bloqueio de produtos sem estoque
- Validação de quantidade disponível
- Controle de estoque automático
- Impedimento de alteração em pedidos finalizados
- Impedimento de alteração em pedidos cancelados
- Atualização automática do total do pedido

---

# Conceitos Back-end Trabalhados

- Rotas Flask
- Recebimento de dados via formulário
- Integração com MySQL
- Consultas SQL
- Modularização
- Organização em camadas
- Fluxo de requisição HTTP
- Regras de negócio no back-end
- Relacionamento entre tabelas

---

# Objetivo de Aprendizado

Este projeto faz parte da minha evolução como desenvolvedor back-end, buscando aprender não apenas sintaxe, mas também:

- Estruturação de sistemas
- Padrões de desenvolvimento
- Organização profissional de projetos
- Lógica de negócio
- Fluxo real de aplicações web

---

# Próximos Passos

- Melhorar interface
- Implementar autenticação
- Melhorar arquitetura do projeto
- Adicionar paginação
- Evoluir regras de negócio
- Melhorar tratamento de erros

# consumindo-api-groq-ia
Consumo da API da Groq IA para gerar automaticamente textos (conteúdos) para posts em blogs e redes sociais. Desenvolvido com FastAPI, o sistema é otimizado para criar conteúdo de alta qualidade, aplicando técnicas de processamento de linguagem natural para entregar textos relevantes.

**Versão**: 1.0

## Requisitos

Antes de consumir essa API, você precisará criar uma conta no site:

[EstampaVerso.shop - Crie sua conta aqui](https://estampaverso.shop/register/)

Após criar a conta, você poderá utilizar a API para gerar textos automaticamente com a IA.

## URL Base da API

A URL base para todas as requisições é:
https://estampaverso.shop/api/groq/v1/

### Endpoint: Gerar Texto com IA

Para gerar um texto com a IA, use o seguinte endpoint:


### Estrutura do Corpo da Requisição (JSON)

A requisição deve ser feita com o método **POST** e o corpo da requisição deverá ser um **JSON stringificado**. Aqui está um exemplo de como estruturar o corpo da requisição:

POST /generate-post-text-with-groq-IA/

```json
{
    "username": "email@exemplo.com",
    "password": "sua_senha_aqui",
    "context": "Escreva um contexto para a IA gerar o seu texto."
}
```

* username: O e-mail da sua conta no EstampaVerso.Shop.
* password: A senha associada à sua conta.
* context: O contexto ou tema sobre o qual você quer que a IA gere o texto.


```
curl -X 'POST' \
  'https://estampaverso.shop/api/groq/v1/generate-post-text-with-groq-IA/' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "email@exemplo.com",
    "password": "sua_senha_aqui",
    "context": "Escreva um contexto para a IA gerar o seu texto."
}'
```

### Respostas da API
A API retorna uma resposta JSON com o texto gerado pela IA ou um erro caso algo tenha dado errado.

### Resposta Sucesso
Se a requisição for bem-sucedida, você receberá um JSON como este:

```json
{
  "data": {
    "statusCode": 200,
    "content": "Texto gerado pela IA com base no seu contexto."
  }
}
```

* statusCode: Código de status HTTP, 200 indica sucesso.
* content: O texto gerado pela IA.

### Resposta de Erro
Se houver um erro (por exemplo, credenciais inválidas), a resposta será algo como:

```json
{
  "data": {
    "statusCode": 400,
    "content": "",
    "msg": "Erro ao gerar conteúdo! Verifique suas credenciais ou o conteúdo inserido."
  }
}
```

* statusCode: Código de status HTTP, 400 indica erro de requisição.
* msg: Mensagem explicativa sobre o erro.


### Considerações Finais
* Certifique-se de que o username e password estão corretos antes de fazer a requisição.
* O campo context deve ser preenchido com um tema ou contexto claro para gerar um texto relevante.
* A API gera um texto baseado no contexto fornecido, então quanto mais detalhado o contexto, mais preciso será o texto gerado.

### Contato e Suporte
Se você tiver dúvidas ou problemas com a API, entre em contato em:<br>
    [Suporte aqui](https://estampaverso.shop/contato)
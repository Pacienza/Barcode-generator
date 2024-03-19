

# Gerador de Código de Barras

Gerador de código de barras feito em Python, usando Flask Framework e a biblioteca Barcode

![](Pacienza.png)

### Passo a passo para gerar Código de Barras

- ###### Rodar o servidor Flask e abrir o cliente REST (Postman, ApiDog, similares)
- ###### Cabeçalho HTTP para gerar o código de barras

```
POST /create_tag HTTP/1.1
Host: localhost:3000
Content-Type: application/json
Content-Length: 36
```
- ###### Body da Requisição POST
```
{
	"product_code": "{conteudo}"
}
```

Conteúdo do código de barras pode ser `integer` ou `string`

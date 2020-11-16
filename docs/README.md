<!-- docsify serve docs -->

# Lógica de Programação [ Python ]

## 1. Introdução
> _"A lógica está presente em nossa vida sempre que pensamos, falamos ou escrevemos."_

Em programação, independente de qual seja a linguagem, a lógica possui a função de ordenar as instruções em uma sequência lógica para atingir um determinado objetivo.

Um exemplo do uso de lógica do nosso dia-a-dia é:

- Todo mamífero bebe leite;
- O ser humano é um mamífero;

Logo:

- O ser humano bebe leite;

Portanto, a lógica é a ciência que têm como objetivo o estudo das leis que formam o raciocínio, podendo distinguir entre o correto e o incorreto.

### 1.1. Algoritmos
> _"Algoritmo é uma sequência lógica de passos que levam a um determinado objetivo."_

Por mais que não percebamos, nosso cérebro utiliza algoritmos a todo instante.
Um exemplo disso é quando uma lâmpada queima, e precisamos trocá-la:

```
> Pegue a escada
> Coloque-a embaixo da lâmpada queimada
> Pegue a lâmpada nova
> Suba a escada
> Retire a lâmpada velha
> Coloque a lâmpada nova
> Desça da escada
```

Ainda que bem simplificado, mas o processo a cima é exatamente o que realizamos para trocar uma lâmpada.

Esses passos nada mais são do que um algoritmo.

### 1.2. Console
> _"Python disponibiliza um console para seu desenvolvimento."_

O console Python pode ser acessado pelo comando abaixo:

```bash
$ python3
```

Esse comando abre o console Python, nos permitindo executar qualquer um dos comandos da linguagem que veremos adiante.

## 2. Dados
> _"Os dados são as informações que serão processadas pelo computador."_

Não existe nenhum programa que não manipule dados.

### 2.1. Tipos
> _"Os tipos de dados são uma forma de classificá-los, para tornar mais fácil seu manuseio."_

Em Python, temos alguns tipos de dados comuns entre outras linguagems, como **Int**, **Float** e **Bool**, porém tambem possui alguns tipos próprios, porém com funções similares à outros tipos de outras linguagens.

Vejamos abaixo alguns dos tipos mais comuns dessa linguagem:

|Exemplo|Tipo||
|---|---|---|
|```"Hello World"```|str|*String*|
|```20```|int|*Integer*|
|```20.5```|float|*Float*|
|```range(6)```|range|*Array*|
|```["apple", "banana", "cherry"]```|list|*Array*|
|```("apple", "banana", "cherry")```|tuple|*Array*|
|```{"name" : "John", "age" : 36}```|dict|*Hash*|
|```True```|bool|*Boolean*|

Para verificar o tipo de um dado/variável, você pode usar a função ```type()```, passando o valor como parâmetro:

```python
type("Hello World") # <class 'str'>
```

### 2.1.1. Casting
> _"Casting se resume a especificar o tipo de um dado."_

É possível especificar o tipo de um dado usando casting. Basta usar o tipo desejado como uma função, passando o dado a ser moldado como parâmetro:

```python
str(2.25) # '2.25'
float('2.25') # 2.25
int(2.98) # 2
bool(0) # False
```

### 2.2. Variáveis
> _"Variável é aquilo sugeito a mudanças, instável ou inconstante."_

Váriaveis, fazendo uma analogia, são como gavetas. Elas podem armazenar quaiquer tipos de dados, mas somente um tipo por vez.

Sendo mais técnico, elas correspondem a uma posição de memória onde será armazenada uma informação que pode variar no decorrer da execução do algoritmo.

Em Python, uma variável pode ser declarada da seguinte maneira:

```python
# Regular variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
myvar2 = "John"

# Irregular variable names
2myvar = "John"
my-var = "John"
my var = "John"
```

### 2.3. Constantes
> _"Constante é aquilo que não está sugeito a mudanças, ou seja inalterável."_

Indo direto ao ponto, constantes funcionam exatamente igual a variáveis, tendo somente um diferencial: são imutáveis.

Constantes costumam ser utilizadas para centralização de dados que jamais serão alterados por serem verdades absolutas, ou por possuirem valores globais.

Em Python, uma constante pode ser declarada da mesma maneira que uma variável, seguindo as mesmas normas, porém, segue a boa prática de ser sempre em maiúsculo:

```python
APP_VERSION = "2.6.7.beta"
PI = 3.14
```

## 3. Operadores
> _"Operadores são meios pelo qual se altera, compara e avalia os dados."_

Os operadores são divididos em três classes distintas, vejamos um pouco sobre.

### 3.1. Operadores Aritméticos
> _"Operadores aritméticos são utilizados para realizar operações numéricas."_

Dentre os três tipos de operadores dispostos para programação, os aritméticos são os de mais fácil compreenção.

Eles são utilizados para incrementar, decrementar, multiplicar ou mesmo dividir valores numéricos.

Veja alguns exemplos abaixo:

```python
x = 5

x + 5 # 10
x - 5 # 0
x * 5 # 25
x / 5 # 1.0
```

Também é possível alterar o valor de uma variável com os operadores aritméticos, somados ao operador relacional *=* (igual):

```python
x = 5
x += 5
# x = 10

x = 5
x -= 5
# x = 0

x = 5
x *= 5
# x = 25

x = 5
x /= 5
# x = 1.0
```

### 3.2. Operadores Relacionais
> _"Operadores relacionais são utilizados para comparar e atribuir dados."_

Desde a atribuição de uma variável, até a comparação de valores entre vetores, os operadores relacionais são indispensáveis.

Eles são de simples compreenção, mas podem realizar comparações bem complexas quando somados aos operadores lógicos.

Vejamos alguns exemplos:

```python
x = 5

x > 5 # False
x < 5 # False
x == 5 # True
x != 5 # False
x >= 5 # True
x <= 5 # True
```

### 3.3. Operadores Lógicos
> _"Operadores lógicos são utilizados para composição de proposições lógicas."_

Imagine o seguinte cenário:

Numa livraria, se o valor de um livro for **superior** à **R$ 70,00**, o cliente leva um marcador de páginas como brinde, mas se a compra for realizada num **final de semana**, ele ganha o marcador **independente do valor** do livro.

Agora, imagine que precisemos traduzir isso para Python. Separadamente, seria algo como abaixo:

```python
# Verifica se o valor do livro é superior à R$ 70,00
book_price > 70.0

# Verifica se o dia da compra é num final de semana
date.today().weekday() > 4
```

Porém, precisamos realizar essas duas comparações numa única verificação, e, para isso, podemos utilizar o operador lógico *or* (ou):

```python
# O valor do livro é superior à R$ 70,00
# OU
# O dia da compra é num final de semana
book_price > 70.0 or date.today().weekday() > 4
```
Em Python, podemos usar três operadores lógicos: *and*, *or* e *not*:

```python
x = 5

x > 4 and x < 6 # True
x < 4 or x < 6 # True
not(x < 4) # True
```

#### 3.3.1. AND
> _"Valida se ambas as afirmações são verdadeiras."_

Para que a resposta seja *True*, todas as afirmações devem ser verdadeiras.

```python
x = 5

x > 4 and x < 6 # True
x < 4 and x < 6 # False
x > 4 and x < 6 and x == 5 # True
```

#### 3.3.2. OR
> _"Valida se ao menos uma das afirmações é verdadeira."_

Para que a resposta seja *True*, uma das afirmações deve ser verdadeira (não necessariamente todas).

```python
x = 5

x > 4 or x > 6 # True
x < 4 or x > 6 # False
x > 4 or x > 6 or x == 5 # True
```

#### 3.3.3. NOT
> _"Inverte o resultado da afirmação."_

Para que a resposta seja *True*, o resultado final **não** deve ser verdadeiro (pois o resultado será invertido).

```python
x = 5

not(x < 4) # True
not(x > 4) # False
not(x < 4 and x == 5) # True
```

## 4. Lógica Proposicional
> _"Proposição é uma frase declarativa a qual pode ser apenas verdadeira ou falsa."_

Proposições podem ser simples, quando contém somente uma proposição integrante, ou ainda compostas, quando formada por duas ou mais.

### 4.1. Tabela Verdade
> _"A tabela verdade existe para auxiliar na análise de proposições - e queimar nosso cérebro..."_

A tabela verdade é uma maneira prática de dispor organizadamente os valores lógicos envolvidos em uma proposição.

Nela podemos analisar proposições de conjunção, disjunção, negação, condicional e bicondicional.

Mas vamos nos abster e usar somente uma proposição de conjunção como exemplo:

```
p: "Gatos gostam de leite"
q: "Gatos são deuses egípcios"
p^q: "Gatos gostam de leite E são deuses egípcios"
```

A tabela verdade dessa proposição seria a seguinte:

|p|q|p^q|
|---|---|---|
|```V```|```V```|```V```|
|```V```|```F```|```F```|
|```F```|```V```|```F```|
|```F```|```V```|```F```|

## 5. Estruturas de Controle
> _"Toda linguagem de programação possui instruções para controle de fluxo."_

Estruturas de controle são instruções responsaveis pelo fluxo do sistema, é através delas que o programa decide qual caminho seguir.

### 5.1. IF
> _"Quando há necessidade de testar uma condição antes de executar uma ação."_

```python
if 1 > 0:
  print("1 é maior que 0")

# 1 é maior que 0
```

### 5.2. IF..ELSE
> _"Quando há necessidade de testar uma condição antes de executar duas ações distintas."_

```python
if 1 < 0:
  print("1 é menor que 0")
else:
  print("1 é maior que 0")

# 1 é maior que 0
```

### 5.3. IF..ELIF..ELSE
> _"Quando há necessidade de testar uma condição antes de executar multiplas ações distintas."_

```python
if 1 < 0:
  print("1 é menor que 0")
elif 1 > 0:
  print("1 é maior que 0")
else:
  print("1 é igual a 0")

# 1 é maior que 0
```

### 5.4. WHILE
> _"Quando há necessidade de uma ação ser executada multiplas vezes de forma incremental."_

```python
i = 1
while i < 4:
  print('Número', i)
  i += 1

# Número 1
# Número 2
# Número 3
```

### 5.5. WHILE..ELSE
> _"Quando há necessidade de ações distintas serem executadas multiplas vezes de forma incremental."_

```python
i = 1
while i < 4:
  print('Número', i)
  i += 1
else:
  print("i não é menor que 4")

# Número 1
# Número 2
# Número 3
# i não é menor que 4
```

### 5.6. FOR
> _"Quando há necessidade de iterar algo."_

```python
fruits = ["Maçã", "Banana", "Cereja"]
for x in fruits:
  print(x)

# Maçã
# Banana
# Cereja
```

### 5.7. FOR..ELSE
> _"Quando há necessidade de iterar algo e executar uma ação no final."_

```python
fruits = ["Maçã", "Banana", "Cereja"]
for x in fruits:
  print(x)
else:
  print("Fim")

# Maçã
# Banana
# Cereja
# Fim
```

### 5.8. FOR..FOR
> _"Quando há necessidade de iterar algo dentro de uma iteração."_

```python
colors = ["Vermelha", "Azul", "Amarela"]
fruits = ["Maçã", "Banana", "Cereja"]
for x in fruits:
  for y in colors:
    print(x, y)

# Maçã Vermelha
# Maçã Azul
# Maçã Amarela
# Banana Vermelha
# Banana Azul
# Banana Amarela
# Cereja Vermelha
# Cereja Azul
# Cereja Amarela
```

## 6. Estruturas de Dados
> _"Estruturas de dados são como armários."_

Voltando à analogia das variáveis (que são como gavetas, podendo armazenar quaiquer tipo de dado, mas somente um tipo por vez), as estruturas de dados são como armários, que possuem várias gavetas.

### 6.1. Vetor
> _"Um vetor é uma variável composta unidimensional."_

Usando palavras simples, um vetor é uma lista de dados.

Em Python, existem dois tipos de vetores: *Listas* e *Tuplas*.

#### 6.1.1. Python Lists
> _"Listas são vetores mutáveis."_

```python
fruits = ["Maçã", "Banana", "Cereja"]

fruits
# ['Maçã', 'Banana', 'Cereja']

fruits[0]
# 'Maçã'

fruits[-1]
# 'Cereja'

fruits[1:2]
# ['Banana']

fruits[0:2]
# ['Maçã', 'Banana']

fruits[0] = 'Uva'
fruits
# ['Uva', 'Banana', 'Cereja']

```

#### 6.1.2. Python Tuples
> _"Tuplas são vetores imutáveis."_

```python
fruits = ("Maçã", "Banana", "Cereja")

fruits
# ('Maçã', 'Banana', 'Cereja')

fruits[0]
# 'Maçã'

fruits[-1]
# 'Cereja'

fruits[1:2]
# ['Banana',]

fruits[0:2]
# ['Maçã', 'Banana']
```

### 6.2. Hash
> _"Um Hash é uma variável indexada unidimensional."_

Hashs possuem o mesmo conceito de vetores, porém seus valores são indexados.

Na prática, isso significa que cada gaveta possui uma etiqueta, assim você não precisa abrir uma a uma para chegar na gaveta de meias.

Em Python, os Hashs são chamados de *Dicionários*.

#### 6.2.1. Python Dictionary
> _"Tuplas são vetores imutáveis."_

```python
person = {
  "name": "Fred",
  "age": "22",
  "hobby": 'Watch animes'
}

person
# {'name': 'Fred', 'age': '22', 'hobby': 'Watch animes'}

person['name']
# 'Fred'
```

### 6.3. Matriz
> _"Uma matriz é uma variável composta multidimensional."_

Se um vetor é um armário repleto de gavetas, uma matriz é um galpão repleto de armários.

```python
people = [
  {
    "name": "Fred",
    "age": "22",
    "hobby": 'Watch animes'
  },{
    "name": "Beatriz",
    "age": "20",
    "hobby": 'Watch series'
  },{
    "name": "Diego",
    "age": "23",
    "hobby": 'Watch movies'
  }
]

people
# [{'name': 'Fred', 'age': '22', 'hobby': 'Watch animes'},
# {'name': 'Beatriz', 'age': '20', 'hobby': 'Watch series'},
# {'name': 'Diego', 'age': '23', 'hobby': 'Watch movies'}]

people[0]['name']
# 'Fred'

people[-1]['hobby']
# 'Watch movies'

for person in people:
  print(person['name'])

# Fred
# Beatriz
# Diego
```

## 7. Funções
> _"Funções são a **cereja do bolo** de um código não repetitivo."_

Uma função é um trecho de código que pode ser executado em determinados pontos de uma aplicação.

Separar trechos repetitivos, ou mesmo quebrar partes do código em partes menores, é o principal intuito de uma função.

Funções também são chamadas de *métodos*, elas podem receber nenhum ou vários parâmetros, e podem retornar um valor.

### 7.1. Sintaxe
> _def \<function_name\>()_

```python
def hello():
  print("Hello World!")

hello() #
```

### 7.2. Parâmetros
> _def \<function_name\>(\<parameters\>)_

É possível passar dados para uma função utilizando-se de parâmetros.

```python
def hello(name):
  print("Hello", name + "!")

hello('Fred') # Hello Fred!

hello('Beatriz') # Hello Beatriz!

hello() # TypeError: hello() missing 1 required positional argument: 'name'
```

Também é possível determinar um valor padrão de um parâmetro, para caso o mesmo não seja enviado.

```python
def hello(name = 'World'):
  print("Hello", name + "!")

hello('Fred') # Hello Fred!

hello('Beatriz') # Hello Beatriz!

hello()  # Hello World!
```

### 7.3. Retorno
> _return_

Muitas das vezes uma função será chamada no intuito de obter algum dado novo; para esses casos, podemos fazer nossa função retornar um valor.

```python
def sum(num1, num2):
  return num1 + num2

sum(5, 5) # 10
```

## 8. Arquivos
> _"Manipulação de arquivos é uma parte importante para qualquer aplicação."_

Independente de qual projeto tenhamos que desenvolver, ler arquivos costuma ser algo sempre presente, podendo variar desde um arquivo de configuração até uma lista de integração de usuários externos.

Ler arquivos em Python é simples:

```python
f = open("demofile.txt", "r")
```

Sendo o primeiro parâmetro o caminho do arquivo, o segundo é o tipo de permissão naquele arquivo.

|Sigla|Nome|Descrição|
|---|---|---|
|```r```|*Read*|Abre o arquivo somente para leitura - retorna um erro se o arquivo não existir.|
|```a```|*Append*|Abre o arquivo para adição - cria o arquivo se não existir.|
|```w```|*Write*|Abre o arquivo para escrita - cria o arquivo se não existir.|
|```x```|*Create*|Cria o arquivo - retorna um erro se o arquivo já existir.|

Em alguns os exemplos a seguir, usaremos o arquivo **demofile.txt**, demonstrado abaixo:

```
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!
```

Vejamos alguns exemplos de métodos de leitura e manipulação de arquivos:

```python
# Leitura - Arquivo por completo
f = open("demofile.txt", "r")

print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

f.close()
```
```python
# Leitura - 6 primeiros caracteres
f = open("demofile.txt", "r")

print(f.read(6))
# Hello!

f.close()
```
```python
# Leitura - Primeira linha
f = open("demofile.txt", "r")

print(f.readline())
# Hello! Welcome to demofile.txt

f.close()
```
```python
# Escrita - Adiciona conteúdo ao final do arquivo
f = open("demofile.txt", "a")

f.write("Now the file has more content!")
# 30

f.close()

f = open("demofile.txt", "r")
print(f.read())
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!
# Now the file has more content!

f.close()
```
```python
# Escrita - Sobrescreve conteúdo do arquivo
f = open("demofile.txt", "w")

f.write("Ops..!")
# 6

f.close()

f = open("demofile.txt", "r")
print(f.read())
# Ops..!

f.close()
```
```python
# Deleção - Apaga o arquivo
import os

os.remove("demofile.txt")
```
```python
# Deleção - Apaga o arquivo se existir
import os

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("Arquivo não encontrado")
```

### 8.1. JSON
> _"O tipo de arquivo sobre todos os outros."_

JSON (JavaScript Object Notation), assim como XML ou YML, é um tipo de arquivo que utiliza marcações e indexação de conteúdo, tornando, assim, sua manipulação simples, além de ser relativamente mais leve e de fácil entendimento.

JSON costuma ser utilizado em peso por APIs, mas também possui incontáveis aplicações no mercado atual de TI.

Diferente de arquivos regulares .txt, JSON precisa ser parseado para que possamos utilizar 100% de seu potêncial.

Em alguns os exemplos a seguir, usaremos o arquivo **person.json**, demonstrado abaixo:

```json
{
  "name": "Beatriz",
  "languages": ["Portuguese", "English"]
}
```

Vejamos abaixo alguns exemplos:

```python
# Parseia uma variável JSON - vinda de uma API
import json

person_json = '{"name": "Beatriz", "languages": ["Portuguese", "English"]}'
person = json.loads(person_json)

print(person)
# {'name': 'Beatriz', 'languages': ['Portuguese', 'English']}

print(person['name'])
# Beatriz
```
```python
# Parseia um arquivo JSON
import json

person_json = open("person.json", "r").read()
person = json.loads(person_json)

print(person)
# {'name': 'Beatriz', 'languages': ['Portuguese', 'English']}

print(person['name'])
# Beatriz
```
```python
# Cria um arquivo JSON
import json

person = {'name': 'Beatriz', 'languages': 'English'}
person_json = json.dumps(person)
print(person_json)
# {'name': 'Beatriz', 'languages': 'English'}

f = open("person.json", "w")
f.write(person_json)
# 45

f.close()

f = open("person.json", "r")
print(f.read())
# {"name": "Beatriz", "languages": "English"}

f.close()
```

## 9. Estrutura de Projeto
> _"A divisão e estruturação de seu projeto é uma parte muito importante do desenvolvimento, e deve ser clara."_

Por mais simples que seja um projeto, é sempre bom seguir uma estrutura padrão, assim, entendendo um de seus projetos, se torna fácil entender os demais - ainda que mais complexos.

Segue abaixo uma estrutura simples, porém eficaz, de um projeto Python:

```
project/
|-- src/
|   |-- __init__.py
|   |-- file.py
|
|-- project.py
|-- README.md
```

### 9.1. \__init__
> _"O arquivo chave de Python."_

Esse arquivo é responsável por determinar quais são os métodos/classes a serem importados do módulo em questão - além de definir como o mesmo será importado nos demais pontos da aplicação.

https://packaging.python.org/tutorials/packaging-projects

https://towardsdatascience.com/whats-init-for-me-d70a312da583

### 9.2. Projeto Bookstore
> _"Localizado em **samples/bookstore/**"_

Como exemplo de estrutura de projeto, temos o **Bookstore**.

Ele é um projeto simples que utiliza de programação estruturada e Python para imprimir na tela qual livro estamos lendo.

## 10. Programação Orientada a Objetos (OOP)
> _"OOP é um paradigma de programação."_

Diferente da programação estruturada, a programação orientada a objetos é mais dinámica e de fácil escalonamento e depuração.

Em resumo, tudo é um objeto. Objetos possuem duas caracteristicas: *atributo(s)* e *comportamento(s)*.

- Atributos podem ser, por exemplo, _nome_, _idade_, _cargo_, ...
- Já comportamentos podem ser _falar_, _correr_, ...

https://www.programiz.com/python-programming/object-oriented-programming

### 10.1. Classes
> _"O blueprint de um objeto."_

As classes são a definição dos moldes de um objeto. Todo objeto possui uma classe.

```python
class Book:
  def __init__(self, tittle):
    self.tittle = tittle

  def read(self):
    return "I am reading {}".format(self.tittle)

  @classmethod
  def all(cls):
    return 'List all books'
```

No exemplo acima, `Book` é uma classe que possui o atributo `tittle` e dois comportamentos: `read` e `all` - sendo o primeiro um comportamento de instância e o segundo de classe.

### 10.2. Objeto
> _"A instância de uma classe."_

Se a classe é um molde, o objeto é o produto feito com base nele.

```python
book = Book('Game of Thrones')

print(book.read()) # I am reading Game of Thrones
```

Como podemos ver, a partir da instância de uma classe, podemos chamar quaisquer métodos que ela implemente.

Porém, métodos de classe podem ser executados diretamente da classe (sem precisar de uma instância):

```python
print(Book.all()) # List all books
```

### 10.3. Os três pilares
> _"Todo bom projeto Orientado a Objetos segue os três pilares."_

#### 10.3.1. Herança
> _"Permite a criação de uma nova classe baseada em outra."_

```python
class Magazine(Book):
  def __init__(self, tittle):
    super().__init__(tittle)

  def gossip(self):
    return "I am gossiping about {}..".format(self.tittle)

  @classmethod
  def all(cls):
    return 'List all magazines'
```

`Magazine` é uma classe que herda todas as caracteristicas de `Book`, logo, todos os métodos presentes na classe pai (`Book`) estão na classe filho(`Magazine`).

```python
magazine = Magazine('Woman\'s Day')

print(magazine.read()) # I am reading Woman's Day
print(magazine.gossip()) # I am gossiping about Woman's Day..
print(Magazine.all()) # List all magazines
```

#### 10.3.2. Encapsulamento
> _"Permite a melhor manipulação dos atributos de um objeto."_

Acessar e alterar os atributos de um objeto é algo corriqueiro, porém existe uma 'melhor maneira' de fazer isso.

O encapsulamento é o pilar responsável por isso.

De um modo bem resumido, nunca acesse os atributos de um objeto pelo lado de fora diretamente, crie Getters e Setters para isso.

```python
class Book:
  def __init__(self, tittle):
    self.__tittle = tittle

  def getTittle(self):
    return self.__tittle

  def setTittle(self, tittle):
    self.__tittle = tittle

  def read(self):
    return "I am reading {}".format(self.getTittle())
```

Dessa forma, não é mais possível acessar o título do livro chamando `book.tittle` ou `book.__tittle`.
Para acessar esse atributo agora é necessário usar `book.getTittle()` e `book.setTittle('Novo Título')` para alterar o título.

#### 10.3.3. Polimorfismo
> _"Permite utilização de uma interface comum entre classes."_

É algo mais simples do que a palavra sugere.

Imagine que temos a classe abaixo:

```python
class Librarian:
  @classmethod
  def read(cls, book: Book):
    print(book.read())
```

A classe `Librarian` possui o método de classe `read`, que recebe um objeto do tipo `Book`.

O polimorfismo nos permite enviar tanto um objeto da classe `Book` quando um objeto `Magazine`:

```python
Librarian.read(book) # I am reading Dracarys
Librarian.read(magazine) # I am reading Woman's Day
```

### 10.4. Projeto Bookstore OOP
> _"Localizado em **samples/bookstore_oop/**"_

Como exemplo de estrutura de projeto oop, temos o **Bookstore OOP**.

Ele é um projeto simples que utiliza de programação orientada a objetos e Python para imprimir na tela qual livro ou revista estamos lendo.

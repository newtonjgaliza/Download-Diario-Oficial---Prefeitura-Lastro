# Download Diario Oficial - Prefeitura Lastro

## Como foi feito

Para os anos de 2017-2021

![alt text](https://github.com/newtonjgaliza/Download-Diario-Oficial---Prefeitura-Lastro/blob/main/images/diarios_2017_2021.png)

É feita a interação com os botões de Download de cada elemento

Para os anos de 2022-2024

![alt text](https://github.com/newtonjgaliza/Download-Diario-Oficial---Prefeitura-Lastro/blob/main/images/diarios_2022_2024.png)

Precisamos selecionar o ano que queremos coletar, coletamos o href dentro do elemento ...

```
<ul class="dropdown-menu show" x-placement="top-start" style="position: absolute; transform: translate3d(0px, -39px, 0px); top: 0px; left: 0px; will-change: transform;"><li>
	<a data-loadmethod="xhr" class="fabrik_view fabrik__rowlink btn-default" data-list="list_27_com_fabrik_27" data-isajax="0" data-rowid="267" data-iscustom="0" href="/diario-oficial/details/27/267.html" title="Visualizar" target="_self">
<i data-isicon="true" class="icon-search "></i> Visualizar</a></li>
	</ul>
```
e concatenamos o endereço principal para ter uma url da seguinte forma 
https://www.lastro.pb.gov.br/diario-oficial/details/27/137.html

é criado um arquivo txt com todos esses links


![alt text](https://github.com/newtonjgaliza/Download-Diario-Oficial---Prefeitura-Lastro/blob/main/images/diarios_2017_2021-1.png)

Acessando cada link do arquivo, na página buscamos o href do elemento
```
<a title="Edição:&nbsp;2096 - 02/01/2025" href="/download/diario_oficial/DIARIO-OFICIAL-EDICAO-2096-LASTRO-31-12-2024.pdf" target="_blank">Clique aqui para baixar o Diário Oficial</a>
````

e montamos uma url semelhante a https://www.lastro.pb.gov.br/download/diario_oficial/DIARIO-OFICIAL-ESPECIAL-02-01-2023-LASTRO.pdf
fazendo um request para o endereço é realizado o download do arquivo pdf

![alt text](https://github.com/newtonjgaliza/Download-Diario-Oficial---Prefeitura-Lastro/blob/main/images/diarios_2017_2021-2.png)



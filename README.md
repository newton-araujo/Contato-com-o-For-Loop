<h1>Desafio 11 - Contando com o For Loop</h1>

<p>O código em Python utiliza um loop for para contar de 1 a 10, pausando por 1 segundo entre cada iteração usando sleep da biblioteca time. O resultado é a impressão dos números na mesma linha, criando uma contagem com intervalos de 1 segundo entre cada número.</p>

<ol>

<h2><li>Importação da biblioteca ' sleep ':</li></h2>
<ul>
<li><b>from time import sleep:</b> Importa o método sleep da biblioteca time. O método sleep é usado para adicionar atrasos (pausas) no código.</li>
</ul>

<h2><li>For Loop:</li></h2>
<ul>
<li><b>for contador in range(1, 11):</b> Inicia um loop for que itera sobre os números de 1 a 10 (o último valor no intervalo range é exclusivo).</li>
</ul>

<h2><li>Atraso de 1 segundo:</li></h2>
<ul>
<li><b>sleep(1):</b>Dentro do loop, adiciona um atraso de 1 segundo a cada iteração. Isso significa que o programa vai pausar por 1 segundo antes de continuar para a próxima iteração do loop.</li>
</ul>

<h2><li>Impressão do Contador:</li></h2>
<ul>
<li><b>print(contador, end=' '):</b> Imprime o valor atual de contador na mesma linha, seguido de um espaço. O argumento end=' ' é usado para evitar a quebra de linha após cada número impresso.</li>
</ul>
</ol>

<h1>Saída Esperada:</h1>
<p>Se você executar esse código, verá a contagem de 1 a 10, com um segundo de intervalo entre cada número. A saída será algo assim:
</p>

<b>TERMINAL:</b>
            
    1 2 3 4 5 6 7 8 9 10
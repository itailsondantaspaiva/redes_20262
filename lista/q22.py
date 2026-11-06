from bs4 import BeautifulSoup

html = """
<div class="produto">
  <h2>Notebook</h2>
  <span class="preco">R$ 3500</span>
</div>

<div class="produto">
  <h2>Mouse</h2>
  <span class="preco">R$ 80</span>
</div>

<div class="produto">
  <h2>Teclado</h2>
  <span class="preco">R$ 150</span>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

for produto in soup.find_all("div", class_="produto"):
    nome = produto.find("h2").text
    preco = produto.find("span", class_="preco").text
    print(f"{nome} - {preco}")
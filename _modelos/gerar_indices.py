import pathlib
R = pathlib.Path(r"C:\Users\alexs\Projetos\cerebro-autoridades")
S = {
 "marketing": ("Marketing", "Estratégia de marketing, funil, posicionamento de mercado, growth, retenção e LTV."),
 "ia": ("Inteligência Artificial", "Ferramentas, fluxos e visão de IA aplicada a marketing, criação, vendas e negócios."),
 "design": ("Design", "Design gráfico, direção de arte, tipografia, UI/UX, motion e processo criativo."),
 "branding": ("Branding", "Marca, identidade, posicionamento, arquitetura de marcas, marca pessoal e tom de voz."),
 "conteudo-e-redes": ("Conteúdo e Redes Sociais", "Instagram, YouTube, TikTok, LinkedIn: formatos, algoritmo, ganchos, roteiros e calendário."),
 "trafego-pago": ("Tráfego Pago", "Meta Ads (Andromeda, Advantage+), Google Ads, criativos de performance, formulários, CPL/CAC."),
 "vendas": ("Vendas", "Processo comercial, atendimento, follow-up, CRM, oferta, preço e negociação."),
 "mercado-imobiliario": ("Mercado Imobiliário", "Incorporação, lançamentos, corretores, jornada do comprador de imóvel e dados de mercado."),
 "negocios-e-gestao": ("Negócios e Gestão", "Estratégia de empresa, gargalos, liderança, cultura, finanças e modelo de negócio."),
}
P = {
 "michelly-muller": ("Michelly Müller", "marketing imobiliário prático, Instagram e Meta Ads para corretores",
     ["mercado-imobiliario","conteudo-e-redes","trafego-pago","branding","ia","vendas"]),
 "dener-lippert": ("Dener Lippert", "performance, gargalos, preço e LTV", ["marketing","vendas","negocios-e-gestao","trafego-pago"]),
 "alfredo-soares": ("Alfredo Soares", "marca como acelerador de vendas, eventos como ativo", ["branding","vendas","negocios-e-gestao"]),
 "tay-dantas": ("Tay Dantas", "diagnóstico e estratégia de marca em 8 camadas, brand performance", ["branding","marketing","conteudo-e-redes","negocios-e-gestao"]),
 "bruno-nardon": ("Bruno Nardon", "marca conforme o critério de valor do cliente", ["negocios-e-gestao","branding"]),
}
F = [
 ("2026-01-24", "Como criar conteúdo para vender imóveis em 2026", "Michelly Müller",
  "setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md",
  ["mercado-imobiliario","conteudo-e-redes","trafego-pago","branding","ia","vendas"]),
 ("2026-10-14", "Marketing e vendas para 2027 (EXTREMOS)", "Dener Lippert, Alfredo Soares, Bruno Nardon",
  "setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md",
  ["marketing","branding","vendas","negocios-e-gestao","trafego-pago","conteudo-e-redes"]),
 ("2025-05-28", "Branding que vende: marcas sexys (ROI Hunters #296)", "Tay Dantas",
  "setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md",
  ["branding","marketing","conteudo-e-redes","negocios-e-gestao"]),
]
F.sort(key=lambda x: x[0])
T = "setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md"
M = "setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md"
D = "setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md"
PRINC = {
 "branding": [
  "- **Marca e venda andam juntas:** marca serve para vender mais rápido e mais barato, não é desculpa para gasto sem retorno. Fontes: [Alfredo e Dener](../../%s), [Tay — brand performance](../../%s)." % (D, T),
  "- **Pessoas na frente da marca:** rostos (donos, equipe, clientes) conectam mais que logo. Marca pessoal dá velocidade e marca da empresa dá escala. Fontes: [Michelly](../../%s), [Tay](../../%s)." % (M, T),
  "- **O peso da marca depende do que o cliente valoriza:** quanto mais premium e exclusivo, mais a marca pesa. Fontes: [Nardon](../../%s), [Tay — luxo](../../%s)." % (D, T),
 ],
 "trafego-pago": ["- **Criativo é a principal alavanca da mídia.** Criativos realmente diferentes entre si (Andromeda) e muitos testes, com gancho nos 3 primeiros segundos e CTA claro. Fontes: [Michelly](../../%s), [Dener](../../%s)." % (F[0][3], F[1][3])],
 "vendas": ["- **O gargalo costuma estar depois do lead:** atendimento lento e falta de follow-up desperdiçam a mídia. Fontes: [Michelly — pós-captação 8–12 meses](../../%s), [Dener — elo mais fraco](../../%s)." % (F[0][3], F[1][3])],
 "conteudo-e-redes": ["- **Todo conteúdo precisa levar a uma ação** (CTA para comentário, direct ou WhatsApp). Fontes: [Michelly](../../%s), [Dener](../../%s)." % (F[0][3], F[1][3])],
}
for k,(nome,desc) in S.items():
    L = [f"# {nome}", "", desc, "", "## Autoridades de referência", "", "| Pessoa | Por que ouvir | Ficha |", "|---|---|---|"]
    for slug,(n,why,sets) in P.items():
        if k in sets: L.append(f"| {n} | {why} | [ficha](../../autoridades/{slug}.md) |")
    L += ["", "## Fontes resumidas", "", "| Data | Fonte | Autoridade | Arquivo |", "|---|---|---|---|"]
    for d,t,a,path,sets in F:
        if k in sets: L.append(f"| {d} | {t} | {a} | [resumo](../../{path}) |")
    L += ["", "## Princípios consolidados", "", "<!-- Ideias que aparecem em mais de uma fonte. Cada item cita os arquivos de origem. -->"]
    L += PRINC.get(k, [])
    (R/"setores"/k/"README.md").write_text("\n".join(L)+"\n", encoding="utf-8")
print("ok")

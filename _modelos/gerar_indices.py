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
 "alfredo-soares": ("Alfredo Soares", "marca como acelerador de vendas, agenda conectada, influência, conteúdo e marca pessoal", ["branding","vendas","negocios-e-gestao","marketing","conteudo-e-redes"]),
 "tay-dantas": ("Tay Dantas", "diagnóstico e estratégia de marca em 8 camadas, brand performance, audiência própria", ["branding","marketing","conteudo-e-redes","negocios-e-gestao","trafego-pago"]),
 "ana-couto": ("Ana Couto", "branding como gestão de valor, método, gap de percepção, CBO", ["branding","marketing","negocios-e-gestao"]),
 "philip-kotler": ("Philip Kotler", "base conceitual do marketing; série Marketing X.0", ["marketing","branding","negocios-e-gestao","ia"]),
 "seth-godin": ("Seth Godin", "ser notável; permissão, confiança e consistência", ["marketing","branding","conteudo-e-redes","ia"]),
 "claude-hopkins": ("Claude C. Hopkins", "copy de resposta direta: testar, medir, ser específico", ["marketing","trafego-pago","vendas","conteudo-e-redes"]),
 "david-ogilvy": ("David Ogilvy", "copy que vende + imagem de marca e grande ideia", ["marketing","branding","conteudo-e-redes","trafego-pago"]),
 "erich-shibata": ("Erich Shibata", "Cimed: marca-mãe, cor proprietária, colabs, varejo como parceiro", ["branding","marketing","vendas"]),
 "marty-neumeier": ("Marty Neumeier", "marca é a sensação do cliente, não o logo", ["branding","design"]),
 "alex-hormozi": ("Alex Hormozi", "marca pessoal: prova, associação, momentos de marca", ["branding","conteudo-e-redes","marketing","vendas"]),
 "gary-vaynerchuk": ("Gary Vaynerchuk", "mídia de interesse, volume, dar antes de pedir, marca acima de performance", ["conteudo-e-redes","marketing","mercado-imobiliario","branding"]),
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
F.append(("2024-01-22", "O poder do branding (Como Você Fez Isso?)", "Ana Couto",
  "setores/branding/fontes/2024-01-22_ana-couto_o-poder-do-branding.md",
  ["branding","marketing","negocios-e-gestao"]))
F.append(("2010", "Marketing 3.0 (livro)", "Philip Kotler, Hermawan Kartajaya, Iwan Setiawan",
  "setores/marketing/fontes/2010-01-01_philip-kotler_marketing-3-0.md",
  ["marketing","branding","negocios-e-gestao","vendas"]))
F.append(("2026-08-05", "Posicionamento do Nardon: o nerd rico", "Alfredo Soares, Bruno Nardon",
  "setores/conteudo-e-redes/fontes/2026-08-05_alfredo-soares_posicionamento-nardon-nerd-rico.md",
  ["conteudo-e-redes","branding","marketing"]))
F.append(("2021", "Marketing 5.0 (livro)", "Philip Kotler, Hermawan Kartajaya, Iwan Setiawan",
  "setores/marketing/fontes/2021-01-01_philip-kotler_marketing-5-0.md",
  ["marketing","ia","conteudo-e-redes","vendas","negocios-e-gestao"]))
F.append(("2023-11-23", "Marketing de influência que funciona (Jota Jota #142)", "Alfredo Soares",
  "setores/marketing/fontes/2023-11-23_alfredo-soares_marketing-de-influencia-jota-jota.md",
  ["marketing","vendas","branding","conteudo-e-redes","ia","negocios-e-gestao"]))
F.append(("2025-05-21", "Como vender mais e melhor (G4 Day)", "Alfredo Soares",
  "setores/vendas/fontes/2025-05-21_alfredo-soares_como-vender-mais-e-melhor-g4-day.md",
  ["vendas","marketing","negocios-e-gestao","branding"]))
F.append(("2026-11-06", "Marketing à prova de crise (The Code Vinci)", "Tay Dantas",
  "setores/branding/fontes/2026-11-06_tay-dantas_marketing-a-prova-de-crise.md",
  ["branding","marketing","conteudo-e-redes","trafego-pago"]))
F.append(("2026-08-16", "Advisor: a empresa da marca pessoal do Ninja", "Alfredo Soares",
  "setores/conteudo-e-redes/fontes/2026-08-16_alfredo-soares_advisor-ninja-arquitetura-de-marca-pessoal.md", ["conteudo-e-redes","branding","negocios-e-gestao","marketing"]))
F.append(("2003", "A Vaca Roxa (livro, via resumo Bookey)", "Seth Godin",
  "setores/marketing/fontes/2003-01-01_seth-godin_a-vaca-roxa.md",
  ["marketing","branding","conteudo-e-redes","negocios-e-gestao"]))
F.append(("1923", "Scientific Advertising (livro)", "Claude C. Hopkins",
  "setores/marketing/fontes/1923-01-01_claude-hopkins_scientific-advertising.md",
  ["marketing","trafego-pago","vendas","conteudo-e-redes","branding"]))
F.append(("1983", "Ogilvy on Advertising (livro, via resumo Bookey)", "David Ogilvy",
  "setores/marketing/fontes/1983-01-01_david-ogilvy_ogilvy-on-advertising.md",
  ["marketing","branding","conteudo-e-redes","trafego-pago","negocios-e-gestao"]))
F.append(("2024-06-18", "Branding & Cultura na Cimed (ROI Hunters #240)", "Erich Shibata",
  "setores/branding/fontes/2024-06-18_erich-shibata_branding-e-cultura-cimed.md",
  ["branding","marketing","vendas","conteudo-e-redes","negocios-e-gestao"]))
F.append(("2019-12-31", "O que é branding (The Futur)", "Marty Neumeier",
  "setores/branding/fontes/2019-12-31_marty-neumeier_o-que-e-branding.md",
  ["branding","design","marketing"]))
F.append(("2026-10-23", "Como construir uma marca pessoal em 2027", "Alex Hormozi",
  "setores/branding/fontes/2026-10-23_alex-hormozi_como-construir-marca-pessoal-2027.md",
  ["branding","conteudo-e-redes","marketing"]))
F.append(("2026-04-14", "Marca notável na era da IA (The Entrepreneur's Studio)", "Seth Godin",
  "setores/marketing/fontes/2026-04-14_seth-godin_marca-notavel-na-era-da-ia.md",
  ["marketing","branding","ia","conteudo-e-redes","negocios-e-gestao"]))
F.append(("2026-09-04", "Mídia de interesse e volume (2 vídeos)", "Gary Vaynerchuk",
  "setores/conteudo-e-redes/fontes/2026-09-04_garyvee_midia-de-interesse-e-volume.md",
  ["conteudo-e-redes","marketing","mercado-imobiliario","ia"]))
F.append(("2022-05-26", "Marca acima de venda digital (Inside 4Ds)", "Gary Vaynerchuk",
  "setores/branding/fontes/2022-05-26_garyvee_marca-acima-de-vendas-digitais.md",
  ["branding","marketing","conteudo-e-redes","negocios-e-gestao"]))
F.append(("2026-11-09", "Estudo de caso: Elephant Skin (portfólio, copy e lançamento)", "Pesquisa própria (Elephant Skin)",
  "setores/mercado-imobiliario/fontes/2026-11-09_estudo_elephant-skin.md",
  ["mercado-imobiliario","branding","marketing","conteudo-e-redes","design"]))
F.sort(key=lambda x: x[0])
T = "setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md"
M = "setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md"
A = "setores/branding/fontes/2024-01-22_ana-couto_o-poder-do-branding.md"
D = "setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md"
PRINC = {
 "marketing": [
  "- **Clientes falando de você valem mais que você falando de você:** dê algo notável para contar (status, pertencimento, história) e cumpra a promessa, principalmente quando é difícil. Fontes: [Godin — era da IA](../../setores/marketing/fontes/2026-04-14_seth-godin_marca-notavel-na-era-da-ia.md), [Godin — Vaca Roxa](../../setores/marketing/fontes/2003-01-01_seth-godin_a-vaca-roxa.md), [Tay — outros falam por você](../../setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md), [Hormozi — ciclo de marca](../../setores/branding/fontes/2026-10-23_alex-hormozi_como-construir-marca-pessoal-2027.md).",
  "- **Copy específica e com prova:** fatos, números e processo convencem; generalidade (\"alto padrão\", \"melhor\") é ignorada; depoimento real e demonstração valem mais que celebridade. Fontes: [Hopkins](../../setores/marketing/fontes/1923-01-01_claude-hopkins_scientific-advertising.md), [Ogilvy](../../setores/marketing/fontes/1983-01-01_david-ogilvy_ogilvy-on-advertising.md).",
  "- **Repetir o que funciona e manter consistência:** campanha e tom vencedores rodam até os números caírem, não até a equipe enjoar. Fontes: [Hopkins — individualidade](../../setores/marketing/fontes/1923-01-01_claude-hopkins_scientific-advertising.md), [Ogilvy — grande ideia e P&G](../../setores/marketing/fontes/1983-01-01_david-ogilvy_ogilvy-on-advertising.md), [Ana Couto — consistência](../../setores/branding/fontes/2024-01-22_ana-couto_o-poder-do-branding.md).",
 ],
 "branding": [
  "- **Patrocínio e evento só com verba e gente para ativar:** reservar mais verba para distribuir/ativar o ativo; patrocínio por ego não. Fontes: [Erich — Cimed](../../setores/branding/fontes/2024-06-18_erich-shibata_branding-e-cultura-cimed.md), [Alfredo — dobro para distribuir](../../setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md).",
  "- **Marca-mãe e ativo visual consistente:** concentrar atenção numa marca e repetir um ativo próprio (cor, selo) sempre igual; o logo é pequena parte da marca. Fontes: [Erich — Cimed](../../setores/branding/fontes/2024-06-18_erich-shibata_branding-e-cultura-cimed.md), [Ogilvy](../../setores/marketing/fontes/1983-01-01_david-ogilvy_ogilvy-on-advertising.md), [Ana Couto](../../setores/branding/fontes/2024-01-22_ana-couto_o-poder-do-branding.md).",
  "- **Diferenciação real, não \"muito bom\":** o comum é invisível; o notável (produto, experiência, atendimento) gera boca a boca e baixa o custo de aquisição. Fontes: [Godin — Vaca Roxa](../../setores/marketing/fontes/2003-01-01_seth-godin_a-vaca-roxa.md), [Tay — marca mais desejada](../../setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md), [Ana Couto — pontos de contato com intenção](../../setores/branding/fontes/2024-01-22_ana-couto_o-poder-do-branding.md).",
  "- **Identidade se mostra, não se declara:** escolher traços e mostrar os momentos reais do dia a dia que os provam (disciplina = postar a mesma coisa todo dia). Fontes: [Alfredo — Ninja](../../setores/conteudo-e-redes/fontes/2026-08-16_alfredo-soares_advisor-ninja-arquitetura-de-marca-pessoal.md), [Alfredo — nerd rico](../../setores/conteudo-e-redes/fontes/2026-08-05_alfredo-soares_posicionamento-nardon-nerd-rico.md), [Tay — marca pessoal](../../setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md).",
  "- **Marca e venda andam juntas:** marca serve para vender mais rápido e mais barato, não é desculpa para gasto sem retorno. Fontes: [Alfredo e Dener](../../%s), [Tay — brand performance](../../%s)." % (D, T),
  "- **Pessoas na frente da marca:** rostos (donos, equipe, clientes) conectam mais que logo. Marca pessoal dá velocidade e marca da empresa dá escala. Fontes: [Michelly](../../%s), [Tay](../../%s)." % (M, T),
  "- **\"Branding só dá resultado no longo prazo\" é falso dilema:** começar certo gera resultado no curto, médio e longo prazo. Fontes: [Tay](../../%s), [Ana Couto](../../%s)." % (T, A),
  "- **Marca é a percepção criada por todos os pontos de contato** (produto, loja, atendimento, equipe), não só pelo marketing ou pelo logo. Fontes: [Tay](../../%s), [Ana Couto](../../%s), [Neumeier](../../setores/branding/fontes/2019-12-31_marty-neumeier_o-que-e-branding.md)." % (T, A),
  "- **Diagnóstico pelo gap de percepção:** como o público quer ser visto e como a marca é vista, por dentro e por fora, vale mais que perfil demográfico. Fontes: [Tay](../../%s), [Ana Couto](../../%s)." % (T, A),
  "- **O peso da marca depende do que o cliente valoriza:** quanto mais premium e exclusivo, mais a marca pesa. Fontes: [Nardon](../../%s), [Tay — luxo](../../%s)." % (D, T),
 ],
 "trafego-pago": [
  "- **Documentação oficial da Meta** (campanhas, públicos, leilão, criativos, formulários, WhatsApp, mensuração, políticas): ver a pasta [META](../../META/README.md).",
  "- **Testar e medir pelo custo por cliente/venda, não pelo gosto:** mesmo criativo com ganchos/títulos diferentes, escalar o vencedor. Fontes: [Hopkins](../../setores/marketing/fontes/1923-01-01_claude-hopkins_scientific-advertising.md), [Michelly — Andromeda](../../setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md), [Dener — volume de testes](../../setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md).",
  "- **Não depender só de mídia paga:** construir audiência própria, marca e indicação para baixar o custo de aquisição e aguentar a alta do CPC. Fontes: [Tay — terra e tijolo](../../setores/branding/fontes/2026-11-06_tay-dantas_marketing-a-prova-de-crise.md), [GaryVee — venda digital muda, marca fica](../../setores/branding/fontes/2022-05-26_garyvee_marca-acima-de-vendas-digitais.md), [Alfredo — 30% orgânico](../../setores/vendas/fontes/2025-05-21_alfredo-soares_como-vender-mais-e-melhor-g4-day.md), [Dener — superestimam o tráfego](../../setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md).","- **Criativo é a principal alavanca da mídia.** Criativos realmente diferentes entre si (Andromeda) e muitos testes, com gancho nos 3 primeiros segundos e CTA claro. Fontes: [Michelly](../../%s), [Dener](../../%s)." % (M, D)],
 "vendas": [
  "- **Horário do cliente, não o seu:** ligar e atender na hora em que o cliente tem atenção (empresário à noite). Fontes: [Alfredo — Jota Jota](../../setores/marketing/fontes/2023-11-23_alfredo-soares_marketing-de-influencia-jota-jota.md), [Alfredo — G4 Day](../../setores/vendas/fontes/2025-05-21_alfredo-soares_como-vender-mais-e-melhor-g4-day.md), [Kotler 5.0 — marketing contextual](../../setores/marketing/fontes/2021-01-01_philip-kotler_marketing-5-0.md).",
  "- **CRM com disciplina + dados + IA:** registrar preferências do cliente, enriquecer dados e usar IA para priorizar e tratar objeções. Fontes: [Alfredo — tríade](../../setores/marketing/fontes/2023-11-23_alfredo-soares_marketing-de-influencia-jota-jota.md), [Kotler — Marketing 5.0](../../setores/marketing/fontes/2021-01-01_philip-kotler_marketing-5-0.md).",
  "- **O cliente atual é a alavanca mais barata (LTV):** vender melhor para quem já comprou e gerar indicação antes de buscar canais novos. Fontes: [Alfredo](../../setores/marketing/fontes/2023-11-23_alfredo-soares_marketing-de-influencia-jota-jota.md), [Dener](../../setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md), [Kotler 3.0 — credo 7](../../setores/marketing/fontes/2010-01-01_philip-kotler_marketing-3-0.md).","- **O gargalo costuma estar depois do lead:** atendimento lento e falta de follow-up desperdiçam a mídia. Fontes: [Michelly — pós-captação 8–12 meses](../../%s), [Dener — elo mais fraco](../../%s)." % (M, D)],
 "conteudo-e-redes": [
  "- **Falar do interesse do público, não de si:** conteúdo egoísta (\"compre de mim\") não tem alcance; o algoritmo entrega por interesse, então o criativo relevante gera o alcance. Fontes: [GaryVee](../../setores/conteudo-e-redes/fontes/2026-09-04_garyvee_midia-de-interesse-e-volume.md), [Alfredo — G4 Day](../../setores/vendas/fontes/2025-05-21_alfredo-soares_como-vender-mais-e-melhor-g4-day.md), [Michelly](../../setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md).",
  "- **Seguidor não é a métrica principal:** priorize vendas, leads qualificados, encaminhamentos e engajamento. Fontes: [Alfredo/Nardon](../../setores/conteudo-e-redes/fontes/2026-08-05_alfredo-soares_posicionamento-nardon-nerd-rico.md), [Tay](../../setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md).",
  "- **Conteúdo por etapa do funil com formatos fixos** (topo/meio/fundo), cada post com objetivo. Fontes: [Michelly](../../setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md), [Alfredo/Nardon](../../setores/conteudo-e-redes/fontes/2026-08-05_alfredo-soares_posicionamento-nardon-nerd-rico.md).","- **Todo conteúdo precisa levar a uma ação** (CTA para comentário, direct ou WhatsApp). Fontes: [Michelly](../../%s), [Dener](../../%s)." % (M, D)],
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

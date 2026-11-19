import pathlib
R = pathlib.Path(__file__).resolve().parents[1]
S = {
 "marketing": ("Marketing", "Estratégia de marketing, funil, posicionamento de mercado, growth, retenção e LTV."),
 "ia": ("Inteligência Artificial", "Ferramentas, fluxos e visão de IA aplicada a marketing, criação, vendas e negócios."),
 "design": ("Design", "Design gráfico, direção de arte, tipografia, UI/UX, motion e processo criativo."),
 "branding": ("Branding", "Marca, identidade, posicionamento, arquitetura de marcas, marca pessoal e tom de voz."),
 "conteudo-e-redes": ("Conteúdo e Redes Sociais", "Instagram, YouTube, TikTok, LinkedIn: formatos, algoritmo, ganchos, roteiros e calendário."),
 "trafego-pago": ("Tráfego Pago", "Meta Ads (Andromeda, Advantage+), Google Ads, criativos de performance, formulários, CPL/CAC."),
 "vendas": ("Vendas", "Processo comercial, atendimento, follow-up, CRM, oferta, preço e negociação."),
 "mercado-imobiliario": ("Mercado Imobiliário", "Incorporação, lançamentos, corretores, jornada do comprador de imóvel e dados de mercado."),
 "storytelling": ("Storytelling", "Narrativa, estrutura de história, roteiro, ganchos, tensão e retenção em vídeo, texto e apresentação."),
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
 "jason-murray": ("Jason Murray", "direção de arte como ingredientes: insight → ideia → 2–3 ingredientes de destaque; sensação × solução visual", ["design","branding","marketing"]),
 "artclass": ("ArtClass", "fundamentos: 7 princípios visuais e 7 regras de tipografia", ["design"]),
 "satori-graphics": ("Satori Graphics", "logo: contexto e categoria primeiro, testes no uso real, lacuna de propriedade", ["design","branding"]),
 "kittl": ("Kittl", "glossário de estilos de design com palavras de busca", ["design","branding"]),
 "louis-moss": ("Louis Moss", "moodboard como argumento: cada referência com razão, quadro enxuto e legendado", ["design","branding"]),
 "orenmeetsworld": ("orenmeetsworld", "direção de foto e vídeo de marca: ação/adereço, swipe file, curva de adoção", ["design","conteudo-e-redes"]),
 "fernando-kuwahara": ("Fernando F. Kuwahara", "monografia UFPR que resume Aaker, Keller e Kapferer: identidade, prisma, arquitetura, mensuração", ["branding","marketing"]),
 "rick-rubin": ("Rick Rubin", "processo criativo: fazer o que é seu, guardar versões, sem ego", ["design","branding"]),
 "luciana-silveira": ("Luciana Martha Silveira", "teoria da cor (UTFPR): física, percepção e cultura; contraste simultâneo; esquemas de paleta", ["design","branding"]),
 "nur-niaz": ("Nur Niaz", "direção de comercial: preparação resolve o set; editor no set; antes e depois na lente e na trilha", ["design","conteudo-e-redes"]),
 "designspo": ("DesignSpo", "tipografia para iniciantes: famílias, ajustes e sistema tipográfico", ["design"]),
 "jeremy-haynes": ("Jeremy Haynes", "Meta Ads ligado à venda: funil pelo time comercial, mensagem como segmentação, pixel com leads bons, gargalo", ["trafego-pago","vendas","marketing"]),
 "kallaway": ("Kallaway", "storytelling como loop e público em alvo (ICP no centro, mix 3-2-1); fundador da Sandcastles.ai", ["storytelling","conteudo-e-redes","trafego-pago","marketing","ia"]),
 "carmine-gallo": ("Carmine Gallo", "histórias de origem, clareza, apresentações e cultura organizacional", ["storytelling","branding","vendas","negocios-e-gestao","conteudo-e-redes","marketing"]),
 "chris-do": ("Chris Do", "The Futur: história de antes e depois, prova contra a lacuna de imaginação, nicho por perguntas A ou B", ["storytelling","branding","conteudo-e-redes","marketing","design"]),
 "philipp-humm": ("Philipp Humm", "zoom no momento com PAST: lugar, ação, fala, pensamentos", ["storytelling","conteudo-e-redes","vendas"]),
 "remi": ("Remi (Open Residency)", "agentes de IA na prática: contexto .md, MCPs, skills e pasta OS", ["ia","negocios-e-gestao","marketing","trafego-pago"]),
 "brock-johnson": ("Brock Johnson", "crescimento no Instagram: método NAP, retenção, Trial Reels, Stories STD e automação de DM", ["conteudo-e-redes","storytelling","vendas","marketing"]),
 "nate-gaffney": ("Nate Gaffney", "Trial Reels com método dos 5 e ideia vencedora virando série (de 10 mil a 800 mil em 78 dias)", ["conteudo-e-redes","storytelling","marketing"]),
 "hyeser": ("Hyeser", "crescer até 10 mil no Instagram: conteúdo com consumo comprovado e fases (consistência → vendas)", ["conteudo-e-redes","marketing"]),
 "george-clements": ("George Clements", "Meta Ads para high-ticket: oferta × mercado, confiança via marca pessoal, setter/closer e LTV", ["trafego-pago","vendas","marketing","negocios-e-gestao"]),
 "chase-chappell": ("Chase Chappell", "criativos de Meta Ads para o Andromeda: regra dos 33% (IA, UGC, própria), funil no nível do anúncio, avatares", ["trafego-pago","conteudo-e-redes","ia"]),
 "daniel-priestley": ("Daniel Priestley", "geração de leads por diagnóstico/scorecard: 15 perguntas que pontuam e qualificam", ["marketing","vendas","trafego-pago","mercado-imobiliario","negocios-e-gestao"]),
 "matt-gray": ("Matt Gray", "marca pessoal de fundador como empresa de mídia: 5 níveis, método 4-3-2-1, cascata de conteúdo e e-mail", ["branding","conteudo-e-redes","negocios-e-gestao","marketing"]),
 "mateo-jimenez": ("Mateo Jiménez", "funil de conteúdo TOFU/MOFU/BOFU com proporções", ["conteudo-e-redes","marketing"]),
 "teo-egana": ("Teo Egaña", "conteúdo para imobiliárias: séries de bairro, pessoas reais, newsletter", ["mercado-imobiliario","conteudo-e-redes","marketing","vendas"]),
 "ketherin-kaffka": ("Ketherin Kaffka", "perfil como programa de TV: séries recorrentes (monoflow)", ["conteudo-e-redes","branding","mercado-imobiliario"]),
 "metics-media": ("Metics Media (Matt)", "comparação prática OpenClaw x Hermes, instalação em VPS", ["ia","negocios-e-gestao"]),
 "kaye-creatives": ("Carima (kaye.creatives)", "crescimento no Instagram: outliers, Trial Reels, compartilhamentos e salvamentos", ["conteudo-e-redes","ia","marketing"]),
 "tim-runia": ("Tim Runia", "estrutura de história em 5 linhas antes de roteirizar e filmar", ["storytelling","conteudo-e-redes","design"]),
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
F.append(("2026-04-22", "A neurociência do storytelling viciante", "Kallaway",
  "setores/storytelling/fontes/2026-04-22_kallaway_neurociencia-do-storytelling-viciante.md",
  ["storytelling","conteudo-e-redes","trafego-pago"]))
F.append(("2016", "Storytelling (The Storyteller's Secret, livro)", "Carmine Gallo",
  "setores/storytelling/fontes/2016-01-01_carmine-gallo_storytelling.md",
  ["storytelling","branding","vendas","negocios-e-gestao","conteudo-e-redes"]))
F.append(("2026-11-11", "Roube esta abertura do CEO do Telegram (metáfora do Titanic)", "Philipp Humm",
  "setores/storytelling/fontes/2026-11-11_philipp-humm_abertura-do-ceo-do-telegram.md",
  ["storytelling","conteudo-e-redes","vendas"]))
F.append(("2026-04-19", "Zoom no momento: método PAST", "Philipp Humm",
  "setores/storytelling/fontes/2026-04-19_philipp-humm_zoom-no-momento-past.md",
  ["storytelling","conteudo-e-redes","vendas"]))
F.append(("2019", "Storytelling — leitura complementar: mapa dos 37 capítulos e páginas", "Carmine Gallo",
  "setores/storytelling/fontes/2019-01-01_carmine-gallo_storytelling.md",
  ["storytelling","branding","marketing","conteudo-e-redes","vendas","negocios-e-gestao"]))
F.append(("2026-07-22", "Agentes de IA: o curso completo (Open Residency)", "Remi",
  "setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md",
  ["ia","negocios-e-gestao","marketing","trafego-pago"]))
F.append(("2026-11-09", "Reel: funil de conteúdo TOFU, MOFU, BOFU", "Mateo Jiménez",
  "setores/conteudo-e-redes/fontes/2026-11-09_mateo-jimenez_funil-tofu-mofu-bofu.md",
  ["conteudo-e-redes","marketing"]))
F.append(("2026-09-19", "Reel: sistema TOFU com Trial Reels e YouTube", "Mateo Jiménez",
  "setores/conteudo-e-redes/fontes/2026-09-19_mateo-jimenez_sistema-tofu-trial-reels.md", ["conteudo-e-redes","marketing"]))
F.append(("2026-09-10", "Reel: estratégia de conteúdo para imobiliárias", "Teo Egaña",
  "setores/mercado-imobiliario/fontes/2026-09-10_teo-egana_estrategia-conteudo-inmobiliarias.md", ["mercado-imobiliario","conteudo-e-redes","marketing","vendas"]))
F.append(("2026-06-03", "Reel: perfil como programa de TV (monoflow)", "Ketherin Kaffka",
  "setores/conteudo-e-redes/fontes/2026-06-03_ketherin-kaffka_monoflow-perfil-como-programa-de-tv.md", ["conteudo-e-redes","branding","mercado-imobiliario"]))
F.append(("2026-10-23", "Corte Open Residency: público em alvo e mix 3-2-1", "Kallaway",
  "setores/conteudo-e-redes/fontes/2026-10-23_kallaway_publico-em-alvo-321.md", ["conteudo-e-redes","marketing","trafego-pago"]))
F.append(("2026-11-05", "Corte Open Residency (evidência fraca)", "Gary Vaynerchuk",
  "setores/conteudo-e-redes/fontes/2026-11-05_garyvee_corte-open-residency.md", ["conteudo-e-redes","marketing"]))
F.append(("2026-06-15", "OpenClaw vs Hermes Agent: qual escolher", "Metics Media",
  "setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md", ["ia","negocios-e-gestao"]))
F.append(("2026-10-16", "1M seguidores em 6 meses: 3 passos", "Carima (kaye.creatives)",
  "setores/conteudo-e-redes/fontes/2026-10-16_kaye-creatives_1m-seguidores-3-passos.md", ["conteudo-e-redes","marketing","ia"]))
F.append(("2026-10-29", "6 vantagens para crescer na era do AI slop", "Kallaway",
  "setores/conteudo-e-redes/fontes/2026-10-29_kallaway_6-alphas-contra-ai-slop.md", ["conteudo-e-redes","ia","branding","storytelling"]))
F.append(("2026-10-28", "Hermes Agent do zero: VPS, Telegram, vigias e memória", "Metics Media",
  "setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md", ["ia","negocios-e-gestao"]))
F.append(("2026-08-05", "Psicologia dos ganchos: texto, fala, imagem e lock-in", "Kallaway",
  "setores/storytelling/fontes/2026-08-05_kallaway_psicologia-dos-ganchos.md", ["storytelling","conteudo-e-redes","trafego-pago"]))
F.append(("2025-02-03", "Storytelling em 9 min: 5 técnicas do zoom (2025)", "Philipp Humm",
  "setores/storytelling/fontes/2025-02-03_philipp-humm_storytelling-em-9-minutos.md", ["storytelling","conteudo-e-redes","vendas"]))
F.append(("2025-07-10", "As 5 linhas para contar qualquer história", "Tim Runia",
  "setores/storytelling/fontes/2025-07-10_tim-runia_5-linhas-para-contar-qualquer-historia.md", ["storytelling","conteudo-e-redes","design"]))
F.append(("2026-08-14", "Se eu começasse nas redes em 2026 (lives, nicho, pós-post)", "Gary Vaynerchuk",
  "setores/conteudo-e-redes/fontes/2026-08-14_garyvee_se-eu-comecasse-nas-redes-em-2026.md", ["conteudo-e-redes","marketing","branding"]))
F.append(("2026-11-09", "Instagram Masterclass 2027: nicho, perfil, retenção, Trial Reels, Stories e DM", "Brock Johnson",
  "setores/conteudo-e-redes/fontes/2026-11-09_brock-johnson_instagram-masterclass-2027.md", ["conteudo-e-redes","storytelling","vendas","marketing"]))
F.append(("2026-10-18", "800 mil seguidores em 78 dias: método dos 5, série e estrutura", "Nate Gaffney",
  "setores/conteudo-e-redes/fontes/2026-10-18_nate-gaffney_800k-seguidores-em-78-dias.md", ["conteudo-e-redes","storytelling","marketing"]))
F.append(("2026-11-15", "Série de assinatura e colunas de ideias (967 mil seguidores)", "Nate Gaffney",
  "setores/conteudo-e-redes/fontes/2026-11-15_nate-gaffney_serie-assinatura-e-colunas.md", ["conteudo-e-redes","storytelling","marketing"]))
F.append(("2026-10-08", "A ordem certa para crescer no Instagram (fases até 10 mil)", "Hyeser",
  "setores/conteudo-e-redes/fontes/2026-10-08_hyeser_ordem-certa-para-crescer-no-instagram.md", ["conteudo-e-redes","marketing"]))
F.append(("2026-10-07", "Meta Ads 2027: oferta × mercado, confiança, processo de vendas e LTV", "George Clements",
  "setores/trafego-pago/fontes/2026-10-07_george-clements_meta-ads-2027-quatro-regras.md", ["trafego-pago","vendas","marketing","negocios-e-gestao"]))
F.append(("2026-06-26", "Criativos de Meta Ads 2027: regra dos 33%, funil no anúncio, verba distribuída", "Chase Chappell",
  "setores/trafego-pago/fontes/2026-06-26_chase-chappell_criativos-facebook-ads-2027.md", ["trafego-pago","conteudo-e-redes","ia"]))
F.append(("2025-10-11", "Landing page de diagnóstico (scorecard) que gera e qualifica leads", "Daniel Priestley",
  "setores/marketing/fontes/2025-10-11_daniel-priestley_landing-page-de-diagnostico.md", ["marketing","vendas","trafego-pago","mercado-imobiliario"]))
F.append(("2025-07-03", "Os 4 erros que matam um gancho: atraso, confusão, irrelevância, desinteresse", "Kallaway",
  "setores/storytelling/fontes/2025-07-03_kallaway_4-erros-de-gancho.md", ["storytelling","conteudo-e-redes","trafego-pago"]))
F.append(("2026-11-13", "Linguagem corporal em 5 ajustes (postura, mãos, gestos, olhar, rosto)", "Philipp Humm",
  "setores/storytelling/fontes/2026-11-13_philipp-humm_linguagem-corporal.md", ["storytelling","vendas","conteudo-e-redes"]))
F.append(("2026-07-22", "Os 5 níveis da marca pessoal lucrativa (4-3-2-1, CEO de mídia)", "Matt Gray",
  "setores/branding/fontes/2026-07-22_matt-gray_5-niveis-da-marca-pessoal.md", ["branding","conteudo-e-redes","negocios-e-gestao","marketing"]))
F.append(("2026-07-30", "Sistema de marca pessoal em 7 passos com skills de IA (voz, cascata, isca, workshop, 20/20/20)", "Matt Gray",
  "setores/branding/fontes/2026-07-30_matt-gray_sistema-operacional-da-marca-pessoal.md", ["branding","ia","vendas","negocios-e-gestao","conteudo-e-redes"]))
F.append(("2026-10-22", "8 dicas impopulares de estratégia (formato fixo, IA na entrada, CTA-presente, recorte)", "Kallaway",
  "setores/conteudo-e-redes/fontes/2026-10-22_kallaway_8-dicas-impopulares-de-estrategia.md", ["conteudo-e-redes","ia","marketing","vendas"]))
F.append(("2026-07-08", "5 skills do Claude para conteúdo (contexto, análise de canal, pulso de outliers, máquina de ganchos)", "Kallaway",
  "setores/ia/fontes/2026-07-08_kallaway_5-skills-do-claude-para-conteudo.md", ["ia","conteudo-e-redes","storytelling"]))
F.append(("2026-08-29", "Pare de promover, conte histórias (antes e depois, prova, nicho por A ou B)", "Chris Do",
  "setores/storytelling/fontes/2026-08-29_chris-do_pare-de-promover-conte-historias.md", ["storytelling","branding","conteudo-e-redes","marketing","ia"]))
F.append(("2026-08-26", "Marca pessoal é de uma pessoa só (fã número um, mostrar o lado que esconde)", "Chris Do",
  "setores/branding/fontes/2026-08-26_chris-do_marca-pessoal-e-de-uma-pessoa.md", ["branding","storytelling","conteudo-e-redes"]))
F.append(("2026-09-15", "Ingredientes de direção de arte (insight, ideia, sensação × solução visual)", "Jason Murray",
  "setores/design/fontes/2026-09-15_jason-murray_ingredientes-de-direcao-de-arte.md", ["design","branding","marketing","trafego-pago","conteudo-e-redes"]))
F.append(("2023-06-14", "O segredo do design ótimo (dominar o bom, critérios em escala, briefing vago)", "Chris Do",
  "setores/design/fontes/2023-06-14_chris-do_o-segredo-do-design-otimo.md", ["design","negocios-e-gestao"]))
F.append(("2026-10-05", "7 princípios de design visual (hierarquia, contraste, espaço em branco, teste dos 5 s)", "ArtClass",
  "setores/design/fontes/2026-10-05_artclass_7-principios-de-design-visual.md", ["design"]))
F.append(("2026-10-18", "7 regras de tipografia (linha, entrelinha, modo escuro, órfãs)", "ArtClass",
  "setores/design/fontes/2026-10-18_artclass_7-regras-de-tipografia.md", ["design"]))
F.append(("2026-10-21", "Guia de logo 2027 (contexto, requisitos, testes, lacuna de propriedade)", "Satori Graphics",
  "setores/design/fontes/2026-10-21_satori-graphics_guia-de-logo-2027.md", ["design","branding"]))
F.append(("2025-05-02", "15 estilos de design e palavras de busca", "Kittl",
  "setores/design/fontes/2025-05-02_kittl_15-estilos-de-design.md", ["design","branding","conteudo-e-redes"]))
F.append(("2026-07-16", "Portfólio de diretor de arte (grande ideia, key visual, 4–6 pontos de contato)", "Jason Murray",
  "setores/design/fontes/2026-07-16_jason-murray_portfolio-de-diretor-de-arte.md", ["design","branding","marketing","negocios-e-gestao"]))
F.append(("2025-01-12", "Guia de direção de arte (ação e adereço, swipe file, curva de adoção)", "orenmeetsworld",
  "setores/design/fontes/2025-01-12_orenmeetsworld_guia-de-direcao-de-arte.md", ["design","marketing","conteudo-e-redes","trafego-pago","branding"]))
F.append(("2026-04-09", "Como montar moodboard (referência com razão, quadro do cliente, teste dos 10 s)", "Louis Moss",
  "setores/design/fontes/2026-04-09_louis-moss_como-montar-moodboard.md", ["design","branding","marketing"]))
F.append(("2025-04-30", "Por que o design parece amador (uma emoção, 3 formatos, pré-mortem, arquivos)", "Satori Graphics",
  "setores/design/fontes/2025-04-30_satori-graphics_por-que-o-design-parece-amador.md", ["design","branding","marketing"]))
F.append(("2023-01-01", "Branding: o processo de construção de marcas (Aaker, Keller, Kapferer)", "Fernando F. Kuwahara",
  "setores/branding/fontes/2023-01-01_fernando-kuwahara_branding-processo-de-construcao-de-marcas.md", ["branding","marketing","design","conteudo-e-redes"]))
F.append(("2026-08-18", "Processo criativo sem ego (compilação de entrevistas)", "Rick Rubin",
  "setores/design/fontes/2026-08-18_rick-rubin_processo-criativo-sem-ego.md", ["design","branding","conteudo-e-redes"]))
F.append(("2015-01-01", "Introdução à teoria da cor (livro, 2ª ed., UTFPR)", "Luciana Martha Silveira",
  "setores/design/fontes/2015-01-01_luciana-silveira_introducao-a-teoria-da-cor.md", ["design","branding","marketing"]))
F.append(("2026-10-26", "Dirigir um comercial: preparação, set e pós", "Nur Niaz",
  "setores/design/fontes/2026-10-26_nur-niaz_dirigir-um-comercial.md", ["design","conteudo-e-redes","trafego-pago","marketing"]))
F.append(("2024-08-06", "Guia de tipografia para iniciantes (famílias, entrelinha, espaçamento, sistema)", "DesignSpo",
  "setores/design/fontes/2024-08-06_designspo_guia-de-tipografia-para-iniciantes.md", ["design","branding"]))
F.append(("2026-11-14", "Meta Ads em 15 minutos (funil, mensagem, estrutura, pixel, gargalo, escala)", "Jeremy Haynes",
  "setores/trafego-pago/fontes/2026-11-14_jeremy-haynes_meta-ads-em-15-minutos.md", ["trafego-pago","vendas","marketing"]))
F.append(("2026-09-16", "Algoritmo: viral × conversão ("recrute os 200 certos")", "Kallaway",
  "setores/conteudo-e-redes/fontes/2026-09-16_kallaway_algoritmo-viral-vs-conversao.md", ["conteudo-e-redes","marketing","vendas"]))
F.append(("2026-09-09", "Storytelling que converte (6 técnicas: dor do comprador, amplo→estreito, duplo aha)", "Kallaway",
  "setores/storytelling/fontes/2026-09-09_kallaway_storytelling-que-converte-6-tecnicas.md", ["storytelling","conteudo-e-redes","vendas","marketing"]))
F.append(("2024-10-29", "Psicologia do medo e da compra", "Kallaway",
  "setores/conteudo-e-redes/fontes/2024-10-29_kallaway_psicologia-do-medo-e-compra.md", ["conteudo-e-redes","marketing","storytelling","vendas"]))
F.append(("2025-11-06", "Psicologia da confiança (clareza, espelhamento, prova, um passo ao lado do desejo)", "Kallaway",
  "setores/conteudo-e-redes/fontes/2025-11-06_kallaway_psicologia-da-confianca-8-principios.md", ["conteudo-e-redes","storytelling","marketing","vendas"]))
F.sort(key=lambda x: x[0])
T = "setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md"
M = "setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md"
A = "setores/branding/fontes/2024-01-22_ana-couto_o-poder-do-branding.md"
D = "setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md"
PRINC = {
 "marketing": [
  "- **Clientes falando de você valem mais que você falando de você:** dê algo notável para contar (status, pertencimento, história) e cumpra a promessa, principalmente quando é difícil. Fontes: [Godin — era da IA](../../setores/marketing/fontes/2026-04-14_seth-godin_marca-notavel-na-era-da-ia.md), [Godin — Vaca Roxa](../../setores/marketing/fontes/2003-01-01_seth-godin_a-vaca-roxa.md), [Tay — outros falam por você](../../setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md), [Hormozi — ciclo de marca](../../setores/branding/fontes/2026-10-23_alex-hormozi_como-construir-marca-pessoal-2027.md).",
  "- **Copy específica e com prova:** fatos, números e processo convencem; generalidade (\"alto padrão\", \"melhor\") é ignorada; depoimento real e demonstração valem mais que celebridade. Fontes: [Hopkins](../../setores/marketing/fontes/1923-01-01_claude-hopkins_scientific-advertising.md), [Ogilvy](../../setores/marketing/fontes/1983-01-01_david-ogilvy_ogilvy-on-advertising.md), [Chris Do — lacuna de imaginação](../../setores/storytelling/fontes/2026-08-29_chris-do_pare-de-promover-conte-historias.md).",
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
 "storytelling": [
  "- **Estrutura mínima antes de roteirizar:** situação, desejo, obstáculo, virada e resultado, encadeados por causa e efeito; escreva em poucas linhas antes de gravar ou montar. Fontes: [Tim Runia, 5 linhas](../../setores/storytelling/fontes/2025-07-10_tim-runia_5-linhas-para-contar-qualquer-historia.md), [Gallo, Pixar e Guber](../../setores/storytelling/fontes/2016-01-01_carmine-gallo_storytelling.md), [Kallaway, stakes e virada](../../setores/storytelling/fontes/2026-04-22_kallaway_neurociencia-do-storytelling-viciante.md), [Kuwahara — identidade, imagem e promessa vazia (Aaker/Kapferer)](../../setores/branding/fontes/2023-01-01_fernando-kuwahara_branding-processo-de-construcao-de-marcas.md).",
  "- **Promessa clara e prova logo em seguida:** o gancho diz do que é e o que a pessoa ganha, com palavras específicas e sem trocadilho; a prova vem nos segundos seguintes para segurar e gerar confiança. Fontes: [Kallaway, psicologia dos ganchos](../../setores/storytelling/fontes/2026-08-05_kallaway_psicologia-dos-ganchos.md), [Ogilvy, títulos específicos e prova](../../setores/marketing/fontes/1983-01-01_david-ogilvy_ogilvy-on-advertising.md), [Kallaway — confiança e prova cedo](../../setores/conteudo-e-redes/fontes/2025-11-06_kallaway_psicologia-da-confianca-8-principios.md), [Chris Do — prova antes da compra](../../setores/storytelling/fontes/2026-08-29_chris-do_pare-de-promover-conte-historias.md).",
  "- **Sem conflito não há história:** o que está em jogo, a luta e a tensão vêm antes do triunfo; a versão 'deu tudo certo' não prende. Fontes: [Kallaway — stakes](../../setores/storytelling/fontes/2026-04-22_kallaway_neurociencia-do-storytelling-viciante.md), [Gallo — luta e triunfo, Hardy, Purdy](../../setores/storytelling/fontes/2016-01-01_carmine-gallo_storytelling.md), [Humm — sair da visão de helicóptero](../../setores/storytelling/fontes/2026-04-19_philipp-humm_zoom-no-momento-past.md), [Chris Do — McKee, querer × precisar](../../setores/storytelling/fontes/2026-08-29_chris-do_pare-de-promover-conte-historias.md).",
  "- **Detalhe concreto e específico gera crença e imagem mental:** nomear lugar, objeto, fala e número exatos, sem descrição genérica nem detalhe irrelevante. Fontes: [Gallo — Blakely, Frates](../../setores/storytelling/fontes/2016-01-01_carmine-gallo_storytelling.md), [Humm — PAST](../../setores/storytelling/fontes/2026-04-19_philipp-humm_zoom-no-momento-past.md).",
  "- **Comece no meio da ação, com pouco contexto:** a pergunta ou situação deve aparecer cedo, com contexto suficiente só para o público prever o que vem. Fontes: [Humm — ação e lugar](../../setores/storytelling/fontes/2026-04-19_philipp-humm_zoom-no-momento-past.md), [Kallaway — grande pergunta](../../setores/storytelling/fontes/2026-04-22_kallaway_neurociencia-do-storytelling-viciante.md), [Gallo — manchete nos primeiros 60 s](../../setores/storytelling/fontes/2016-01-01_carmine-gallo_storytelling.md).",
  "- **Surpresa que faz sentido:** quebrar a expectativa do público prende, desde que a virada tenha pista plantada e lógica. Fontes: [Kallaway — head fake](../../setores/storytelling/fontes/2026-04-22_kallaway_neurociencia-do-storytelling-viciante.md), [Gallo — violação de expectativa, Gates/Jobs](../../setores/storytelling/fontes/2016-01-01_carmine-gallo_storytelling.md).",
 ],
 "design": [
  "- **Menos elementos, mais clareza:** 2–3 ingredientes de destaque, um ponto de entrada, uma cor de destaque e espaço em branco; quando tudo grita, nada é ouvido. Fontes: [Jason Murray — contenção](../../setores/design/fontes/2026-09-15_jason-murray_ingredientes-de-direcao-de-arte.md), [ArtClass — 7 princípios](../../setores/design/fontes/2026-10-05_artclass_7-principios-de-design-visual.md), [Chris Do — fazer menos, melhor](../../setores/design/fontes/2023-06-14_chris-do_o-segredo-do-design-otimo.md), [Luciana Silveira — menos matizes, variar valor e textura](../../setores/design/fontes/2015-01-01_luciana-silveira_introducao-a-teoria-da-cor.md).",
  "- **Palavras vagas viram critérios e requisitos:** \"clean\", \"premium\", \"moderno\" precisam virar perguntas e uma lista curta de critérios julgáveis antes de executar e para aprovar. Fontes: [Chris Do — critérios em escala](../../setores/design/fontes/2023-06-14_chris-do_o-segredo-do-design-otimo.md), [Satori — adjetivos viram requisitos](../../setores/design/fontes/2026-10-21_satori-graphics_guia-de-logo-2027.md), [Louis Moss — cada referência com razão declarada](../../setores/design/fontes/2026-04-09_louis-moss_como-montar-moodboard.md).",
  "- **Ideia antes do visual e ocupar espaço próprio:** insight e conceito em uma frase antes do layout; olhar o que a categoria já faz para não ficar intercambiável. Fontes: [Jason Murray — insight e ideia](../../setores/design/fontes/2026-09-15_jason-murray_ingredientes-de-direcao-de-arte.md), [Satori — lacuna de propriedade](../../setores/design/fontes/2026-10-21_satori-graphics_guia-de-logo-2027.md), [Kallaway — fuga do cluster](../../setores/conteudo-e-redes/fontes/2026-10-29_kallaway_6-alphas-contra-ai-slop.md), [Satori — uma emoção só](../../setores/design/fontes/2025-04-30_satori-graphics_por-que-o-design-parece-amador.md), [Jason Murray — uma grande ideia por projeto](../../setores/design/fontes/2026-07-16_jason-murray_portfolio-de-diretor-de-arte.md).",
 ],
 "ia": [
  "- **Correção vira memória persistente:** preferência ensinada uma vez fica salva e vale em toda sessão nova, de preferência em arquivo seu. Fontes: [Remi, memory.md](../../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md), [Metics, memória do Hermes](../../setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md).",
  "- **Agente que age em contas roda isolado e começa com pouca permissão:** máquina separada (VPS, Mac mini) em vez do PC de trabalho, só leitura e envio em rascunho até ganhar confiança, e versões sempre atualizadas. Fontes: [Remi — só leitura e aprovação](../../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md), [Metics — VPS e CVEs](../../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md), [Metics — VPS e allow list no Telegram](../../setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md).",
  "- **Tarefa repetida vira skill:** fazer uma vez, ajustar e salvar como skill (ou deixar o agente aprender sozinho) é o que deixa o agente útil e mais barato com o tempo. Fontes: [Remi — processo primeiro](../../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md), [Metics — Curator do Hermes](../../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md), [Kallaway — 5 skills de pesquisa de conteúdo](../../setores/ia/fontes/2026-07-08_kallaway_5-skills-do-claude-para-conteudo.md).",
 ],
 "trafego-pago": [
  "- **Documentação oficial da Meta** (campanhas, públicos, leilão, criativos, formulários, WhatsApp, mensuração, políticas): ver a pasta [META](../../META/README.md).",
  "- **Testar e medir pelo custo por cliente/venda, não pelo gosto:** mesmo criativo com ganchos/títulos diferentes, escalar o vencedor. Fontes: [Hopkins](../../setores/marketing/fontes/1923-01-01_claude-hopkins_scientific-advertising.md), [Michelly — Andromeda](../../setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md), [Dener — volume de testes](../../setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md), [Jeremy Haynes — análise de gargalo e pixel com leads qualificados](../../setores/trafego-pago/fontes/2026-11-14_jeremy-haynes_meta-ads-em-15-minutos.md).",
  "- **Não depender só de mídia paga:** construir audiência própria, marca e indicação para baixar o custo de aquisição e aguentar a alta do CPC. Fontes: [Tay — terra e tijolo](../../setores/branding/fontes/2026-11-06_tay-dantas_marketing-a-prova-de-crise.md), [GaryVee — venda digital muda, marca fica](../../setores/branding/fontes/2022-05-26_garyvee_marca-acima-de-vendas-digitais.md), [Alfredo — 30% orgânico](../../setores/vendas/fontes/2025-05-21_alfredo-soares_como-vender-mais-e-melhor-g4-day.md), [Dener — superestimam o tráfego](../../setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md), [George Clements — marca pessoal cortou o custo por agendamento pela metade](../../setores/trafego-pago/fontes/2026-10-07_george-clements_meta-ads-2027-quatro-regras.md).","- **Criativo é a principal alavanca da mídia.** Criativos realmente diferentes entre si (Andromeda) e muitos testes, com gancho nos 3 primeiros segundos e CTA claro. Fontes: [Michelly](../../%s), [Dener](../../%s), [Chase Chappell — formatos únicos por etapa no mesmo conjunto, verba distribuída](../../setores/trafego-pago/fontes/2026-06-26_chase-chappell_criativos-facebook-ads-2027.md)." % (M, D)],
 "vendas": [
  "- **Horário do cliente, não o seu:** ligar e atender na hora em que o cliente tem atenção (empresário à noite). Fontes: [Alfredo — Jota Jota](../../setores/marketing/fontes/2023-11-23_alfredo-soares_marketing-de-influencia-jota-jota.md), [Alfredo — G4 Day](../../setores/vendas/fontes/2025-05-21_alfredo-soares_como-vender-mais-e-melhor-g4-day.md), [Kotler 5.0 — marketing contextual](../../setores/marketing/fontes/2021-01-01_philip-kotler_marketing-5-0.md).",
  "- **CRM com disciplina + dados + IA:** registrar preferências do cliente, enriquecer dados e usar IA para priorizar e tratar objeções. Fontes: [Alfredo — tríade](../../setores/marketing/fontes/2023-11-23_alfredo-soares_marketing-de-influencia-jota-jota.md), [Kotler — Marketing 5.0](../../setores/marketing/fontes/2021-01-01_philip-kotler_marketing-5-0.md).",
  "- **O cliente atual é a alavanca mais barata (LTV):** vender melhor para quem já comprou e gerar indicação antes de buscar canais novos. Fontes: [Alfredo](../../setores/marketing/fontes/2023-11-23_alfredo-soares_marketing-de-influencia-jota-jota.md), [Dener](../../setores/marketing/fontes/2026-10-14_dener-lippert_marketing-e-vendas-2027-extremos.md), [Kotler 3.0 — credo 7](../../setores/marketing/fontes/2010-01-01_philip-kotler_marketing-3-0.md).","- **O gargalo costuma estar depois do lead:** atendimento lento e falta de follow-up desperdiçam a mídia. Fontes: [Michelly — pós-captação 8–12 meses](../../%s), [Dener — elo mais fraco](../../%s), [George Clements — setter, faltas e perdidos](../../setores/trafego-pago/fontes/2026-10-07_george-clements_meta-ads-2027-quatro-regras.md)." % (M, D)],
 "conteudo-e-redes": [
  "- **Postar é só o começo:** responder comentários, fazer lives e transformar as perguntas do público em pauta. Fontes: [GaryVee, começar em 2026](../../setores/conteudo-e-redes/fontes/2026-08-14_garyvee_se-eu-comecasse-nas-redes-em-2026.md), [GaryVee, Q&A semanal](../../setores/branding/fontes/2022-05-26_garyvee_marca-acima-de-vendas-digitais.md), [Michelly, caixinhas de dúvidas](../../setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md).",
  "- **Documentar o trabalho real em vez de inventar conteúdo.** Fontes: [GaryVee, documentar](../../setores/conteudo-e-redes/fontes/2026-08-14_garyvee_se-eu-comecasse-nas-redes-em-2026.md), [Hormozi, volume de trabalho documentado](../../setores/branding/fontes/2026-10-23_alex-hormozi_como-construir-marca-pessoal-2027.md).",
  "- **Assinatura visual própria e reconhecível:** personagem, cenário, seleção visual, layout, tipografia e movimento repetidos até virar marca; com IA deixando tudo igual, é a vantagem difícil de copiar. Fontes: [Kallaway — fosso visual](../../setores/conteudo-e-redes/fontes/2026-10-29_kallaway_6-alphas-contra-ai-slop.md), [Ketherin Kaffka — Jean Black e séries](../../setores/conteudo-e-redes/fontes/2026-06-03_ketherin-kaffka_monoflow-perfil-como-programa-de-tv.md).",
  "- **Trial Reels para multiplicar o que já funcionou:** reel que vai bem nas primeiras 24 h ganha 2 ou 3 variações publicadas como trial (só para não seguidores) antes de pôr verba. Atenção à ordem: vídeo que já está no feed trava como trial (duplicado), então o trial sai primeiro e a variação muda o gancho e os primeiros segundos. Fontes: [Kaye — variações como trial](../../setores/conteudo-e-redes/fontes/2026-10-16_kaye-creatives_1m-seguidores-3-passos.md), [Mateo Jiménez — reels virais viram trial](../../setores/conteudo-e-redes/fontes/2026-09-19_mateo-jimenez_sistema-tofu-trial-reels.md), [Brock Johnson — trial antes do feed](../../setores/conteudo-e-redes/fontes/2026-11-09_brock-johnson_instagram-masterclass-2027.md), [Nate Gaffney — método dos 5](../../setores/conteudo-e-redes/fontes/2026-10-18_nate-gaffney_800k-seguidores-em-78-dias.md).",
  "- **Ideia que funcionou vira série, não peça avulsa:** formato fixo, nome e episódios dão motivo para seguir (Nate: mesmo conceito deu 13 mil seguidores avulso e 57 mil como episódio 1). Fontes: [Nate Gaffney — contêiner](../../setores/conteudo-e-redes/fontes/2026-10-18_nate-gaffney_800k-seguidores-em-78-dias.md), [Ketherin Kaffka — perfil como programa de TV](../../setores/conteudo-e-redes/fontes/2026-06-03_ketherin-kaffka_monoflow-perfil-como-programa-de-tv.md), [Brock Johnson — formatos repetíveis](../../setores/conteudo-e-redes/fontes/2026-11-09_brock-johnson_instagram-masterclass-2027.md), [Nate Gaffney — colunas e abertura](../../setores/conteudo-e-redes/fontes/2026-11-15_nate-gaffney_serie-assinatura-e-colunas.md), [Kallaway — 1 ou 2 formatos como série de TV](../../setores/conteudo-e-redes/fontes/2026-10-22_kallaway_8-dicas-impopulares-de-estrategia.md).",
  "- **Tema e formato vêm do que já tem consumo; o ângulo é seu:** pesquisar busca e outliers (inclusive no TikTok) antes de pautar e testar o formato em Trial Reels. Fontes: [Hyeser — palavra-chave e formato](../../setores/conteudo-e-redes/fontes/2026-10-08_hyeser_ordem-certa-para-crescer-no-instagram.md), [Kaye — outliers](../../setores/conteudo-e-redes/fontes/2026-10-16_kaye-creatives_1m-seguidores-3-passos.md), [Brock Johnson — formato vence tema](../../setores/conteudo-e-redes/fontes/2026-11-09_brock-johnson_instagram-masterclass-2027.md).",
  "- **Compartilhamento é o sinal que leva ao viral; retenção leva ao médio:** otimize o topo para envios (específico, identificável, entretém) e corte setup e CTA final que derrubam a curva. Fontes: [Brock Johnson — hierarquia de sinais e 5 gráficos](../../setores/conteudo-e-redes/fontes/2026-11-09_brock-johnson_instagram-masterclass-2027.md), [Kallaway — ganchos e lock-in](../../setores/storytelling/fontes/2026-08-05_kallaway_psicologia-dos-ganchos.md), [Mateo Jiménez — topo medido por compartilhamentos](../../setores/conteudo-e-redes/fontes/2026-11-09_mateo-jimenez_funil-tofu-mofu-bofu.md).",
  "- **Formato validado adaptado, não ideia do zero:** salvar só referências que explodiram (outliers), inclusive de fora do nicho, e adaptar estrutura e gancho à marca, com crédito quando copiar muito. Contraponto: copiar outliers sem ângulo próprio leva todos ao mesmo \"cluster\"; use dados para o tema e coloque ângulo, substância e visual seus ([Kallaway — anti-slop](../../setores/conteudo-e-redes/fontes/2026-10-29_kallaway_6-alphas-contra-ai-slop.md)). Fontes: [Kaye — regra do outlier](../../setores/conteudo-e-redes/fontes/2026-10-16_kaye-creatives_1m-seguidores-3-passos.md), [Teo Egaña — formato validado e imaginável](../../setores/mercado-imobiliario/fontes/2026-09-10_teo-egana_estrategia-conteudo-inmobiliarias.md).",
  "- **Falar do interesse do público, não de si:** conteúdo egoísta (\"compre de mim\") não tem alcance; o algoritmo entrega por interesse, então o criativo relevante gera o alcance. Fontes: [GaryVee](../../setores/conteudo-e-redes/fontes/2026-09-04_garyvee_midia-de-interesse-e-volume.md), [Alfredo — G4 Day](../../setores/vendas/fontes/2025-05-21_alfredo-soares_como-vender-mais-e-melhor-g4-day.md), [Michelly](../../setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md).",
  "- **Seguidor não é a métrica principal:** priorize vendas, leads qualificados, encaminhamentos e engajamento. Fontes: [Alfredo/Nardon](../../setores/conteudo-e-redes/fontes/2026-08-05_alfredo-soares_posicionamento-nardon-nerd-rico.md), [Tay](../../setores/branding/fontes/2025-05-28_tay-dantas_branding-que-vende-marcas-sexys.md).",
  "- **Conteúdo por etapa do funil com formatos fixos** (topo/meio/fundo), cada post com objetivo; o topo é a maior fatia (Mateo sugere ~60–70% topo, 20–30% meio, 10–20% fundo). Fontes: [Mateo Jiménez](../../setores/conteudo-e-redes/fontes/2026-11-09_mateo-jimenez_funil-tofu-mofu-bofu.md), [Michelly](../../setores/mercado-imobiliario/fontes/2026-01-24_michelly-muller_conteudo-para-vender-imoveis-2026.md), [Alfredo/Nardon](../../setores/conteudo-e-redes/fontes/2026-08-05_alfredo-soares_posicionamento-nardon-nerd-rico.md).","- **Todo conteúdo precisa levar a uma ação** (CTA para comentário, direct ou WhatsApp), de preferência um presente ligado ao tema do post (\"comente X e receba…\") com automação de DM, nunca \"compre\" nem \"siga\". Fontes: [Michelly](../../%s), [Dener](../../%s), [Kallaway — native embed](../../setores/conteudo-e-redes/fontes/2026-10-22_kallaway_8-dicas-impopulares-de-estrategia.md), [Brock Johnson — automação de DM](../../setores/conteudo-e-redes/fontes/2026-11-09_brock-johnson_instagram-masterclass-2027.md), [Matt Gray — isca contextual](../../setores/branding/fontes/2026-07-30_matt-gray_sistema-operacional-da-marca-pessoal.md)." % (M, D),
  "- **Público certo vale mais que view:** para gerar venda, conteúdo específico para um comprador (tema filtrado, palavras dele, CTA por comentário) supera alcance amplo; medir por lead e visita, e tratar viral como outro jogo. Fontes: [Kallaway — algoritmo viral × conversão](../../setores/conteudo-e-redes/fontes/2026-09-16_kallaway_algoritmo-viral-vs-conversao.md), [Kallaway — recorte em vez de viral](../../setores/conteudo-e-redes/fontes/2026-10-22_kallaway_8-dicas-impopulares-de-estrategia.md), [Chris Do — quem serve todos não serve ninguém](../../setores/storytelling/fontes/2026-08-29_chris-do_pare-de-promover-conte-historias.md), [GaryVee — interesse do público](../../setores/conteudo-e-redes/fontes/2026-09-04_garyvee_midia-de-interesse-e-volume.md), [Mateo Jiménez — fundo medido por leads](../../setores/conteudo-e-redes/fontes/2026-11-09_mateo-jimenez_funil-tofu-mofu-bofu.md).",
  "- **IA na entrada, humano na saída:** pesquisa, pauta e análise com IA; ângulo, roteiro, voz, gravação e edição com gente, senão o conteúdo fica genérico. Fontes: [Kallaway — IA na entrada](../../setores/conteudo-e-redes/fontes/2026-10-22_kallaway_8-dicas-impopulares-de-estrategia.md), [Kallaway — anti-slop](../../setores/conteudo-e-redes/fontes/2026-10-29_kallaway_6-alphas-contra-ai-slop.md), [Matt Gray — voz real gravada](../../setores/branding/fontes/2026-07-30_matt-gray_sistema-operacional-da-marca-pessoal.md), [Brock Johnson — AI slop](../../setores/conteudo-e-redes/fontes/2026-11-09_brock-johnson_instagram-masterclass-2027.md), [Kallaway — skills só de pesquisa e régua de ganchos](../../setores/ia/fontes/2026-07-08_kallaway_5-skills-do-claude-para-conteudo.md), [Rick Rubin — IA dá a resposta média, a perspectiva é humana](../../setores/design/fontes/2026-08-18_rick-rubin_processo-criativo-sem-ego.md)."],
}
GT = {"roteiro-de-video-e-reels":"Roteiro de vídeo e reels","estrategia-de-conteudo-nas-redes":"Estratégia de conteúdo","conteudo-para-imobiliario":"Conteúdo imobiliário","apresentacoes-decks-e-pitch":"Apresentações e pitch","marca-e-posicionamento":"Marca e posicionamento","anuncios-e-trafego-pago":"Anúncios e tráfego","vendas-e-atendimento":"Vendas e atendimento","agentes-de-ia":"Agentes de IA","direcao-de-arte":"Direção de arte"}
GS = {  # guias relacionados a cada setor
 "marketing": ["anuncios-e-trafego-pago","marca-e-posicionamento","estrategia-de-conteudo-nas-redes"],
 "ia": ["agentes-de-ia"],
 "design": ["direcao-de-arte","marca-e-posicionamento","roteiro-de-video-e-reels"],
 "branding": ["marca-e-posicionamento","direcao-de-arte","apresentacoes-decks-e-pitch"],
 "conteudo-e-redes": ["estrategia-de-conteudo-nas-redes","roteiro-de-video-e-reels","conteudo-para-imobiliario"],
 "trafego-pago": ["anuncios-e-trafego-pago"],
 "vendas": ["vendas-e-atendimento","apresentacoes-decks-e-pitch"],
 "mercado-imobiliario": ["conteudo-para-imobiliario","vendas-e-atendimento","anuncios-e-trafego-pago"],
 "storytelling": ["roteiro-de-video-e-reels","apresentacoes-decks-e-pitch"],
 "negocios-e-gestao": ["agentes-de-ia","marca-e-posicionamento"],
}
for k,(nome,desc) in S.items():
    L = [f"# {nome}", "", desc, "", "**Guias relacionados:** " + " · ".join(f"[{GT[g]}](../../guias/{g}.md)" for g in GS.get(k,[])) + " · [← início](../../README.md)", "", "## Autoridades de referência", "", "| Pessoa | Por que ouvir | Ficha |", "|---|---|---|"]
    for slug,(n,why,sets) in P.items():
        if k in sets: L.append(f"| {n} | {why} | [ficha](../../autoridades/{slug}.md) |")
    L += ["", "## Fontes resumidas", "", "| Data | Fonte | Autoridade | Arquivo |", "|---|---|---|---|"]
    for d,t,a,path,sets in F:
        if k in sets: L.append(f"| {d} | {t} | {a} | [resumo](../../{path}) |")
    L += ["", "## Princípios consolidados", "", "<!-- Ideias que aparecem em mais de uma fonte. Cada item cita os arquivos de origem. -->"]
    L += PRINC.get(k, [])
    (R/"setores"/k/"README.md").write_text("\n".join(L)+"\n", encoding="utf-8")
print("ok")

# ---------------------------------------------------------------------------
# Índices globais: README.md (raiz), INDICE.md e guias/README.md
# Gerados a partir de S, P, F, PRINC, G e do frontmatter das fontes. Não editar à mão.
# ---------------------------------------------------------------------------
import re as _re, datetime as _dt

G = [  # guias por tarefa: (arquivo, título, use quando)
 ("roteiro-de-video-e-reels.md", "Roteiro de vídeo e reels", "escrever ou revisar roteiro, gancho, depoimento, manifesto"),
 ("estrategia-de-conteudo-nas-redes.md", "Estratégia de conteúdo nas redes", "planejar calendário, linha editorial, séries, métricas"),
 ("conteudo-para-imobiliario.md", "Conteúdo para incorporadora e imobiliária", "pauta e séries de empreendimentos, corretores, lista de espera"),
 ("apresentacoes-decks-e-pitch.md", "Apresentações, decks e pitch", "deck de lançamento, apresentação a corretores, investidores, propostas"),
 ("marca-e-posicionamento.md", "Marca e posicionamento", "posicionamento, manual, arquitetura de marcas, marca pessoal"),
 ("anuncios-e-trafego-pago.md", "Anúncios e tráfego pago (Meta)", "campanha, criativos de performance, formulário, WhatsApp, mensuração"),
 ("vendas-e-atendimento.md", "Vendas e atendimento", "material para corretores, follow-up, CRM, argumentário"),
 ("direcao-de-arte.md", "Direção de arte", "visual de campanha, feed ou peça, briefing para designer ou IA, revisar arte sem cara"),
 ("agentes-de-ia.md", "Criar ou escolher um agente de IA", "decidir Hermes x OpenClaw x skill, permissões, onde rodar"),
]

def _front(path):
    t = (R/path).read_text(encoding="utf-8")
    m = _re.match(r"^---\n(.*?)\n---", t, _re.S)
    d = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                d[k.strip()] = v.split(" #")[0].strip().strip('"')
    return d

def _evid(e):
    el = e.lower()
    if "muito fraca" in el: return "⚠️ fraca"
    if "não é o livro completo" in el or "bookey" in el: return "◐ resumo de terceiros"
    if "frames" in el or "sem áudio" in el: return "◐ parcial (sem áudio)"
    if "tradução automática" in el or "traduzida" in el: return "◑ tradução automática"
    if "pesquisa web" in el: return "● pesquisa própria"
    if "leitura integral" in el or "legenda manual" in el or "lida inteira" in el or "leitura do pdf" in el: return "● completa"
    return "● legenda original"

FX = []
for d,t,a,path,sets in F:
    fm = _front(path)
    FX.append(dict(data=d, titulo=t, autor=a, path=path, setor=sets[0], sets=sets,
                   tipo=fm.get("tipo","?"), inc=fm.get("data_inclusao",""), ev=_evid(fm.get("evidencia","")),
                   auts=fm.get("autoridades","")))
ns = {k: sum(1 for f in FX if f["setor"]==k) for k in S}
nx = {k: sum(1 for f in FX if k in f["sets"]) for k in S}
npr = {k: len(PRINC.get(k, [])) for k in S}

# INDICE.md
L = ["# Índice geral de fontes", "",
     f"{len(FX)} fontes de {len(P)} autoridades. Gerado por `_modelos/gerar_indices.py`; não editar à mão.", "",
     "**Evidência:** ● completa ou legenda original · ◑ tradução automática · ◐ parcial (resumo de terceiros ou reel sem áudio) · ⚠️ fraca (reassistir antes de citar).", "",
     "## Mais recentes (por data de inclusão)", "",
     "| Incluída | Fonte | Autoridade | Setor | Tipo | Evidência |", "|---|---|---|---|---|---|"]
for f in sorted(FX, key=lambda x:(x["inc"], x["data"]), reverse=True):
    L.append(f"| {f['inc']} | [{f['titulo']}]({f['path']}) | {f['autor']} | {S[f['setor']][0]} | {f['tipo']} | {f['ev']} |")
L += ["", "## Por setor principal", ""]
for k,(nome,_) in S.items():
    fs = [f for f in FX if f["setor"]==k]
    if not fs: continue
    L += [f"### [{nome}](setores/{k}/README.md)", ""]
    for f in sorted(fs, key=lambda x:x["data"], reverse=True):
        L.append(f"- {f['data']} · [{f['titulo']}]({f['path']}) · {f['autor']} · {f['ev']}")
    L.append("")
L += ["## Por autoridade", "", "| Autoridade | Foco | Fontes |", "|---|---|---|"]
for slug,(n,why,sets) in sorted(P.items(), key=lambda x:x[1][0].lower()):
    c = sum(1 for f in FX if slug in f["auts"])
    L.append(f"| [{n}](autoridades/{slug}.md) | {why} | {c} |")
(R/"INDICE.md").write_text("\n".join(L)+"\n", encoding="utf-8")

# guias/README.md
L = ["# Guias por tarefa", "", "Comece por aqui quando for **fazer** algo. Cada guia tem um checklist rápido, as fontes para ler em ordem e os cuidados.", "",
     "| Guia | Use quando |", "|---|---|"]
for arq,tit,quando in G:
    L.append(f"| [{tit}]({arq}) | {quando} |")
L += ["", "[← Voltar ao início](../README.md)"]
(R/"guias"/"README.md").write_text("\n".join(L)+"\n", encoding="utf-8")

# README.md (raiz)
rec = sorted(FX, key=lambda x:(x["inc"], x["data"]), reverse=True)[:8]
L = ["# Cérebro de Autoridades", "",
 "Base de conhecimento **externo** do Alex (We Inc / Ecossistema WE): o que pessoas de referência dizem sobre marketing, conteúdo, storytelling, branding, tráfego, vendas, mercado imobiliário e IA, resumido em português com **aplicação para a We** e **pontos fracos** de cada fonte.", "",
 "> O conhecimento **interno** (clientes, projetos, aprendizados) fica no `cerebroagent` e em `G:\\Meu Drive\\00_CEREBRO CRIAÇÃO`. Aqui só entra o que vem de fora.", "",
 f"**{len(FX)} fontes · {len(P)} autoridades · {len(S)} setores · {len(G)} guias · {sum(npr.values())} princípios consolidados**", "",
 "## Como consultar", "",
 "| Quero… | Vá para |", "|---|---|",
 "| **fazer** algo (roteiro, calendário, deck, campanha, agente) | [Guias por tarefa](guias/README.md) |",
 "| saber o que já está **confirmado por mais de uma fonte** | **Princípios consolidados** no README de cada setor (tabela abaixo) |",
 "| achar uma fonte específica ou ver as mais recentes | [Índice geral](INDICE.md) |",
 "| saber o que uma pessoa pensa | [Autoridades](#autoridades) |",
 "| regras oficiais de anúncios na Meta | [Pasta META](META/README.md) |", "",
 "## Guias por tarefa", "", "| Guia | Use quando |", "|---|---|"]
for arq,tit,quando in G:
    L.append(f"| [{tit}](guias/{arq}) | {quando} |")
L += ["", "## Setores", "", "| Setor | Assunto | Fontes (principal / total) | Princípios |", "|---|---|---|---|"]
for k,(nome,desc) in S.items():
    L.append(f"| [{nome}](setores/{k}/README.md) | {desc} | {ns[k]} / {nx[k]} | {npr[k] or '—'} |")
L += ["", "## Entraram por último", ""]
for f in rec:
    L.append(f"- {f['inc']} · [{f['titulo']}]({f['path']}) · {f['autor']} · {f['ev']}")
L += ["", "[Ver todas →](INDICE.md)", "", "## Autoridades", "", "| Pessoa | Foco | Setores |", "|---|---|---|"]
for slug,(n,why,sets) in sorted(P.items(), key=lambda x:x[1][0].lower()):
    L.append(f"| [{n}](autoridades/{slug}.md) | {why} | {', '.join(S[s][0] for s in sets[:4])} |")
L += ["", "## Pasta META (Meta Ads, Facebook, Instagram, WhatsApp)", "",
 "O que a Meta ensina oficialmente (estrutura de campanha, públicos, leilão, criativos, formulários e WhatsApp, mensuração, políticas, certificações), resumido e aplicado à We. Ver [META/README.md](META/README.md).", "",
 "## Estrutura", "", "```",
 "cerebro-autoridades/",
 "├── guias/                      checklists por tarefa (comece por aqui)",
 "├── setores/<setor>/README.md   autoridades, fontes e princípios consolidados do setor",
 "├── setores/<setor>/fontes/     um resumo por conteúdo (AAAA-MM-DD_autor_titulo.md)",
 "├── autoridades/                uma ficha por pessoa",
 "├── META/                       documentação oficial da Meta resumida",
 "├── INDICE.md                   todas as fontes (recentes, por setor, por autoridade)",
 "└── _modelos/                   modelos de fonte e ficha + gerar_indices.py", "```", "",
 "## Como adicionar um conteúdo", "",
 "1. Assista ou leia. Para vídeo, `/watch <url>` no Claude Code.",
 "2. Copie `_modelos/fonte.md` para `setores/<setor-principal>/fontes/AAAA-MM-DD_autor_titulo.md` e preencha (o que foi dito, aplicação para a We, pontos fracos).",
 "3. Crie ou atualize a ficha em `autoridades/`.",
 "4. Registre em `_modelos/gerar_indices.py` (listas `P`, `F` e, se a ideia já apareceu em outra fonte, `PRINC`) e rode `python -I _modelos/gerar_indices.py`.",
 "5. Se a fonte mudar um checklist, atualize o guia em `guias/`.", "",
 "Regras completas para agentes (Claude Code, Hermes): [CLAUDE.md](CLAUDE.md).",
 "", f"_Índices gerados em {_dt.date.today().isoformat()}._"]
(R/"README.md").write_text("\n".join(L)+"\n", encoding="utf-8")

# Verificação de links relativos quebrados
bad = []
for md in R.rglob("*.md"):
    if ".git" in md.parts: continue
    for link in _re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", md.read_text(encoding="utf-8")):
        if link.startswith(("http", "mailto")): continue
        if not (md.parent/link).resolve().exists():
            bad.append(f"{md.relative_to(R)} -> {link}")
if bad:
    print("LINKS QUEBRADOS:"); print("\n".join(bad))
print(f"índices globais: {len(FX)} fontes, {len(G)} guias")

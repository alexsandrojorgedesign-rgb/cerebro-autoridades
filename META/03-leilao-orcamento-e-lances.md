# 03 · Leilão, orçamento e lances

> Consultado em **2026-11-09**. Fontes: Meta for Business, notícias da Meta, Meta for Developers. Artigos da Central de Ajuda via resumo de busca (marcados).

## Como funciona o leilão

- Cada vez que há espaço para mostrar um anúncio a alguém, os anúncios elegíveis disputam um leilão. Não vence o maior lance sozinho: o sistema pesa vários fatores. Fonte: https://www.facebook.com/business/ads/ad-auction
- **Valor total** = valor para o anunciante (lance × taxa de ação estimada) + qualidade do anúncio. Fonte: artigo de notícias da Meta sobre aprendizado de máquina na entrega — https://www.facebook.com/business/news/good-questions-real-answers-how-does-facebook-use-machine-learning-to-deliver-ads (via resumo de busca; página antiga).
- **Taxa de ação estimada:** previsão de que aquela pessoa faça a ação otimizada.
- **Qualidade:** sinais de quem vê ou esconde o anúncio e atributos de baixa qualidade, como informação faltando, linguagem sensacionalista e isca de engajamento. Taxa estimada + qualidade = relevância. Fonte: https://www.facebook.com/business/ads/ad-auction
- Anúncio com lance menor pode vencer se o sistema prever mais resposta ou mais qualidade. Fonte: resumo de busca das páginas acima.
- A página de leilão também lista os 5 componentes de um anúncio que performa: objetivo certo, segmentação, orçamento suficiente, duração suficiente e criativo atraente. Fonte: https://www.facebook.com/business/ads/ad-auction

## O motor por trás (IA da entrega)

- **Andromeda:** sistema de recuperação que reduz dezenas de milhões de anúncios candidatos a alguns milhares antes do ranqueamento. Fonte: https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ (02/12/2024).
- **GEM, Lattice e Sequence Learning:** modelos de ranqueamento citados pela Meta em 27/03/2025. Fonte: https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance
- Detalhes e implicação para criativos em `05-criativos-boas-praticas.md`.

## Orçamento: campanha vs. conjunto

- **Advantage+ campaign budget** (antes "otimização do orçamento da campanha", CBO): um orçamento na campanha, distribuído em tempo real entre os conjuntos com melhores oportunidades. Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/budget
- Requisitos: todos os conjuntos com o mesmo tipo de orçamento, a mesma estratégia de lance e entrega padrão. Dá para pôr **limite mínimo e máximo de gasto por conjunto**. Mesma fonte.
- A Meta diz reduzir CPA em média 4,6% (dado próprio). Mesma fonte.
- Para manter uma campanha de Cadastros como Advantage+, o orçamento de campanha precisa ficar ligado. Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/leads
- **Orçamento de conjunto:** cada conjunto tem o seu; útil quando é preciso garantir verba fixa por segmento (ex.: um empreendimento por conjunto). Inferência nossa a partir do conceito; a Meta não detalha nas páginas lidas.

## Estratégias de lance

Nomes mudaram ao longo do tempo (versões antigas: "maior volume", "meta de custo por resultado", "meta de ROAS"; versões novas: "menor custo", "limite de custo", "ROAS mínimo"). Fontes: https://en-gb.facebook.com/business/help/1619591734742116 e https://en-gb.facebook.com/business/help/491846184627504 (via resumo de busca).

- **Maior volume / menor custo:** busca o máximo de resultados com o orçamento; o custo por resultado pode oscilar. É o padrão quando não se informa controle e o recomendado pela API para campanhas Advantage+ (`LOWEST_COST_WITHOUT_CAP`). Fontes: as acima e https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-campaigns
- **Limite de custo / meta de custo por resultado:** tenta manter o custo médio perto de um valor; a Meta avisa que não é garantido.
- **Limite de lance (bid cap):** teto do lance em cada leilão, não do custo reportado; indicado para quem sabe calcular o lance pelas taxas de conversão previstas. Fonte: https://en-gb.facebook.com/business/help/586282251886816 (via resumo).
- **ROAS mínimo / maior valor:** exige otimização por valor; pode não gastar todo o orçamento. Fonte: https://www.facebook.com/business/help/1113453135474912 (via resumo).

## Fase de aprendizado

- O aprendizado acontece no **conjunto**. A referência da Meta é cerca de **50 eventos de otimização em 7 dias** após a última edição significativa. Fontes: https://en-gb.facebook.com/business/help/269269737396981 ("aprendizado limitado") e https://developers.meta.com/vr/resources/optimize-ad-campaign/ (via resumo).
- **Aprendizado limitado:** rótulo quando o conjunto não deve chegar a ~50 eventos na semana; a Meta diz que não é punição. Mesma fonte.
- **Edições significativas** que podem reiniciar o aprendizado: pausar o conjunto, mudar evento de otimização, público ou criativo; mudanças de lance ou orçamento dependem do tamanho. Fonte: https://www.facebook.com/business/help/942374239243867 (via resumo).

## Aplicação para a We

- Com lead imobiliário em praça média, 50 cadastros/semana por conjunto é alto. Implicações práticas: **poucos conjuntos**, orçamento concentrado, otimizar para o evento mais frequente (lead) e só passar para "lead de conversão/qualificado" quando o CRM devolver volume.
- Começar com **menor custo** (sem limite). Usar limite de custo só quando houver histórico de CPL aceitável por empreendimento.
- Evitar mexer em criativo, público e orçamento juntos várias vezes por semana; agrupar mudanças.
- Se usar orçamento de campanha com Vicente e Bioma no mesmo lugar, colocar **gasto mínimo por conjunto** para nenhum empreendimento ficar sem verba.

## A verificar

- Lista oficial atual de edições significativas e o percentual de mudança de orçamento que reinicia aprendizado (artigo da Central não lido na íntegra).
- Nomenclatura exata das estratégias de lance no Gerenciador em português hoje.
- Data da página de notícias sobre a fórmula do valor total (antiga); a fórmula pode ter sido simplificada nas versões novas.

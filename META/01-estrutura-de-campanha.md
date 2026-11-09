# 01 · Estrutura de campanha e objetivos (ODAX)

> Consultado em **2026-11-09**. Observação: os artigos da Central de Ajuda para Empresas (facebook.com/business/help) carregam por JavaScript; a ferramenta só leu o título. O conteúdo deles veio de resumos de busca restritos aos domínios da Meta e de páginas de marketing da Meta que renderizam. Marcado onde for o caso.

## Três níveis

- **Campanha:** onde se escolhe o objetivo (o resultado de negócio). Com Advantage+ campaign budget, o orçamento também fica aqui.
- **Conjunto de anúncios:** onde ficam local de conversão (site, formulário instantâneo, mensagens, ligação), meta de desempenho, público, posicionamentos, orçamento (se não for de campanha), agenda e lance. O aprendizado da entrega acontece neste nível.
- **Anúncio:** criativo, texto, chamada para ação e destino.
- Fontes: artigo "Como escolher o objetivo do anúncio certo" (https://www.facebook.com/business/help/1438417719786914, via resumo de busca); documentação da Marketing API sobre campanhas Advantage+ (https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-campaigns).

## Objetivo, local de conversão e meta de desempenho

A Meta separa três escolhas: o **objetivo** (campanha), o **local de conversão** (onde a pessoa age) e a **meta de desempenho** (o que o sistema otimiza). Fonte: https://www.facebook.com/business/help/1438417719786914 (via resumo de busca).

## Os seis objetivos (ODAX — Outcome-Driven Ad Experiences)

A Meta reduziu os antigos 11 objetivos para 6 em 2021. Fonte: blog Meta for Developers, 21/12/2021 — https://developers.facebook.com/blog/post/2021/12/21/simplifying-campaign-objectives-outcome-driven-ad-experiences

| Objetivo | Para que serve (nas nossas palavras) | Quando usar |
|---|---|---|
| **Reconhecimento** | Mostrar a marca a quem tem mais chance de lembrar dela; metas como alcance, impressões e lift de lembrança do anúncio | Pré-lançamento, assinatura de marca, apresentar bairro/conceito |
| **Tráfego** | Levar gente a um destino (site, app, Messenger, WhatsApp) | Quando o importante é a visita (ex.: página do empreendimento), não o cadastro |
| **Engajamento** | Interação com anúncio ou página, visualização de vídeo, conversas | Aquecer público, gerar visualizações de vídeo para remarketing |
| **Cadastros (Leads)** | Coletar contato por formulário instantâneo, formulário do site, mensagens ou ligações | **Objetivo central da We**: formulário e clique para WhatsApp |
| **Promoção do app** | Instalação ou ação dentro de app | Não se aplica à We hoje |
| **Vendas** | Compra ou etapas de compra (ex.: adicionar ao carrinho), inclusive vendas em conversa | E-commerce; em imobiliário só faz sentido com evento de venda/reserva medido |

Fontes: https://www.facebook.com/business/help/1438417719786914 (via resumo de busca); página "Objetivos de anúncio" https://www.facebook.com/business/ads/ad-objectives (diz para escolher o objetivo que combina com a meta de negócio e que o leilão procura quem tem mais chance de fazer a ação escolhida); artigo "About the Traffic objective" https://en-gb.facebook.com/business/help/301780226847564 (destinos site, app, Messenger, WhatsApp — via resumo de busca).

- Visualização de vídeo aparece tanto em Reconhecimento quanto em Engajamento; a Meta diz para escolher pelo objetivo de marketing geral. Fonte: https://www.facebook.com/business/ads/ad-objectives

## Campanhas Advantage+ (automação ponta a ponta)

- Existem campanhas Advantage+ de **Vendas**, **App** e **Cadastros**. Fonte: https://www.facebook.com/business/ads/meta-advantage
- Uma campanha é considerada Advantage+ quando os três "alavancas" estão ligados: orçamento de campanha (Advantage+ campaign budget), posicionamentos Advantage+ (sem exclusões no conjunto, só no nível da conta) e público Advantage+ em pelo menos um conjunto. Se uma delas for desligada, a campanha deixa de ser Advantage+. Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-campaigns
- Para Cadastros, o Advantage+ vem ligado por padrão; adicionar públicos como "sugestão" não desliga, mas restrições amplas desligam. Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/leads
- A Meta afirma, com dados próprios, 14% menos custo por lead e 10% menos custo por lead qualificado com Advantage+ ligado em campanhas de cadastro. Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/leads e https://www.facebook.com/business/news/more-quality-leads-this-q5-with-metas-latest-ai-enabled-updates (30/10/2025).

## Simplificar a conta

- A Meta recomenda consolidar conjuntos e evitar mudanças na fase de aprendizado; diz que quem gasta menos de 20% do investimento em aprendizado pode reduzir custo por compra em até 68% (dado da Meta). Fonte: https://www.facebook.com/business/ads/performance-marketing
- Existe um vídeo do Blueprint só sobre "fragmentação de anúncios". Fonte: https://www.facebook.com/business/learn — link em `00-catalogo-blueprint.md`.

## Aplicação para a We

- **Padrão para captação:** objetivo **Cadastros**, com local de conversão formulário instantâneo **ou** mensagens (WhatsApp). A Meta recomenda até combinar formulário do site com instantâneo na mesma campanha (ver `06`).
- **Funil de lançamento:** Reconhecimento/Engajamento (vídeo do empreendimento, bairro, obra) no pré-lançamento para formar público de quem assistiu; Cadastros no lançamento e sustentação, com remarketing sobre quem viu vídeo ou interagiu.
- **Menos campanhas, mais criativos:** um conjunto amplo por empreendimento (Cascavel ou Toledo) com vários criativos tende a aprender mais rápido do que muitos conjuntos pequenos — o que conversa com o volume de leads de uma praça média.
- **Vendas** só quando houver evento de venda/reserva voltando do CRM; antes disso, otimizar para lead (ou lead de conversão, ver `06` e `07`).

## A verificar

- Texto integral do artigo de objetivos da Central de Ajuda (só lido via resumo). Abrir no navegador logado e conferir as metas de desempenho disponíveis para Cadastros no Brasil.
- Se o fluxo "configuração simplificada para vendas, app e cadastros" (webinar de 18/11) mudou a tela de criação.
- Os percentuais de melhora são da própria Meta, sem metodologia aberta.

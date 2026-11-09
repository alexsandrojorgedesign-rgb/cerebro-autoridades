# 02 · Públicos e segmentação

> Consultado em **2026-11-09**. Fontes: páginas de produto Meta for Business, documentação Meta for Developers, Padrões de Publicidade (transparency.meta.com). Artigos da Central de Ajuda só via resumo de busca.

## Tipos de público

- **Público principal (core/salvo):** idade, gênero, localização, interesses, comportamentos. A Meta orienta começar amplo e diz que o sistema funciona melhor com públicos entre 2 e 10 milhões de pessoas; para segmentação detalhada por interesse, sugere usar só se o público tiver ao menos 2 milhões. Fonte: https://www.facebook.com/business/ads/ad-targeting
- **Públicos personalizados (custom audiences):** listas de clientes, visitantes do site, quem interagiu com vídeo, perfil, formulário etc. Devem seguir os termos de públicos personalizados (https://www.facebook.com/ads/manage/customaudiences/tos.php). Fonte: Padrões de Publicidade, política de segmentação — https://transparency.meta.com/policies/ad-standards/
- **Semelhantes (lookalike):** criados a partir de um público de origem. Continuam aceitos como "sugestão" dentro do Advantage+ audience. Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/audience
- **Segmentação ampla:** só localização, idade mínima e idioma, deixando o sistema achar as pessoas. Citada como opção na página de segmentação. Fonte: https://www.facebook.com/business/ads/ad-targeting

## Advantage+ audience

- Parte da segmentação que você der (lista, interesse, idade) e pode ir além dela quando prever resultado melhor. Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/audience
- **Sugestões** (públicos personalizados, semelhantes, idade, gênero, detalhada) são priorizadas primeiro, depois o sistema amplia.
- **Controles** (limites rígidos que o sistema não ultrapassa): localização, idade mínima, idiomas e exclusão de públicos personalizados.
- Vem ligado por padrão em campanhas novas quando disponível; dá para voltar às "opções originais de público".
- A Meta cita melhoras medianas de CPA de 14,8% (topo), 9,7% (meio) e 7,2% (fundo de funil), dados próprios. Mesma fonte.
- Em campanhas de Cadastros com Advantage+ ligado, as condições incluem 18+, qualquer local/idioma e **apenas exclusões de públicos personalizados**. Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/leads

## Exclusões

- No Advantage+ audience, exclusão de público personalizado é um controle (ex.: excluir quem já é cliente ou já virou lead). Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/audience
- Exclusão por interesse/detalhada não é permitida quando a campanha está em categoria especial (ver abaixo).

## Categorias especiais de anúncio

Categorias: **Moradia (HOUSING)**, **Emprego**, **Produtos e serviços financeiros** (substituiu "Crédito" em jan/2025) e **Temas sociais, eleições ou política**. Fonte: https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category

### Destaque: Moradia / Habitação (housing)

**Onde é obrigatória** (pela documentação da Marketing API e pela política de Práticas Discriminatórias):
- **Estados Unidos** (desde 04/12/2019), **Canadá** (desde 03/12/2020) e **partes da Europa** (desde 07/12/2021) — para anunciantes sediados nesses lugares ou que miram pessoas lá.
- **Fora desses lugares, o anunciante pode optar** por aplicar ou não as restrições de público.
- Fontes: https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category e https://transparency.meta.com/policies/ad-standards/unacceptable-content/discriminatory-practices/ (a política fala em "Estados Unidos, Canadá ou certas partes da Europa").
- **O Brasil não aparece** em nenhuma dessas listas. Conclusão: para a We, anunciando no Brasil para público no Brasil, a categoria de Moradia **não é obrigatória** pelas regras atuais da Meta.

**O que ela restringe quando marcada:**
- Idade fixa 18 a 65+ (não dá para escolher faixa).
- Gênero: não dá para escolher (todos).
- Localização: sem exclusão de local; raio mínimo de 15 milhas (25 km) nos EUA/Canadá e 15 km na Europa em torno de cidade, endereço ou alfinete; sem CEP, bairro, sub-cidade, área metropolitana.
- Segmentação detalhada: sem comportamentos e dados demográficos, sem exclusões de interesse; interesses só de uma lista aprovada.
- **Semelhantes indisponíveis**; públicos salvos indisponíveis.
- Públicos personalizados: a documentação não traz proibição geral; há verificação de elegibilidade de lista de clientes.
- Fonte de tudo: https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category
- Advantage+ audience e expansões para categorias especiais estão em liberação gradual. Fonte: https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-campaigns

**A regra de não discriminar vale em qualquer país:** anúncios não podem discriminar nem incentivar discriminação por atributos pessoais (raça, religião, idade, sexo, orientação, estado familiar, deficiência etc.), nem usar a segmentação para excluir grupos de forma indevida. Fonte: https://transparency.meta.com/policies/ad-standards/unacceptable-content/discriminatory-practices/

## Aplicação para a We

- **Não marcar Moradia por padrão no Brasil** mantém liberados raio pequeno (bairro/cidade), faixa etária, semelhantes de compradores e segmentação detalhada. Mesmo assim, evitar exclusões que pareçam discriminatórias (ex.: excluir por idade, gênero ou "estado familiar") porque a política vale aqui.
- Se a We anunciar para público fora do Brasil (ex.: brasileiros nos EUA/Europa comprando para investir), a categoria passa a ser **obrigatória** para esses países.
- **Configuração sugerida pela lógica da Meta:** Advantage+ audience com controle de localização (Cascavel/Toledo + raio regional), idade mínima, e como sugestões: lista de leads/compradores, semelhante de compradores, quem assistiu vídeo do empreendimento. Excluir como controle: compradores do próprio empreendimento e leads recentes já atendidos.
- Praça média: Cascavel e Toledo dão públicos bem abaixo dos 2–10 milhões que a Meta considera ideais; mais um motivo para não fatiar demais e deixar o público amplo regional.

## A verificar

- A Central de Ajuda "Como escolher uma categoria de anúncio especial" (https://www.facebook.com/business/help/298000447747885) só carregou o título; confirmar na conta se o Gerenciador oferece a opção "Moradia" para país Brasil e o que muda.
- Se a Meta ampliar a obrigatoriedade a outros países (já aconteceu com Canadá e Europa). Rever a cada semestre.
- Data de atualização da página de desenvolvedores não aparece.
- Tamanho real dos públicos em Cascavel/Toledo deve ser conferido na estimativa do Gerenciador.

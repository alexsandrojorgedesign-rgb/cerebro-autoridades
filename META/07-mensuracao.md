# 07 · Mensuração

> Consultado em **2026-11-09**. Fontes: Meta for Developers (API de Conversões), Meta for Business, Central de Ajuda (via resumo de busca, marcados).

## Pixel e API de Conversões (CAPI)

- **Pixel da Meta:** código no site que registra eventos do navegador (visualização, lead, etc.).
- **API de Conversões:** liga dados de marketing (site, app, mensagens, offline, CRM) direto do servidor/plataforma/CRM aos sistemas da Meta, para otimizar entrega, reduzir custo por resultado e medir. Fonte: https://developers.facebook.com/docs/marketing-api/conversions-api
- Quem já tem Pixel pode ligar a CAPI para eventos do site **com um clique** no Gerenciador de Eventos, sem código. Mesma fonte.
- A etapa de verificação confere se os eventos estão **deduplicados** (Pixel + CAPI enviando o mesmo evento) e bem combinados. Mesma fonte. Os detalhes de `event_id` e qualidade de correspondência não estavam nessa página.
- A Meta põe "qualidade de dados e sinais via API de Conversões" como uma das práticas centrais de performance. Fonte: https://www.facebook.com/business/ads/performance-marketing
- Variações relevantes para a We: **CAPI para CRM** (leads de formulário, ver `06`) e **CAPI para mensagens empresariais** (eventos no WhatsApp/Messenger): https://developers.facebook.com/documentation/ads-commerce/conversions-api/business-messaging

## Eventos e Aggregated Event Measurement (AEM)

- Páginas da Central de Ajuda ainda descrevem limite de **8 eventos priorizados por domínio** para otimização no AEM (criado após o iOS 14). Fontes: https://en-gb.facebook.com/business/help/223073145946545 e https://www.facebook.com/business/help/126789292407737 (via resumo de busca; sem data clara).
- Não achei comunicado oficial confirmando mudança desse limite. Ver "A verificar".

## Atribuição

- Configuração no conjunto de anúncios: 1 dia clique, 7 dias clique, 1 dia clique ou 1 dia visualização, 7 dias clique ou 1 dia visualização (citado como padrão). Fonte: https://en-gb.facebook.com/business/help/460276478298895 (via resumo).
- A Meta anunciou que janelas de 7 e 28 dias de visualização deixam de ser retornadas pela API de Insights a partir de **12/01/2026**. Fonte: https://developers.facebook.com/blog/post/2025/10/16/ads-insights-api-metric-availability-updates/ (via resumo).

## Testes

- **Teste A/B:** compara duas versões mudando uma variável (criativo, texto, público, posicionamento), cada uma para um segmento separado; criado no Gerenciador ou em Experimentos. Fonte: https://www.facebook.com/business/help/1738164643098669 e https://www.facebook.com/business/measurement/ab-testing (via resumo).
- Referências encontradas: testar uma variável por vez; rodar pelo menos 2 semanas (até 30 dias); resultados confiáveis a partir de ~100 eventos de conversão por versão. Mesmas fontes (via resumo; páginas de datas diferentes).
- **Conversion Lift:** mede conversões **incrementais** com grupo de controle que não vê os anúncios. Fonte: resumo de busca de https://www.facebook.com/business/help/1915029282150425
- **Brand Lift:** pesquisa com grupo teste vs. controle para medir diferença de resposta (lembrança, consideração). Fonte: https://www.facebook.com/business/help/2774809055882496 (via resumo).
- **Experimentos** é gratuito e reúne os resultados; testes com grupo de controle podem afetar CPM. Mesma fonte.
- A/B responde "qual tática é melhor"; Lift responde "quanto o anúncio causou". Mesma fonte.

## Relatórios principais (para lead)

- Resultado/Custo por resultado (lead), CPM, CTR, frequência, alcance; em vídeo, reproduções e retenção. Termos do glossário do Gerenciador; as fórmulas não foram verificadas aqui.
- **Opportunity Score:** pontuação com recomendações para melhorar a campanha; Meta cita 5% menos custo por resultado em média para quem aplica (disponível só para alguns anunciantes). Fonte: https://www.facebook.com/business/ads/meta-advantage-plus/placements

## Aplicação para a We

- **Pixel + CAPI nas landing pages** dos empreendimentos (ligar pelo Gerenciador de Eventos) e conferir deduplicação.
- **O maior ganho para a We é o caminho CRM → Meta:** sem isso, a Meta otimiza para "quem preenche", não para "quem visita o decorado". Marcar no CRM o ID do lead e devolver uma etapa (visita ou proposta).
- **A/B simples por trimestre:** formulário "Mais volume" vs. "Maior intenção"; formulário instantâneo vs. clique para WhatsApp — medido por lead qualificado no CRM, não só CPL.
- Brand Lift/Conversion Lift costumam exigir verba maior; reservar para um lançamento grande, se a Meta liberar para a conta.

## A verificar

- Limite atual de eventos do AEM e se ainda é preciso priorizar eventos no Gerenciador.
- Padrão atual de atribuição no Brasil para campanhas de Cadastros.
- Requisitos mínimos de orçamento/volume para Conversion Lift e Brand Lift (não encontrados).
- Página de "event match quality" e parâmetros de cliente (hash) não lida.

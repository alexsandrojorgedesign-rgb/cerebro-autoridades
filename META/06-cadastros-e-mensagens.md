# 06 · Cadastros (formulários instantâneos) e anúncios de mensagem

> Consultado em **2026-11-09**. Fontes: Meta for Business (lead ads, Advantage+ leads, click-to-message), notícias da Meta (abr/2024 e out/2025), Meta for Developers, WhatsApp Business (whatsappbusiness.com). Artigos da Central de Ajuda via resumo de busca (marcados).

## Formulários instantâneos

**Tipos** (via resumo de busca de https://www.facebook.com/business/help/252352181957512/):
- **Mais volume:** rápido de preencher e enviar no celular.
- **Maior intenção:** acrescenta uma etapa de revisão para a pessoa confirmar os dados antes de enviar.
- Existe também o tipo de criativo rico (rich creative).

**Perguntas e lógica:**
- Até **15 perguntas** no total; listas de múltipla escolha curtas (3 a 4 opções); formulário longo derruba a taxa de conclusão. Fonte: https://www.facebook.com/business/help/1231792023638635 (via resumo).
- **Respostas condicionais:** as opções de uma pergunta mudam conforme a resposta anterior; as perguntas e a ordem são as mesmas para todos. Configuração por CSV em UTF-8. Fonte: https://www.facebook.com/business/help/154286325106161 (via resumo).
- A Meta cita a lógica condicional como forma de qualificar leads em um fluxo de perguntas. Fonte: https://www.facebook.com/business/news/create-more-valuable-leads-than-ever-with-metas-instant-forms (18/04/2024).
- Não criar campo que duplique pergunta pré-preenchida existente (ex.: usar a de data de nascimento para idade). Fonte: política de Anúncios de Cadastro em https://transparency.meta.com/policies/ad-standards/
- Dados que **não podem ser pedidos sem autorização prévia por escrito da Meta**: números de conta, antecedentes criminais, **informações financeiras (renda, patrimônio, dívidas, score)**, documentos oficiais (CPF/RG equivalem a "identificadores governamentais"), saúde, seguros, política, raça, religião, orientação sexual, sindicato, usuário/senha. Fonte: https://transparency.meta.com/policies/ad-standards/

**Verificação de lead** (anúncio de 30/10/2025):
- Verificação de telefone por SMS no formulário instantâneo; verificação de e-mail corporativo; verificação de endereço em teste. Fonte: https://www.facebook.com/business/news/more-quality-leads-this-q5-with-metas-latest-ai-enabled-updates
- Também cita agente de leads automatizado no Messenger (teste) e modelos de nutrição de terceiros (Manychat, Botcake). Mesma fonte.

**Formulário instantâneo vs. formulário do site:**
- Instantâneo: experiência rápida, autopreenchimento; a Meta cita 20% menos custo por lead qualificado que formulários de site (estudo próprio 2023). Fontes: https://www.facebook.com/business/ads/ad-objectives/lead-generation/lead-ads-with-forms e notícia de 18/04/2024.
- Site: quando a pessoa precisa de mais contexto, agendar, cotar ou ver detalhes. Mesma fonte.
- **Os dois na mesma campanha**: a Meta reporta ~60% menos custo por lead e 125% mais volume que só formulário do site; em out/2025 citou 14–24% menos custo por lead. Fontes: https://www.facebook.com/business/ads/meta-advantage-plus/leads e notícia de 30/10/2025.

## Integração com CRM

Há **duas integrações diferentes**:
1. **Recuperação de leads** (Meta → CRM): o lead cai direto no CRM, sem baixar planilha; sem CRM, a Meta oferece a **Central de Leads** (Leads Center) e um CRM leve no Meta Business Suite. Fontes: https://www.facebook.com/business/ads/ad-objectives/lead-generation/lead-ads-with-forms e notícia de 18/04/2024.
2. **API de Conversões para CRM** (CRM → Meta): devolve as etapas do funil (ex.: visita, proposta, venda) para a Meta otimizar por **leads de conversão**. Fonte: https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration
   - Funciona com formulário instantâneo e a meta de desempenho de leads de conversão (a doc diz só formulário instantâneo; uma página de marketing cita também formulário de site — conflito).
   - Requisitos na doc de desenvolvedores: guardar o **ID do lead** da Meta (15–17 dígitos) no CRM; subir dados pelo menos 1x/dia; etapa-alvo ocorrer em até 28 dias do lead; taxa de conversão da etapa entre 1% e 40%; mínimo de 200 leads/mês. **Em 30/10/2025 a Meta anunciou a remoção do volume mínimo mensal** e a opção de escolher um único evento de conversão na criação do anúncio. Fonte: notícia de 30/10/2025.
   - Integração por Zapier (até 100 mil eventos sem custo), Salesforce e outros parceiros; desenvolvimento próprio leva 3–4 semanas segundo a doc; aprendizado de 2–4 semanas.
   - Ganho citado pela Meta: 15% menos custo por lead qualificado e +44% na taxa de lead→lead qualificado; em 2025, 19% menos custo por lead qualificado. Fontes: https://www.facebook.com/business/ads/meta-advantage-plus/leads e notícia de 30/10/2025.

## Anúncios de clique para mensagem (WhatsApp, Messenger, Direct)

- O clique abre uma conversa 1 a 1 com a empresa. Com mais de um destino, a Meta envia cada pessoa ao app em que ela tem mais chance de conversar. Fonte: https://www.facebook.com/business/ads/click-to-message-ads
- Objetivos possíveis: conversas (Engajamento), **Cadastros** (qualificar na conversa), Vendas. Mesma fonte.
- **Clique para WhatsApp otimizado para leads:** objetivo Cadastros, local de conversão "Destino das mensagens" → WhatsApp. A opção só aparece se a campanha cumprir critérios de elegibilidade (não detalhados). A Meta reporta ~24% menos custo por lead do que otimizar para conversas (experimento de nov/2024 com 116 mil campanhas). Fonte: https://whatsappbusiness.com/pt-br/resources/resource-library/down-funnel-optimizations-whatsapp/
- Boas práticas listadas: deixar claro que o clique abre conversa ("Enviar mensagem"); imagens/vídeos quadrados ou verticais; mensagem de saudação e respostas automáticas; rodar pelo menos 7 dias com orçamento competitivo; usar vários destinos (Meta cita 9% menos custo por mensagem e 11% mais conversão); devolver dados de ação do cliente. Fonte: https://www.facebook.com/business/ads/click-to-message-ads
- Existe **API de Conversões para Mensagens Empresariais** para devolver eventos que acontecem na conversa. Fonte: https://developers.facebook.com/documentation/ads-commerce/conversions-api/business-messaging (encontrado via busca; não lido na íntegra).
- Conversas iniciadas por anúncio de clique para WhatsApp abrem uma **janela gratuita de até 7 dias** na Plataforma WhatsApp (ver `09`).

## Aplicação para a We

- **Formulário instantâneo "Maior intenção"** para lançamentos de alto padrão (Vicente) e "Mais volume" para captação ampla; testar os dois por A/B (ver `07`).
- **Perguntas qualificadoras permitidas:** tipologia de interesse, prazo de compra, objetivo (morar/investir), forma de pagamento (à vista/financiado/permuta) em múltipla escolha. **Não perguntar renda, valor de entrada ou CPF** sem autorização da Meta (categoria de informação financeira/identificador). Usar faixas de "orçamento do imóvel" exige cuidado — confirmar se a Meta trata como informação financeira.
- **Lógica condicional:** ex.: escolhe "Toledo" → opções de empreendimentos de Toledo; escolhe "Cascavel" → Vicente/Bioma.
- **Ligar verificação de telefone por SMS** onde disponível — o lead da We é atendido por WhatsApp, telefone errado é perda direta.
- **CRM → Meta:** guardar o ID do lead da Meta no Chatwoot/planilha/CRM e devolver "visita ao decorado" ou "proposta" como evento; com a remoção do mínimo de 200 leads/mês, isso fica viável para a praça da We.
- **Clique para WhatsApp no objetivo Cadastros** (não Engajamento/conversas) e mensagem de saudação com perguntas iniciais; o fluxo de DM→WhatsApp que a We já usa no Zernio conversa com isso.

## A verificar

- Artigos da Central de Ajuda sobre tipos de formulário, respostas condicionais e boas práticas (só via resumo). Abrir logado.
- Disponibilidade no Brasil de: verificação por SMS, e-mail corporativo, agente de leads do Messenger.
- Critérios de elegibilidade para "otimizar para leads" no clique para WhatsApp.
- Se a meta de leads de conversão aceita formulário do site (fontes divergem).

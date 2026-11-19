---
titulo: "AI Agents: The Most Valuable Skill You Can Learn in 2026 (Full Course)"
autoridades: [remi]
tipo: podcast
url: "https://youtu.be/5p-sq8v3OXw"
canal_ou_editora: "Open Residency (YouTube/podcast), entrevista conduzida por Mark"
data_publicacao: 2026-07-22
data_inclusao: 2026-11-10
duracao: "2:24:11"
setor_principal: ia
setores_secundarios: [negocios-e-gestao, marketing, trafego-pago]
evidencia: "legenda automática original em inglês (YouTube), sem análise de imagem. O vídeo mostra telas (Claude Code, pastas, skills) que não foram vistas; a descrição das demos vem só da fala. O sobrenome do convidado não aparece na legenda; nomes de ferramentas podem estar distorcidos (a legenda escreve 'Zapify/Appify' para Apify e 'Hexfield' para Higgsfield)."
tags: [agentes, claude-code, contexto, skills, mcp, memoria, sistema-operacional-pessoal, automacao]
---

# Agentes de IA: o curso completo (Remi no Open Residency)

**Em uma frase:** a vantagem saiu do chat (pergunta → resposta) para os agentes (objetivo → resultado). Um agente só fica útil quando você o "contrata" como um funcionário novo: **contexto** (arquivos .md sobre você e o negócio), **ferramentas** (MCPs/conectores) e **skills** (SOPs reutilizáveis), tudo numa pasta "OS" que é sua e roda em qualquer harness.

## O que foi dito

**Chat x agente [01:23–07:05]**
- Fase 1 foi o chat (ChatGPT, Claude, Gemini); fase 2 são os agentes. Quem usa agentes seria de 5 a 10 vezes mais produtivo (estimativa dos dois, sem dado). Chat continua bom para coisa pequena (comparar hotéis, traduzir uma placa); trabalho de verdade vai para o agente.
- Definição: chat é **pergunta → resposta**; agente é **objetivo → resultado**. O nome vem de "agency", a capacidade de agir por você.
- Exemplo da agência de ads [07:08]: antes, uma campanha "Natal em julho" passava por brief no Notion, copy no ChatGPT, designer, calendário e subida manual no Ads Manager. Agora o agente lê o brief, gera imagens (Higgsfield), escreve e-mails e anúncios, monta no Klaviyo e deixa em **rascunho** para aprovação humana.

**O loop do agente [09:42–19:51]**
- Todo agente roda o ciclo **observar → pensar → agir** até cumprir o objetivo. Quanto mais específico o objetivo (ex.: "10 podcasts num PowerPoint de 10 páginas"), melhor ele sabe quando parar.
- Demo: pediu a análise dos 10 melhores reels dele (hooks, temas, por que funcionaram) em HTML. O agente achou arquivos no computador, cruzou com views e lançou um subagente para buscar o gancho falado que faltava.
- O programa que roda o loop é o **harness** (Claude Code, Cowork, Codex, Manus…). Quem diz "construí um agente" quase sempre configurou um harness pronto, não construiu o loop.
- Analogia do carro: o modelo (Opus, GPT) é o motor, e contexto, skills e ferramentas são a regulagem. "Um Volvo bem regulado ganha de um Lamborghini mal regulado." Os harnesses são carros diferentes, com o mesmo jeito de dirigir, então dá para trocar.

**Pilar 1: contexto [20:21–50:32]**
- O agente é um "estranho muito capaz" contratado: sem saber quem você é, do que gosta e como trabalha, não serve.
- Contexto = arquivos **markdown** (.md), um degrau acima do .txt. O agente lê .md muito mais rápido e barato que PDF ou .docx.
- Arquivos sugeridos: sobre mim, negócio, catálogo de ofertas e preços, ICP (cliente ideal), voz da marca, valores, preferências de trabalho.
- Revise cada linha: um ICP gerado por IA e não revisado pode mandar a copy para um ângulo errado (ex.: "pele vermelha" num skincare que não trata isso). Minimizar a subjetividade.
- Para criar os arquivos, pediu ao Claude "me entreviste para montar esses arquivos" e respondeu por voz (Wispr Flow) por cerca de 3 horas.
- A "memória" do ChatGPT é, na prática, um arquivo markdown escondido que você não controla e que mistura assuntos. Melhor ter os seus próprios.
- Estrutura: um **CLAUDE.md / AGENTS.md** é carregado em toda sessão (a "estrela-guia": quem sou, o que faço, regras) e aponta para uma pasta `context/` com os demais. Sem o arquivo-raiz, o agente tem de procurar a cada vez, mais lento.
- **memory.md / lessons**: toda correção vira regra ("quando eu te corrigir, escreva a lição aqui e consulte antes de cada tarefa"). Os harnesses já têm memória própria, mas ela fica presa a eles; a sua roda em qualquer um. Faça uma "faxina" de vez em quando, pedindo ao agente para auditar regras conflitantes.
- **Janela de contexto**: começa cada sessão já ocupada pelos arquivos carregados (6% na demo, com `/context`). Sessão longa sofre de "context rot" (esquece e alucina). Manter os arquivos enxutos e densos e abrir sessão nova por tarefa.

**Pilar 2: ferramentas (MCP) [51:42–78:23]**
- MCP é o "tradutor no meio": cada ferramenta fala uma língua (Gmail, Notion, Slack), e o MCP evita integração sob medida para cada uma. Basta clicar em "+" nos conectores e fazer login.
- Ele diz não abrir mais o front-end do Gmail, Stripe ou Calendly; o dia inteiro roda dentro do harness. A existência de um MCP virou critério de compra de software para ele. Tese: SaaS cobrado por assento sofre, e produtos novos deveriam nascer como MCP/plugin dentro do Claude, não como app separado.
- Segurança: pesar o ganho contra o risco. Comece com permissão de **só leitura** e "perguntar antes", e suba conforme ganhar confiança. Ele já dá acesso total e aprova ações pontuais (mandar e-mail). Ter cuidado especial com dados sensíveis e compras.
- As 6 ferramentas que ele conecta:
  1. **Apify**: marketplace de raspadores (Instagram, TikTok, Reddit, LinkedIn, transcrição de YouTube…). Foi a conexão que "mudou o jogo".
  2. **Firecrawl**: lê e raspa páginas de verdade (cores da marca, auditoria de CRO). A busca padrão só acha fatos.
  3. **Composio**: um único conector que agrega centenas de apps e várias contas do mesmo serviço. Protege contra a queda de um harness: ele conecta uma vez e usa no Claude, no Codex, onde for.
  4. **Chrome DevTools MCP**: o agente abre um navegador para checar o próprio trabalho (site) e preencher formulários.
  5. **Playwright**: navegador com login salvo (LinkedIn etc.).
  6. **Higgsfield MCP**: geração de imagem e vídeo com vários modelos. Na demo, raspou anúncios de concorrentes na biblioteca da Meta e gerou anúncios estáticos para uma marca de gomas: alguns bons, outros com o produto deformado. É preciso gerar muito e escolher.
- Ele também cita o conector oficial da Meta para ler anúncios.

**Pilar 3: skills [78:39–107:40]**
- Skill = **SOP** em markdown, como o passo a passo que você daria a um assistente virtual. Resolve o problema de explicar de novo, a cada sessão, como você quer uma proposta, um título etc.
- Anatomia: pasta com `SKILL.md` contendo **nome + descrição** (a "lombada do livro na estante") e o conteúdo. Só nome e descrição ficam carregados; o conteúdo entra quando a tarefa pede (**divulgação progressiva**), o que economiza contexto. Pode incluir exemplos de saída.
- Duas formas de criar: **objetivo primeiro** (pedir "crie uma skill de manual de marca" com o PDF, usando o *skill-creator* que vem no Claude) ou **processo primeiro**, que é como ele faz 90%: executar a tarefa uma vez numa sessão, ajustando, e no fim pedir "transforme esse processo em skill".
- Demos:
  - *ads analyst*: link da biblioteca de anúncios → baixa todos os anúncios, abre e fotografa as landing pages, entrega relatório HTML (formatos, preço, anúncio mais antigo, o que copiar ou superar).
  - *subject lines* conectada ao Beehiiv: lê as linhas de assunto com melhor abertura e escreve 10 opções ranqueadas.
  - *product shoot*: fotos de celular do produto → fotos de estúdio para a página de produto (Higgsfield + Nano Banana Pro).
- A primeira versão nunca é boa; as skills que ele usa estão na v5 a v10. Corrija na conversa e peça para atualizar a skill.
- **Skill orquestradora**: chama outras em sequência (ex.: estratégia criativa → títulos → publicação no YouTube).
- Para ele, o valor e a propriedade intelectual da empresa vão morar nas skills ("como eu penso sobre títulos").

**Estrutura de pastas: o "OS" [107:40–126:47]**
- Ele começou com um "agente" (pasta) por função, como pasta de ads e pasta de e-mail, e abandonou: dá trabalho demais. Hoje trabalha tudo a partir de **uma pasta `OS`**, como uma holding: dentro, uma pasta por empresa ou pilar (e "pessoal", "saúde"), mais uma pasta `active/` para tarefas avulsas.
- **Global x projeto**: o CLAUDE.md e as skills do OS valem para tudo; cada subpasta pode ter o seu CLAUDE.md e skills locais, que se somam. Marcar a pasta com `@` ajuda, mas o agente acha sozinho.
- "Agente de marketing que trabalhou enquanto eu dormia" costuma ser só uma pasta, algumas skills e uma tarefa agendada.
- Não buscar a estrutura perfeita no início; ela cresce com o uso.

**Custos, empresas e times [123:03–136:20]**
- Ele gasta cerca de US$ 1.000 por mês em IA, em várias ferramentas. Os planos estão subsidiados (US$ 200 de plano renderiam cerca de US$ 6.000 em tokens, estimativa dele), e a tendência é os preços subirem e surgirem modelos locais.
- Camada 2 da empresa: agentes que rodam 24h fora do computador do fundador (Hermes, OpenClaw num Mac mini), com a mesma lógica de contexto, ferramentas e skills.
- Compartilhar skills e contexto num time ainda é bagunçado; não há solução boa. O CLAUDE.md da empresa (o que não muda) pode ser comum; o gosto e o jeito de trabalhar são individuais.
- Para levar IA à empresa, ele prefere **de baixo para cima**: treinar cada funcionário a montar o próprio OS, já que ninguém conhece a tarefa melhor que quem a faz. Incentivos: "skill do mês" com prêmio e uma call semanal de IA. Mark defende misturar com o de cima para baixo (questionário de ferramentas e gargalos por pessoa).

**Respostas rápidas [136:28–142:02]**
- Melhor skill de produtividade: triagem da caixa de e-mail, rodando várias vezes ao dia.
- Maior erro de iniciante: perfeccionismo e medo de "estragar algo".
- Ferramenta superestimada: construtores de app (Lovable etc.); melhor criar uma pasta-projeto e pedir ao Claude.
- Subestimada: Composio.
- Skill favorita: um "conselho" de várias sessões com personas diferentes que analisam uma decisão, revisam as respostas umas das outras às cegas e passam a um "presidente" que dá o veredito. Contra a bajulação do modelo.
- Por onde começar: criar a pasta OS → montar os arquivos de contexto (pedir ao agente para te entrevistar) → conectar as ferramentas → fazer o dia de trabalho inteiro dentro do harness → transformar em skill toda tarefa que vai se repetir.

## Frases-chave
- "Chat é pergunta → resposta; agente é objetivo → resultado." [04:39]
- Analogia: um Volvo com contexto, skills e ferramentas bem regulados ganha de um Lamborghini [16:53].
- A primeira versão de uma skill nunca é boa; as dele estão na v5 a v10 [95:01].

## Aplicação prática (exemplos de clientes)
- **O Alex já roda essa arquitetura** (CLAUDE.md global, memória em arquivos, cérebro de criação no Drive, skills /criativo e /programar, Hermes 24h, MCPs de Higgsfield, Zernio e Meta). O vídeo serve mais como checklist de lacunas do que como novidade:
  - **Apify** (raspar Instagram e TikTok de concorrentes e de referências imobiliárias) e **Firecrawl** (ler sites de concorrentes, CRO das LPs do Bioma e do Vicente) ainda não aparecem no fluxo.
  - **Chrome DevTools/Playwright** para o agente conferir os sites que publica (linkbio, terceiros, painéis) antes de entregar.
  - **Skill "analista de anúncios"** com base na biblioteca de anúncios da Meta, para concorrentes de Cascavel e Toledo (incorporadoras, imobiliárias). Encaixa no kit de tráfego.
  - **Skill de "conselho"** para decisões (naming, posicionamento, verba) e para revisar peças antes do AGUARDANDO.
- **Contexto como ativo da empresa:** ICP, ofertas, voz e tabelas de cada empreendimento em .md revisados linha a linha e em lugar comum (Drive ou repo). Hoje parte disso está espalhada em memórias e skills de copy.
- **Levar para a equipe We (de baixo para cima):** pequena trilha para a equipe de marketing e comercial montar o próprio contexto + 2 ou 3 skills (atendimento de lead, follow-up, relatório), com "skill do mês". Conecta com o formulário de agentes de IA já feito.
- **Segurança:** começar MCPs de CRM (Facilita) e Chatwoot só em leitura (já é o caso) e manter envio de mensagens e campanhas sempre em rascunho com aprovação, como ele faz no Klaviyo.

## Discordâncias e pontos fracos
- Os números de produtividade ("5–10x", "um fundador de bilhões", "US$ 6 mil em tokens") são opinião, sem dado.
- O episódio tem vários anúncios e venda de um produto do próprio convidado, que monta o sistema em 90 minutos. O conteúdo é gratuito e sólido, mas há interesse comercial.
- "Dar acesso total ao agente" é uma escolha pessoal dele; para empresa com dados de clientes (LGPD, CRM, contratos) vale o caminho que ele mesmo recomenda a iniciantes: só leitura e aprovação.
- Pouco sobre avaliação de qualidade: as imagens geradas na demo vieram com produto deformado, e a resposta foi "gere 100 e escolha". Para imóvel isso conflita com a regra de não alterar a arquitetura.
- Versões citadas (Opus 4.8, GPT 5.5, Fable 5) e preços mudam rápido; os princípios (contexto, ferramentas, skills) são o que fica.

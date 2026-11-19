---
titulo: "OpenClaw vs Hermes Agent (Don't choose WRONG!)"
autoridades: [metics-media]
tipo: video
url: "https://youtu.be/jOK10k70XWE"
canal_ou_editora: "Metics Media (YouTube), apresentado por Matt"
data_publicacao: 2026-06-15
data_inclusao: 2026-11-10
duracao: "9:29"
setor_principal: ia
setores_secundarios: [negocios-e-gestao]
evidencia: "legenda manual original em inglês (YouTube), lida inteira. Números (skills, CVEs, versões) são do autor em junho/2026 e mudam rápido; conferir antes de decidir."
tags: [agentes, hermes, openclaw, vps, seguranca, skills, custo, decisao]
---

# OpenClaw x Hermes Agent: qual escolher (Metics Media)

**Em uma frase:** os dois são agentes open source que rodam num servidor e conversam pelo Telegram, Slack ou Discord com as mesmas capacidades; a diferença é a aposta de cada um. O **OpenClaw** aposta no **catálogo da comunidade** (mais de 50 mil skills, mais provedores, painel web). O **Hermes** aposta no **agente que melhora sozinho** (o Curator escreve e refina skills a partir do seu uso).

## O que foi dito
**O que são [00:39–01:47]**
- Os dois leem arquivos, rodam scripts, navegam, mandam e-mail e agendam tarefas.
- **OpenClaw:** "tudo que você quiser, alguém já fez uma skill" (mais de 50 mil no Claw Hub em junho/2026). Você navega, instala e usa.
- **Hermes:** quando resolve um problema novo, anota como fez e não precisa descobrir de novo. Constrói a própria biblioteca de skills pelo seu uso. O recurso (Curator) chegou na versão 0.12, em abril/2026.
- O OpenClaw lançou o equivalente (Skill Workshop) em junho/2026, mas pede aprovação para cada skill nova; o Hermes faz automaticamente.

**Onde o OpenClaw ganha [01:50–02:56]**
1. **Catálogo:** mais de 50 mil skills e plugins (Google Workspace, raspagem, imagem, contabilidade…) com instalação em um clique. O do Hermes é menor e cresce com o uso.
2. **Provedores:** mais de 50 nativos (Anthropic, OpenAI, Gemini, Grok, DeepSeek, Ollama local…). O Hermes tem uma lista curta (OpenRouter, Anthropic, OpenAI, Nous Portal, Ollama) e chega ao resto via OpenRouter.
3. **Painel web** pronto. O Hermes é de linha de comando; o painel é extra. "O OpenClaw parece uma ferramenta que você navega; o Hermes, uma ferramenta com quem você conversa."

**Onde o Hermes ganha [03:00–04:19]**
1. **Aprendizado automático:** o Curator escreve skills, monitora quais são usadas e refatora as fracas, sem pedir aprovação. "Hermes entrega um agente que se aprimora; o OpenClaw, um que propõe e você supervisiona."
2. **Custo em tarefas repetidas:** o custo por mensagem é parecido (mesmos modelos, mesmo desconto de cache), mas no repetido o Hermes roda a skill salva e a conta "achata" mais cedo.
3. **Primeiro dia:** padrões enxutos (escolhe provedor, cola a chave, conversa). O OpenClaw é mais configurável, com mais lugares para travar.

**Instalação e custo [04:21–05:52]**
- Os dois têm template de um clique em VPS (ele indica o plano KVM 2 como mínimo); também rodam em Mac mini, Raspberry Pi ou notebook, com mais trabalho técnico.
- Custos: servidor + modelo. Com cache de cerca de 90%, o custo por turno é parecido. Os dois rodam "abaixo de US$ 20/mês" depois de configurados, se você usar o modelo mais barato que faz o trabalho. Se o trabalho é variado e avulso, os dois ficam parecidos no custo.

**Segurança [05:55–07:57]**
- Os dois leem seus arquivos e agem nas suas contas. **Rodar num VPS** é a proteção mais limpa: se der problema, você apaga a máquina virtual, não o seu computador. Ambos têm sandbox (Hermes com cinco backends; OpenClaw roda sessões secundárias em Docker).
- **OpenClaw:** mais de 130 alertas de segurança entre fevereiro e abril/2026, incluindo uma falha grave de execução remota por link malicioso com mais de 40 mil instâncias expostas (corrigida rápido). Uma auditoria achou mais de mil skills maliciosas no Claw Hub. Instale só de quem você confia e mantenha atualizado.
- **Hermes:** pelo menos uma dúzia de CVEs em 2026 e uma auditoria de abril com 4 achados críticos e 9 altos na configuração padrão, todos corrigidos. Menos incidentes, em parte porque não há marketplace de terceiros.
- Resumo: os dois são seguros se atualizados; o OpenClaw tem ecossistema e superfície de ataque maiores.

**Recomendação por perfil [07:57–09:10]**
- **Primeira vez, um assistente pessoal no Telegram/Discord, sem passar o fim de semana configurando, e um agente que melhora com os meses → Hermes.**
- **Quer painel clicável, marketplace enorme ou controle fino de provedores → OpenClaw** (atualizado e com skills só de autores confiáveis).
- **Faz as mesmas tarefas todo dia (briefing diário, mesma pesquisa, triagem de e-mail) e quer que fique mais barato com o tempo → Hermes.**

## Frases-chave
- "OpenClaw bets on the community catalogue. Hermes bets on the agent improving itself." [01:42]
- "Hermes ships you a self-improving agent. OpenClaw ships you a self-proposing one that you supervise." [03:28]

## Aplicação prática (guia de decisão para um agente novo)
Situação atual do Alex: o **Hermes** já roda no PC (perfil "criacao", gerente via claude-criar) e numa **VPS Hostinger** (Docker + Telegram), com o cérebro no repo cerebroagent. Antes de criar um agente novo, responder:

1. **O trabalho é repetitivo e previsível?** (briefing diário de leads, relatório de mídia, triagem do Chatwoot, pauta semanal) → **Hermes**: o Curator transforma em skill e o custo cai. É o caso da maioria dos agentes da We.
2. **Precisa de uma integração pronta que não existe no Hermes** (ferramenta de nicho, provedor específico) ou de **painel visual para alguém da equipe não técnico** → considerar **OpenClaw**, instalando só skills de autor confiável e mantendo atualizado.
3. **Onde roda?** Agente que mexe em contas, CRM ou WhatsApp de cliente → **VPS separada** (como a da Hostinger), nunca no PC de trabalho. Agente de criação que usa arquivos locais (Drive, PhotoCraft, VectorCraft) → PC, com escopo de pastas limitado.
4. **Permissões:** começar só leitura (Facilita, Chatwoot) e envio em rascunho com aprovação, como recomenda o [curso do Remi](2026-07-22_remi_agentes-de-ia-curso-completo.md).
5. **Custo:** escolher o modelo mais barato que resolve a tarefa; reservar modelo caro para criação e decisão.
6. **Não multiplicar agentes:** um agente por "empresa/pilar" com skills, como no "OS" do Remi, em vez de um agente por função. Novo agente só quando precisar de outro lugar para rodar, outras permissões ou outra pessoa usando.

## Discordâncias e pontos fracos
- Os links de VPS da descrição são de afiliado (10% de desconto): o vídeo ganha comissão em qualquer escolha.
- Números e versões são de junho/2026; os dois projetos mudam todo mês. Confira CVEs e recursos atuais antes de decidir.
- A comparação de custo é qualitativa; não há medição de tokens.
- "Aprendizado automático sem aprovação" também é risco: skills criadas sozinhas podem fixar um jeito errado. Vale auditar as skills do Curator de tempos em tempos.

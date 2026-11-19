# Guia: criar ou escolher um agente de IA

**Use quando:** for criar um agente novo (Hermes, OpenClaw, skill no Claude Code, automação 24 h) para você ou para um cliente, ou decidir se precisa de um.

## As 6 perguntas antes de criar
1. **A tarefa é repetitiva e previsível?** (briefing diário, relatório de mídia, triagem de mensagens, pauta semanal) → **Hermes**, que aprende sozinho e fica mais barato com a repetição. → [Metics: OpenClaw x Hermes](../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md)
2. **Precisa de integração pronta ou painel para alguém não técnico?** → considerar **OpenClaw**, com skills só de autores confiáveis e versão atualizada. → [Metics: OpenClaw x Hermes](../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md)
3. **Onde roda?** Mexe em contas, CRM ou WhatsApp de cliente → **VPS separada**, nunca no PC de trabalho; criação com arquivos locais → PC, com pastas limitadas. → [Metics: OpenClaw x Hermes](../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md)
4. **Permissões mínimas:** começar só com leitura e envio em rascunho com aprovação, liberando aos poucos. → [Metics: OpenClaw x Hermes](../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md)
5. **Custo:** o modelo mais barato que resolve; modelo caro só para criação e decisão. → [Metics: OpenClaw x Hermes](../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md)
6. **Precisa mesmo de agente novo?** Muitas vezes basta uma **skill** num agente existente; agente novo só quando mudam o lugar onde roda, as permissões ou quem usa. → [Remi](../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md)

## Complementos
- **Primeira tarefa = vigia:** checar algo num horário, lembrar o que já mostrou e **avisar só quando houver novidade** (ex.: leads novos no CRM, mensagens paradas no atendimento, relatório de mídia de segunda, anúncios novos de concorrentes, saúde do próprio sistema, "pulso" diário dos posts de concorrentes acima da média, com link). → [Kallaway, 5 skills](../setores/ia/fontes/2026-07-08_kallaway_5-skills-do-claude-para-conteudo.md), [Metics, tutorial do Hermes](../setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md)
- **Bot calado, ordem de checagem:** créditos/limite do provedor → gateway → logs filtrados por erro → reiniciar o app no Docker. No canal: `/sethome`, allow list só com o seu ID, nada sensível pelo Telegram (sem criptografia ponta a ponta). → [Metics, tutorial do Hermes](../setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md)
- **Pilar contexto:** arquivos .md revisados linha a linha (quem somos, ofertas, cliente ideal, voz da marca), um arquivo principal carregado em toda sessão e memória de correções ("salve como preferência" e confira na sessão seguinte). → [Remi](../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md)
- **Pilar ferramentas (MCP/conectores):** Apify (redes), Firecrawl (sites), Composio (vários apps), Chrome DevTools/Playwright (navegador). → [Remi](../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md)
- **Pilar skills:** faça a tarefa uma vez, ajuste na conversa e peça "transforme em skill"; as boas estão na versão 5 a 10. → [Remi](../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md)
- **Organização:** arquivos "como eu falo", "como eu trabalho", "quem sou eu" + um claude.md que manda ler os três; uma pasta por frente com as mesmas subpastas (archive, assets, references, skills, videos). → [Kallaway, 5 skills](../setores/ia/fontes/2026-07-08_kallaway_5-skills-do-claude-para-conteudo.md) Uma pasta "OS" como holding (uma subpasta por empresa ou cliente), em vez de um agente por função. → [Remi](../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md)

## Leia nesta ordem
1. [Metics Media: OpenClaw x Hermes](../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md) (decisão, segurança, custo) e [Hermes do zero](../setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md) (instalação, vigias, memória, problemas)
2. [Remi: agentes de IA, curso completo](../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md) (contexto, ferramentas, skills, pasta OS)
3. [Princípios de IA](../setores/ia/README.md#princípios-consolidados)
4. IA para pesquisa de conteúdo: [Kallaway, 5 skills do Claude](../setores/ia/fontes/2026-07-08_kallaway_5-skills-do-claude-para-conteudo.md)
5. Conteúdo feito com IA: [Kallaway, anti-slop e sistema híbrido](../setores/conteudo-e-redes/fontes/2026-10-29_kallaway_6-alphas-contra-ai-slop.md)

## Cuidados
- Versões, CVEs e preços mudam todo mês: confira o estado atual antes de decidir.
- Um vigia agêntico pode levar 30 a 45 min para se montar e custa bem mais que uma conversa; dimensione a VPS pelo número de tarefas (o mesmo canal indicou KVM 2 em junho e KVM 1 em outubro).
- Skills criadas sozinhas pelo agente também precisam de auditoria periódica.
- Dados de clientes (LGPD): acesso mínimo e registro do que o agente pode fazer.

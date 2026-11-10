# Guia: criar ou escolher um agente de IA

**Use quando:** for criar um agente novo (Hermes, OpenClaw, skill no Claude Code, automação 24 h) ou decidir se precisa de um.

## As 6 perguntas antes de criar
1. **A tarefa é repetitiva e previsível?** (briefing diário, relatório de mídia, triagem de mensagens, pauta semanal) → **Hermes** (aprende sozinho e o custo cai com a repetição).
2. **Precisa de integração pronta que o Hermes não tem, ou de painel visual para alguém não técnico?** → considerar **OpenClaw**, com skills só de autores confiáveis e versão atualizada.
3. **Onde roda?** Mexe em contas, CRM ou WhatsApp de cliente → **VPS separada**, nunca no PC de trabalho. Criação com arquivos locais → PC, com pastas limitadas.
4. **Permissões:** começar só leitura e envio em rascunho com aprovação; liberar aos poucos.
5. **Custo:** o modelo mais barato que resolve; modelo caro só para criação e decisão.
6. **Precisa mesmo de agente novo?** Muitas vezes basta uma **skill** num agente que já existe. Agente novo só quando muda o lugar onde roda, as permissões ou quem usa.

## Primeira tarefa: o padrão "vigia"
Comece todo agente novo com um vigia: checar algo num horário, lembrar o que já mostrou e **avisar só quando houver novidade**. Exemplos na We: leads novos no Facilita, mensagens paradas no Chatwoot, relatório de mídia de segunda, anúncios novos de concorrentes, saúde do próprio sistema. → [Metics, tutorial do Hermes](../setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md)

## Quando o bot fica calado (ordem de checagem)
1. Créditos e limite do provedor do modelo. 2. Gateway. 3. Logs filtrados por erro. 4. Reiniciar o app no Docker. No canal: `/sethome`, allow list só com o seu ID e nada de dado sensível pelo Telegram (o chat do bot não tem criptografia ponta a ponta).

## Como deixar o agente útil (os 3 pilares)
- **Contexto** em arquivos .md revisados linha a linha (quem somos, ofertas, cliente ideal, voz da marca) + um arquivo principal carregado em toda sessão + memória de correções.
- **Ferramentas (MCP/conectores):** Apify (raspagem de redes), Firecrawl (ler sites), Composio (vários apps num conector), Chrome DevTools/Playwright (navegador).
- **Skills:** faça a tarefa uma vez, ajuste na conversa e peça "transforme em skill"; as boas estão na versão 5 a 10.
- **Preferência ensinada vira memória:** "salve como preferência" e confira que vale na sessão seguinte.
- **Uma pasta "OS"** como holding (uma subpasta por empresa ou pilar), em vez de um agente por função.

## Leia nesta ordem
1. [Metics Media: OpenClaw x Hermes](../setores/ia/fontes/2026-06-15_metics-media_openclaw-vs-hermes.md) (decisão, segurança, custo)
2. [Metics: Hermes do zero](../setores/ia/fontes/2026-10-28_metics-media_hermes-agent-tutorial.md) (instalação, vigias, memória, solução de problemas)
3. [Remi: agentes de IA, curso completo](../setores/ia/fontes/2026-07-22_remi_agentes-de-ia-curso-completo.md) (contexto, ferramentas, skills, pasta OS)
4. [Princípios de IA](../setores/ia/README.md#princípios-consolidados)
5. Para conteúdo feito com IA: [Kallaway, anti-slop e sistema híbrido](../setores/conteudo-e-redes/fontes/2026-10-29_kallaway_6-alphas-contra-ai-slop.md)

## Cuidados
- Versões, CVEs e preços mudam todo mês; conferir o estado atual antes de decidir.
- Um vigia agêntico pode levar 30 a 45 min para se montar e custa bem mais que uma conversa; dimensione a VPS pelo número de tarefas (o mesmo canal indicou KVM 2 em junho e KVM 1 em outubro).
- Skills criadas sozinhas pelo agente também precisam de auditoria periódica.
- Dados de clientes (LGPD): acesso mínimo e registro do que o agente pode fazer.

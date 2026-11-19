---
titulo: "Master Hermes Agent in 20 Minutes (Beginner Tutorial)"
autoridades: [metics-media]
tipo: video
url: "https://youtu.be/q5RagIqBtjc"
canal_ou_editora: "Metics Media (YouTube), apresentado por Matt"
data_publicacao: 2026-10-28
data_inclusao: 2026-11-10
duracao: "21:16"
setor_principal: ia
setores_secundarios: [negocios-e-gestao]
evidencia: "legenda automática original em inglês (YouTube), lida inteira, sem análise de imagem (as telas do painel foram descritas só pela fala). A legenda distorce nomes: 'Now/Nouse/NUS/Mouse Portal' = Nous Portal; 'traffic' = Traefik; 'made model' = main model. Menus, nomes de modelos, preços e planos são de outubro/2026 e o próprio autor avisa que botões e rótulos mudam; conferir antes de seguir à risca."
tags: [agentes, hermes, vps, hostinger, telegram, cron, skills, memoria, custo, seguranca, tutorial]
---

# Hermes Agent em 20 minutos: tutorial do zero (Metics Media)

**Em uma frase:** em cinco passos e sem terminal (VPS Hostinger com template de um clique, modelo barato via Nous Portal, Telegram por QR code, um "vigia" agendado como primeira tarefa e uma preferência ensinada uma vez), o Hermes vira um agente 24 h que só avisa quando algo muda e lembra do seu jeito em toda conversa nova.

Mesmo canal e apresentador do comparativo [OpenClaw x Hermes](2026-06-15_metics-media_openclaw-vs-hermes.md): aquele vídeo ajuda a escolher a ferramenta; este mostra a montagem passo a passo.

## O que foi dito

**Promessa e roteiro [00:00–01:09]**
- Ao final, o agente roda sozinho, verifica o que importa, manda mensagem quando há novidade e lembra como você gosta das coisas. Sem código nem terminal.
- Matt diz usar o Hermes todo dia, com **mais de 20 tarefas agendadas** (preço de passagem, planejamento de viagem).
- O Hermes é gratuito; paga-se só o **servidor** e o **modelo**.
- Cinco perguntas, uma por passo: onde o agente mora; qual modelo (esperto e barato); como falar com ele pelo celular; qual o primeiro trabalho; como ensinar uma vez e ele lembrar em toda conversa nova.

**Passo 1: por que um servidor (VPS) [01:11–02:26]**
- A máquina precisa ser três coisas:
  1. **Acordada**: tarefas agendadas e mensagens dependem dela ligada às 3 da manhã; notebook na mochila não serve.
  2. **Separada das suas coisas**: o agente roda comandos, instala software, escreve e apaga arquivos. Enquanto aprende, isso deve acontecer onde não há fotos pessoais, senhas, documentos sensíveis nem navegador logado no banco. É uma "oficina de treino": se quebrar, apaga e recomeça em 10 minutos.
  3. **Acessível** de celular, notebook e tablet, como portas para o mesmo agente.
- Dá para instalar no próprio computador, mas aí só funciona com ele ligado e roda comandos "ao lado de tudo que você tem". Para o primeiro agente: alugue o servidor. O menor custa "poucos dólares por mês".

**Passo 1b: contratar e implantar na Hostinger [02:26–06:22]**
- Na maioria dos provedores a instalação é por terminal; a Hostinger tem **template de um clique** que instala o Hermes atrás de um endereço web seguro, com página de login, backups, atualização em um clique e botão de reiniciar.
- Aviso [02:58]: o software muda sempre; siga a ideia geral, não o visual exato.
- Custos do dia: servidor (poucos dólares/mês) + conta do modelo ("o preço de um streaming").
- Link de afiliado com 10% extra sobre promoções. Plano recomendado: **KVM 1** (o menor; roda um agente com folga; dá para subir de plano depois sem reinstalar).
- Carrinho: período mínimo de **12 meses** para o desconto; garantia de **30 dias**. **Desmarcar "Ready to use AI"** (assina outro serviço de IA desnecessário). Não mexer nos outros adicionais e conferir o desconto.
- Cadastro (Google, GitHub ou e-mail; telefone opcional) e pagamento.
- Formulário do Hermes: usuário admin (padrão "Hermes", pode mudar) e senha gerada. Copiar a senha para um **gerenciador de senhas**, nunca bloco de notas. Clicar em **Deploy**.
- Esperar o app "Hermes agent" ficar com check verde e status **running**. Em **Docker Manager > aplicações** aparecem dois itens: o Hermes e o **Traefik**, que protege a conexão.

**Passo 1c: o painel [06:22–07:58]**
- Docker Manager > Hermes agent > coluna Access > **Open**: abre o login do painel; salvar a URL nos favoritos e entrar com usuário e senha.
- Menu lateral: **Sessions** (todas as conversas, de qualquer aparelho, com uma memória só); **Models** (qual IA pensa; vem sem nenhum escolhido); **Cron** (agenda, "trabalha enquanto você dorme"); **Chat** no topo (chat estilo terminal retrô).
- Ao mandar "hello", erro **"no inference provider configured"**: está instalado mas não pensa. O **Gateway** é a parte que conecta com o mundo de fora (leva mensagens ao celular) e ainda não tem a que se ligar.

**Passo 2: modelo e provedor [07:58–12:02]**
- O modelo é o "cérebro emprestado" (o mesmo tipo de IA do ChatGPT e do Claude). O Hermes não vem com um.
- Ele usa o **Nous Portal** (dos criadores do Hermes), integrado: conecta com login, sem copiar chave. Uma conta dá acesso a **mais de 200 modelos** e às ferramentas (busca na web, leitura de páginas, geração de imagem, navegador, fala).
- Preço: **US$ 20/mês dá US$ 22 de créditos**. Com o link de afiliado, US$ 15 de desconto no primeiro mês (sai US$ 5), o que "cobre este vídeo e semanas depois".
- Cadastro (Google, e-mail, GitHub, Discord...), código de 6 dígitos por e-mail, checkout.
- No painel: **Keys** > Nous Portal > **Login** > "permitir que o Hermes use seu plano Plus" > **Connect**.
- **Models** > **Change** ao lado do modelo principal. Recomendação: começar com modelo **rápido e barato**, porque se manda muita mensagem aprendendo. Ele escolhe **DeepSeek V4 Flash** (na lista: V4 Pro, V4 Pro 0813, V4 Flash 0731); pegar sempre a versão Flash mais nova. Motivo: bom com ferramentas e cada mensagem custa "uma fração de centavo". **Switch** > **Reload**.
- Teste no Chat: responde. Perguntado "que ferramentas você tem?", lista navegador, terminal, arquivos, execução de código, busca na web, **delegar a subagentes**, memória, agendamento e outras.

**Passo 3: Telegram [12:02–16:46]**
- Telegram porque é o mais fácil (um QR code, sem copiar código) e aceita arquivos, áudio e fotos na mesma conversa. O Hermes suporta **mais de 20 plataformas** (Discord, Slack, WhatsApp...), adicionáveis na mesma página.
- **Channels** > Telegram (desativado) > ligar o toggle > **Restart** (o gateway reinicia em alguns minutos; se demorar, atualizar o navegador).
- Aparece "no bot token configured" > **Create with QR**. No celular: escanear, abrir conversa com o bot hospedado da Nous ("HermesBot"), **Create bot** > **Create**; voltar a essa conversa (ou escanear de novo) e tocar em **Connect this bot**.
- O bot aparece no painel com nome e **allowed user** (seu ID do Telegram). **Save and restart**.
- No Telegram, abrir o bot (@Hermes + números e letras), **Start** e mandar uma mensagem (o Start sozinho não inicia nada).
- Aviso de "no home channel": usar o comando **/sethome**. O home channel é onde chegam resultados do cron e mensagens entre plataformas.
- **Segurança [15:33]**: o fluxo colocou só a sua conta na **allow list**; estranhos não recebem resposta. Conversas com bot do Telegram **não têm criptografia ponta a ponta**: não mandar senhas nem dados bancários.
- **Bot calado, checar nesta ordem [15:47]**: (1) crédito e limite de uso no provedor do modelo, a causa mais comum (o Hermes costuma avisar na última mensagem); (2) status do **gateway**, e reiniciar se estranho; (3) **Logs** (filtro por debug, info, warning, error; filtrar erros). Se nada resolver, reiniciar o app inteiro no Docker Manager da Hostinger (três pontos > Restart).

**Passo 4: primeiro trabalho, um "vigia" [16:46–19:04]**
- Vigia = checa algo num horário e **só avisa quando muda**. Você descreve o que importa uma vez; ele escreve a própria skill, se agenda e passa a avisar só em novidade.
- Skill = "notas passo a passo que o agente escreve para si" para repetir o trabalho.
- Ele usa o **app de desktop do Hermes** (mesmo agente; dá para mandar pelo Telegram). Pedido, em sessão nova: acompanhar a tendência de preço de passagem Barcelona–Londres, **criar uma skill reutilizável**, **guardar o que já foi mostrado**, agendar a cada poucas horas e avisar no Telegram **só quando houver algo novo**.
- Levou **30 a 45 minutos**: foi à internet, descobriu como fazer, montou o script, a skill, o agendamento e uma memória do que já mostrou. Em scheduled jobs aparece o "Barcelona London flight price watch", rodando **a cada 6 horas**. Depois chegou um aviso sozinho quando o preço mudou.
- Exemplos dos 20+ jobs dele: conferir a contabilidade toda segunda; acompanhar aniversários e pesquisar presentes com antecedência; trabalhar num plano de viagem duas vezes por dia trazendo cotações; dar follow-up numa negociação.
- Outros alvos: preço, notícias de um tema, previsão do tempo. Alguns sites bloqueiam agentes; peça para achar outra fonte.

**Passo 5: ensinar uma vez (memória) [19:04–20:34]**
- Problema comum: você corrige a IA e na sessão seguinte ela esqueceu.
- Demo: pediu um post curto sobre iluminação de estúdio; veio com títulos, tópicos e prolixo. Correção: "prolixo; prefiro frases curtas e diretas, no máximo três parágrafos, sem títulos nem tópicos. **Salve como preferência**." Ele salvou na memória e refez.
- Em **sessão nova**, pediu um post sobre torra de café: veio no mesmo formato. Sem página de configuração, só falando, "como se treina um contratado novo". Vale para toda conversa e todo aparelho.

**Custos [20:34–21:16]**
- Servidor é fixo por mês; o modelo varia (centavos por mensagem). O gasto aparece na página **Usage** do Nous Portal. No primeiro dia, o modelo custou a ele "um pouco mais de 8" (a legenda não diz a unidade; provavelmente US$ 8, incluindo o vigia de 30 a 45 minutos).
- Fecha indicando o guia completo dele (conectar apps e "dar um time" ao agente) e repete o link da Hostinger.
- Observação: o vídeo **não cita o Curator pelo nome** nem aborda sandbox, backups manuais ou permissões finas; a segurança se resume a VPS separada, senha no gerenciador, allow list e não mandar dados sensíveis pelo Telegram.

## Frases-chave
- "Think of it as a practice workshop. You're going to make a mess in it, which is what it's for." [01:47]
- "A watcher checks something on a schedule, and it only messages you when something changes." [16:53]
- "Telegram bot chats aren't end-to-end encrypted. So don't send it passwords or banking details." [15:40]
- "I described an outcome once and now it comes to me." [18:29]
- "I told it plainly the way you would tell a new hire as you're training them." [19:52]

## Aplicação para a We

**O que o Alex já tem (bate com o tutorial):** Hermes em **VPS Hostinger com Docker** e **Telegram** (agente "Alex", @alexhermes2026_bot), memórias e skills versionadas no repo **cerebroagent**, e um segundo Hermes no PC (perfil "criacao") como gerente que delega ao Claude Code via claude-criar. Ou seja, os passos 1 a 3 estão feitos e a arquitetura já vai além do tutorial (dois agentes, cérebro em Git, delegação).

**O que pode estar faltando (checar):**
- **Vigias de verdade no cron.** O ganho central do vídeo é o padrão "checa no horário e só avisa se mudou". Vale listar quantos jobs o agente Alex tem hoje; a meta do Matt é 20+.
- **Home channel definido** (/sethome) e **allow list** só com o ID do Alex no bot da VPS; conferir que nenhum outro usuário fala com o agente.
- **Memória do que já foi mostrado** em cada vigia (para não repetir aviso) e preferências salvas explicitamente ("salve como preferência"), espelhadas no cerebroagent para não ficarem presas ao Hermes.
- **Rotina de pane:** créditos/limite do provedor > gateway > logs > restart no Docker Manager. Um job semanal que avise se créditos estão baixos evita o "bot calado".
- **Custo por agente:** usar modelo barato (tipo Flash) para vigias e triagem, e o modelo caro só para criação e decisão; acompanhar o gasto no painel do provedor.
- **Dados sensíveis fora do Telegram:** CPF, contratos, senhas e dados de clientes não trafegam pelo chat do bot (sem criptografia ponta a ponta); o aviso traz só resumo e link para o sistema.

**Vigias/agendamentos concretos para a We (todos com permissão mínima):**
1. **Vigia de leads (Facilita + painel de leads)**: a cada 2 h em horário comercial, lê pela API pública só GET e avisa no Telegram apenas lead novo sem atendimento há mais de X horas ou queda brusca de volume por origem (RD/Facebook). Permissão: só leitura; nada de editar etapa do funil.
2. **Vigia do Chatwoot**: de hora em hora, lê as inboxes Livia (leads) e Wilson (corretores) com o token de agente só leitura e avisa conversa sem resposta acima do prazo ou pedido de visita. Não responde a ninguém; no máximo sugere rascunho de resposta para o Alex aprovar.
3. **Relatório de mídia semanal** (segunda cedo, como o "contabilidade toda segunda" do Matt): CPL, CTR e frequência das campanhas do Bioma e do Vicente e posts via Zernio, com alerta de fadiga de criativo. Permissão: leitura de métricas; pausar ou escalar campanha continua manual.
4. **Vigia de concorrentes** (diário ou 2x por semana): biblioteca de anúncios da Meta e sites/Instagram de incorporadoras de Cascavel e Toledo; avisa só anúncio, lançamento ou preço novo, guardando o histórico do que já mostrou. Permissão: navegação pública, sem login em contas da We.
5. **Saúde do próprio sistema** (diário): créditos do provedor, gateway e erros nos logs do Hermes, posts com falha no Zernio e programação da semana em 03_PROGRAMAÇÃO; avisa só se algo estiver fora do normal.

Cada vigia vira uma skill no cerebroagent (com o que ele lê, o critério de "novidade" e para onde avisa) e deve ser auditada de tempos em tempos, porque skills escritas pelo agente podem fixar um jeito errado.

## Discordâncias e pontos fracos
- **Afiliado em dobro:** os dois links da descrição (Hostinger com 10% e Nous Portal com US$ 15 de desconto) geram comissão. A escolha de Hostinger e Nous Portal é apresentada como a mais fácil, sem comparar outros provedores (OpenRouter, Anthropic, OpenAI direto).
- **Contradição com o vídeo de junho do mesmo canal:** lá o mínimo indicado era o plano **KVM 2**; aqui é o **KVM 1**. Para um agente com muitos jobs, navegador e subagentes, o menor plano pode ficar curto.
- **Versões mudam:** nomes de modelos (DeepSeek V4 Flash 0731), menus do painel e preços são de outubro/2026; o próprio autor pede para seguir "a ideia geral".
- **Custo subestimado na fala:** "fração de centavo por mensagem", mas o primeiro dia custou cerca de 8 (provavelmente dólares), porque um vigia levou 30 a 45 minutos para se montar. Tarefas agênticas longas gastam bem mais que conversa.
- **Segurança rasa para empresa:** não fala de permissões por ferramenta, sandbox, chaves com escopo mínimo, revisão das skills criadas sozinho nem LGPD. Para dados de clientes, seguir o que já está no [curso do Remi](2026-07-22_remi_agentes-de-ia-curso-completo.md) (só leitura e rascunho com aprovação).
- **Memória presa à ferramenta:** a preferência fica na memória do Hermes; se o Alex trocar de harness, perde. Por isso vale espelhar no cerebroagent.
- Sites que bloqueiam agentes ("peça outra fonte") podem levar o vigia a fontes menos confiáveis sem você perceber; conferir de onde vem o dado.

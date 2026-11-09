# Regras para agentes neste repositório

Este repositório é o cérebro de **conhecimento externo** do Alex (We Inc / Ecossistema WE): resumos do que autoridades dizem, por setor. Siga estas regras ao adicionar ou consultar conteúdo.

## Ao adicionar uma fonte
- Escreva em **português do Brasil**, mesmo que a fonte esteja em outra língua.
- **Nunca cole a transcrição inteira** nem trechos longos (direitos autorais). Faça um resumo próprio com timestamps e, no máximo, citações curtas.
- Nome do arquivo: `setores/<setor>/fontes/AAAA-MM-DD_<autor-slug>_<titulo-slug>.md`. A data é a da **publicação** da fonte; se não souber, use a data de inclusão e marque `data_publicacao: desconhecida`.
- Preencha o frontmatter do modelo (`_modelos/fonte.md`). Cada fonte tem **um setor principal**; os demais vão em `setores_secundarios`.
- Indique a **qualidade da evidência**: legenda original, tradução automática, transcrição local, leitura etc. Nomes e números vindos de tradução automática podem estar distorcidos e precisam ser marcados como tal.
- Separe três blocos: **o que a pessoa disse** (fiel), **aplicação para a We** (opinião nossa) e **discordâncias ou pontos fracos**.
- Atualize a ficha da autoridade, o README do setor principal, o README dos setores secundários e o README raiz (só se a pessoa for nova).

## Ao consultar
- Cite o arquivo de origem e o timestamp ao usar uma ideia daqui.
- Prefira os **Princípios consolidados** dos setores: são ideias confirmadas por mais de uma fonte.
- Ideia de uma única pessoa é opinião, não regra.

## Setores válidos
`marketing`, `ia`, `design`, `branding`, `conteudo-e-redes`, `trafego-pago`, `vendas`, `mercado-imobiliario`, `negocios-e-gestao`. Para criar um setor novo, copie a estrutura de um existente e adicione-o à tabela do README raiz.

## Commits
Mensagens curtas em português, por exemplo: `fonte: Michelly Müller — conteúdo que vende imóveis 2026`.

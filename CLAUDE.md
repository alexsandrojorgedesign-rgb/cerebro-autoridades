# Regras para agentes neste repositório

Este repositório é o cérebro de **conhecimento externo** do Alex: resumos do que autoridades dizem, por setor. O foco é **geral** (qualquer cliente ou projeto: We Inc e Ecossistema WE, Creare, Nós Gastronomia, Casa do Jardineiro, GW, marca pessoal e o que vier); a We é um exemplo, não o único público. Siga estas regras ao adicionar ou consultar conteúdo.

## Ao adicionar uma fonte
- Escreva em **português do Brasil**, mesmo que a fonte esteja em outra língua.
- **Nunca cole a transcrição inteira** nem trechos longos (direitos autorais). Faça um resumo próprio com timestamps e, no máximo, citações curtas.
- Nome do arquivo: `setores/<setor>/fontes/AAAA-MM-DD_<autor-slug>_<titulo-slug>.md`. A data é a da **publicação** da fonte; se não souber, use a data de inclusão e marque `data_publicacao: desconhecida`.
- Preencha o frontmatter do modelo (`_modelos/fonte.md`). Cada fonte tem **um setor principal**; os demais vão em `setores_secundarios`.
- Indique a **qualidade da evidência**: legenda original, tradução automática, transcrição local, leitura etc. Nomes e números vindos de tradução automática podem estar distorcidos e precisam ser marcados como tal.
- Separe três blocos: **o que a pessoa disse** (fiel), **aplicação prática** (opinião nossa, geral; exemplos de clientes só quando ajudam) e **discordâncias ou pontos fracos**.
- Atualize a ficha da autoridade, o README do setor principal, o README dos setores secundários e o README raiz (só se a pessoa for nova).

- **Gerados automaticamente** por `_modelos/gerar_indices.py`: os READMEs dos setores, o `README.md` da raiz, o `INDICE.md` e o `guias/README.md`. Não edite esses arquivos à mão; edite as listas do script (`P` autoridades, `F` fontes, `PRINC` princípios, `G` guias, `GS` guias por setor) e rode `python -I _modelos/gerar_indices.py`. O script avisa se houver link quebrado.
- **Guias por tarefa** (`guias/*.md`) são escritos à mão: checklist rápido, "leia nesta ordem" e cuidados. Quando uma fonte nova mudar ou reforçar um checklist, atualize o guia correspondente e cite a fonte.
- A qualidade da evidência no `INDICE.md` é calculada pelo campo `evidencia` do frontmatter: escreva nele palavras como "lida inteira", "tradução automática", "frames"/"sem áudio", "NÃO é o livro completo" ou "MUITO FRACA" para a classificação sair certa.
- Os READMEs dos setores são gerados por `_modelos/gerar_indices.py` (listas `P` = autoridades, `F` = fontes, `PRINC` = princípios consolidados). Para atualizar, edite as listas e rode `python -I _modelos/gerar_indices.py`; não edite os READMEs dos setores à mão.

## O que entra (curadoria)
- Prefira quem mostra **caso real com número**, pesquisa ou prática de mercado (sobretudo brasileiro e imobiliário) a vídeo de iniciante ou de motivação.
- Se uma fonte só **repete** o que já está no repositório (mesmo autor ou fundamentos já cobertos por Ogilvy, Hopkins etc.), não crie arquivo novo: acrescente uma linha "reforçado por …" na fonte existente ou no princípio e registre o link no índice só se trouxer algo novo.
- Guias: no máximo **10 itens** no checklist; o resto vai para "Complementos". Ao incluir item novo, troque com o mais fraco em vez de só somar.

## Casos próprios
- `casos/` guarda o que **nós** testamos (peça, campanha, reel, deck) com métrica e aprendizado, usando `_modelos/caso.md`. Caso próprio com número pesa mais que opinião de autoridade; cite-o no guia quando confirmar ou contrariar um item.

## Ao consultar
- Comece pelos **guias** (`guias/README.md`) quando a pergunta for "como faço X"; vá ao `INDICE.md` para achar uma fonte específica.
- Cite o arquivo de origem e o timestamp ao usar uma ideia daqui.
- Prefira os **Princípios consolidados** dos setores: são ideias confirmadas por mais de uma fonte.
- Ideia de uma única pessoa é opinião, não regra.

## Setores válidos
`marketing`, `ia`, `design`, `branding`, `conteudo-e-redes`, `trafego-pago`, `vendas`, `mercado-imobiliario`, `storytelling`, `negocios-e-gestao`. Para criar um setor novo, copie a estrutura de um existente e adicione-o à tabela do README raiz.

## Commits
Mensagens curtas em português, por exemplo: `fonte: Michelly Müller — conteúdo que vende imóveis 2026`.

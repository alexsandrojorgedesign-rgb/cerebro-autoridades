# Cérebro de Autoridades

Base de conhecimento **externo**: o que pessoas de referência dizem sobre marketing, IA, design, branding, storytelling, vendas e mercado imobiliário. Aqui ficam resumos de vídeos, podcasts, livros, cursos e posts, organizados por setor, para consultar na hora de criar estratégia, conteúdo e campanhas.

> O conhecimento **interno** (clientes, projetos, aprendizados do Alex) fica no `cerebroagent` e em `G:\Meu Drive\00_CEREBRO CRIAÇÃO`. Este repositório guarda só o que vem de fora.

## Estrutura

```
cerebro-autoridades/
├── autoridades/            uma ficha por pessoa (quem é, setores, ideias centrais, fontes)
├── setores/
│   ├── marketing/
│   ├── ia/
│   ├── design/
│   ├── branding/
│   ├── conteudo-e-redes/
│   ├── trafego-pago/
│   ├── vendas/
│   ├── mercado-imobiliario/
│   ├── storytelling/
│   └── negocios-e-gestao/
│       ├── README.md       índice do setor: autoridades, fontes e princípios consolidados
│       └── fontes/         um resumo por conteúdo (AAAA-MM-DD_autor_titulo.md)
└── _modelos/               modelos de ficha de autoridade e de fonte
```

**Cada fonte mora em um setor só** (o principal). Os outros setores a que ela interessa apenas apontam para ela na tabela do README de cada um.

## Setores

| Setor | Assunto |
|---|---|
| [Marketing](setores/marketing/) | estratégia, funil, growth, retenção, LTV |
| [IA](setores/ia/) | IA aplicada a criação, marketing e vendas |
| [Design](setores/design/) | direção de arte, tipografia, UI/UX, motion |
| [Branding](setores/branding/) | marca, identidade, posicionamento, marca pessoal |
| [Conteúdo e Redes](setores/conteudo-e-redes/) | formatos, algoritmo, ganchos, roteiros |
| [Tráfego Pago](setores/trafego-pago/) | Meta Ads, Google Ads, criativos de performance |
| [Vendas](setores/vendas/) | atendimento, follow-up, CRM, oferta e preço |
| [Mercado Imobiliário](setores/mercado-imobiliario/) | incorporação, corretores, jornada do comprador |
| [Storytelling](setores/storytelling/) | narrativa, roteiro, ganchos, tensão e retenção |
| [Negócios e Gestão](setores/negocios-e-gestao/) | estratégia, gargalos, liderança, modelo de negócio |

## Pasta META (Meta Ads, Facebook, Instagram, WhatsApp)

O que a Meta ensina oficialmente, estudado pela documentação pública e pelo catálogo do Meta Blueprint: estrutura de campanha, públicos (incluindo a categoria especial de Moradia), leilão, formatos, criativos, formulários e clique para WhatsApp, mensuração e API de Conversões, políticas e certificações. Ver [META/README.md](META/README.md).

## Autoridades

| Pessoa | Setores | Ficha |
|---|---|---|
| Michelly Müller | mercado imobiliário, conteúdo, tráfego pago, branding | [ficha](autoridades/michelly-muller.md) |
| Dener Lippert (V4 Company) | marketing, vendas, negócios, tráfego pago | [ficha](autoridades/dener-lippert.md) |
| Alfredo Soares (G4) | branding, vendas, negócios | [ficha](autoridades/alfredo-soares.md) |
| Bruno Nardon (G4) | negócios, branding | [ficha](autoridades/bruno-nardon.md) |
| Tay Dantas (Vince Société) | branding, marketing, conteúdo | [ficha](autoridades/tay-dantas.md) |
| Ana Couto | branding, marketing, negócios | [ficha](autoridades/ana-couto.md) |
| Philip Kotler | marketing, branding, negócios | [ficha](autoridades/philip-kotler.md) |
| Seth Godin | marketing, branding, conteúdo | [ficha](autoridades/seth-godin.md) |
| Claude C. Hopkins | marketing, tráfego pago, vendas | [ficha](autoridades/claude-hopkins.md) |
| David Ogilvy | marketing, branding, conteúdo | [ficha](autoridades/david-ogilvy.md) |
| Erich Shibata (Cimed) | branding, marketing, vendas | [ficha](autoridades/erich-shibata.md) |
| Marty Neumeier | branding, design | [ficha](autoridades/marty-neumeier.md) |
| Alex Hormozi | branding, conteúdo, marketing | [ficha](autoridades/alex-hormozi.md) |
| Gary Vaynerchuk | conteúdo e redes, marketing | [ficha](autoridades/gary-vaynerchuk.md) |
| Kallaway | storytelling, conteúdo e redes | [ficha](autoridades/kallaway.md) |
| Carmine Gallo | storytelling, branding, vendas | [ficha](autoridades/carmine-gallo.md) |
| Philipp Humm | storytelling, conteúdo e redes | [ficha](autoridades/philipp-humm.md) |

## Como adicionar um conteúdo

1. Assista ou leia o conteúdo. Para vídeo, use `/watch <url>` no Claude Code.
2. Copie `_modelos/fonte.md` para `setores/<setor-principal>/fontes/AAAA-MM-DD_autor_titulo.md` e preencha.
3. Crie ou atualize a ficha em `autoridades/` (modelo em `_modelos/autoridade.md`).
4. Atualize as tabelas: README do setor principal, README dos setores secundários e este README, se a pessoa for nova.
5. Se uma ideia já apareceu em outra fonte, registre-a em **Princípios consolidados** do setor.

As regras completas para agentes (Claude Code, Hermes) estão no [CLAUDE.md](CLAUDE.md).

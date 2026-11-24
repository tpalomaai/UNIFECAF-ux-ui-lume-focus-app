# Revisão da F2 — Wireframes

Arquivo Figma: [Lume — UX/UI](https://www.figma.com/design/z7C1XSWQhlIpYry549Ba3Q/Lume-%E2%80%94-UX-UI?node-id=2-2) · página "🔲 Wireframes" (id 2:2)
Frames: 3:2 (01) · 3:10 (02) · 3:30 (03) · 3:50 (04) · 10:8 (04b) · 3:66 (05) · 3:81 (06)

## Resultado da revisão
- Verificado: estrutura do arquivo, nomes dos frames, camadas, textos e um print da página Wireframes.
- Não verificável pela leitura: ligações do modo Prototype. Foram testadas no Prototype Preview.
- Nomes dos frames, ordem das telas e conteúdo seguem o docs/02-fluxo.md. A F2 estava ~90% pronta.

| Tela | Certo | Problema |
|---|---|---|
| 01 - Boas-vindas | Mensagem "sem contagem regressiva" clara, um botão só | — |
| 02 - Início | Continuar daqui com onde parei, próximo passo e Retomar | Hierarquia invertida |
| 03 - Escolher tarefa | Tarefas recentes com "última vez: X min" | Campo sem rótulo visível |
| 04 - Sessão | Cronômetro grande, fundo escuro, Concluir em destaque | Pausa sem fluxo |
| 05 - Lembrar depois | Título como pergunta, lista de lembretes | — (o título já funciona como rótulo) |
| 06 - Sessão concluída | Métricas e mensagem gentil ("e tudo bem") | Campos sem rótulo visível |

## Problemas e motivos
1. **Hierarquia invertida (02):** "Nova sessão" estava como botão primário (escuro, cheio) e "Retomar" só com contorno. Isso contradiz o doc 1.3, que define Retomar como a ação mais importante (Lei de Fitts; a pesquisa mostrou 30 min–1 h perdidos para retomar). O design precisa bater com o documento.
2. **Campos sem rótulo (03, 06):** o texto do campo era só placeholder e some ao digitar; quem se distrai (nosso público) esquece o que o campo pedia. Boa prática NN/g e WCAG: rótulo visível acima do campo. Vira argumento na seção 1.5.
3. **Pausa sem fluxo (04):** pausar não troca de tela, só muda o estado (cronômetro para, botão vira "Continuar"). A tabela de interações só listava trocas de tela, então a pausa ficou de fora (falha de planejamento). Solução agora: frame "04b - Sessão pausada". Solução na F4: componente interativo com estados Rodando/Pausado (Change to) — conta pontos em "componentes reutilizáveis".

## Observações menores (sem ação no Figma agora)
- Fundamentos e Componentes estão como seções dentro da página "🧩 Library" (não páginas separadas). Manter; só atualizar a documentação.
- Frames "Espaço" servem no wireframe; na F4 viram espaçamento do Auto Layout.

## Correções aplicadas (24/11/2026)
| # | Onde | O que mudou |
|---|---|---|
| 1 | 02 - Início | "Botão — Retomar" virou primário (cinza escuro cheio, texto branco, 56 px). "Botão — Nova sessão" virou secundário (fundo branco, contorno cinza, texto escuro) |
| 2 | 03 - Escolher tarefa | Rótulo visível "No que vai focar?" (13 px, Medium, escuro) acima do campo · placeholder "Ex.: Estatística — cap. 4" em cinza médio |
| 2 | 05 - Lembrar depois | Sem mudança: o título "O que você precisa lembrar?" funciona como rótulo · placeholder mantido |
| 2 | 06 - Sessão concluída | Rótulos "Onde parei?" e "Próximo passo" acima dos campos · placeholders "Ex.: revisei o cap. 3" e "Ex.: fazer os exercícios 4 a 6" |
| 3 | 04b - Sessão pausada | Novo frame (cópia do 04), ao lado do 04; 05 e 06 empurrados para a direita. "Pausado" no lugar da mensagem de apoio; "Botão — Pausar" virou "Botão — Continuar" |
| 4 | Prototype | Reações antigas apagadas e 14 ligações recriadas com as transições do docs/02-fluxo.md; 01 é o flow starting point "Fluxo principal" |

Os rótulos ficaram dentro de um Auto Layout `Campo — <rótulo>` (rótulo + input, 6 px de espaço), mantendo alinhamento e espaçamentos da tela. Tudo em cinza, sem cor, ícone ou ilustração.

### Interações criadas
| Origem | Gatilho (On click) | Destino | Transição |
|---|---|---|---|
| 01 | Começar | 02 | Dissolve 250 ms |
| 02 | Nova sessão | 03 | Slide da direita 250 ms |
| 02 | Retomar | 04 | Dissolve 300 ms |
| 03 | ← Voltar | 02 | Slide da esquerda 250 ms |
| 03 | Começar | 04 | Dissolve 300 ms |
| 04 | Pausar | 04b | Dissolve 200 ms |
| 04b | Continuar | 04 | Dissolve 200 ms |
| 04 | Lembrar depois | 05 | Slide de baixo 250 ms |
| 04b | Lembrar depois | 05 | Slide de baixo 250 ms |
| 05 | Guardar e voltar | 04 | Slide para baixo 250 ms |
| 05 | ← Voltar à sessão | 04 | Slide para baixo 250 ms |
| 04 | Concluir | 06 | Smart Animate 300 ms |
| 04b | Concluir | 06 | Smart Animate 300 ms |
| 06 | Salvar e sair | 02 | Dissolve 250 ms |

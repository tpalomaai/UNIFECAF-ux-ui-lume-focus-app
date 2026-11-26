# Script de gravação da narração — Lume

> Texto pronto pra ler em voz alta e gravar, um arquivo de áudio por vez. Fonte da verdade do texto: `docs/05-slides-narracao.md` (aqui é só formatado pra leitura durante a gravação).

## Como gravar
- Grave cada bloco como um arquivo separado, salvando em `video-editor/entrada/narracao/` com o nome indicado.
- Ritmo calmo, sem pressa — é melhor passar um pouco do tempo estimado do que engolir palavra.
- Se errar no meio, pare e regrave só aquele bloco — não precisa regravar os outros.
- Slides 1 e 11 não têm fala, só música — não precisam de gravação.
- Deixe ~1 segundo de silêncio no início e no fim de cada gravação (facilita cortar depois).

---

## Slide 2 — `narracao/slide-02.m4a` (~8 s)
> Quem estuda ou trabalha sozinho, em casa, sabe o problema: não tem ninguém puxando sua atenção de volta.

## Slide 3 — `narracao/slide-03.m4a` (~12 s)
> Pensei em pessoas que estudam a distância, trabalham em home office ou aprendem um idioma, e perdem de 30 minutos a uma hora só para lembrar onde pararam.

## Slide 4 — `narracao/slide-04.m4a` (~12 s)
> E os apps de foco mais conhecidos usam contagem regressiva — que vira uma corrida contra o relógio e gera ansiedade quando o tempo acaba antes da tarefa.

## Slide 5 — `narracao/slide-05.m4a` (~15 s)
> O Lume inverte isso: em vez de cobrar um prazo, ele mede. Um cronômetro progressivo registra quanto tempo cada tarefa levou, sem prazo e sem alarme — e guarda onde você parou, pra retomar em segundos.

## Slide 6 — `narracao/slide-06.m4a` (~2 s)
> Vamos ver o fluxo.

## Protótipo — `narracao/prototipo.m4a` (~1 min 35 s)
Grave esta fala junto com a tela do protótipo em modo apresentação (ou grave só o áudio e sincronize depois — como preferir). Sequência de telas pra acompanhar enquanto fala: **02 Início → 03 Escolher tarefa → 04 Sessão → 05 Lembrar depois → 04 → 06 Concluída**.

> Na tela inicial, o card "Continuar daqui" já mostra onde parei e o próximo passo — um toque em "Retomar" e eu volto direto pra sessão, sem precisar escolher nada de novo. Pra começar algo novo, escolho a tarefa — as mais recentes aparecem com o tempo da última vez, pra eu não digitar de novo. Na sessão, o cronômetro sobe sem pressão, sem contagem regressiva. Se alguma outra tarefa me distrai no meio do caminho, eu só toco em "Lembrar depois", anoto rapidinho, e volto exatamente pra onde estava — sem perder o fio. Quando termino, toco em "Concluir": vejo quanto tempo levei, comparo com a última vez de forma gentil, e já registro onde parei e o próximo passo pra próxima sessão.

## Slide 7 — `narracao/slide-07.m4a` (~17 s)
> Por trás disso tem um design system único no Figma: cada cor tem uma função fixa — índigo pra ação principal, amarelo pra progresso, rosa só pro atalho de retomar. A fonte Lexend foi escolhida justamente por facilitar a leitura.

## Slide 8 — `narracao/slide-08.m4a` (~12 s)
> E cada botão, card e input é um componente reutilizável ligado a tokens — então uma correção de contraste, por exemplo, atualiza as sete telas de uma vez só.

## Slide 9 — `narracao/slide-09.m4a` (~18 s)
> Isso também guiou a parte de acessibilidade: todo contraste de cor passa o padrão AA do WCAG, todo elemento clicável tem no mínimo 48 pixels de área de toque, e nada no app depende só de cor pra passar uma informação.

## Slide 10 — `narracao/slide-10.m4a` (~27 s)
> O maior diferencial do Lume não é visual — é a ausência da contagem regressiva. Pra quem tem ansiedade ou dificuldade de manter o foco, medir o tempo em vez de cobrar ele faz toda a diferença. Junto com o histórico por tarefa, o "Lembrar depois" e o "Continuar daqui", o Lume trata o progresso como ele realmente é: no seu próprio ritmo.

---

**Duração total estimada: ~3:46** (alvo 3:45, nunca acima de 3:55). Se algum bloco passar muito do tempo estimado na gravação, me avise — ajustamos o texto do bloco "protótipo" primeiro, antes de mexer na estrutura dos slides.

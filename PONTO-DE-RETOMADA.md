# 📍 Ponto de retomada — Lume

> **Seção 🎨 Fundamentos concluída** ✅ em 25/11/2026 — Etapas 1 a 5 todas prontas (as Etapas 3–5, Tipografia/Medidas/Conferência, acabaram indo via MCP a pedido da Paloma, não à mão como planejado originalmente).
> Este arquivo guiava só os Fundamentos — a partir daqui, o `PROJECT_OVERVIEW.md` é a referência para a próxima etapa (componentes compostos, F4 em diante). Arquivo Figma: [Lume — UX/UI](https://www.figma.com/design/z7C1XSWQhlIpYry549Ba3Q).

## Como ficou a divisão MCP + à mão
Desde 25/11, o plano é **Figma Professional** (vaga Full) — o MCP voltou a funcionar. A divisão é por tipo de tarefa, não por limite: tarefas em lote (componentes com variantes, listas repetitivas como Tipografia/Medidas, telas finais, interações) ficam com o Claude via MCP; ajustes pontuais de poucos cliques (renomear, trocar 1 texto/cor/ícone, testar o protótipo, gerar o link público) ficam com a Paloma à mão. Regras completas em CLAUDE.md, seção "💳 Política de uso do Figma MCP".

## ✅ Já pronto no Figma
- [x] Variables: `Primitivos` (12, incluindo `vermelho/600`) · `Tokens` (14, incluindo `destaque/erro`) · `Medidas` (10)
- [x] 7 Text Styles (Sniglet + Lexend)
- [x] Fundamentos — Etapa 1: frame **Fundamentos** (1320 × Hug, Auto Layout vertical, fill `bg/app`, gap e padding `espaco/xl`) + título e subtítulo
- [x] Fundamentos — Etapa 2: título **Cores (Tokens)** + frame **Paleta** (Wrap) com as **13 cores**
- [x] Fundamentos — Etapas 3–5: Tipografia (7 linhas), Medidas (Espaço/Raio/Toque mínimo) e conferência — via MCP em 25/11
- [x] Componentes atômicos: `Botão` (18 variantes), `Chip/Tarefa` (2), `Input` (4)
- [x] `Mascote` (Feliz/Focado/Comemorando, imagens finais)

## ⏭️ Etapa 3 — Tipografia (~10 min) ← COMEÇAR AQUI
1. **Bloco:** dentro de *Fundamentos*, abaixo da Paleta, crie um Frame **Tipografia**: **Shift + A**, flow **Vertical**, gap `espaco/md`, sem fill, **Fill × Hug**.
2. **Título:** dentro dele, texto **Tipografia (Text Styles)** — estilo **Título/Seção**, cor `texto/principal`.
3. **Primeira linha:** Frame **Tipo — Display/Saudação**: flow **Horizontal**, gap `espaco/lg`, alinhamento **centro-esquerda**, sem fill, **Fill × Hug**. Dentro:
   - Frame **Rótulo**: flow Vertical, gap 0, **Fixed 320 × Hug**, sem fill, com 2 textos: nome do estilo (**Corpo/Destaque**, `texto/principal`) e descrição (**Legenda/Padrão**, `texto/secundario`).
   - **Exemplo**: texto com o próprio estilo da linha, cor `texto/principal`, **Fill × Hug**.
4. **Duplique** a linha 6 vezes (**Ctrl + D**) e preencha:

| Linha | Nome (Corpo/Destaque) | Descrição (Legenda/Padrão) | Exemplo (com o estilo da linha) |
|---|---|---|---|
| 1 | Display/Saudação | Sniglet Regular · 24 / 120% · só logo e saudação | Oi, Camila |
| 2 | Título/Tela | Lexend SemiBold · 24 / 130% | Foque no seu ritmo |
| 3 | Título/Seção | Lexend Medium · 16 / 140% | Tarefas recentes |
| 4 | Corpo/Padrão | Lexend Regular · 14 / 150% | Sem contagem regressiva. Só você e o seu tempo. |
| 5 | Corpo/Destaque | Lexend SemiBold · 14 / 150% | Retomar |
| 6 | Legenda/Padrão | Lexend Regular · 12 / 140% | última vez: 42 min |
| 7 | Cronômetro/Número | Lexend Medium · 38 / 100% · caixa fixa 180 px | *(ver abaixo)* |

**Linha 7:** no lugar do exemplo, Frame **Caixa fixa 180** — Auto Layout alinhado ao **centro**, **Fixed 180 × Hug**, fill `bg/foco`, raio `raio/card`, padding vertical `espaco/sm`. Dentro, texto **00:16:42**: estilo **Cronômetro/Número**, cor `destaque/progresso`, alinhado ao **centro**, **Fill × Hug**.

## Etapa 4 — Medidas (~10 min)
1. Frame **Medidas** dentro de *Fundamentos*: flow **Horizontal**, gap `espaco/xl`, sem fill, **Fill × Hug**. Dentro, 3 colunas (Frames, flow **Vertical**, gap `espaco/sm`, sem fill, **Hug × Hug**):
2. **Espaço:** texto **Espaço** (Corpo/Destaque) + 5 linhas (Frame horizontal, gap `espaco/sm`, alinhamento centro): retângulo de altura 16, fill `acao/primaria`, largura = valor + texto (Legenda/Padrão, `texto/secundario`):
   `espaco/xs · 4` · `espaco/sm · 8` · `espaco/md · 16` · `espaco/lg · 24` · `espaco/xl · 32`
3. **Raio:** texto **Raio** (Corpo/Destaque) + Frame horizontal (gap `espaco/md`) com 4 caixas 96 × 64, fill `bg/card`, stroke `acao/borda` 1,5 px, raio = variável, e legenda embaixo de cada:
   `raio/chip · 999` · `raio/card · 14` · `raio/botao · 16` · `raio/tela · 24`
4. **Toque mínimo:** texto **Toque mínimo** (Corpo/Destaque) + quadrado 48 × 48 (W e H ligados a `toque/minimo`), fill `destaque/progresso-fundo`, stroke `destaque/progresso`, raio `raio/card` + legenda **toque/minimo · 48 × 48**.

## Etapa 5 — Conferência (~5 min)
- [ ] Nenhum valor solto: toda cor é token, todo texto tem Text Style.
- [ ] Todo Frame que guarda elementos tem Auto Layout; textos **Fill × Hug**, alinhados à esquerda (exceto cronômetro, centro).
- [ ] Nada vazando das caixas; sem Frames vazios ou soltos fora de *Fundamentos*.
- [ ] Ajustar a seção 🎨 Fundamentos para caber o frame (arrastar a borda da seção).
- [ ] Marcar no PROJECT_OVERVIEW.md: "Seção 🎨 Fundamentos montada".

## Depois dos Fundamentos (F3)
Componentes atômicos: `Botão` (variantes), `Chip/Tarefa`, `Input` → compostos → `Mascote` → congelar a Library. Detalhes em `docs/03-design-system.md`.

## 🧠 Dicas que aprendi hoje (Figma à mão)
- **Todo Frame que guarda outros elementos leva Shift + A** logo ao ser criado. Sem isso, "Fill container" não aparece nos filhos.
- **Frame de organização não tem fill** (Paleta, Cor — …, Tipografia, linhas). Só têm cor o *Fundamentos* e as amostras.
- **Estilos e tokens ficam em pastas:** "Legenda/Padrão" = pasta **Legenda** → **Padrão**; `texto/secundario` = **Tokens** → **texto** → **secundario**. Ícone de quatro pontinhos em *Typography* e *Fill*.
- **Token de texto só aparece no fill de texto** (e de fundo só em frame/forma; `acao/borda` só em stroke). Se não aparecer, confira o tipo selecionado no topo do painel.
- **Padding automático do Shift + A** pode fazer elemento vazar: zere o padding quando a caixa tiver tamanho fixo.
- **Duplicar o grupo inteiro** (Frame pai), não só a peça de dentro.
- Para fixar algo selecionado em lote: Ctrl + clique nas camadas e mude uma vez só.

## Prompt para retomar no Claude Code
> Leia CLAUDE.md, PROJECT_OVERVIEW.md e PONTO-DE-RETOMADA.md. Estou na F3, seção 🎨 Fundamentos, Etapa 3 (Tipografia), fazendo à mão no Figma. Me guie uma etapa por vez, esperando eu confirmar.

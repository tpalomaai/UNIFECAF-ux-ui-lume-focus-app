# Figma IDs — Lume (arquivo `z7C1XSWQhlIpYry549Ba3Q`)

> Atualizado em 25/11/2026 via leitura de metadata da página 🧩 Library (Etapa 2 do diagnóstico). IDs de 🔲 Wireframes / 📱 Telas ainda não lidos — só ler quando a F4 começar, e então completar este arquivo em vez de buscar de novo os IDs já aqui.

## Páginas
| Página | ID |
|---|---|
| 🧩 Library | `0:1` |
| 🔲 Wireframes | `2:2` |
| 📱 Telas | `2:3` |

## 🧩 Library → seções
| Seção | ID | Status |
|---|---|---|
| 🎨 Fundamentos | `2:4` | Paleta pronta; tipografia/medidas pendentes |
| 🧩 Componentes | `2:5` | Botão, Chip/Tarefa e Input prontos (1490×1000) |

## 🎨 Fundamentos (completo — Etapas 1 a 5 ✅)
| Elemento | ID |
|---|---|
| Frame `Fundamentos` | `20:4` (padding/gap agora ligados a `espaco/xl`) |
| Frame `Paleta` (13 cores) | `22:12` |
| Frame `Tipografia` | `36:2` |
| Frame `Medidas` | `36:41` |

> As 13 cores individuais têm IDs de `22:13` a `22:145` (ver metadata completa se precisar editar uma cor pontual).

## 🧩 Componentes (criados via MCP em 25/11)
| Componente | ID | Variantes |
|---|---|---|
| `Botão` | `25:47` | Tipo × Estado × Ícone (18) — property `Label` |
| `Chip/Tarefa` | `27:6` | Tipo (2) — properties `Label` e `Legenda` |
| `Input` | `27:15` | Estado (4) — properties `Placeholder` e `Valor` |
| `Mascote` | `28:20` | Humor: Feliz (`28:2`) · Focado (`28:8`) · Comemorando (`28:14`) — fill de imagem (PNG gerado no ChatGPT), sem Auto Layout (ícone) |
| `Card/Tarefa` | `37:8` | Estado: Padrão · Selecionado (2) — properties `Nome`, `ÚltimaVez` |
| `Card/Métrica` | `37:18` | Tipo: Tempo de hoje · Última vez · Lembretes (3) — property de valor exclusiva por tipo |
| `Card/Lembrete` | `37:19` | Sem variantes — property `Texto` |
| `Card/ContinuarDaqui` | `39:10` | Estado: Com conteúdo · Vazio (2) — usa instância de `Botão` (Primário); properties `OndeParei`, `ProximoPasso` |
| `Cronômetro` | `39:19` | Estado: Rodando · Pausado (2) — número em caixa fixa 180px; legenda em `texto/sobre-acao` (corrigido 25/11 — `texto/secundario` tinha baixo contraste sobre `bg/foco`) |
| `Header/Saudação` | `39:20` | Sem variantes — usa instância de `Mascote` (Feliz); properties `Saudação`, `Subtítulo` |
| `Barra/Topo` | `39:30` | Tipo: Com voltar · Sem voltar (2) — largura fixa 390px; property `Título` |

> **Atenção para o próximo lote de componentes:**
> 1. Dar nomes de property DIFERENTES quando o texto padrão deve diferir entre variantes (ex. `Label` vs `Legenda`). Mesmo nome em variantes diferentes funde a property e todas passam a mostrar o mesmo texto padrão.
> 2. `resize()` sempre reseta `primaryAxisSizingMode`/`counterAxisSizingMode` para `FIXED` — só restaurar `AUTO` (hug) **depois** do `resize()`, nunca antes. Dois bugs desta sessão (Card/Tarefa, Card/Métrica com texto cortado; Cronômetro com número deslocado) vieram dessa ordem errada ou de esquecer de setar `counterAxisSizingMode='AUTO'` num frame-wrapper sem `resize()` (o padrão novo do Figma é 100×100 fixo, não hug).
> Token novo criado para o Input Estado=Erro: `destaque/erro` (vermelho/600, #D23C3C) — ver docs/03-design-system.md. Conferir contraste na F5.

## 🔲 Wireframes (intactos, não editar)
| Tela | ID |
|---|---|
| 01 - Boas-vindas | `3:2` |
| 02 - Início | `3:10` |
| 03 - Escolher tarefa | `3:30` |
| 04 - Sessão em andamento | `3:50` |
| 04b - Sessão pausada | `10:8` |
| 05 - Lembrar depois | `3:66` |
| 06 - Sessão concluída | `3:81` |

## 📱 Telas (F4 em andamento)
> Duplicadas dos wireframes em 25/11. Próximo passo: trocar os placeholders restantes por instâncias dos componentes da Library.

| Tela | ID (cópia em Telas) | Status |
|---|---|---|
| 01 - Boas-vindas | `43:3` | ✅ pronta (Mascote/Feliz, Botão) |
| 02 - Início | `43:11` | ✅ pronta (Header/Saudação, Card/ContinuarDaqui, Botão, 2× Card/Tarefa) |
| 03 - Escolher tarefa | `43:31` | ✅ pronta (Barra/Topo, campo+Input, 3× Card/Tarefa, Botão) |
| 04 - Sessão em andamento | `43:53` | ✅ pronta |
| 04b - Sessão pausada | `43:69` | ✅ pronta |
| 05 - Lembrar depois | `43:85` | ✅ pronta (Barra/Topo, Input, 2× Card/Lembrete, Botão) |
| 06 - Sessão concluída | `43:100` | ✅ pronta (Mascote/Comemorando, 3× Card/Métrica, 2 campos, Botão) |

**F4 — construção das 7 telas: concluída ✅ (25/11).**

## 🔗 Interações do protótipo (concluído ✅ 25/11)
Ponto de partida do fluxo: tela **01** (`43:3`), flow "Fluxo principal".

| Origem (nó) | Ação | Destino | Transição |
|---|---|---|---|
| 01 Botão "Começar" (`48:18`) | Navigate | 02 (`43:11`) | Dissolve 300ms |
| 02 Botão "Nova sessão" (`49:35`) | Navigate | 03 (`43:31`) | Dissolve 300ms |
| 02 Botão "Retomar" dentro do Card/ContinuarDaqui (`I49:29;39:6`) | Navigate | 04 (`43:53`) | Dissolve 300ms |
| 03 Botão "Começar" (`50:52`) | Navigate | 04 (`43:53`) | Dissolve 300ms |
| 04 Botão "Pausar" (`44:13`) | Navigate | 04b (`43:69`) | **Smart Animate** 200ms |
| 04b Botão "Continuar" (`44:29`) | Navigate | 04 (`43:53`) | **Smart Animate** 200ms |
| 04 Botão "Lembrar depois" (`44:15`) | Navigate | 05 (`43:85`) | Dissolve 300ms |
| 04b Botão "Lembrar depois" (`44:31`) | Navigate | 05 (`43:85`) | Dissolve 300ms |
| 04 Botão "Concluir" (`44:17`) | Navigate | 06 (`43:100`) | Dissolve 300ms |
| 04b Botão "Concluir" (`44:33`) | Navigate | 06 (`43:100`) | Dissolve 300ms |
| 06 Botão "Salvar e sair" (`51:62`) | Navigate | 02 (`43:11`) | Dissolve 300ms |
| 05 Botão "Guardar e voltar" (`48:29`) | **Back** | (origem: 04 ou 04b) | — |
| 05 Barra/Topo (`48:20`) | **Back** | (origem: 04 ou 04b) | — |
| 03 Barra/Topo (`50:38`) | **Back** | (origem: 02) | — |

> Nota técnica: `node.setReactionsAsync([...])` substitui a API antiga `node.reactions` (read-only). Ação `BACK` não leva `destinationId` — o Figma resolve pra tela de onde a navegação partiu, por isso é melhor que um destino fixo quando uma tela é acessada de mais de um lugar (caso das telas 03 e 05). ID de filho dentro de uma instância usa o formato `I<idDaInstância>;<idOriginalNoComponente>` (ex. `I49:29;39:6`) e funciona normalmente em `getNodeByIdAsync`.

Falta só Paloma testar o fluxo (Present/Preview) e gerar o link público.

> **Correção 25/11:** as 7 telas tinham sido duplicadas mantendo as coordenadas originais dos wireframes, soltas no canvas (nunca filhas de nenhuma *section*) — por isso telas 01/02/03 apareciam em cima da section "📖 Capa". Corrigido: as 7 telas agora são filhas de fato da section "📱 Telas finais" (`2:7`, redimensionada pra 3200×1000), lado a lado com espaçamento de 50px. A section "🗂 Arquivo" (`2:8`, ainda vazia) foi deslocada pra x=4050 pra não sobrepor. Lição: `clone()` + `page.appendChild()` nunca posiciona dentro de uma section — pra isso use `section.appendChild(node)` (preserva a posição visual absoluta automaticamente) e só depois ajuste x/y se quiser reorganizar.

> **Atenção para a próxima etapa (interações):**
> 1. `instance.layoutSizingHorizontal/Vertical = 'FILL'` só pode ser setado **depois** que a instância já foi inserida num frame com Auto Layout (`insertChild`/`appendChild`) — setar antes (instância ainda sem pai) lança erro e o Figma desfaz o script inteiro (nenhuma mutação anterior fica salva). Ordem certa: criar → inserir no pai → setar sizing.
> 2. **`Card/Métrica` expõe as 3 properties de valor (`ValorTempodehoje`, `ValorÚltimavez`, `ValorLembretes`) em TODAS as variantes**, não uma exclusiva por tipo como o texto antigo deste arquivo sugeria — cada variante só *exibe* a sua, mas as três existem no `componentProperties` de qualquer instância. Pegar "a primeira property de texto encontrada" é um bug (causou a tela 06 mostrar "47 min" em vez de "45 min" no Card "Tempo de hoje"). Sempre setar pelo nome exato que corresponde ao tipo da variante.

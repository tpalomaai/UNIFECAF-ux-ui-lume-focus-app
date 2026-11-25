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
> Duplicadas dos wireframes em 25/11 — ainda em cinza, placeholders. Próximo passo: trocar por instâncias dos componentes da Library, trocar frames "Espaço" por Auto Layout real, interações, link público.

| Tela | ID (cópia em Telas) |
|---|---|
| 01 - Boas-vindas | `43:3` |
| 02 - Início | `43:11` |
| 03 - Escolher tarefa | `43:31` |
| 04 - Sessão em andamento | `43:53` |
| 04b - Sessão pausada | `43:69` |
| 05 - Lembrar depois | `43:85` |
| 06 - Sessão concluída | `43:100` |

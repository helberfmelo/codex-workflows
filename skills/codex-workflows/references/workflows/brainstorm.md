---
description: Codex-native ideation workflow for evaluating multiple approaches before implementation.
---

# /brainstorm - Codex-Native Option Design

$ARGUMENTS

---

## Objective

Explore solution options before writing code.

Use this workflow when:

- requirements are open-ended;
- architecture direction is still undecided;
- tradeoffs need explicit comparison.

Do not implement code during `/brainstorm`.

---

## Discovery Inputs

Capture:

1. user outcome;
2. primary constraints (stack, time, compliance);
3. success criteria;
4. known unknowns.

If key inputs are missing, ask up to 3 focused questions.

---

## Option Generation Rules

Generate at least 3 materially different options.

Each option must include:

- approach summary;
- technical path;
- impact on delivery speed;
- risk profile (`low|medium|high`).

Avoid cosmetic variants of the same design.

---

## Comparison Protocol

Score each option across:

1. implementation complexity;
2. operational risk;
3. maintainability;
4. time-to-value.

Use a simple 1-5 score scale and explain one key tradeoff per option.

---

## Recommendation Gate

Return one recommended option and one fallback option.

Recommendation must state:

- why it wins under current constraints;
- what would make fallback preferable.

End by asking the user to confirm direction before moving to `/plan` or `/create`.

---

## Output Contract

```markdown
## Brainstorm Report

### Problem Frame
[short context and desired outcome]

### Options
| Option | Summary | Complexity (1-5) | Risk | Time-to-Value |
| --- | --- | --- | --- | --- |
| A | ... | ... | ... | ... |
| B | ... | ... | ... | ... |
| C | ... | ... | ... | ... |

### Tradeoff Notes
- Option A: ...
- Option B: ...
- Option C: ...

### Recommendation
- Primary: [option]
- Fallback: [option]
- Reason: ...

### Decision Prompt
[ask user to choose]
```

---

## Quality Bar

Before closing, confirm:

- minimum 3 distinct options;
- explicit scoring table;
- recommendation tied to constraints;
- no implementation output.


# Pourquoi Utiliser `cw` avec GPT Codex + VS Code

Oui, c'est courant pour un site de documentation GitHub professionnel.

Un portail de documentation doit expliquer :

- quel probleme le projet resout ;
- quelle valeur concrete il apporte ;
- dans quels cas il n'est pas necessaire.

Cette page couvre ces points sans metriques artificielles.

## Probleme que `cw` Resout

Sans modele operationnel, l'usage de Codex dans des projets plus larges provoque souvent :

- des prompts incoherents selon les contributeurs ;
- une transition faible entre planification, implementation et validation ;
- des etapes de release/gouvernance sautees sous pression ;
- du setup repete d'un depot a l'autre.

## Ce que `cw` Apporte

`cw` ajoute un modele d'execution reproductible :

- activation explicite du workflow (`cw /orchestrate`, `cw /debug`, etc.) ;
- contrats codex-native pour le comportement des workflows ;
- packs de validation par domaine et stack (Node, Python, Rust) ;
- automatisation CI/release alignee avec l'operation reelle ;
- documentation multilanguage et playbooks operationnels.

## Comparatif : Avec et Sans `cw`

| Dimension | Sans `cw` | Avec `cw` |
| --- | --- | --- |
| Demarrage de tache | Style de prompt variable | Trigger workflow explicite + objectif |
| Travail multi-domaine | Coordination ad hoc | `/orchestrate` avec phases structurees |
| Discipline de validation | Checks facilement oublies | Routines de validation + gates CI |
| Hygiene de release | Manuel et fragile | Flux automatise tag/changelog/release |
| Onboarding | Connaissance dispersee dans les chats | Docs, exemples et commandes centralises |
| Reproductibilite | Depend de la memoire individuelle | Conventions et checks de depot |

## Quand `cw` n'est pas Necessaire

Pour des taches tres petites et ponctuelles, des prompts directs peuvent suffire.

`cw` devient utile quand vous avez besoin de :

- coherence entre contributeurs ;
- gates de qualite auditables ;
- operation et release a l'echelle.

## Recommandation Pratique

Utiliser un modele mixte :

1. Taches simples : prompt direct.
2. Travail produit : workflows `cw` + validations.
3. Cycles de release : checks automatises et pipeline.

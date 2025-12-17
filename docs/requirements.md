---
title: "Requisiti di Git Alias CLI"
description: "Specifiche dei requisiti software"
date: "2025-12-15"
author: "Francesco Rolando"
scope:
  paths:
    - "**/*.py"
  excludes:
    - ".*/**"
visibility: "bozza"
tags: ["markdown", "requisiti", "git-alias"]
---

# Requisiti di Git Alias CLI
**Versione**: 0.15
**Autore**: Francesco Rolando  
**Data**: 2025-12-15

## Indice
- [Requisiti di Git Alias CLI](#requisiti-di-git-alias-cli)
  - [Indice](#indice)
  - [Cronologia Revisioni](#cronologia-revisioni)
  - [1. Introduzione](#1-introduzione)
    - [1.1 Regole del Documento](#11-regole-del-documento)
    - [1.2 Ambito del Progetto](#12-ambito-del-progetto)
  - [2. Requisiti di Progetto](#2-requisiti-di-progetto)
    - [2.1 Funzioni di Progetto](#21-funzioni-di-progetto)
    - [2.2 Vincoli di Progetto](#22-vincoli-di-progetto)
    - [2.3 Componenti e Librerie](#23-componenti-e-librerie)
  - [3. Requisiti](#3-requisiti)
    - [3.1 Progettazione e Implementazione](#31-progettazione-e-implementazione)
    - [3.2 Funzioni](#32-funzioni)

## Cronologia Revisioni
| Data | Versione | Motivo e descrizione della modifica |
|------|----------|--------------------------------------|
| 2025-12-15 | 0.1 | Prima bozza automatizzata dei requisiti |
| 2025-12-15 | 0.2 | Configurazione dei branch tramite `.g.conf` e flag `--write-config` |
| 2025-12-15 | 0.3 | Aggiunta configurazione dell'editor via `.g.conf` e default `edit` |
| 2025-12-15 | 0.4 | Ordinamento output help con sezioni per funzioni di gestione |
| 2025-12-15 | 0.5 | Rimozione dell'alias `ver` e degli obblighi associati |
| 2025-12-15 | 0.6 | Reintroduzione dell'alias `ver` con ricerca delle versioni configurabile |
| 2025-12-15 | 0.7 | Configurazione del comando `ver` tramite coppie wildcard/regexp abbinate |
| 2025-12-15 | 0.8 | Introduzione del comando `changelog` per generare CHANGELOG.md |
| 2025-12-15 | 0.9 | Rimozione degli alias `mkrepo`, `mkyday`, `mktday`, `mkcma`, `mkmas`, `mkdev` |
| 2025-12-15 | 0.10 | Rimozione degli alias `cmarelease`, `release`, `cowrk`, `codev`, `comas`, `mkwrk` |
| 2025-12-15 | 0.11 | Ridenominazione dell'alias `brall` in `lsbr` |
| 2025-12-15 | 0.12 | Rimozione degli alias specifici per i branch `develop`/`master` (`fedev`, `femas`, `medev`, `mewrk`, `pldev`, `plmas`, `pudev`, `pumas`) |
| 2025-12-15 | 0.13 | Aggiornamento delle categorie del comando `changelog` (tipi `new`/`change`, rimozione `perf`/`test`/`build`/`ci`/`chore`, sezione \"Miscellaneous Tasks\" limitata a `misc`) |
| 2025-12-15 | 0.14 | Rimozione degli alias `hl`/`hlrs` e integrazione dell'help dei reset direttamente nei comandi `rs*` |
| 2025-12-15 | 0.15 | Rimozione degli alias `tree`, `lg1`, `lg2`, `lg3`, `cma`, `rmwrk`, `edbrc`, `edbsh`, `edcfg`, `edgit`, `edign`, `edpro` |

## 1. Introduzione
Questo documento descrive i requisiti del progetto Git Alias, un pacchetto CLI che riproduce alias git personalizzati e li espone tramite `git-alias`/`g` e `uvx`. I requisiti sono organizzati per funzioni di progetto, vincoli e requisiti funzionali verificabili.

### 1.1 Regole del Documento
Questo documento deve sempre seguire queste regole:
- Questo documento è scritto in italiano
- Ogni identificativo di requisito (ad esempio **PRJ-001**, **CTN-001**, **DES-001**, **REQ-001**) deve essere univoco.
- Ogni identificativo deve iniziare con il prefisso che identifica il gruppo di appartenenza:
  * I requisiti di funzione di progetto iniziano con **PRJ-**
  * I requisiti di vincolo di progetto iniziano con **CTN-**
  * I requisiti per componenti e librerie **CPT-**
  * I requisiti di progettazione e implementazione iniziano con **DES-**
  * I requisiti funzionali iniziano con **REQ-**
- Ogni requisito deve essere identificabile, verificabile e testabile.
- A ogni modifica del documento si deve aggiornare il numero di versione e aggiungere una nuova riga alla cronologia revisioni.

### 1.2 Ambito del Progetto
Il progetto fornisce un eseguibile CLI per riprodurre alias git definiti in un file di configurazione personalizzato, permettendone l'uso locale o tramite `uvx` senza dover installare manualmente gli alias nel profilo git dell'utente.

## 2. Requisiti di Progetto
### 2.1 Funzioni di Progetto
- **PRJ-001**: Il sistema deve esporre i comandi `git-alias` e `g` che instradano le chiamate verso gli alias implementati nel modulo `core.py`, eseguendoli nel repository git corrente.
- **PRJ-002**: Il sistema deve fornire un sistema di help integrato che elenca tutti gli alias disponibili e ne mostra la descrizione in inglese su richiesta.
- **PRJ-003**: Il sistema deve supportare l'aggiornamento e la rimozione dell'installazione tramite comandi dedicati integrati nel CLI (--upgrade, --remove).

### 2.2 Vincoli di Progetto
- **CTN-001**: Il pacchetto deve richiedere Python 3.11 o superiore come ambiente di runtime.
- **CTN-002**: Il sistema deve dipendere dalla disponibilità del comando `git` (e degli strumenti correlati `gitk` e `uv`) nel `PATH`, poiché tutte le operazioni invocano processi git esterni.
- **CTN-003**: I comandi di modifica file devono disporre di un editor invocabile dal CLI, configurato tramite il parametro `editor` del file `.g.conf` e impostato di default sul comando `edit` (alias shell disponibile nel `PATH`).

### 2.3 Componenti e Librerie
- **CPT-001**:Modulo `core.py` con dispatcher CLI e implementazione degli alias.
- **CPT-002**:Script di lancio `core.py` e entrypoint console `git-alias`/`g`.
- **CPT-003**:Suite di test `tests/test_alias_help.py` che verifica coerenza degli help.
- **CPT-004**:Librerie standard Python: `os`, `shlex`, `subprocess`, `sys`, `datetime`, `pathlib`.
- **CPT-005**:Dipendenze esterne: eseguibili `git`, `gitk`, `uv`/`uvx`, editor `cudatext`.

## 3. Requisiti
### 3.1 Progettazione e Implementazione
- **DES-001**: Il dispatcher CLI deve rifiutare comandi non mappati, mostrare l'elenco degli alias e terminare con errore quando un comando non è riconosciuto.
- **DES-002**: Ogni alias deve inoltrare eventuali argomenti aggiuntivi al comando git corrispondente, propagando il codice di uscita del processo esterno. 
- **DES-003**: Ogni comando deve avere un testo di help e il comando globale `--help` deve elencarli in ordine alfabetico.
- **DES-004**: Se l'eseguibile viene chiamato senza argomenti deve stampare un messaggio, mostrare l'help completo e uscire con codice di errore.
- **DES-005**: Gli alias costituiscono la base per lo sviluppo di alias più complessi, pertanto se nell'implementazione di un alias è necessario svolgere una attività implementata in un alias più semplice verrà utilizzata la funzione che specializza quella più semplice.
- **DES-006**: L'eseguibile deve leggere ad ogni invocazione il file `.g.conf` presente alla root del repository git e usare le configurazioni dei branch `master`, `develop`, `work` e del comando `editor` lì definite, ripiegando sui valori di default (`master`, `develop`, `work`, `edit`) se il file è assente o incompleto.

### 3.2 Funzioni
- **REQ-001**: Il comando `--upgrade` deve reinstallare l'utility usando `uv tool install git-alias --force --from git+https://github.com/Ogekuri/G.git`.
- **REQ-002**: Il comando `--remove` deve disinstallare l'utility globale tramite `uv tool uninstall git-alias`.
- **REQ-003**: Il comando `--help` deve elencare tutti gli alias disponibili o mostrare la descrizione del comando richiesto quando viene specificato un alias.
- **REQ-004**: L'alias `aa` deve aggiungere tutte le modifiche e i file nuovi all'area di staging con `git add --all`.
- **REQ-005**: L'alias di commit `cm` deve permettere commit standard senza automatismi aggiuntivi né messaggi precompilati.
- **REQ-006**: Gli alias di navigazione branch devono consentire checkout mirati (`co`) utilizzando i nomi di branch configurati nel file `.g.conf` (default `work`, `develop`, `master`).
- **REQ-007**: Gli alias di fetch/pull/push devono eseguire le varianti generiche per il ramo corrente (`fe`, `feall`, `pl`, `pt`, `pu`), senza scorciatoie dedicate ai rami configurati.
- **REQ-008**: Gli alias di ispezione devono fornire viste su branch, log e stato (`br`, `lsbr`, `ck`, `lg`, `ll`, `lm`, `lh`, `lt`, `ver`, `gp`, `gr`, `de`, `rf`, `st`).
- **REQ-009**: Gli alias di merge devono offrire merge fast-forward generici (`me`) per integrare i rami configurati senza workflow automatizzati aggiuntivi.
- **REQ-010**: Il sistema non deve fornire alias di rilascio automatico; le operazioni di promozione tra branch e tagging vanno eseguite manualmente con i comandi git standard.
- **REQ-011**: Gli alias di reset e pulizia devono applicare le modalità di reset (`rs`, `rssft`, `rsmix`, `rshrd`, `rsmrg`, `rskep`, `unstg`) e le pulizie dello working tree (`rmloc`, `rmstg`, `rmunt`). I comandi di reset (`rs*`) devono stampare il testo di help dedicato quando invocati con `--help`, senza dipendere da alias separati.
- **REQ-012**: Gli alias di tagging e archiviazione devono gestire la creazione di tag annotati (`tg`), la rimozione locale/remota (`rmtg`), la visualizzazione (`lt`) e l'archiviazione del ramo `master` in tar.gz (`ar`).
- **REQ-013**: L'alias `ed` deve consentire l'apertura di file arbitrari usando il comando definito dal parametro `editor` nel file `.g.conf` (default `edit`), segnalando errore se non viene passato alcun percorso.
- **REQ-014**: Il comando `--write-config` deve generare nella root del repository git il file `.g.conf` contenente i nomi di default dei branch `master`, `develop`, `work`, il comando `editor=edit` e la lista di coppie abbinate `(<wildcard>, <regexp>)` usate dal comando `ver`, così che l'utente possa personalizzarle manualmente.
- **REQ-015**: All'avvio della CLI il valore del parametro `editor` definito in `.g.conf` deve essere caricato e utilizzato per tutte le operazioni di editing, adottando `edit` quando il parametro manca o è vuoto.
- **REQ-016**: L'invocazione della CLI con `--help` o senza comandi deve mostrare prima le funzioni `--write-config`, `--upgrade`, `--remove` e poi l'elenco completo degli alias disponibili.
- **REQ-017**: Il comando `ver` deve leggere la lista di coppie `(<wildcard>, <regexp>)` dal file `.g.conf` (o usare i valori di default), applicare ogni regexp solo ai file che corrispondono alla wildcard associata, raccogliere tutte le versioni trovate e: (a) stampare la versione quando tutte le occorrenze coincidono, oppure (b) terminare con errore indicando i primi due file che presentano versioni differenti.
- **REQ-018**: Il comando `changelog` deve replicare la logica dello script `mkchangelog.py`, generare sempre il file `CHANGELOG.md` dal repository corrente usando le descrizioni dei commit, supportare l'opzione `--include-unreleased`, stampare il contenuto quando si usa `--print-only` e scrivere su disco solo se il file non esiste o quando viene specificato `--force-write`. Il parser deve riconoscere i nuovi tipi `new` (Features) e `change` (Refactor/Changes), ignorare i vecchi tipi `perf`, `test`, `build`, `ci`, `chore`, e includere la sezione \"Miscellaneous Tasks\" esclusivamente per il tipo `misc`, senza generare la sezione \"Other\".

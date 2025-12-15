---
title: "Requisiti di Git Alias Emulator"
description: "Specifiche dei requisiti software"
date: "2025-12-15"
author: "Francesco Rolando"
scope:
  paths:
    - "**/*.py"
    - "**/*.ipynb"
    - "**/*.c"
    - "**/*.h"
    - "**/*.cpp"
  excludes:
    - ".*/**"
visibility: "bozza"
tags: ["markdown", "requisiti", "git-alias"]
---

# Requisiti di Git Alias Emulator
**Versione**: 0.3
**Autore**: Francesco Rolando  
**Data**: 2025-12-15

## Indice
- [Requisiti di Git Alias Emulator](#requisiti-di-git-alias-emulator)
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
- **REQ-005**: Gli alias di commit devono permettere commit standard (`cm`, `cma`) e commit automatizzati con messaggi precompilati (`mkcma`, `mkyday`, `mktday`) che eseguono anche il workflow di integrazione `mkdev`.
- **REQ-006**: Gli alias di navigazione branch devono consentire checkout mirati (`co`) e scorciatoie dedicate a rami predefiniti (`cowrk`, `codev`, `comas`) oltre alla creazione e rimozione del ramo `work` (`mkwrk`, `rmwrk`), utilizzando i nomi di branch configurati nel file `.g.conf` (default `work`, `develop`, `master`).
- **REQ-007**: Gli alias di fetch/pull/push devono eseguire le varianti per il ramo corrente e per i rami `develop` e `master` (`fe`, `feall`, `fedev`, `femas`, `pl`, `pldev`, `plmas`, `pt`, `pu`, `pudev`, `pumas`).
- **REQ-008**: Gli alias di ispezione devono fornire viste su branch, log e stato (`br`, `brall`, `ck`, `lg`, `lg1`, `lg2`, `lg3`, `ll`, `lm`, `lh`, `lt`, `ver`, `tree`, `gp`, `gr`, `de`, `rf`, `st`).
- **REQ-009**: Gli alias di merge e promozione devono offrire merge fast-forward (`me`, `medev`, `mewrk`) e i workflow automatizzati `mkdev` e `mkmas` per integrare `work` su `develop` con pull e push coordinati.
- **REQ-010**: Gli alias di rilascio devono orchestrare la promozione da `work` verso `develop` e `master`, applicando tag annotati e pushando il tag remoto (`release`, `cmarelease`).
- **REQ-011**: Gli alias di reset e pulizia devono applicare le modalità di reset (`rs`, `rssft`, `rsmix`, `rshrd`, `rsmrg`, `rskep`, `unstg`) e le pulizie dello working tree (`rmloc`, `rmstg`, `rmunt`) con help dedicato (`hlrs`).
- **REQ-012**: Gli alias di tagging e archiviazione devono gestire la creazione di tag annotati (`tg`), la rimozione locale/remota (`rmtg`), la visualizzazione (`lt`, `ver`) e l'archiviazione del ramo `master` in tar.gz (`ar`).
- **REQ-013**: L'alias `mkrepo` deve creare un nuovo repository remoto clonandolo, inizializzandolo, configurando `.gitignore` di esempio e pushando i branch `master` e `develop`.
- **REQ-014**: Gli alias di modifica file (`conf`, `ed`, `edcfg`, `edign`, `edpro`, `edbsh`, `edbrc`) devono aprire i rispettivi file di configurazione usando il comando definito dal parametro `editor` nel file `.g.conf` (default `edit`), segnalando errore se non viene passato alcun percorso quando richiesto.
- **REQ-015**: Il comando `--write-config` deve generare nella root del repository git il file `.g.conf` contenente i nomi di default dei branch `master`, `develop`, `work` e il comando `editor=edit`, in modo che l'utente possa personalizzarli manualmente.
- **REQ-016**: All'avvio della CLI il valore del parametro `editor` definito in `.g.conf` deve essere caricato e utilizzato per tutte le operazioni di editing, adottando `edit` quando il parametro manca o è vuoto.

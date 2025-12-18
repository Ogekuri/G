---
title: "Requisiti di Git Alias CLI"
description: "Specifiche dei requisiti software"
date: "2025-12-17"
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
**Versione**: 0.35
**Autore**: Francesco Rolando  
**Data**: 2025-12-17

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
| 2025-12-15 | 0.16 | Aggiunta dell'alias `bd` per la cancellazione di un branch locale |
| 2025-12-15 | 0.17 | Ridenominazione dell'alias `lsbr` in `lb` e riordino alfabetico dei comandi `l*` |
| 2025-12-15 | 0.18 | Aggiunta delle funzioni diagnostiche sullo stato del repository e nuova validazione per l'alias `aa` |
| 2025-12-17 | 0.19 | Validazione preventiva del comando `cm` sugli stati work/index |
| 2025-12-17 | 0.20 | Aggiornamento remoto prima delle verifiche di pull e conferma controlli per `aa` |
| 2025-12-17 | 0.21 | Introduzione dell'alias `wip` con messaggio predefinito e verifiche condivise con `cm` |
| 2025-12-17 | 0.22 | Nuove verifiche WIP/amend condivise tra `cm` e `wip` |
| 2025-12-17 | 0.23 | Aggiornamento messaggio WIP fisso senza timestamp e controlli correlati |
| 2025-12-17 | 0.24 | Ordinamento cronologico rivisto per le sezioni del comando `changelog` |
| 2025-12-17 | 0.25 | Nuovi alias convenzionali per commit compatibili con il changelog |
| 2025-12-17 | 0.26 | Testi di output della CLI tradotti in inglese |
| 2025-12-17 | 0.27 | Commenti descrittivi per tutte le funzioni di core.py |
| 2025-12-17 | 0.28 | Fallback ai comandi git nativi quando un alias sconosciuto viene richiesto |
| 2025-12-17 | 0.29 | Gestione centralizzata delle eccezioni dei processi esterni e propagazione controllata degli errori |
| 2025-12-17 | 0.30 | Messaggi CLI obbligatoriamente in inglese con spiegazione delle operazioni di commit relative ad amend |
| 2025-12-17 | 0.31 | Struttura completa dell'help globale con usage, comandi di gestione, configurazione attiva e alias |
| 2025-12-17 | 0.32 | Introduzione del comando `chver` per aggiornare o ripristinare la versione del progetto |
| 2025-12-17 | 0.33 | Nuovi comandi `major`/`minor`/`patch` per automatizzare il rilascio incrementale delle versioni |
| 2025-12-17 | 0.34 | Miglioramenti ai comandi `major`/`minor`/`patch` con logging degli step e push automatici dei branch `develop` e `master` |
| 2025-12-17 | 0.35 | Introduzione del comando `release` come commit regolamentato usato dai workflow `major`/`minor`/`patch` |
| 2025-12-17 | 0.35 | Introduzione del comando `release` come commit regolamentato usato dai workflow `major`/`minor`/`patch` |

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
- **DES-001**: Il dispatcher CLI deve accettare un comando come primo argomento, invocare l'alias corrispondente quando il nome è mappato e, quando il comando richiesto non è riconosciuto, eseguire `git` inoltrando tutti gli argomenti originali senza interrompere il flusso, mantenendo invariato il comportamento di help/errore quando non vengono forniti argomenti o viene richiesto `--help`.
- **DES-002**: Ogni alias deve inoltrare eventuali argomenti aggiuntivi al comando git corrispondente, propagando il codice di uscita del processo esterno e gestendo ogni errore dei processi esterni catturando le eccezioni (ad esempio `subprocess.CalledProcessError`) tramite un wrapper condiviso che converte l'errore in una segnalazione esplicita stampata dall'alias chiamante senza mostrare trace Python grezzi. 
- **DES-008**: Tutti i messaggi stampati dalla CLI (stdout/stderr) devono essere in inglese e le operazioni di commit devono spiegare esplicitamente quando viene eseguito un `--amend` o quando viene creata una nuova commit, indicando il motivo della scelta.
- **DES-009**: L'output del comando globale `--help` deve essere strutturato nel seguente ordine: (a) una riga di usage che mostra la sintassi generale del comando; (b) una sezione \"Management Commands\" con l'elenco delle opzioni di gestione ricavate da `MANAGEMENT_HELP`; (c) una sezione \"Configuration Parameters\" che stampa i valori correnti dei parametri letti da `.g.conf` (o, se non presenti, i default di `DEFAULT_CONFIG`); (d) una sezione \"Commands\" che elenca gli help di tutti gli alias disponibili in ordine alfabetico.
- **DES-003**: Ogni comando deve avere un testo di help e il comando globale `--help` deve elencarli in ordine alfabetico.
- **DES-004**: Se l'eseguibile viene chiamato senza argomenti deve stampare un messaggio, mostrare l'help completo e uscire con codice di errore.
- **DES-005**: Gli alias costituiscono la base per lo sviluppo di alias più complessi, pertanto se nell'implementazione di un alias è necessario svolgere una attività implementata in un alias più semplice verrà utilizzata la funzione che specializza quella più semplice.
- **DES-007**: Le verifiche sul readiness del commit (worktree, staging, commit precedente) devono essere centralizzate in funzioni riutilizzabili da tutti gli alias che eseguono commit (`cm`, `wip`, e futuri).
- **DES-006**: L'eseguibile deve leggere ad ogni invocazione il file `.g.conf` presente alla root del repository git e usare le configurazioni dei branch `master`, `develop`, `work` e del comando `editor` lì definite, ripiegando sui valori di default (`master`, `develop`, `work`, `edit`) se il file è assente o incompleto.

### 3.2 Funzioni
- **REQ-001**: Il comando `--upgrade` deve reinstallare l'utility usando `uv tool install git-alias --force --from git+https://github.com/Ogekuri/G.git`.
- **REQ-002**: Il comando `--remove` deve disinstallare l'utility globale tramite `uv tool uninstall git-alias`.
- **REQ-003**: Il comando `--help` deve elencare tutti gli alias disponibili o mostrare la descrizione del comando richiesto quando viene specificato un alias.
- **REQ-004**: L'alias `aa` deve aggiungere tutte le modifiche e i file nuovi all'area di staging con `git add --all`, ma prima deve verificare (riutilizzando le funzioni diagnostiche sullo working tree) che esistano file o modifiche non ancora aggiunti allo staging e, quando non c'è nulla da aggiungere, deve terminare con errore descrivendo il problema.
- **REQ-005**: L'alias di commit `cm` deve permettere commit standard senza automatismi aggiuntivi né messaggi precompilati, ma prima di eseguire `git commit` deve verificare (riutilizzando funzioni diagnostiche centralizzate) che (a) non esistano file o modifiche nello working tree ancora da aggiungere all'index/stage, (b) l'index contenga effettivamente modifiche pronte al commit, e (c) l'ultimo commit del branch corrente non sia una WIP irrisolta. Se l'ultimo commit ha il messaggio `wip: work in progress.` e non è stato ancora portato sul ramo `develop` configurato, `cm` deve aggiornare quel commit tramite `git commit --amend` e stampare un messaggio esplicito; in tutti gli altri casi deve creare un nuovo commit e segnalare l'azione eseguita.
- **REQ-006**: Gli alias di navigazione branch devono consentire checkout mirati (`co`) utilizzando i nomi di branch configurati nel file `.g.conf` (default `work`, `develop`, `master`).
- **REQ-007**: Gli alias di fetch/pull/push devono eseguire le varianti generiche per il ramo corrente (`fe`, `feall`, `pl`, `pt`, `pu`), senza scorciatoie dedicate ai rami configurati.
- **REQ-008**: Gli alias di ispezione devono fornire viste su branch, log e stato (`br`, `lb`, `ck`, `lg`, `ll`, `lm`, `lh`, `lt`, `ver`, `gp`, `gr`, `de`, `rf`, `st`).
- **REQ-009**: Gli alias di merge devono offrire merge fast-forward generici (`me`) per integrare i rami configurati senza workflow automatizzati aggiuntivi.
- **REQ-010**: Il sistema deve limitare i workflow di rilascio agli alias dedicati documentati (attualmente `major`, `minor`, `patch`) e non deve introdurre ulteriori scorciatoie automatiche oltre a quelli descritti.
- **REQ-011**: Gli alias di reset e pulizia devono applicare le modalità di reset (`rs`, `rssft`, `rsmix`, `rshrd`, `rsmrg`, `rskep`, `unstg`) e le pulizie dello working tree (`rmloc`, `rmstg`, `rmunt`). I comandi di reset (`rs*`) devono stampare il testo di help dedicato quando invocati con `--help`, senza dipendere da alias separati.
- **REQ-012**: Gli alias di tagging e archiviazione devono gestire la creazione di tag annotati (`tg`), la rimozione locale/remota (`rmtg`), la visualizzazione (`lt`) e l'archiviazione del ramo `master` in tar.gz (`ar`).
- **REQ-013**: L'alias `ed` deve consentire l'apertura di file arbitrari usando il comando definito dal parametro `editor` nel file `.g.conf` (default `edit`), segnalando errore se non viene passato alcun percorso.
- **REQ-014**: Il comando `--write-config` deve generare nella root del repository git il file `.g.conf` contenente i nomi di default dei branch `master`, `develop`, `work`, il comando `editor=edit` e la lista di coppie abbinate `(<wildcard>, <regexp>)` usate dal comando `ver`, così che l'utente possa personalizzarle manualmente.
- **REQ-015**: All'avvio della CLI il valore del parametro `editor` definito in `.g.conf` deve essere caricato e utilizzato per tutte le operazioni di editing, adottando `edit` quando il parametro manca o è vuoto.
- **REQ-016**: L'invocazione della CLI con `--help` o senza comandi deve mostrare prima le funzioni `--write-config`, `--upgrade`, `--remove` e poi l'elenco completo degli alias disponibili.
- **REQ-017**: Il comando `ver` deve leggere la lista di coppie `(<wildcard>, <regexp>)` dal file `.g.conf` (o usare i valori di default), applicare ogni regexp solo ai file che corrispondono alla wildcard associata, raccogliere tutte le versioni trovate e: (a) stampare la versione quando tutte le occorrenze coincidono, oppure (b) terminare con errore indicando i primi due file che presentano versioni differenti.
- **REQ-018**: Il comando `changelog` genera il file `CHANGELOG.md` dal repository corrente usando le descrizioni dei commit, supportare l'opzione `--include-unreleased`, stampare il contenuto quando si usa `--print-only` e scrivere su disco solo se il file non esiste o quando viene specificato `--force-write`. Il parser deve riconoscere i nuovi tipi `new` (Features) e `change` (Refactor/Changes), ignorare i vecchi tipi `perf`, `test`, `build`, `ci`, `chore`, e includere la sezione \"Miscellaneous Tasks\" esclusivamente per il tipo `misc`, senza generare la sezione \"Other\". La sezione \"# Changelog\" deve elencare i rilasci in ordine cronologico inverso (il più recente in alto), mentre la sezione \"# History\" deve restare in ordine cronologico (la voce più recente in fondo).
- **REQ-019**: L'alias `bd` deve eliminare un branch locale specificato dall'utente utilizzando `git branch -d <branch>`.
- **REQ-020**: Il sistema deve fornire funzioni di supporto riutilizzabili dagli alias che consentano di verificare (a) la presenza di file o modifiche non ancora aggiunti allo staging, (b) la presenza di file già in staging ma non ancora committati, (c) la disponibilità di aggiornamenti remoti per il branch `develop`, e (d) la disponibilità di aggiornamenti remoti per il branch `master`. Le funzioni per i punti (c) e (d) devono prima sincronizzare i riferimenti remoti (ad esempio con `git remote -v update`) e poi determinare se il branch remoto è in avanti rispetto a quello locale.
- **REQ-021**: L'alias `wip` deve eseguire un commit "work in progress" riutilizzando le stesse funzioni di verifica dell'alias `cm`, generando automaticamente un messaggio fisso `wip: work in progress.` e, come `cm`, deve rilevare se l'ultimo commit è una WIP non ancora presente su `develop`: in tal caso deve aggiornare il commit esistente con `git commit --amend` e stampare l'azione; altrimenti deve creare un nuovo commit e segnalarlo.
- **REQ-022**: Gli alias `new`, `fix`, `change`, `docs`, `style`, `revert` e `misc` devono eseguire commit convenzionali compatibili con il comando `changelog`, utilizzando messaggi nel formato `<tipo>(<modulo>): <descrizione>`. Ogni comando deve riutilizzare gli stessi controlli di readiness di `cm`/`wip`, accettare il testo del commit come argomento obbligatorio e consentire di specificare il modulo anticipando il testo con `nome_modulo: descrizione`. Quando il modulo non viene indicato, deve essere applicato un valore di default configurabile tramite `.g.conf` (default `core`).
- **REQ-023**: Tutti i messaggi stampati da `core.py` (su stdout, stderr, in modalità normale, verbose o debug) devono essere in lingua inglese, inclusi gli help dei comandi e le diagnostiche degli alias.
- **REQ-024**: Ogni funzione definita in `core.py` deve essere preceduta da un breve commento descrittivo in italiano che inizi con il carattere `#`, e tutti i commenti presenti nel file devono seguire lo stesso formato e lingua.
- **REQ-025**: Il comando `chver` deve accettare esattamente un argomento nel formato `major.minor.patch` (tre interi separati da punti), verificare la versione corrente tramite `ver`, terminare con errore se `ver` non restituisce una versione univoca o se l'argomento non è valido, evitare modifiche quando la versione richiesta coincide con quella corrente, determinare se l'operazione è un upgrade o un downgrade confrontando `major`, `minor` e `patch`, riscrivere tutte le occorrenze che corrispondono alle regole `ver_rules` attive (quelle lette da `.g.conf` o, in mancanza, `DEFAULT_CONFIG`), e al termine rieseguire `ver` per confermare la nuova versione stampando un messaggio di successo esplicito (upgrade o downgrade). Se la riesecuzione di `ver` non conferma la versione impostata, `chver` deve segnalare un errore critico.
- **REQ-026**: I comandi `major`, `minor` e `patch` devono automatizzare il rilascio di una nuova versione incrementando rispettivamente il numero `major`, `minor` o `patch` (azzerando gli indici meno significativi) e condividere la stessa implementazione di supporto. Prima dell'esecuzione devono verificare che (a) i branch configurati `master`, `develop`, `work` esistano localmente; (b) i remote `origin/master` e `origin/develop` esistano; (c) non ci siano aggiornamenti remoti pendenti per `master` e `develop`; (d) il branch corrente sia `work`; (e) la working area sia pulita; (f) l'index sia vuoto. Ogni step deve stampare un messaggio di progresso quando va a buon fine e segnalare con un messaggio esplicito l'eventuale fallimento dello step corrente. Superati i controlli devono: determinare la versione corrente tramite `ver`; calcolare la nuova versione applicando la regola del comando richiesto; aggiornare i file tramite `chver`; aggiungere tutte le modifiche allo stage; creare il commit di rilascio con l'alias `release`; creare un tag annotato `v<ver>` con descrizione `release version: <ver>`; rigenerare `CHANGELOG.md` con `changelog --force-write`; aggiungere il changelog allo stage; aggiornare l'ultima commit con `git commit --amend`; eseguire merge fast-forward da `work` verso `develop`, effettuare il push del branch `develop` su `origin`, eseguire merge fast-forward da `develop` verso `master`, effettuare il push del branch `master` su `origin`; tornare sul branch `work`; mostrare un messaggio di successo e l'output di `de` relativo all'ultima commit.
- **REQ-027**: Il comando `release` deve condividere la stessa logica e gli stessi controlli dell'alias `wip` per quanto riguarda lo stato dello staging/worktree e gli eventuali amend, ma prima di eseguire la commit deve determinare la versione corrente tramite `ver`; se la versione non può essere determinata il comando deve fallire riportando il messaggio di errore restituito dal processo di rilevazione. Quando la versione è disponibile deve generare un commit standard con il messaggio `release version: <ver>` (dove `<ver>` è `major.minor.patch`), così da essere usato dagli alias `major`/`minor`/`patch`.

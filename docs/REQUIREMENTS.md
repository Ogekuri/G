---
title: "Requisiti di Git-Alias CLI"
description: "Specifiche dei requisiti software"
date: "2026-01-11"
author: "Francesco Rolando"
scope:
  paths:
    - "**/*.py"
  excludes:
    - ".*/**"
visibility: "bozza"
tags: ["markdown", "requisiti", "git-alias"]
---

# Requisiti di Git-Alias CLI
**Versione**: 0.57
**Autore**: Francesco Rolando  
**Data**: 2026-02-10

## Indice
- [Requisiti di Git-Alias CLI](#requisiti-di-git-alias-cli)
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
    - [3.3 Struttura File Progetto](#33-struttura-file-progetto)
    - [3.4 Organizzazione Componenti](#34-organizzazione-componenti)

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
| 2025-12-19 | 0.36 | Introduzione del comando `ra` per rimuovere lo staging sul branch `work` |
| 2025-12-19 | 0.37 | Elenco di link alle release nella sezione \"# History\" del changelog |
| 2025-12-20 | 0.38 | Errore su `ver` quando una regola `ver_rules` non produce alcun match |
| 2025-12-20 | 0.39 | Formato JSON per `.g.conf` e adeguamento di lettura/scrittura configurazione |
| 2025-12-20 | 0.40 | Limitazione predefinita del changelog ai tag >=0.1.0 e introduzione del flag `--include-draft` |
| 2025-12-20 | 0.41 | Formato dei messaggi di step per `major`/`minor`/`patch` con prefisso e separazione |
| 2025-12-20 | 0.42 | Flag `--include-unreleased` e `--include-draft` per i comandi `major`/`minor`/`patch` |
| 2025-12-20 | 0.43 | Help dei comandi con opzioni esplicite nella stringa di help |
| 2025-12-31 | 0.44 | Versione CLI in usage senza argomenti e flag globali `--ver`/`--version` |
| 2026-01-02 | 0.45 | Rimozione del comando CLI `release` mantenendo la funzione interna per i workflow di rilascio |
| 2026-01-02 | 0.46 | Requisito esplicito per tutti i messaggi CLI in lingua inglese |
| 2026-01-02 | 0.47 | Requisito esplicito per tutti i commenti del codice sorgente in lingua italiana |
| 2026-01-11 | 0.48 | Controllo non bloccante della disponibilità di una nuova versione tramite GitHub API |
| 2026-01-25 | 0.49 | Aggiunta del comando `cover` (Cover Requirements) come alias convenzionale con icona 🎯; comportamento identico agli altri comandi convenzionali |
| 2026-02-03 | 0.50 | Matching dei pattern `ver_rules` tramite libreria pathspec |
| 2026-02-03 | 0.51 | Pulizia hardcoded dei file esclusi dal matching `ver_rules` |
| 2026-02-03 | 0.52 | Ottimizzazione ricerca file tramite `git ls-files` nel comando `ver` |
| 2026-02-03 | 0.53 | Cache temporizzata per il controllo versione online (TTL 6 ore) |
| 2026-02-04 | 0.54 | Aggiunta del comando `ori` per visualizzare e analizzare i remote del repository |
| 2026-02-04 | 0.55 | Rinominato comando `ori` in `str` (Show remotes) |
| 2026-02-10 | 0.56 | Output verbose/debug del comando `ver` con evidenze di matching |
| 2026-02-10 | 0.57 | Ricerca `ver_rules` tramite rglob senza uso di `git ls-files` |

## 1. Introduzione
Questo documento descrive i requisiti del progetto Git-Alias, un pacchetto CLI che riproduce alias git personalizzati e li espone tramite `git-alias`/`g` e `uvx`. I requisiti sono organizzati per funzioni di progetto, vincoli e requisiti funzionali verificabili.

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
- **CPT-005**:Dipendenze esterne: eseguibili `git`, `gitk`, `uv`/`uvx`.
- **CPT-006**:Libreria esterna `pathspec` per il matching dei pattern di configurazione.

## 3. Requisiti
### 3.1 Progettazione e Implementazione
- **DES-001**: Il dispatcher CLI deve accettare un comando come primo argomento, invocare l'alias corrispondente quando il nome è mappato e, quando il comando richiesto non è riconosciuto, eseguire `git` inoltrando tutti gli argomenti originali senza interrompere il flusso, mantenendo invariato il comportamento di help/errore quando non vengono forniti argomenti o viene richiesto `--help`.
- **DES-002**: Ogni alias deve inoltrare eventuali argomenti aggiuntivi al comando git corrispondente, propagando il codice di uscita del processo esterno e gestendo ogni errore dei processi esterni catturando le eccezioni (ad esempio `subprocess.CalledProcessError`) tramite un wrapper condiviso che converte l'errore in una segnalazione esplicita stampata dall'alias chiamante senza mostrare trace Python grezzi. 
- **DES-003**: Ogni comando deve avere un testo di help e il comando globale `--help` deve elencarli in ordine alfabetico.
- **DES-004**: Se l'eseguibile viene chiamato senza argomenti deve stampare un messaggio, mostrare l'help completo e uscire con codice di errore.
- **DES-005**: Gli alias costituiscono la base per lo sviluppo di alias più complessi, pertanto se nell'implementazione di un alias è necessario svolgere una attività implementata in un alias più semplice verrà utilizzata la funzione che specializza quella più semplice.
- **DES-006**: L'eseguibile deve leggere ad ogni invocazione il file `.g.conf` presente alla root del repository git come documento JSON valido, interpretando un oggetto che può definire `master`, `develop`, `work`, `editor`, `default_module` e `ver_rules`, e deve ripiegare sui valori di default quando il file è assente o una chiave è mancante o non valida.
- **DES-007**: Le verifiche sul readiness del commit (worktree, staging, commit precedente) devono essere centralizzate in funzioni riutilizzabili da tutti gli alias che eseguono commit (`cm`, `wip`, e futuri).
- **DES-008**: Tutti i messaggi stampati in console devono essere in inglese.
- **DES-009**: L'output del comando globale `--help` deve essere strutturato nel seguente ordine: (a) una riga di usage che mostra la sintassi generale del comando; (b) una sezione \"Management Commands\" con l'elenco delle opzioni di gestione ricavate da `MANAGEMENT_HELP`; (c) una sezione \"Configuration Parameters\" che stampa i valori correnti dei parametri letti da `.g.conf` (o, se non presenti, i default di `DEFAULT_CONFIG`); (d) una sezione \"Commands\" che elenca gli help di tutti gli alias disponibili in ordine alfabetico.

### 3.2 Funzioni
- **REQ-001**: Il comando `--upgrade` deve reinstallare l'utility usando `uv tool install git-alias --force --from git+https://github.com/Ogekuri/G.git`.
- **REQ-002**: Il comando `--remove` deve disinstallare l'utility globale tramite `uv tool uninstall git-alias`.
- **REQ-003**: Il comando `--help` deve elencare tutti gli alias disponibili o mostrare la descrizione del comando richiesto quando viene specificato un alias; quando il comando dispone di opzioni/flag, la stringa di help del comando deve includere esplicitamente tali opzioni.
- **REQ-004**: L'alias `aa` deve aggiungere tutte le modifiche e i file nuovi all'area di staging con `git add --all`, ma prima deve verificare (riutilizzando le funzioni diagnostiche sullo working tree) che esistano file o modifiche non ancora aggiunti allo staging e, quando non c'è nulla da aggiungere, deve terminare con errore descrivendo il problema.
- **REQ-005**: L'alias di commit `cm` deve permettere commit standard senza automatismi aggiuntivi né messaggi precompilati, ma prima di eseguire `git commit` deve verificare (riutilizzando funzioni diagnostiche centralizzate) che (a) non esistano file o modifiche nello working tree ancora da aggiungere all'index/stage, (b) l'index contenga effettivamente modifiche pronte al commit, e (c) l'ultimo commit del branch corrente non sia una `wip: work in progress.` non mergiata. Se l'ultimo commit ha il messaggio `wip: work in progress.` e non è stato ancora portato ne sui rami `develop`/`master` configurati, `cm` deve aggiornare quel commit tramite `git commit --amend` e stampare un messaggio esplicito; in tutti gli altri casi deve creare un nuovo commit e segnalare l'azione eseguita.
- **REQ-006**: Gli alias di navigazione branch devono consentire checkout mirati (`co`) utilizzando i nomi di branch configurati nel file `.g.conf` (default `work`, `develop`, `master`).
- **REQ-007**: Gli alias di fetch/pull/push devono eseguire le varianti generiche per il ramo corrente (`fe`, `feall`, `pl`, `pt`, `pu`), senza scorciatoie dedicate ai rami configurati.
- **REQ-008**: Gli alias di ispezione devono fornire viste su branch, log e stato (`br`, `lb`, `ck`, `lg`, `ll`, `lm`, `lh`, `lt`, `ver`, `gp`, `gr`, `de`, `rf`, `st`, `str`).
- **REQ-009**: Gli alias di merge devono offrire merge fast-forward generici (`me`) per integrare i rami configurati senza workflow automatizzati aggiuntivi.
- **REQ-010**: Il sistema deve limitare i workflow di rilascio agli alias dedicati documentati (attualmente `major`, `minor`, `patch`) e non deve introdurre ulteriori scorciatoie automatiche oltre a quelli descritti.
- **REQ-011**: Gli alias di reset e pulizia devono applicare le modalità di reset (`rs`, `rssft`, `rsmix`, `rshrd`, `rsmrg`, `rskep`, `unstg`) e le pulizie dello working tree (`rmloc`, `rmstg`, `rmunt`). I comandi di reset (`rs*`) devono stampare il testo di help dedicato quando invocati con `--help`, senza dipendere da alias separati.
- **REQ-012**: Gli alias di tagging e archiviazione devono gestire la creazione di tag annotati (`tg`), la rimozione locale/remota (`rmtg`), la visualizzazione (`lt`) e l'archiviazione del ramo `master` in tar.gz (`ar`).
- **REQ-013**: L'alias `ed` deve consentire l'apertura di file arbitrari usando il comando definito dal parametro `editor` nel file `.g.conf` (default `edit`), segnalando errore se non viene passato alcun percorso.
- **REQ-014**: Il comando `--write-config` deve generare nella root del repository git il file `.g.conf` come JSON ben formattato, contenente `master`, `develop`, `work`, `editor`, `default_module` e la lista `ver_rules` composta da oggetti con campi `pattern` e `regex`, così che l'utente possa personalizzarli manualmente.
- **REQ-015**: All'avvio della CLI il valore del parametro `editor` definito in `.g.conf` deve essere caricato e utilizzato per tutte le operazioni di editing, adottando `edit` quando il parametro manca o è vuoto.
- **REQ-016**: L'invocazione della CLI con `--help` o senza comandi deve mostrare prima le funzioni `--write-config`, `--upgrade`, `--remove` e poi l'elenco completo degli alias disponibili.
- **REQ-017**: Il comando `ver` deve leggere `ver_rules` dal file `.g.conf` come lista di oggetti JSON con campi `pattern` e `regex` (o usare i valori di default), usare la libreria `pathspec` (sintassi GitIgnore) per determinare i file che corrispondono al pattern associato, interpretando i pattern con `/` come ancorati alla root del repository. Per ottenere l'elenco dei file da analizzare, il comando deve utilizzare esclusivamente `rglob()` dalla root del repository senza dipendere dallo stato di tracciamento git, escludendo i percorsi che corrispondono ad espressioni regolari hardcoded per `.git/`, `.vscode/`, `tmp/`, `temp/`, `.cache/`, `.pytest_cache/`, `node_modules/.cache`. Il comando deve quindi applicare ogni regexp solo ai file selezionati dal pattern, raccogliere tutte le versioni trovate e: (a) stampare la versione quando tutte le occorrenze coincidono, oppure (b) terminare con errore indicando i primi due file che presentano versioni differenti, oppure (c) terminare con errore quando una regola non produce alcun match, riportando la stringa della regola che non ha prodotto risultati.
- **REQ-018**: Il comando `changelog` genera il file `CHANGELOG.md` dal repository corrente usando le descrizioni dei commit, deve considerare per impostazione predefinita solo i tag e le commit a partire dalla versione `0.1.0` (escludendo i tag `0.0.*` e la storia precedente) e deve includere tali elementi solo quando viene passato il nuovo flag `--include-draft`. Il comando deve supportare le opzioni `--include-unreleased`, `--include-draft`, `--force-write` e `--print-only`, stampare il contenuto quando si usa `--print-only` e scrivere su disco solo se il file non esiste o quando viene specificato `--force-write`. Il parser deve riconoscere i nuovi tipi `new` (Features) e `change` (Refactor/Changes), ignorare i vecchi tipi `perf`, `test`, `build`, `ci`, `chore`, e includere la sezione "Miscellaneous Tasks" esclusivamente per il tipo `misc`, senza generare la sezione "Other". La sezione "# Changelog" deve elencare i rilasci in ordine cronologico inverso (il più recente in alto), mentre la sezione "# History" deve restare in ordine cronologico (la voce più recente in fondo) e includere, tra il titolo e le definizioni dei link in stile reference, un elenco puntato di link cliccabili alle pagine di release per ogni tag rilevato. L'help del comando deve elencare esplicitamente tutte le opzioni disponibili.
- **REQ-019**: L'alias `bd` deve eliminare un branch locale specificato dall'utente utilizzando `git branch -d <branch>`.
- **REQ-020**: Il sistema deve fornire funzioni di supporto riutilizzabili dagli alias che consentano di verificare (a) la presenza di file o modifiche non ancora aggiunti allo staging, (b) la presenza di file già in staging ma non ancora committati, (c) la disponibilità di aggiornamenti remoti per il branch `develop`, e (d) la disponibilità di aggiornamenti remoti per il branch `master`. Le funzioni per i punti (c) e (d) devono prima sincronizzare i riferimenti remoti (ad esempio con `git remote -v update`) e poi determinare se il branch remoto è in avanti rispetto a quello locale.
- **REQ-021**: L'alias `wip` deve eseguire un commit "work in progress" riutilizzando le stesse funzioni di verifica dell'alias `cm`, generando automaticamente un messaggio fisso `wip: work in progress.` e, come `cm`, deve rilevare se l'ultimo commit è una WIP non ancora presente su `develop`: in tal caso deve aggiornare il commit esistente con `git commit --amend` e stampare l'azione; altrimenti deve creare un nuovo commit e segnalarlo.
 - **REQ-022**: Gli alias `new`, `fix`, `change`, `refactor`, `docs`, `style`, `revert`, `misc` e `cover` devono eseguire commit convenzionali compatibili con il comando `changelog`, utilizzando messaggi nel formato `<tipo>(<modulo>): <descrizione>`. Il comando `cover` (Cover Requirements) deve avere come icona 🎯 e deve comportarsi in modo identico agli altri comandi convenzionali elencati. Ogni comando deve riutilizzare gli stessi controlli di readiness di `cm`/`wip`, accettare il testo del commit come argomento obbligatorio e consentire di specificare il modulo anticipando il testo con `nome_modulo: descrizione`. Quando il modulo non viene indicato, deve essere applicato un valore di default configurabile tramite `.g.conf` (parametro `default_module`, default `core`).

  Nota: Il tipo `refactor` è definito come "Code Refactoring" e deve essere visualizzato nelle sezioni del changelog con l'icona ✨ (U+2728) nella relativa intestazione di sezione.
- **REQ-023**: Tutti i messaggi stampati da `core.py` (su stdout, stderr, in modalità normale, verbose o debug) devono essere in lingua inglese, inclusi gli help dei comandi e le diagnostiche degli alias.
- **REQ-024**: Ogni funzione definita in `core.py` deve essere preceduta da un breve commento descrittivo in italiano che inizi con il carattere `#`, e tutti i commenti presenti nel file devono seguire lo stesso formato e lingua.
- **REQ-025**: Il comando `chver` deve accettare esattamente un argomento nel formato `major.minor.patch` (tre interi separati da punti), verificare la versione corrente tramite `ver`, terminare con errore se `ver` non restituisce una versione univoca o se l'argomento non è valido, evitare modifiche quando la versione richiesta coincide con quella corrente, determinare se l'operazione è un upgrade o un downgrade confrontando `major`, `minor` e `patch`, riscrivere tutte le occorrenze che corrispondono alle regole `ver_rules` attive (quelle lette da `.g.conf` o, in mancanza, `DEFAULT_CONFIG`), e al termine rieseguire `ver` per confermare la nuova versione stampando un messaggio di successo esplicito (upgrade o downgrade). Se la riesecuzione di `ver` non conferma la versione impostata, `chver` deve segnalare un errore critico.
- **REQ-026**: I comandi `major`, `minor` e `patch` devono automatizzare il rilascio di una nuova versione incrementando rispettivamente il numero `major`, `minor` o `patch` (azzerando gli indici meno significativi) e condividere la stessa implementazione di supporto. Devono accettare i flag `--include-unreleased` e `--include-draft`: quando presenti devono inoltrarli al comando `changelog` nello step di rigenerazione del changelog, mantenendo sempre `--force-write`; quando assenti devono rigenerare il changelog usando solo `--force-write`. Prima dell'esecuzione devono verificare che (a) i branch configurati `master`, `develop`, `work` esistano localmente; (b) i remote `origin/master` e `origin/develop` esistano; (c) non ci siano aggiornamenti remoti pendenti per `master` e `develop`; (d) il branch corrente sia `work`; (e) la working area sia pulita; (f) l'index sia vuoto. Ogni step deve stampare un messaggio di progresso quando va a buon fine e segnalare con un messaggio esplicito l'eventuale fallimento dello step corrente: la riga di log deve iniziare con `--- `, includere l'etichetta `[release:major]`, `[release:minor]` oppure `[release:patch]` a seconda del comando, e terminare con ` ---`, con una riga vuota prima della prima riga di log di release per separarla dalle stampe precedenti. Superati i controlli devono: determinare la versione corrente tramite `ver`; calcolare la nuova versione applicando la regola del comando richiesto; aggiornare i file tramite `chver`; aggiungere tutte le modifiche allo stage; creare il commit di rilascio con l'alias `release`; creare un tag annotato `v<ver>` con descrizione `release version: <ver>`; rigenerare `CHANGELOG.md` con `changelog --force-write` più i flag inoltrati; aggiungere il changelog allo stage; aggiornare l'ultima commit con `git commit --amend`; eseguire merge fast-forward da `work` verso `develop`, effettuare il push del branch `develop` su `origin`, eseguire merge fast-forward da `develop` verso `master`, effettuare il push del branch `master` su `origin`; tornare sul branch `work`; mostrare un messaggio di successo e l'output di `de` relativo all'ultima commit.
- **REQ-027**: La funzione `cmd_release` deve condividere la stessa logica e gli stessi controlli dell'alias `wip` per quanto riguarda lo stato dello staging/worktree e gli eventuali amend, ma prima di eseguire la commit deve determinare la versione corrente tramite `ver`; se la versione non può essere determinata il comando deve fallire riportando il messaggio di errore restituito dal processo di rilevazione. Quando la versione è disponibile deve generare un commit standard con il messaggio `release version: <ver>` (dove `<ver>` è `major.minor.patch`), così da essere usato internamente dagli alias `major`/`minor`/`patch`. Questa funzione non deve essere esposta come comando CLI accessibile dall'utente.
- **REQ-028**: L'alias `ra` deve comportarsi come inverso di `aa`: deve verificare di trovarsi sul branch `work` configurato, assicurarsi che non esistano modifiche nel working tree da aggiungere allo staging, verificare che lo staging contenga file pronti per la commit e, solo allora, rimuovere tutte le voci dallo staging riportandole nella working area.
- **REQ-029**: Quando la CLI viene invocata senza argomenti deve stampare la riga di usage con la versione letta da `__init__.py` e appenderla alla fine nel formato `(x.y.z)`.
- **REQ-030**: Quando la CLI viene invocata con i flag globali `--ver` o `--version` deve stampare la versione letta da `__init__.py` ed uscire con successo.
- **REQ-031**: Tutti i messaggi di output della CLI (usage, help, informazioni, verbose, debug, messaggi di errore) devono essere in lingua inglese.
- **REQ-032**: Tutti i commenti nei codici sorgenti devono essere scritti esclusivamente in lingua italiana. Ogni parte importante del codice (classi, funzioni complesse, logica di business, algoritmi critici) deve essere adeguatamente commentata. Ogni nuova funzionalità aggiunta deve includere commenti esplicativi. In caso di modifica di codice esistente, è obbligatorio aggiornare i commenti preesistenti affinché riflettano fedelmente il nuovo comportamento. Non lasciare mai commenti obsoleti o incoerenti con l'implementazione attuale.
- **REQ-033**: Dopo aver validato gli input e prima di eseguire qualsiasi operazione, la CLI deve verificare la disponibilità di una nuova versione utilizzando un meccanismo di cache temporizzata. Il sistema deve memorizzare il risultato del controllo in un file cache JSON nella directory temporanea di sistema (utilizzando `tempfile.gettempdir()`) con nome `.g_version_check_cache.json` e tempo di vita (TTL) di 6 ore. All'avvio, se esiste una cache valida (non scaduta), il sistema deve utilizzare i dati memorizzati senza effettuare chiamate di rete; se la cache è assente o scaduta, deve effettuare una chiamata HTTP GET con timeout di 1 secondo a `https://api.github.com/repos/Ogekuri/G/releases/latest`, determinare l'ultima versione disponibile dalla risposta JSON (campo `tag_name`, con eventuale prefisso `v`), confrontarla con la versione corrente e salvare il risultato nella cache con timestamp di scadenza. Se il server non è contattabile o la chiamata fallisce, la CLI deve considerare la versione attuale come ultima disponibile e procedere senza segnalare nulla. Se la versione disponibile è maggiore di quella attuale (sia da cache che da chiamata online), la CLI deve stampare un messaggio di avviso che indichi la versione attuale e quella disponibile e includa l'istruzione di aggiornamento tramite `--upgrade`. Eventuali errori di lettura o scrittura della cache non devono impedire l'esecuzione del comando.
- **REQ-034**: Il comando `str` deve eseguire `git remote -v`, filtrare e stampare tutti i remote univoci trovati nell'output e, per ogni remote univoco identificato, eseguire il comando `git remote show <remote>` stampando lo stato completo restituito dal comando.
- **REQ-035**: Il comando `ver` deve supportare il flag `--verbose` per stampare l'elenco dei file controllati durante il processo e l'esito positivo o negativo del match della `regex` per ciascun file. Con il flag `--debug` deve includere anche le informazioni di ricerca del globbing, stampando l'elenco completo dei file che matchano il `pattern` associato alla regola.

### 3.3 Struttura File Progetto
```
├── src/git_alias/
│   ├── __init__.py          # Versione pacchetto
│   ├── __main__.py          # Entry point modulo
│   └── core.py              # Implementazione principale (66KB)
├── tests/                   # Suite test (77 test case)
├── docs/
│   └── requirements.md      # Requisiti esistenti
├── pyproject.toml           # Configurazione progetto
├── README.md                # Documentazione
├── CHANGELOG.md             # Cronologia modifiche
└── .g.conf                  # Configurazione runtime
```

### 3.4 Organizzazione Componenti
Il sistema è organizzato attorno al modulo `core.py` che implementa:
- Dispatcher principale con gestione comandi e fallback
- alias git implementati come funzioni `cmd_*`
- Sistema di help con testi descrittivi
- Gestione configurazione JSON
- Funzioni diagnostiche per stato repository
- Wrapper per gestione errori processi esterni
- Sistema di validazione per operazioni commit/staging

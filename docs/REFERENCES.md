# __init__.py | Python | 7L | 0 symbols | 1 imports | 1 comments
> Path: `/home/ogekuri/G/src/git_alias/__init__.py`
> Pacchetto principale della CLI git-alias per uvx.

## Imports
```
from .core import main  # noqa: F401
```


---

# __main__.py | Python | 7L | 0 symbols | 2 imports | 1 comments
> Path: `/home/ogekuri/G/src/git_alias/__main__.py`
> Consente l'esecuzione del tool come modulo.

## Imports
```
from .core import main
import sys
```


---

# core.py | Python | 2140L | 163 symbols | 16 imports | 156 comments
> Path: `/home/ogekuri/G/src/git_alias/core.py`
> Implementazione portabile degli alias git dell'utente.

## Imports
```
import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import pathspec
```

## Definitions

- var `CONFIG_FILENAME = ".g.conf"` (L22)
- var `GITHUB_LATEST_RELEASE_API = "https://api.github.com/repos/Ogekuri/G/releases/latest"` (L24)
- var `VERSION_CHECK_CACHE_FILE = Path(tempfile.gettempdir()) / ".g_version_check_cache.json"` (L27) — Configurazione cache per il controllo versione online
- var `VERSION_CHECK_TTL_HOURS = 6` (L28)
- var `DEFAULT_VER_RULES = [` (L30)
- var `VERSION_CLEANUP_REGEXES = [` (L35)
- var `VERSION_CLEANUP_PATTERNS = [re.compile(pattern) for pattern in VERSION_CLEANUP_REGEXES]` (L44)
- var `DEFAULT_CONFIG = {` (L46)
- var `CONFIG = DEFAULT_CONFIG.copy()` (L59)
- var `BRANCH_KEYS = ("master", "develop", "work")` (L60)
- var `MANAGEMENT_HELP = [` (L61)
### fn `def get_config_value(name)` (L72-75)
L71> Restituisce un valore di configurazione con fallback ai default.
L73> `return CONFIG.get(name, DEFAULT_CONFIG[name])`

### fn `def get_branch(name)` (L77-82)
L76> Restituisce il nome di branch configurato per la chiave richiesta.
L79> `raise KeyError(f"Unknown branch key {name}")`
L80> `return get_config_value(name)`

### fn `def get_editor()` (L84-87)
L83> Recupera il comando di editor definito nella configurazione.
L85> `return get_config_value("editor")`

### fn `def _load_config_rules(key, fallback)` `priv` (L89-114)
L88> Carica le coppie wildcard/regexp definite nel file di configurazione.
L93> `return list(fallback)`
L112> `return rules if rules else list(fallback)`

### fn `def get_version_rules()` (L116-119)
L115> Restituisce le regole usate per rilevare le versioni nei file.
L117> `return _load_config_rules("ver_rules", DEFAULT_VER_RULES)`

### fn `def get_cli_version()` (L121-132)
L120> Recupera la versione del pacchetto leggendo __init__.py senza import.
L126> `return "unknown"`
L129> `return match.group(1)`
L130> `return "unknown"`

### fn `def _normalize_semver_text(text: str) -> str` `priv` (L134-140)
L133> Normalizza una tag version in una stringa semver (rimuove l'eventuale prefisso 'v').
L138> `return value`

### fn `def check_for_newer_version(timeout_seconds: float = 1.0) -> None` (L142-223)
L141> Verifica online se esiste una versione più recente e, se presente, avvisa l'utente, usando una cache temporizzata.
L145> `return`
L147> Controlla se esiste una cache valida
L157> Cache valida, controlla se c'è un aggiornamento disponibile
L169> Ignora errori di lettura cache
L172> `return` — Cache valida, skip controllo online
L174> Esegui il controllo online
L187> `return`
L192> `return`
L194> `return`
L199> `return`
L201> Salva nella cache
L212> Ignora errori di scrittura cache
L214> Mostra avviso se disponibile aggiornamento

### fn `def get_git_root()` (L225-240)
L224> Individua la radice del repository git corrente.
L235> `return Path(location)`
L238> `return Path.cwd()`

### fn `def get_config_path(root=None)` (L242-246)
L241> Calcola il percorso del file di configurazione .g.conf.
L244> `return base / CONFIG_FILENAME`

### fn `def load_cli_config(root=None)` (L248-282)
L247> Carica nella memoria le impostazioni definite in .g.conf.
L252> `return config_path`
L257> `return config_path`
L262> `return config_path`
L265> `return config_path`
L280> `return config_path`

### fn `def write_default_config(root=None)` (L284-291)
L283> Scrive il file di configurazione con i valori di default.
L289> `return config_path`

### fn `def _editor_base_command()` `priv` (L293-307)
L292> Parsa la stringa dell'editor e restituisce il comando base.
L305> `return parts`

### fn `def run_editor_command(args)` (L309-311)
L308> Esegue l'editor configurato con gli argomenti specificati.
L310> `return run_command(_editor_base_command() + list(args))`

- var `HELP_TEXTS = {` (L312)
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L453) — RESET_HELP = Reset commands help screen ...
### fn `def _to_args(extra)` `priv` (L457-460)
L456> Converte la sequenza di argomenti extra in una lista espandibile.
L458> `return list(extra) if extra else []`

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L462-496)
L461> Rappresenta un errore emesso da un processo esterno.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L464-471) L463> Inizializza l'eccezione con i dettagli del comando fallito.
- fn `def _format_message(self) -> str` `priv` (L473-483) L472> Compone il messaggio di errore partendo dall'output disponibile.
  L476> `return text`
  L482> `return f"Command '{cmd_display}' failed with exit code {self.returncode}"`
- fn `def _decode_stream(data) -> str` `priv` (L486-496) L485> Decodifica uno stream di output in testo gestendo gli errori.
  L488> `return ""`
  L491> `return data.decode("utf-8")`
  L493> `return data.decode("utf-8", errors="replace")`
  L494> `return str(data)`

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L498-505)
L497> Esegue un comando esterno e converte gli errori in CommandExecutionError.
L501> `return subprocess.run(*popenargs, **kwargs)`
L503> `raise CommandExecutionError(exc) from None`

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L507-510)
L506> Eccezione dedicata alla rilevazione della versione corrente.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L512-515)
L511> Eccezione dedicata al flusso dei rilasci automatici.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L517-521)
L516> Invia un comando git con argomenti principali e supplementari nella directory indicata.
L519> `return _run_checked(full, cwd=cwd, **kwargs)`

### fn `def capture_git_output(base_args, cwd=None)` (L523-527)
L522> Esegue git e restituisce l'output come stringa per usi interni.
L525> `return result.stdout.strip()`

### fn `def run_command(cmd, cwd=None)` (L529-532)
L528> Invoca un comando esterno con la sintassi fornita.
L530> `return _run_checked(cmd, cwd=cwd)`

### fn `def run_git_text(args, cwd=None, check=True)` (L534-551)
L533> Esegue comandi git e restituisce l'output testuale.
L548> `raise RuntimeError(message) from None`
L549> `return proc.stdout.strip()`

### fn `def run_shell(command, cwd=None)` (L553-556)
L552> Esegue una pipeline nella shell quando serve costruire comandi complessi.
L554> `return _run_checked(command, shell=True, cwd=cwd)`

### fn `def run_git_text(args, cwd=None, check=True)` (L558-575)
L557> Esegue comandi git e restituisce l'output testuale.
L572> `raise RuntimeError(message) from None`
L573> `return proc.stdout.strip()`

### fn `def _git_status_lines()` `priv` (L577-589)
L576> Recupera le linee di stato porcelain del repository.
L586> `return []`
L587> `return proc.stdout.splitlines()`

### fn `def has_unstaged_changes(status_lines=None)` (L591-602)
L590> Determina se esistono modifiche non ancora nello staging.
L597> `return True`
L599> `return True`
L600> `return False`

### fn `def has_staged_changes(status_lines=None)` (L604-613)
L603> Verifica la presenza di elementi già pronti nello staging.
L610> `return True`
L611> `return False`

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L615)
### fn `def _refresh_remote_refs()` `priv` (L619-630)
L618> Aggiorna una sola volta i riferimenti remoti usando git.
L622> `return`
L627> `return`

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L632-650)
L631> Calcola la divergenza tra il branch locale e quello remoto.
L639> `return (0, 0)`
L642> `return (0, 0)`
L647> `return (0, 0)`
L648> `return (local_ahead, remote_ahead)`

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L652-656)
L651> Indica se il branch remoto ha commit non ancora recuperati.
L654> `return remote_ahead > 0`

### fn `def has_remote_develop_updates()` (L658-661)
L657> Verifica la presenza di aggiornamenti remoti per develop.
L659> `return has_remote_branch_updates("develop")`

### fn `def has_remote_master_updates()` (L663-666)
L662> Verifica la presenza di aggiornamenti remoti per master.
L664> `return has_remote_branch_updates("master")`

### fn `def _head_commit_message()` `priv` (L668-674)
L667> Restituisce il messaggio dell'ultima commit locale.
L670> `return run_git_text(["log", "-1", "--pretty=%s"]).strip()`
L672> `return ""`

### fn `def _head_commit_hash()` `priv` (L676-682)
L675> Ritorna l'hash della commit HEAD del repository.
L678> `return run_git_text(["rev-parse", "HEAD"]).strip()`
L680> `return ""`

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L684-696)
L683> Controlla se una commit è presente nel branch indicato.
L686> `return False`
L694> `return proc.returncode == 0`

### fn `def _should_amend_existing_commit()` `priv` (L698-713)
L697> Stabilisce se bisogna ammendare la commit WIP corrente.
L701> `return (False, "HEAD is not a WIP commit.")`
L704> `return (False, "Unable to determine the HEAD commit hash.")`
L708> `return (False, f"The last WIP commit is already contained in {develop_branch}.")`
L710> `return (False, f"The last WIP commit is already contained in {master_branch}.")`
L711> `return (True, "HEAD WIP commit is still pending locally.")`

### fn `def is_inside_git_repo()` (L715-722)
L714> Verifica se il processo si trova all'interno di un repository git.
L719> `return False`
L720> `return output.strip().lower() == "true"`

### class `class TagInfo` `@dataclass` (L724-729)

- var `DELIM = "\x1f"` (L730)
- var `RECORD = "\x1e"` (L731)
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L739)
- var `SECTION_EMOJI = {` (L740)
- var `MIN_SUPPORTED_HISTORY_VERSION = (0, 1, 0)` (L752)
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L756-759)
L755> Determina se il tag semantico deve essere incluso nel changelog di default.
L757> `return _parse_semver_tuple(tag_name.lstrip("v"))`

### fn `def _is_supported_release_tag(tag_name: str) -> bool` `priv` (L761-767)
L760> Verifica se un tag semantico rientra nella storia supportata.
L764> `return True`
L765> `return semver >= MIN_SUPPORTED_HISTORY_VERSION`

### fn `def _should_include_tag(tag_name: str, include_draft: bool) -> bool` `priv` (L769-772)
L768> Determina se includere un tag in base al flag draft.
L770> `return include_draft or _is_supported_release_tag(tag_name)`

### fn `def _latest_supported_tag_name(tags: List[TagInfo], include_draft: bool) -> Optional[str]` `priv` (L774-782)
L773> Recupera l'ultimo tag supportato in base alle regole draft.
L776> `return tags[-1].name if tags else None`
L779> `return tag.name`
L780> `return None`

### fn `def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]` (L784-804)
L783> Ottiene i tag semantici ordinati per data di creazione.
L792> `return []`
L802> `return tags`

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L806-817)
L805> Estrae i soggetti dei commit in un intervallo di log.
L814> `return []`
L815> `return [x.strip() for x in out.split(RECORD) if x.strip()]`

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L819-842)
L818> Classifica un soggetto di commit secondo le categorie supportate.
L822> `return (None, "")`
L840> `return (section, line) if section else (None, "")`

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L844-850)
L843> Estrae la versione di rilascio da un commit new(core): release version: X.Y.Z.
L847> `return None`
L848> `return match.group(1)`

### fn `def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]` (L852-887)
L851> Genera la sezione di changelog relativa a un intervallo di commit.
L863> `return None`
L885> `return "\n".join(lines).rstrip() + "\n"`

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L889-906)
L888> Deriva l'URL base del remote origin per i link di confronto.
L892> `return None`
L903> `return None`
L904> `return base`

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L908-915)
L907> Costruisce l'URL di confronto o di release per un tag.
L910> `return None`
L912> `return f"{base_url}/compare/{prev_tag}..{tag}"`
L913> `return f"{base_url}/releases/tag/{tag}"`

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L917-922)
L916> Costruisce l'URL della pagina release per un tag.
L919> `return None`
L920> `return f"{base_url}/releases/tag/{tag}"`

### fn `def build_history_section(` (L924-929)
L923> Compone la sezione History con i riferimenti di confronto.

### fn `def generate_changelog_document(repo_root: Path, include_unreleased: bool, include_draft: bool = False) -> str` (L959-1006)
L958> Assembla il documento completo del changelog.
L1004> `return "\n".join(lines).rstrip() + "\n"`

### fn `def _collect_version_files(root, pattern)` `priv` (L1008-1043)
L1007> Trova i file che corrispondono al pattern di versione usando rglob e pathspec.
L1013> `return files`
L1019> Applica il pattern usando pathspec (mantiene REQ-017)
L1028> skip empty lines
L1041> `return files`

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1045-1048)
L1044> Verifica se un percorso relativo deve essere escluso dalla ricerca versioni.
L1046> `return any(regex.search(relative_path) for regex in VERSION_CLEANUP_PATTERNS)`

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1050-1061)
L1049> Itera tutte le versioni estratte tramite le regex fornite.
L1056> `yield group`
L1059> `yield match.group(0)`

### fn `def _determine_canonical_version(root: Path, rules, *, verbose: bool = False, debug: bool = False)` `priv` (L1063-1122)
L1062> Determina la versione canonica analizzando i file configurati.
L1082> `raise VersionDetectionError(`
L1088> `raise VersionDetectionError(`
L1111> `raise VersionDetectionError(`
L1115> `raise VersionDetectionError(`
L1119> `raise VersionDetectionError("No version string matched the configured rule list.")`
L1120> `return canonical`

### fn `def _parse_semver_tuple(text)` `priv` (L1124-1130)
L1123> Analizza una stringa di versione semantica e restituisce la tupla numerica.
L1127> `return None`
L1128> `return tuple(int(match.group(i)) for i in range(1, 4))`

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1132-1147)
L1131> Sostituisce le occorrenze di versione nel testo in base alle regex fornite.
L1143> `return text, 0`
L1145> `return "".join(pieces), count`

### fn `def _current_branch_name()` `priv` (L1149-1161)
L1148> Determina il nome del branch corrente del repository.
L1158> `raise ReleaseError("Release commands require an active branch head.")`
L1159> `return branch`

### fn `def _ref_exists(ref_name)` `priv` (L1163-1172)
L1162> Verifica l'esistenza di un riferimento git locale.
L1170> `return proc.returncode == 0`

### fn `def _local_branch_exists(branch_name)` `priv` (L1174-1177)
L1173> Verifica che un branch locale esista.
L1175> `return _ref_exists(f"refs/heads/{branch_name}")`

### fn `def _remote_branch_exists(branch_name)` `priv` (L1179-1182)
L1178> Verifica che il branch remoto esista tra i riferimenti locali.
L1180> `return _ref_exists(f"refs/remotes/origin/{branch_name}")`

### fn `def _ensure_release_prerequisites()` `priv` (L1184-1211)
L1183> Assicura che i prerequisiti per i rilasci siano soddisfatti.
L1191> `raise ReleaseError(f"Unable to run release command: missing local branches {joined}.")`
L1196> `raise ReleaseError(f"Unable to run release command: missing remote branches {joined}.")`
L1198> `raise ReleaseError(f"Remote branch {master_branch} has pending updates. Please pull them first.")`
L1200> `raise ReleaseError(f"Remote branch {develop_branch} has pending updates. Please pull them first.")`
L1203> `raise ReleaseError(f"Release commands must be executed from the {work_branch} branch (current: {current_branch}).")`
L1206> `raise ReleaseError("Working tree changes detected. Clean or stage them before running a release.")`
L1208> `raise ReleaseError("Staging area is not empty. Complete or reset pending commits before running a release.")`
L1209> `return {"master": master_branch, "develop": develop_branch, "work": work_branch}`

### fn `def _bump_semver_version(current_version, level)` `priv` (L1213-1231)
L1212> Calcola la prossima versione semantica in base al tipo di rilascio.
L1216> `raise ReleaseError(f"The current version '{current_version}' is not a valid semantic version.")`
L1228> `raise ReleaseError(f"Unsupported release level '{level}'.")`
L1229> `return f"{major}.{minor}.{patch}"`

### fn `def _run_release_step(level, step_name, action)` `priv` (L1233-1253)
L1232> Esegue un singolo step del rilascio con logging.
L1238> `return result`
L1240> `raise`
L1242> `raise`
L1246> `raise ReleaseError(f"\n--- {label} Step '{step_name}' failed: {message} ---") from None`
L1249> `raise ReleaseError(f"\n--- {label} Step '{step_name}' failed: command exited with status {code} ---") from None`
L1251> `raise ReleaseError(f"\n--- {label} Step '{step_name}' failed: {exc} ---") from None`

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1255-1297)
L1254> Esegue il flusso completo del rilascio.
L1259> `raise ReleaseError("No version rules configured. Cannot compute the next version.")`

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1299-1314)
L1298> Gestisce le eccezioni del flusso di rilascio.
L1304> `sys.exit(1)`
L1307> `sys.exit(1)`
L1312> `sys.exit(exc.returncode or 1)`

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1316-1323)
L1315> Gestisce i comandi di reset mostrando l'help quando richiesto.
L1320> `return`
L1321> `return run_git_cmd(base_args, args)`

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1325-1331)
L1324> Verifica che un alias non riceva argomenti posizionali.
L1329> `sys.exit(1)`

### fn `def _parse_release_flags(extra, alias)` `priv` (L1333-1351)
L1332> Valida i flag permessi per i comandi di release e li restituisce.
L1336> `return []`
L1342> `sys.exit(1)`
L1349> `return deduped`

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1353-1363)
L1352> Prepara le operazioni di commit condivise tra gli alias cm e wip.
L1357> `sys.exit(1)`
L1360> `sys.exit(0)`
L1361> `return " ".join(args)`

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1365-1379)
L1364> Costruisce il messaggio convenzionale partendo dagli argomenti.
L1376> `sys.exit(1)`
L1377> `return f"{kind}({scope}): {body}"`

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1381-1386)
L1380> Coordina l'esecuzione dei commit convenzionali condivisi.
L1384> `return _execute_commit(message, alias, allow_amend=False)`

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1388-1417)
L1387> Esegue git commit applicando i controlli e l'eventuale amend.
L1403> `return run_git_cmd(base, input=message, text=True)`
L1411> `sys.exit(exc.returncode or 1)`
L1414> `sys.exit(exc.returncode or 1)`
L1415> `raise`

### fn `def upgrade_self()` (L1419-1432)
L1418> Aggiorna il comando installato sfruttando il tool uv.

### fn `def remove_self()` (L1434-1437)
L1433> Rimuove il comando installato utilizzando lo strumento uv.

### fn `def cmd_aa(extra)` (L1439-1446)
L1438> Aggiunge tutte le modifiche e i nuovi file all'area di staging (alias aa).
L1443> `sys.exit(1)`
L1444> `return run_git_cmd(["add", "--all"], extra)`

### fn `def cmd_ra(extra)` (L1448-1471)
L1447> Rimuove tutti i file dallo staging riportandoli nel working tree (alias ra).
L1453> `return`
L1455> `sys.exit(1)`
L1461> `sys.exit(1)`
L1467> `sys.exit(1)`
L1469> `return run_git_cmd(["reset", "--mixed"], [])`

### fn `def cmd_ar(extra)` (L1473-1486)
L1472> Crea un archivio master compresso e lo nomina con il tag corrente (alias ar).
L1484> `return gzip_proc`

### fn `def cmd_br(extra)` (L1488-1491)
L1487> Mostra i rami locali disponibili (alias br).
L1489> `return run_git_cmd(["branch"], extra)`

### fn `def cmd_bd(extra)` (L1493-1496)
L1492> Elimina un branch locale (alias bd).
L1494> `return run_git_cmd(["branch", "-d"], extra)`

### fn `def cmd_ck(extra)` (L1498-1501)
L1497> Controlla le differenze e i possibili conflitti (alias ck).
L1499> `return run_git_cmd(["diff", "--check"], extra)`

### fn `def _ensure_commit_ready(alias)` `priv` (L1503-1516)
L1502> Esegue commit con messaggio (alias cm).
L1510> `sys.exit(1)`
L1513> `sys.exit(1)`
L1514> `return True`

### fn `def cmd_cm(extra)` (L1518-1523)
L1517> Esegue l'alias 'cm' con i controlli condivisi di commit.
L1521> `return _execute_commit(message, "cm")`

### fn `def cmd_wip(extra)` (L1525-1537)
L1524> Esegue l'alias 'wip' con messaggio fisso e verifiche condivise.
L1530> `return`
L1532> `sys.exit(1)`
L1535> `return _execute_commit(message, "wip")`

### fn `def cmd_release(extra)` (L1539-1561)
L1538> Esegue l'alias 'release' determinando prima la versione corrente.
L1544> `return`
L1546> `sys.exit(1)`
L1551> `sys.exit(1)`
L1557> `sys.exit(1)`
L1559> `return _execute_commit(message, "release")`

### fn `def cmd_new(extra)` (L1563-1566)
L1562> Esegue l'alias 'new' creando un commit convenzionale.
L1564> `return _run_conventional_commit("new", "new", extra)`

### fn `def cmd_refactor(extra)` (L1568-1571)
L1567> Esegue l'alias 'refactor' creando un commit convenzionale per refactoring del codice.
L1569> `return _run_conventional_commit("refactor", "refactor", extra)`

### fn `def cmd_fix(extra)` (L1573-1576)
L1572> Esegue l'alias 'fix' creando un commit convenzionale.
L1574> `return _run_conventional_commit("fix", "fix", extra)`

### fn `def cmd_change(extra)` (L1578-1581)
L1577> Esegue l'alias 'change' creando un commit convenzionale.
L1579> `return _run_conventional_commit("change", "change", extra)`

### fn `def cmd_docs(extra)` (L1583-1586)
L1582> Esegue l'alias 'docs' creando un commit convenzionale.
L1584> `return _run_conventional_commit("docs", "docs", extra)`

### fn `def cmd_style(extra)` (L1588-1591)
L1587> Esegue l'alias 'style' creando un commit convenzionale.
L1589> `return _run_conventional_commit("style", "style", extra)`

### fn `def cmd_revert(extra)` (L1593-1596)
L1592> Esegue l'alias 'revert' creando un commit convenzionale.
L1594> `return _run_conventional_commit("revert", "revert", extra)`

### fn `def cmd_misc(extra)` (L1598-1601)
L1597> Esegue l'alias 'misc' creando un commit convenzionale.
L1599> `return _run_conventional_commit("misc", "misc", extra)`

### fn `def cmd_cover(extra)` (L1603-1606)
L1602> Esegue l'alias 'cover' creando un commit convenzionale per la copertura dei requisiti.
L1604> `return _run_conventional_commit("cover", "cover", extra)`

### fn `def cmd_co(extra)` (L1608-1611)
L1607> Aggiunge tutto e committa con messaggio (alias cma).
L1609> `return run_git_cmd(["checkout"], extra)`

### fn `def cmd_de(extra)` (L1613-1616)
L1612> Descrive la revisione HEAD con git describe (alias de).
L1614> `return run_git_cmd(["describe"], extra)`

### fn `def cmd_di(extra)` (L1618-1621)
L1617> Scarta le modifiche del file indicato (alias di).
L1619> `return run_git_cmd(["checkout", "--"], extra)`

### fn `def cmd_diyou(extra)` (L1623-1626)
L1622> Mantiene la versione locale durante un conflitto (--ours).
L1624> `return run_git_cmd(["checkout", "--ours", "--"], extra)`

### fn `def cmd_dime(extra)` (L1628-1631)
L1627> Mantiene la versione remota durante un conflitto (--theirs).
L1629> `return run_git_cmd(["checkout", "--theirs", "--"], extra)`

### fn `def cmd_ed(extra)` (L1633-1642)
L1632> Apre uno o piu file con l'editor configurato (alias ed).
L1637> `sys.exit(1)`

### fn `def cmd_fe(extra)` (L1644-1647)
L1643> Scarica aggiornamenti dal remote per il ramo corrente (alias fe).
L1645> `return run_git_cmd(["fetch"], extra)`

### fn `def cmd_feall(extra)` (L1649-1652)
L1648> Effettua fetch di tutti i rami, tag e pulisce quelli orfani (alias feall).
L1650> `return cmd_fe(["--all", "--tags", "--prune"] + _to_args(extra))`

### fn `def cmd_gp(extra)` (L1654-1657)
L1653> Apre gitk con tutti i commit (alias gp).
L1655> `return run_command(["gitk", "--all"] + _to_args(extra))`

### fn `def cmd_gr(extra)` (L1659-1662)
L1658> Apre gitk semplificato per semplificare il grafo (alias gr).
L1660> `return run_command(["gitk", "--simplify-by-decoration", "--all"] + _to_args(extra))`

### fn `def cmd_str(extra)` (L1664-1693)
L1663> Visualizza tutti i remote univoci e ne mostra lo stato.
L1665> Esegue git remote -v per ottenere l'elenco dei remote
L1669> Filtra e raccoglie tutti i remote univoci
L1678> Stampa i remote trovati
L1684> Per ogni remote univoco esegue git remote show
L1691> `raise`

### fn `def cmd_lb(extra)` (L1695-1698)
L1694> Elenca tutti i rami locali e remoti con informazioni aggiuntive (alias lb).
L1696> `return run_git_cmd(["branch", "-v", "-a"], extra)`

### fn `def cmd_lg(extra)` (L1700-1713)
L1699> Esegue l'alias 'lg' per mostrare la cronologia dei commit.
L1701> `return run_git_cmd(`

### fn `def cmd_lh(extra)` (L1715-1718)
L1714> Mostra i dettagli dell'ultimo commit (alias lh).
L1716> `return run_git_cmd(["log", "-1", "HEAD"], extra)`

### fn `def cmd_ll(extra)` (L1720-1732)
L1719> Mostra i commit nel formato oneline completo (alias ll).
L1721> `return run_git_cmd(`

### fn `def cmd_lm(extra)` (L1734-1737)
L1733> Mostra soltanto i merge (alias lm).
L1735> `return run_git_cmd(["log", "--merges"], extra)`

### fn `def cmd_lt(extra)` (L1739-1742)
L1738> Elenca i tag presenti (alias lt).
L1740> `return run_git_cmd(["tag", "-l"], extra)`

### fn `def cmd_me(extra)` (L1744-1747)
L1743> Esegue merge con --ff-only (alias me).
L1745> `return run_git_cmd(["merge", "--ff-only"], extra)`

### fn `def cmd_pl(extra)` (L1749-1752)
L1748> Esegue pull --ff-only sul ramo corrente (alias pl).
L1750> `return run_git_cmd(["pull", "--ff-only"], extra)`

### fn `def cmd_pt(extra)` (L1754-1757)
L1753> Esegue push di tutti i tag (alias pt).
L1755> `return run_git_cmd(["push", "--tags"], extra)`

### fn `def cmd_pu(extra)` (L1759-1762)
L1758> Esegue push e imposta upstream nel remote (alias pu).
L1760> `return run_git_cmd(["push", "-u"], extra)`

### fn `def cmd_rf(extra)` (L1764-1767)
L1763> Mostra il reflog (alias rf).
L1765> `return run_git_cmd(["reflog"], extra)`

### fn `def cmd_rmtg(extra)` (L1769-1779)
L1768> Rimuove un tag localmente e lo elimina da origin (alias rmtg).
L1773> `sys.exit(1)`
L1777> `return run_git_cmd(["push", "--delete", "origin", tag], tail)`

### fn `def cmd_rmloc(extra)` (L1781-1784)
L1780> Reset hard e pulisce l'area di lavoro (alias rmloc).
L1782> `return run_git_cmd(["reset", "--hard", "--"], extra)`

### fn `def cmd_rmstg(extra)` (L1786-1789)
L1785> Rimuove i file dallo stage (alias rmstg).
L1787> `return run_git_cmd(["rm", "--cached", "--"], extra)`

### fn `def cmd_rmunt(extra)` (L1791-1794)
L1790> Pulisce i file non tracciati (alias rmunt).
L1792> `return run_git_cmd(["clean", "-d", "-f", "--"], extra)`

### fn `def cmd_rs(extra)` (L1796-1799)
L1795> Resetta HEAD con --hard (alias rs).
L1797> `return _run_reset_with_help(["reset", "--hard", "HEAD"], extra)`

### fn `def cmd_rssft(extra)` (L1801-1804)
L1800> Resetta con --soft per mantenere i contenuti (alias rssft).
L1802> `return _run_reset_with_help(["reset", "--soft", "--"], extra)`

### fn `def cmd_rsmix(extra)` (L1806-1809)
L1805> Resetta con --mixed per deselezionare gli staged (alias rsmix).
L1807> `return _run_reset_with_help(["reset", "--mixed", "--"], extra)`

### fn `def cmd_rshrd(extra)` (L1811-1814)
L1810> Resetta con --hard (alias rshrd).
L1812> `return _run_reset_with_help(["reset", "--hard", "--"], extra)`

### fn `def cmd_rsmrg(extra)` (L1816-1819)
L1815> Resetta con --merge per gestire conflitti parziali (alias rsmrg).
L1817> `return _run_reset_with_help(["reset", "--merge", "--"], extra)`

### fn `def cmd_rskep(extra)` (L1821-1824)
L1820> Resetta con --keep mantenendo i file locali (alias rskep).
L1822> `return _run_reset_with_help(["reset", "--keep", "--"], extra)`

### fn `def cmd_st(extra)` (L1826-1829)
L1825> Mostra lo stato corrente del repository (alias st).
L1827> `return run_git_cmd(["status"], extra)`

### fn `def cmd_tg(extra)` (L1831-1834)
L1830> Crea un tag annotato (alias tg).
L1832> `return run_git_cmd(["tag", "-a", "-m"], extra)`

### fn `def cmd_unstg(extra)` (L1836-1839)
L1835> Cancella lo stage dei file con reset --mixed (alias unstg).
L1837> `return run_git_cmd(["reset", "--mixed", "--"], extra)`

### fn `def cmd_ver(extra)` (L1841-1859)
L1840> Verifica la consistenza delle versioni nei file configurati (alias ver).
L1851> `sys.exit(1)`
L1856> `sys.exit(1)`

### fn `def cmd_chver(extra)` (L1861-1931)
L1860> Aggiorna tutte le versioni nei file configurati applicando la semantica nuova.
L1865> `sys.exit(1)`
L1870> `sys.exit(1)`
L1875> `sys.exit(1)`
L1880> `sys.exit(1)`
L1884> `sys.exit(1)`
L1887> `return`
L1913> `sys.exit(1)`
L1917> `sys.exit(1)`
L1922> `sys.exit(1)`
L1928> `sys.exit(1)`

### fn `def cmd_major(extra)` (L1933-1937)
L1932> Esegue il rilascio incrementando il numero major.

### fn `def cmd_minor(extra)` (L1939-1943)
L1938> Esegue il rilascio incrementando il numero minor.

### fn `def cmd_patch(extra)` (L1945-1949)
L1944> Esegue il rilascio incrementando il numero patch.

### fn `def cmd_changelog(extra)` (L1951-1983)
L1950> Genera il file CHANGELOG.md tramite l'alias 'changelog'.
L1962> `sys.exit(2)`
L1965> `return`
L1968> `sys.exit(2)`
L1973> `return`
L1980> `sys.exit(1)`

- var `COMMANDS = {` (L1984)
### fn `def print_command_help(name, width=None)` (L2046-2052)
L2045> Stampa la descrizione di un singolo comando.

### fn `def print_all_help()` (L2054-2088)
L2053> Stampa la descrizione di tutti i comandi disponibili in ordine alfabetico.

### fn `def main(argv=None, *, check_updates: bool = True)` (L2090-2140)
L2089> Gestisce il parsing degli argomenti ed esegue l'alias richiesto.
L2097> `sys.exit(1)`
L2100> `sys.exit(1)`
L2105> `return`
L2108> `return`
L2111> `return`
L2114> `return`
L2118> `return`
L2122> `return`
L2128> `return`
L2134> `return`
L2140> `sys.exit(exc.returncode or 1)`

## Comments
- L2: Implementazione portabile degli alias git dell'utente.
- L147: Controlla se esiste una cache valida
- L157: Cache valida, controlla se c'è un aggiornamento disponibile
- L174: Esegui il controllo online
- L201: Salva nella cache
- L214: Mostra avviso se disponibile aggiornamento
- L1019: Applica il pattern usando pathspec (mantiene REQ-017)
- L1665: Esegue git remote -v per ottenere l'elenco dei remote
- L1669: Filtra e raccoglie tutti i remote univoci
- L1678: Stampa i remote trovati
- L1684: Per ogni remote univoco esegue git remote show

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CONFIG_FILENAME`|var|pub|22||
|`GITHUB_LATEST_RELEASE_API`|var|pub|24||
|`VERSION_CHECK_CACHE_FILE`|var|pub|27||
|`VERSION_CHECK_TTL_HOURS`|var|pub|28||
|`DEFAULT_VER_RULES`|var|pub|30||
|`VERSION_CLEANUP_REGEXES`|var|pub|35||
|`VERSION_CLEANUP_PATTERNS`|var|pub|44||
|`DEFAULT_CONFIG`|var|pub|46||
|`CONFIG`|var|pub|59||
|`BRANCH_KEYS`|var|pub|60||
|`MANAGEMENT_HELP`|var|pub|61||
|`get_config_value`|fn|pub|72-75|def get_config_value(name)|
|`get_branch`|fn|pub|77-82|def get_branch(name)|
|`get_editor`|fn|pub|84-87|def get_editor()|
|`_load_config_rules`|fn|priv|89-114|def _load_config_rules(key, fallback)|
|`get_version_rules`|fn|pub|116-119|def get_version_rules()|
|`get_cli_version`|fn|pub|121-132|def get_cli_version()|
|`_normalize_semver_text`|fn|priv|134-140|def _normalize_semver_text(text: str) -> str|
|`check_for_newer_version`|fn|pub|142-223|def check_for_newer_version(timeout_seconds: float = 1.0)...|
|`get_git_root`|fn|pub|225-240|def get_git_root()|
|`get_config_path`|fn|pub|242-246|def get_config_path(root=None)|
|`load_cli_config`|fn|pub|248-282|def load_cli_config(root=None)|
|`write_default_config`|fn|pub|284-291|def write_default_config(root=None)|
|`_editor_base_command`|fn|priv|293-307|def _editor_base_command()|
|`run_editor_command`|fn|pub|309-311|def run_editor_command(args)|
|`HELP_TEXTS`|var|pub|312||
|`RESET_HELP_COMMANDS`|var|pub|453||
|`_to_args`|fn|priv|457-460|def _to_args(extra)|
|`CommandExecutionError`|class|pub|462-496|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|464-471|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|473-483|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|486-496|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|498-505|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|507-510|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|512-515|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|517-521|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|523-527|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|529-532|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|534-551|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|553-556|def run_shell(command, cwd=None)|
|`run_git_text`|fn|pub|558-575|def run_git_text(args, cwd=None, check=True)|
|`_git_status_lines`|fn|priv|577-589|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|591-602|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|604-613|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|615||
|`_refresh_remote_refs`|fn|priv|619-630|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|632-650|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|652-656|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|658-661|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|663-666|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|668-674|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|676-682|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|684-696|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|698-713|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|715-722|def is_inside_git_repo()|
|`TagInfo`|class|pub|724-729|class TagInfo|
|`DELIM`|var|pub|730||
|`RECORD`|var|pub|731||
|`SEMVER_RE`|var|pub|739||
|`SECTION_EMOJI`|var|pub|740||
|`MIN_SUPPORTED_HISTORY_VERSION`|var|pub|752||
|`_tag_semver_tuple`|fn|priv|756-759|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_is_supported_release_tag`|fn|priv|761-767|def _is_supported_release_tag(tag_name: str) -> bool|
|`_should_include_tag`|fn|priv|769-772|def _should_include_tag(tag_name: str, include_draft: boo...|
|`_latest_supported_tag_name`|fn|priv|774-782|def _latest_supported_tag_name(tags: List[TagInfo], inclu...|
|`list_tags_sorted_by_date`|fn|pub|784-804|def list_tags_sorted_by_date(repo_root: Path, merged_ref:...|
|`git_log_subjects`|fn|pub|806-817|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`categorize_commit`|fn|pub|819-842|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|844-850|def _extract_release_version(subject: str) -> Optional[str]|
|`generate_section_for_range`|fn|pub|852-887|def generate_section_for_range(repo_root: Path, title: st...|
|`_canonical_origin_base`|fn|priv|889-906|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|908-915|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|917-922|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|924-929|def build_history_section(|
|`generate_changelog_document`|fn|pub|959-1006|def generate_changelog_document(repo_root: Path, include_...|
|`_collect_version_files`|fn|priv|1008-1043|def _collect_version_files(root, pattern)|
|`_is_version_path_excluded`|fn|priv|1045-1048|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1050-1061|def _iter_versions_in_text(text, compiled_regexes)|
|`_determine_canonical_version`|fn|priv|1063-1122|def _determine_canonical_version(root: Path, rules, *, ve...|
|`_parse_semver_tuple`|fn|priv|1124-1130|def _parse_semver_tuple(text)|
|`_replace_versions_in_text`|fn|priv|1132-1147|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1149-1161|def _current_branch_name()|
|`_ref_exists`|fn|priv|1163-1172|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1174-1177|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1179-1182|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1184-1211|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1213-1231|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1233-1253|def _run_release_step(level, step_name, action)|
|`_execute_release_flow`|fn|priv|1255-1297|def _execute_release_flow(level, changelog_args=None)|
|`_run_release_command`|fn|priv|1299-1314|def _run_release_command(level, changelog_args=None)|
|`_run_reset_with_help`|fn|priv|1316-1323|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1325-1331|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1333-1351|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1353-1363|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1365-1379|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1381-1386|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1388-1417|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|1419-1432|def upgrade_self()|
|`remove_self`|fn|pub|1434-1437|def remove_self()|
|`cmd_aa`|fn|pub|1439-1446|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|1448-1471|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|1473-1486|def cmd_ar(extra)|
|`cmd_br`|fn|pub|1488-1491|def cmd_br(extra)|
|`cmd_bd`|fn|pub|1493-1496|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|1498-1501|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|1503-1516|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|1518-1523|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|1525-1537|def cmd_wip(extra)|
|`cmd_release`|fn|pub|1539-1561|def cmd_release(extra)|
|`cmd_new`|fn|pub|1563-1566|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|1568-1571|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|1573-1576|def cmd_fix(extra)|
|`cmd_change`|fn|pub|1578-1581|def cmd_change(extra)|
|`cmd_docs`|fn|pub|1583-1586|def cmd_docs(extra)|
|`cmd_style`|fn|pub|1588-1591|def cmd_style(extra)|
|`cmd_revert`|fn|pub|1593-1596|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|1598-1601|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|1603-1606|def cmd_cover(extra)|
|`cmd_co`|fn|pub|1608-1611|def cmd_co(extra)|
|`cmd_de`|fn|pub|1613-1616|def cmd_de(extra)|
|`cmd_di`|fn|pub|1618-1621|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|1623-1626|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|1628-1631|def cmd_dime(extra)|
|`cmd_ed`|fn|pub|1633-1642|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|1644-1647|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|1649-1652|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|1654-1657|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|1659-1662|def cmd_gr(extra)|
|`cmd_str`|fn|pub|1664-1693|def cmd_str(extra)|
|`cmd_lb`|fn|pub|1695-1698|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|1700-1713|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|1715-1718|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|1720-1732|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|1734-1737|def cmd_lm(extra)|
|`cmd_lt`|fn|pub|1739-1742|def cmd_lt(extra)|
|`cmd_me`|fn|pub|1744-1747|def cmd_me(extra)|
|`cmd_pl`|fn|pub|1749-1752|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|1754-1757|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|1759-1762|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|1764-1767|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|1769-1779|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|1781-1784|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|1786-1789|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|1791-1794|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|1796-1799|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|1801-1804|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|1806-1809|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|1811-1814|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|1816-1819|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|1821-1824|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|1826-1829|def cmd_st(extra)|
|`cmd_tg`|fn|pub|1831-1834|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|1836-1839|def cmd_unstg(extra)|
|`cmd_ver`|fn|pub|1841-1859|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|1861-1931|def cmd_chver(extra)|
|`cmd_major`|fn|pub|1933-1937|def cmd_major(extra)|
|`cmd_minor`|fn|pub|1939-1943|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|1945-1949|def cmd_patch(extra)|
|`cmd_changelog`|fn|pub|1951-1983|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|1984||
|`print_command_help`|fn|pub|2046-2052|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|2054-2088|def print_all_help()|
|`main`|fn|pub|2090-2140|def main(argv=None, *, check_updates: bool = True)|


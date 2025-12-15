#!/usr/bin/env python3
"""Portable implementation of the user's git aliases."""

import os
import shlex
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

HELP_TEXTS = {
    "aa": "Add all file changes/added to stage area for commit.",
    "ar": "Archive master as zip file. Use tag as filename.",
    "br": "Create a new brach.",
    "brall": "Print all branches.",
    "ck": "Check differences.",
    "cm": "Commit with annotation: git cm '<descritoon>'.",
    "cma": "Add all files and commit with annotation: git cma '<descritoon>'.",
    "cmarelease": "Make a commit with all files and do a release [ commit all file on work -> develop -> master -> tag ].",
    "co": "Checkout a specific branch: git co '<branch>'.",
    "codev": "Checkout the develop branch.",
    "comas": "Checkout the master branch.",
    "conf": "Edit this repository configuration file: .git/config.",
    "cowrk": "Checkout the work branch.",
    "de": "Describe current version with tag of last commit.",
    "di": "Discard current changes on file: git di '<filename>'",
    "diyou": "Discard merge changes in favour of mine files.",
    "dime": "Discard merge chanhes in favour of yours files.",
    "ed": "Edit a file. Syntax: git ed <filename>.",
    "edbrc": "Edit bash ~/.bashrc file.",
    "edbsh": "Edit bash ~/.bash_profile file.",
    "edcfg": "Edit git .gitconfig file. This file.",
    "edign": "Edit git .gitignore configuration file.",
    "edpro": "Edit bash ~/.profile file.",
    "fe": "Fetch new data of current branch from origin.",
    "feall": "Fetch new data from origin for all branch.",
    "fedev": "Fetch new data from origin for develop branch.",
    "femas": "Fetch new data from origin for master branch.",
    "gp": "Open git commits graph (Git K).",
    "gr": "Open git tags graph (Git K).",
    "hl": "Help of specific topic. Syntax: git hl <alias|command|..>.",
    "hlrs": "Help of reset commands.",
    "la": "Print all current aliases",
    "lg": "Show commit history.",
    "lg1": "Show decorated oneline history for all refs.",
    "lg2": "Show a formatted log graph for all refs.",
    "lg3": "Show the commit tree in a more verbose format.",
    "lh": "Show last commit details",
    "ll": "Show lastest full commit hash.",
    "lm": "Show all merges.",
    "lt": "Show all tag",
    "me": "Merge",
    "medev": "Merge develop branch on current branch.",
    "mewrk": "Merge work branch on current branch.",
    "mkcma": "Commit all files with a comment and mkdev. Syntax: git mkcma <description>.",
    "mkdev": "Merge work on develop, then puth develop. Syntax: git mkdev.",
    "mkmas": "Merge work on develop, merge develop on master, then push master. Syntax: git mkmas.",
    "mkrepo": "Create new fresh repository from remote url with inizial commit. Syntax: git mkrepo <url>.",
    "mktday": "Commit all files with today date as comment and mkdev. Syntax: git mktday.",
    "mkwrk": "Create local work branch.",
    "mkyday": "Commit all files with yesterday date as comment and mkdev. Syntax: git mkyday.",
    "pl": "Pull (fetch + merge FETCH_HEAD) from origin on current branch.",
    "pldev": "Pull (fetch + merge FETCH_HEAD) from origin develop to current branch.",
    "plmas": "Pull (fetch + merge FETCH_HEAD) from origin master to current branch.",
    "pt": "Push all new tags to origin.",
    "pu": "Push current branch to origin (add upstream (tracking) reference for pull).",
    "pudev": "Push current branch to origin/develop and set upstream.",
    "pumas": "Push all changes of current branch on origin/master. (add upstream reference for pull).",
    "release": "Make release process and create tag on master with current commit [ last commit on work -> develop -> master -> tag ].",
    "rf": "Show changes on HEAD reference.",
    "rmloc": "Remove changed files from the working tree.",
    "rmstg": "Remove staged files from index tree.",
    "rmtg": "Remove a tag on current branch and from origin.",
    "rmunt": "Remove untracked files from the working tree.",
    "rmwrk": "Delete local work branch.",
    "rs": "Reset current branch to HEAD (--hard).",
    "rshrd": "Hard reset alias (--hard).",
    "rskep": "Keep reset alias (--keep).",
    "rsmix": "Mixed reset alias (--mixed).",
    "rsmrg": "Merge reset alias (--merge).",
    "rssft": "Soft reset alias (--soft).",
    "st": "Show current GIT status.",
    "tg": "Create a new annotate tag. Syntax: git tg <description> <tag>.",
    "tree": "Show commit's tree.",
    "unstg": "Un-stage a file from commit: git unstg '<filename>'. Unstage all files with: git unstg *.",
    "ver": "Primt all version tags.",
}

RESET_HELP = """

 git hlrs - print reset mode help screen

 default mode = '--mixed'

 working - area di lavoro
 index   - staging + ready to commit
 HEAD    - ultimo commit
 target  - example: origin/master

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  A       B     C    D     --soft   A       B     D
                           --mixed  A       D     D
                           --hard   D       D     D
                           --merge  (disallowed)
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  A       B     C    C     --soft   A       B     C
                           --mixed  A       C     C
                           --hard   C       C     C
                           --merge  (disallowed)
                           --keep   A       C     C

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       B     C    D     --soft   B       B     D
                           --mixed  B       D     D
                           --hard   D       D     D
                           --merge  D       D     D
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       B     C    C     --soft   B       B     C
                           --mixed  B       C     C
                           --hard   C       C     C
                           --merge  C       C     C
                           --keep   B       C     C

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       C     C    D     --soft   B       C     D
                           --mixed  B       D     D
                           --hard   D       D     D
                           --merge  (disallowed)
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       C     C    C     --soft   B       C     C
                           --mixed  B       C     C
                           --hard   C       C     C
                           --merge  B       C     C
                           --keep   B       C     C

 The following tables show what happens when there are unmerged entries:
 X means any state and U means an unmerged index.

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  X       U     A    B     --soft   (disallowed)
                           --mixed  X       B     B
                           --hard   B       B     B
                           --merge  B       B     B
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  X       U     A    A     --soft   (disallowed)
                           --mixed  X       A     A
                           --hard   A       A     A
                           --merge  A       A     A
                           --keep   (disallowed)

"""


# Converte la sequenza di argomenti extra in una lista espandibile.
def _to_args(extra):
    return list(extra) if extra else []


# Invia un comando git con argomenti principali e supplementari nella directory indicata.
def run_git_cmd(base_args, extra=None, cwd=None, **kwargs):
    full = ["git"] + list(base_args) + _to_args(extra)
    return subprocess.run(full, check=True, cwd=cwd, **kwargs)


# Esegue git e restituisce l'output come stringa per usi interni.
def capture_git_output(base_args, cwd=None):
    result = subprocess.run(
        ["git"] + list(base_args), check=True, cwd=cwd, stdout=subprocess.PIPE, text=True
    )
    return result.stdout.strip()


# Invoca un comando esterno con la sintassi fornita.
def run_command(cmd, cwd=None):
    return subprocess.run(cmd, check=True, cwd=cwd)


# Esegue una pipeline nella shell quando serve costruire comandi complessi.
def run_shell(command, cwd=None):
    return subprocess.run(command, shell=True, check=True, cwd=cwd)


# Aggiunge tutte le modifiche e i nuovi file all'area di staging (alias aa).
def cmd_aa(extra):
    return run_git_cmd(["add", "--all"], extra)


# Crea un archivio master compresso e lo nomina con il tag corrente (alias ar).
def cmd_ar(extra):
    args = _to_args(extra)
    tag = capture_git_output(["describe", "master"])
    filename = f"{tag}.tar.gz"
    archive_cmd = ["git", "archive", "master", "--prefix=/"] + args
    with subprocess.Popen(archive_cmd, stdout=subprocess.PIPE) as archive_proc:
        with open(filename, "wb") as output_io:
            gzip_proc = subprocess.run(["gzip"], stdin=archive_proc.stdout, stdout=output_io, check=True)
        archive_proc.stdout.close()
        archive_proc.wait()
    return gzip_proc


# Mostra i rami locali disponibili (alias br).
def cmd_br(extra):
    return run_git_cmd(["branch"], extra)


# Elenca tutti i rami locali e remoti con informazioni aggiuntive (alias brall).
def cmd_brall(extra):
    return run_git_cmd(["branch", "-v", "-a"], extra)


# Controlla le differenze e i possibili conflitti (alias ck).
def cmd_ck(extra):
    return run_git_cmd(["diff", "--check"], extra)


# Esegue commit con messaggio (alias cm).
def cmd_cm(extra):
    return run_git_cmd(["commit", "-m"], extra)


# Aggiunge tutto e committa con messaggio (alias cma).
def cmd_cma(extra):
    return run_git_cmd(["commit", "-a", "-m"], extra)


# Esegue checkout del ramo indicato (alias co).
def cmd_co(extra):
    return run_git_cmd(["checkout"], extra)


# Passa al ramo work (alias cowrk).
def cmd_cowrk(extra):
    return cmd_co(["work"] + _to_args(extra))


# Passa al ramo develop (alias codev).
def cmd_codev(extra):
    return cmd_co(["develop"] + _to_args(extra))


# Passa al ramo master (alias comas).
def cmd_comas(extra):
    return cmd_co(["master"] + _to_args(extra))


# Crea un ramo work locale (alias mkwrk).
def cmd_mkwrk(extra):
    return cmd_co(["-b", "work"] + _to_args(extra))


# Elimina il ramo work locale (alias rmwrk).
def cmd_rmwrk(extra):
    return cmd_br(["-d", "work"] + _to_args(extra))


# Apre .git/config con cudatext (alias conf).
def cmd_conf(extra):
    return run_command(["/usr/bin/cudatext", ".git/config"] + _to_args(extra))


# Descrive la revisione HEAD con git describe (alias de).
def cmd_de(extra):
    return run_git_cmd(["describe"], extra)


# Scarta le modifiche del file indicato (alias di).
def cmd_di(extra):
    return run_git_cmd(["checkout", "--"], extra)


# Mantiene la versione locale durante un conflitto (--ours).
def cmd_diyou(extra):
    return run_git_cmd(["checkout", "--ours", "--"], extra)


# Mantiene la versione remota durante un conflitto (--theirs).
def cmd_dime(extra):
    return run_git_cmd(["checkout", "--theirs", "--"], extra)


# Apre uno o piu file con cudatext (alias ed).
def cmd_ed(extra):
    paths = _to_args(extra)
    if not paths:
        print("git ed requires at least one file path", file=sys.stderr)
        sys.exit(1)
    for path in paths:
        expanded = os.path.expanduser(path)
        run_command(["/usr/bin/cudatext", expanded])


# Apre ~/.gitconfig (alias edcfg).
def cmd_edcfg(extra):
    return cmd_ed(["~/.gitconfig"] + _to_args(extra))


# Apre ~/.gitignore (alias edign).
def cmd_edign(extra):
    return cmd_ed(["~/.gitignore"] + _to_args(extra))


# Apre ~/.profile (alias edpro).
def cmd_edpro(extra):
    return cmd_ed(["~/.profile"] + _to_args(extra))


# Apre ~/.bash_profile (alias edbsh).
def cmd_edbsh(extra):
    return cmd_ed(["~/.bash_profile"] + _to_args(extra))


# Apre ~/.bashrc (alias edbrc).
def cmd_edbrc(extra):
    return cmd_ed(["~/.bashrc"] + _to_args(extra))


# Scarica aggiornamenti dal remote per il ramo corrente (alias fe).
def cmd_fe(extra):
    return run_git_cmd(["fetch"], extra)


# Effettua fetch di tutti i rami, tag e pulisce quelli orfani (alias feall).
def cmd_feall(extra):
    return cmd_fe(["--all", "--tags", "--prune"] + _to_args(extra))


# Effettua fetch --tags --prune origin develop (alias fedev).
def cmd_fedev(extra):
    return cmd_fe(["--tags", "--prune", "origin", "develop"] + _to_args(extra))


# Effettua fetch --tags --prune origin master (alias femas).
def cmd_femas(extra):
    return cmd_fe(["--tags", "--prune", "origin", "master"] + _to_args(extra))


# Apre gitk con tutti i commit (alias gp).
def cmd_gp(extra):
    return run_command(["gitk", "--all"] + _to_args(extra))


# Apre gitk semplificato per semplificare il grafo (alias gr).
def cmd_gr(extra):
    return run_command(["gitk", "--simplify-by-decoration", "--all"] + _to_args(extra))


# Mostra l'help di git per un argomento specifico (alias hl).
def cmd_hl(extra):
    return run_git_cmd(["--help"] + _to_args(extra))


# Elenca gli alias correnti filtrando con grep (alias la).
def cmd_la(extra):
    args = _to_args(extra)
    pipeline = "git config --list | grep ^alias\\. | grep '=' | grep -v 'echo -e \\\"' | cut -c 7-"
    if args:
        pattern = shlex.quote(args[0])
        pipeline += f" | grep -Ei --color {pattern}"
    return run_shell(pipeline)


# Mostra la cronologia dei commit delegando a lg2 (alias lg).
def cmd_lg(extra):
    return cmd_lg2(_to_args(extra))


# Mostra il log decorato in una vista compatta con grafico (alias lg1).
def cmd_lg1(extra):
    return run_git_cmd(
        [
            "log",
            "--all",
            "--decorate",
            "--oneline",
            "--graph",
        ],
        extra,
    )


# Mostra il log formattato con grafico e abbreviazioni per ogni ref (alias lg2).
def cmd_lg2(extra):
    return run_git_cmd(
        [
            "log",
            "--graph",
            "--abbrev-commit",
            "--decorate",
            "--format=format:%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)",
            "--all",
        ],
        extra,
    )


# Mostra l'albero dei commit con informazioni dettagliate (alias lg3).
def cmd_lg3(extra):
    return run_git_cmd(
        [
            "log",
            "--graph",
            "--abbrev-commit",
            "--decorate",
            "--format=format:%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n %C(white)%s%C(reset) %C(dim white)- %an%C(reset)",
            "--all",
        ],
        extra,
    )


# Mostra i commit nel formato oneline completo (alias ll).
def cmd_ll(extra):
    return run_git_cmd(["log", "--pretty=oneline"], extra)


# Mostra soltanto i merge (alias lm).
def cmd_lm(extra):
    return run_git_cmd(["log", "--merges"], extra)


# Mostra i dettagli dell'ultimo commit (alias lh).
def cmd_lh(extra):
    return run_git_cmd(["log", "-1", "HEAD"], extra)


# Elenca i tag presenti (alias lt).
def cmd_lt(extra):
    return run_git_cmd(["tag", "-l"], extra)


# Esegue merge con --ff-only (alias me).
def cmd_me(extra):
    return run_git_cmd(["merge", "--ff-only"], extra)


# Merge fast-forward del ramo develop (alias medev).
def cmd_medev(extra):
    return run_git_cmd(["merge", "--ff-only", "develop"], extra)


# Merge fast-forward del ramo work (alias mewrk).
def cmd_mewrk(extra):
    return run_git_cmd(["merge", "--ff-only", "work"], extra)


# Esegue la sequenza di merge/push che porta work su master e sincronizza i tag (alias mkmas).
def cmd_mkmas(extra):
    cmd_codev([])
    cmd_pldev([])
    cmd_cowrk([])
    cmd_medev([])
    cmd_codev([])
    cmd_pldev([])
    cmd_mewrk([])
    cmd_pudev([])
    cmd_cowrk([])
    cmd_lg([])
    return cmd_st(extra)


# Esegue la sequenza di merge/push per portare work su develop (alias mkdev).
def cmd_mkdev(extra):
    cmd_codev([])
    cmd_pldev([])
    cmd_cowrk([])
    cmd_medev([])
    cmd_codev([])
    cmd_pldev([])
    cmd_mewrk([])
    cmd_pudev([])
    cmd_cowrk([])
    cmd_lg([])
    return cmd_st(extra)


# Commit di tutti i file con commento e poi mkdev (alias mkcma).
def cmd_mkcma(extra):
    args = _to_args(extra)
    if not args:
        print("usage: git mkcma \"<comment>\"", file=sys.stderr)
        sys.exit(1)
    comment = " ".join(args)
    print(f"Commit and merge on develop with comment: \"{comment}\" on develop branch")
    cmd_cma([comment])
    return cmd_mkdev([])


# Commit con commento datato ieri e poi mkdev (alias mkyday).
def cmd_mkyday(extra):
    target = datetime.now() - timedelta(days=1)
    message = f"In progress {target.strftime('%Y-%m-%d %H:%M')}"
    cmd_cma([message])
    return cmd_mkdev([])


# Commit con commento datato oggi e poi mkdev (alias mktday).
def cmd_mktday(extra):
    target = datetime.now()
    message = f"In progress {target.strftime('%Y-%m-%d %H:%M')}"
    cmd_cma([message])
    return cmd_mkdev([])


# Clona, inizializza e popola un nuovo repository remoto (alias mkrepo).
def cmd_mkrepo(extra):
    args = _to_args(extra)
    if not args:
        print("usage: git mkrepo \"<name>\"", file=sys.stderr)
        sys.exit(1)
    name = args[0]
    print(f"Make new repo for : \"{name}\"")
    remote = f"ssh://git@donsrv707.dl.net/git/{name}.git"
    run_command(["git", "clone", remote])
    repo_dir = Path(name)
    if not repo_dir.exists():
        raise FileNotFoundError(f"Cloned directory {repo_dir} does not exist")
    run_git_cmd(["init"], cwd=repo_dir)
    home_ignore = Path.home() / ".gitignore"
    example = repo_dir / ".gitignore.example"
    if home_ignore.exists():
        run_command(["cp", str(home_ignore), str(example)])
    else:
        example.write_text("")
    run_git_cmd(["add", ".gitignore.example"], cwd=repo_dir)
    run_git_cmd(["commit", "-m", "Initial empty commit"], cwd=repo_dir)
    run_git_cmd(["remote", "remove", "origin"], cwd=repo_dir)
    run_git_cmd(["remote", "add", "origin", remote], cwd=repo_dir)
    run_git_cmd(["push", "origin", "master"], cwd=repo_dir)
    run_git_cmd(["checkout", "-b", "develop"], cwd=repo_dir)
    if example.exists():
        (repo_dir / ".gitignore").unlink(missing_ok=True)
        example.rename(repo_dir / ".gitignore")
    run_git_cmd(["add", "--all"], cwd=repo_dir)
    run_git_cmd(["commit", "-m", "First commit, add .gitignore file"], cwd=repo_dir)
    return run_git_cmd(["push", "origin", "develop"], cwd=repo_dir)


# Esegue pull --ff-only sul ramo corrente (alias pl).
def cmd_pl(extra):
    return run_git_cmd(["pull", "--ff-only"], extra)


# Esegue pull --ff-only da origin develop (alias pldev).
def cmd_pldev(extra):
    return run_git_cmd(["pull", "--ff-only", "origin", "develop"], extra)


# Esegue pull --ff-only da origin master (alias plmas).
def cmd_plmas(extra):
    return run_git_cmd(["pull", "--ff-only", "origin", "master"], extra)


# Esegue push di tutti i tag (alias pt).
def cmd_pt(extra):
    return run_git_cmd(["push", "--tags"], extra)


# Esegue push e imposta upstream nel remote (alias pu).
def cmd_pu(extra):
    return run_git_cmd(["push", "-u"], extra)


# Esegue push -u origin develop (alias pudev).
def cmd_pudev(extra):
    return run_git_cmd(["push", "-u", "origin", "develop"], extra)


# Esegue push -u origin master (alias pumas).
def cmd_pumas(extra):
    return run_git_cmd(["push", "-u", "origin", "master"], extra)


# Mostra il reflog (alias rf).
def cmd_rf(extra):
    return run_git_cmd(["reflog"], extra)


# Rimuove un tag localmente e lo elimina da origin (alias rmtg).
def cmd_rmtg(extra):
    args = _to_args(extra)
    if not args:
        print("usage: git rmtg \"<tag>\"", file=sys.stderr)
        sys.exit(1)
    tag = args[0]
    tail = args[1:]
    run_git_cmd(["tag", "--delete", tag])
    return run_git_cmd(["push", "--delete", "origin", tag], tail)


# Reset hard e pulisce l'area di lavoro (alias rmloc).
def cmd_rmloc(extra):
    return run_git_cmd(["reset", "--hard", "--"], extra)


# Rimuove i file dallo stage (alias rmstg).
def cmd_rmstg(extra):
    return run_git_cmd(["rm", "--cached", "--"], extra)


# Pulisce i file non tracciati (alias rmunt).
def cmd_rmunt(extra):
    return run_git_cmd(["clean", "-d", "-f", "--"], extra)


# Resetta HEAD con --hard (alias rs).
def cmd_rs(extra):
    return run_git_cmd(["reset", "--hard", "HEAD"], extra)


# Resetta con --soft per mantenere i contenuti (alias rssft).
def cmd_rssft(extra):
    return run_git_cmd(["reset", "--soft", "--"], extra)


# Resetta con --mixed per deselezionare gli staged (alias rsmix).
def cmd_rsmix(extra):
    return run_git_cmd(["reset", "--mixed", "--"], extra)


# Resetta con --hard (alias rshrd).
def cmd_rshrd(extra):
    return run_git_cmd(["reset", "--hard", "--"], extra)


# Resetta con --merge per gestire conflitti parziali (alias rsmrg).
def cmd_rsmrg(extra):
    return run_git_cmd(["reset", "--merge", "--"], extra)


# Resetta con --keep mantenendo i file locali (alias rskep).
def cmd_rskep(extra):
    return run_git_cmd(["reset", "--keep", "--"], extra)


# Mostra lo stato corrente del repository (alias st).
def cmd_st(extra):
    return run_git_cmd(["status"], extra)


# Crea un tag annotato (alias tg).
def cmd_tg(extra):
    return run_git_cmd(["tag", "-a", "-m"], extra)


# Mostra l'albero dei commit delegando a lg3 (alias tree).
def cmd_tree(extra):
    return cmd_lg3(extra)


# Cancella lo stage dei file con reset --mixed (alias unstg).
def cmd_unstg(extra):
    return run_git_cmd(["reset", "--mixed", "--"], extra)


# Elenca i tag di versione (alias ver).
def cmd_ver(extra):
    return run_git_cmd(["tag", "-l"], extra)


# Esegue la procedura di release da work a master e aggiunge un tag (alias release).
def cmd_release(extra):
    args = _to_args(extra)
    if len(args) < 2:
        print("usage: git release \"<tag>\" \"<comment>\"", file=sys.stderr)
        sys.exit(1)
    tag = args[0]
    comment = " ".join(args[1:])
    print(f"Make new release with tag: \"{tag}\" - comment: \"{comment}\" on master branch")
    cmd_codev([])
    cmd_fedev([])
    cmd_mewrk([])
    cmd_pudev([])
    cmd_comas([])
    cmd_femas([])
    cmd_medev([])
    cmd_pumas([])
    cmd_cowrk([])
    run_git_cmd(["tag", "-a", "-m", f"{tag}: {comment}", tag])
    run_git_cmd(["push", "origin", tag])
    cmd_cowrk([])
    cmd_lg([])
    return cmd_st([])


# Commit con tag e poi release automatizzata (alias cmarelease).
def cmd_cmarelease(extra):
    args = _to_args(extra)
    if len(args) < 2:
        print("usage: git cmarelease \"<tag>\" \"<comment>\"", file=sys.stderr)
        sys.exit(1)
    tag = args[0]
    comment = " ".join(args[1:])
    print(f"Commit all files with tag: \"{tag}\" - comment: \"{comment}\" on work branch")
    cmd_cma([f"{tag}: {comment}"])
    return cmd_release([tag, comment])

COMMANDS = {
    "aa": cmd_aa,
    "ar": cmd_ar,
    "br": cmd_br,
    "brall": cmd_brall,
    "ck": cmd_ck,
    "cm": cmd_cm,
    "cma": cmd_cma,
    "co": cmd_co,
    "cowrk": cmd_cowrk,
    "codev": cmd_codev,
    "comas": cmd_comas,
    "mkwrk": cmd_mkwrk,
    "rmwrk": cmd_rmwrk,
    "conf": cmd_conf,
    "de": cmd_de,
    "di": cmd_di,
    "diyou": cmd_diyou,
    "dime": cmd_dime,
    "ed": cmd_ed,
    "edcfg": cmd_edcfg,
    "edign": cmd_edign,
    "edpro": cmd_edpro,
    "edbsh": cmd_edbsh,
    "edbrc": cmd_edbrc,
    "fe": cmd_fe,
    "feall": cmd_feall,
    "fedev": cmd_fedev,
    "femas": cmd_femas,
    "gp": cmd_gp,
    "gr": cmd_gr,
    "hl": cmd_hl,
    "hlrs": lambda extra: print(RESET_HELP) if not extra else print(RESET_HELP),
    "la": cmd_la,
    "lg": cmd_lg,
    "lg1": cmd_lg1,
    "lg2": cmd_lg2,
    "lg3": cmd_lg3,
    "ll": cmd_ll,
    "lm": cmd_lm,
    "lh": cmd_lh,
    "lt": cmd_lt,
    "me": cmd_me,
    "medev": cmd_medev,
    "mewrk": cmd_mewrk,
    "mkmas": cmd_mkmas,
    "mkdev": cmd_mkdev,
    "mkcma": cmd_mkcma,
    "mkyday": cmd_mkyday,
    "mktday": cmd_mktday,
    "mkrepo": cmd_mkrepo,
    "pl": cmd_pl,
    "pldev": cmd_pldev,
    "plmas": cmd_plmas,
    "pt": cmd_pt,
    "pu": cmd_pu,
    "pudev": cmd_pudev,
    "pumas": cmd_pumas,
    "rf": cmd_rf,
    "rmtg": cmd_rmtg,
    "rmloc": cmd_rmloc,
    "rmstg": cmd_rmstg,
    "rmunt": cmd_rmunt,
    "rs": cmd_rs,
    "rssft": cmd_rssft,
    "rsmix": cmd_rsmix,
    "rshrd": cmd_rshrd,
    "rsmrg": cmd_rsmrg,
    "rskep": cmd_rskep,
    "st": cmd_st,
    "tg": cmd_tg,
    "tree": cmd_tree,
    "unstg": cmd_unstg,
    "ver": cmd_ver,
    "release": cmd_release,
    "cmarelease": cmd_cmarelease,
}


# Stampa la descrizione di un singolo comando.
def print_command_help(name):
    description = HELP_TEXTS.get(name, "No help text is available for this command.")
    print(f"{name} - {description}")


# Stampa la descrizione di tutti i comandi disponibili in ordine alfabetico.
def print_all_help():
    for name in sorted(COMMANDS.keys()):
        print_command_help(name)


def main(argv=None):
    """Parse CLI arguments and either show help text or invoke the requested alias."""
    args = list(argv) if argv is not None else sys.argv[1:]
    if not args:
        print("Please provide a command or --help", file=sys.stderr)
        print_all_help()
        sys.exit(1)
    if args[0] == "--help":
        if len(args) == 1:
            print_all_help()
            return
        name = args[1]
        if name in COMMANDS:
            print_command_help(name)
        else:
            print(f"Unknown command: {name}", file=sys.stderr)
            sys.exit(1)
        return
    name = args[0]
    extras = args[1:]
    if name not in COMMANDS:
        print(f"Unknown command: {name}", file=sys.stderr)
        print_all_help()
        sys.exit(1)
    if "--help" in extras:
        print_command_help(name)
        return
    COMMANDS[name](extras)


if __name__ == "__main__":
    main()

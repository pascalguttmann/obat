Git Submodules
==============

Literature
----------

Getting general info over git submodules:

- <https://git-scm.com/book/en/v2/Git-Tools-Submodules>
- <https://git-scm.com/docs/git-submodule>

Recommended Configuration for Obat
----------------------------------

If you are unsure how to configure git for smooth usage with git submodules obat
recommends the following configurations. The following commands will set the
configurations globally.
If you wish to set the configuration only for the obat repository run `git
config --local` instead of `--global`.

```bash
git config --global diff.submodule log
git config --global status.submodulesummary 1
git config --global push.recurseSubmodules on-demand
git config --global submodule.recurse true
```

Common operations and workflows
-------------------------------

### Cloning with Submodules

```bash
git clone <repo>
git submodule update --init --recursive
```

### Working on Multi-repository feature

When working on a feature that requires changes in multiple repositories create
a branch `<featurebranch>` in the parent repo. Creating feature branches in the
submodule repos with the same name allows to easily make use of the
`--recurse-submodules=on-demand` flag later, which is configured if you use the
recommended configuration. Additionally it helps to keep track of which branches
over multiple repositories belong together.

```bash
git switch -c <featurebranch>
git submodule foreach 'git switch -c <featurebranch>'
```

Work on the repositories as normal with `add` and `commit`. Commits in
submodules will be visible in the parent repo as changed submodules. When adding
the changes of the submodules in the parent repo the changed submodule can be
used.
After everything is committed you can push your branches to the remote.
Typically with same names and the configuration you should be able to do

```bash
git push
```

which should push to your default remote and if necessary set upstream branches
for your local branches. The operation should also push the branches in the
submodules, as the configuration uses the `--recurse-submodules=on-demand` flag.
This will not work, if you use different branch names and you will have to push
the branches in the submodules manually. (E.g. `git submodules foreach 'git
push'`)

### Creating and Managing Multiple Pull Requests

To manage multiple pull request it is recommended to use the GitHub CLI to
easily create PRs if necessary. This could be achieved by running similar to

```bash
git submodules foreach 'gh pr create'
```


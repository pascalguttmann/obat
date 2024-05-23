# Welcome to Open Battery Tester

Open Battery Tester is a battery tester project with the goal of providing a

- modifiable
- easy to use

battery testing system.
The goal is to make the entry into battery testing easy, while being able to
meet future requirements by enhancing parts of the system as required.

## Documentation

To read the full documentation please visit the [obat documentation][obat-doc].

### Contributing to the Documentation

The documentation is provided in `Markdown` files, which are compiled and
deployed to the [obat documentation][obat-doc] using [MkDocs][mkdocs].

#### Contribution Video Tutorials

[Video tutorials for contributing][tutorial-vid] using git are available for the usage of:

- Command Line Interface of Git
- VS Code Git Integration

#### Editing on Local Machine

To edit the documentation on your local machine you should download the obat
repository and make changes on your local copy. This yields the benefit to be
able to check how the documentation will look after your changes, before merging
them into the main documentation.

##### Setting up the Environment

!!! info "Prerequisites"
    To set up the environment this guide assumes you have installed on your
    machine:

    - [x] Python 3
    - [x] Git

To set up the documentation locally clone the git repository to your local
machine.

```bash
git clone https://github.com/pascalguttmann/obat.git
```

!!! info "Git Submodules"
    To work with Git submodules you can update the contents of the submodules by
    running `git submodule update --init --recursive` after `git clone` in the
    git repository. [Further information how git submodules are used in
    obat.][submodules]

[submodules]: <./git-submodules/>

You can edit the documentation which is located in the `./docs/` directory of
the repository and create a pull request to merge your changes.

To check that the documentation is build correctly you can run a instance of the
documentation server for testing purposes locally.  First activate the python
venv. If you are using windows you can use the provided helper batch script for
this.

```bash
go_venv.bat
```

!!! info
    To deactivate the python venv use the command `deactivate`.

After this the prompt should show `(venv)` to indicate that the python venv is
activated. With the virtual environment activated you can run a local
documentation server, which will by default bind to <http://127.0.0.1:8000/obat/>.

```bash
mkdocs serve
```

To allow for a faster more convenient way to check the documentation build
locally in the shell the script `go_mkdocs_serve.sh` combines the steps

1. activating the venv with `go_venv.sh` and
2. running the local documentation server with `mkdocs serve`
3. opening a webbrowser at <http://127.0.0.1:8000/obat/>

So the only command necessary to run when using this convenience script is:
```bash
./go_mkdocs_serve.sh
```

##### Changing the Documentation

The documentation is stored in the directory `./docs/`. Apply the desired
changes to the files in the `./docs/` directory and observe the changes on the
local documentation server with live preview.

#### Editing on GitHub

To edit a page directly on GitHub click the edit icon on the top of the page.
The link will redirect you directly to the editing view of the source file on
the GitHub repository.

## ECAD

Obat uses [KiCAD 8] as an ECAD tool, a free and open source tool.

[KiCAD 8]: <https://www.kicad.org/download/>

## License

The project including its

- software
- documentation
- and other non software intellectual properties

are distributed under the [MIT License][license].

[obat-doc]: <https://pascalguttmann.github.io/obat/>
[license]: <https://raw.githubusercontent.com/pascalguttmann/obat/main/LICENSE>
[mkdocs]: <https://www.mkdocs.org/>
[tutorial-vid]: <./tutorial-vids/>

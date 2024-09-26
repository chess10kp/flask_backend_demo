# Backend Workshop with Python's Flask

## Installation instructions

#### Windows (using [winget](https://winget.run/))

- Make sure that Git, Python or VScode aren't already installed on your system. You may do this by running `git` and `python` in the command line

```powershell
winget install -e --id Git.Git
winget install -e --id Python.Python.3.11
winget install -e --id Microsoft.VisualStudioCode
```

#### MacOS (using [homebrew](https://brew.sh) )

- Install homebrew (check if it is already installed by running `brew` in the terminal)

```zsh
/bin/bash -c \
"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" \
&& brew update && brew doctor
```

- Make sure that brew is actually installed, then run:

```zsh
brew install git
brew install python
brew install --cask visual-studio-code
```

## Uninstallation instructions (Optional)

1. Windows

```powershell
winget uninstall -e --id Git.Git
winget uninstall -e --id Python.Python.3.11
winget install -e --id Microsoft.VisualStudioCode
```

2. MacOS

```powershell
brew uninstall git
brew uninstall python
```

- Uninstall homebrew

```zsh
NONINTERACTIVE=1 /bin/bash -c \
"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

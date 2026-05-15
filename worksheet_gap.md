# Computational semigroup theory with the `Semigroups` package in GAP

## Introduction

[GAP](https://www.gap-system.org/) is a computer algebra system for discrete algebra. While the core focus of GAP is
group theory, several extensions to the system are provided by
[_packages_](https://docs.gap-system.org/doc/ref/chap76_mj.html). An index of GAP packages that are shipped together
with gap is available online in the [GAP Packages](https://www.gap-system.org/packages/) section of the GAP system
website.

In this worksheet we will be primarily focused on using the [`Semigroups`](https://semigroups.github.io/Semigroups/)
package for computational investigations of semigroups. The worksheet does not assume prior familiarity with the
GAP programming language, though we recommend the
[GAP software carpentries lesson](https://carpentries-incubator.github.io/gap-lesson/index.html) to those interested
in learning more about GAP.

### Installing GAP and `Semigroups`

In this section we detail the installation of GAP and `Semigroups` on various platforms.
Please follow the instructions in the section relevant to your platform to set up
your system and then follow the [Common install steps](#common-install-steps) section.
A newer and slightly simpler installation path is possbile via the Julia
language, it is still experimental, but those interested can refer to the
[EXPERIMENTAL Install using Julia](#experimental-install-using-julia)
section instead.

#### Windows

GAP is primarily developed for Linux-based operating systems. In order to make
it run on Windows, it is generally easier to install a Linux subsystem which
provides a Linux shell than to try and make it run on Windows directly.
Windows provides such a feature via the Windows subsystem for Linux (WSL).

We will follows a the guide available on the 
[miscrosoft docs](https://docs.microsoft.com/en-us/windows/wsl/install)
page to install WSL 2.

1. Open `Powershell` as administrator, this can be done by typing "powershell"
   in the search bar and then right-clicking the application icon and selecting
   "Run as administrator". 
2. Within `Powershell`, run the following command:
   ```powershell
   wsl --install
   ```
   Note that using `Ctrl+V` to paste in the terminal might not work, instead you
   should simply right-click in the window to paste.
   This step enables the feature that will allow us to run Linux as a subsystem
   of Windows. By default it will install the Ubuntu operating system.
   You may need to restart your computer after this step.
5. Once this is all done, open a terminal. This can be either `powershell` 
   or `windows-terminal` or `cmd` (type either one in the search bar).
6. Within the terminal run the command `ubuntu`.
7. If all went well, you should be prompted to create a username and password 
   for the default Linux user.
8. Once this is done, the terminal prompt should read something like 
   `user@computer-name:~$`.

If all went well, you now have an Ubuntu Linux subsystem available via the
`ubuntu` command. To install GAP and `Semigroups`, execute the `ubuntu`
command in `Powershell` and then proceed as described in the
[Common install steps](#common-install-steps) section.

**Troubleshooting**: If the `wsl --install` command has been running for a long
time and produces no output, kill it by pressing `CTRL+C` in the terminal.

1. Check if `wsl` is enabled by running the
   ```powershell
   Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   ```
   command in `powershell`.
2. If the output of the above command indicates that `wsl` is disabled, then
   run 
   ```powershell
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
   ```
   and re-attempt the `wsl --install` step.

#### Mac

For a Mac we need to install some prerequisite packages which we do via
the `Homebrew` package manager. In order to do this we first install `Homebrew`
following the steps outlined on their [website](https://brew.sh/).
   
1. Open the Terminal app. It should be under Utilities. Alternatively you can
   use the Mac spotlight computer search function and look for `Terminal`.
2. In the terminal run 
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   To test the installation, try running `brew -v`.
3. Install the Apple developer tools via
   ```bash
   xcode-select --install
   ```
4. Now use `brew` to install the necessary prerequisites:
   ```bash
   brew update
   brew install curl autoconf libtool pkg-config graphviz gmp readline zlib
   ```

Continue as described in the [Common install steps](#common-install-steps) section.

#### Linux

In this section we assume that you are using the Ubuntu Linux distribution. If
your distribution differs then you may need to modify the package manager used
(e.g. on Fedora this may involve changing `apt` to `dnf` and modifying the
package names).

1. Update the package index and install some necessary prerequisite packages:
   ```bash
   sudo apt-get update
   sudo apt-get install curl build-essential autoconf libtool pkg-config graphviz libgmp-dev libreadline-dev zlib1g-dev
   ```

Continue as described in the [Common install steps](#common-install-steps) section.

#### Common install steps

In order to install GAP we follow the
[installation instructions](https://www.gap-system.org/install/linux/) from the
GAP website.
We will install GAP in the "home" directory. You are free to use any other
directory, if you do so, substitute the `~` in the following commands with
whatever base directory you are using.

2. Run `cd ~`. This will ensure you are in the home directory, where the rest of the install will occur.
3. Download the current GAP distribution, at time of writing it is 4.15.1. If this has changed, then
   substitute the appropriate version number in the `export` command below:
   ```bash
   export GAP_VERSION=4.15.1
   curl -L "https://github.com/gap-system/gap/releases/download/v${GAP_VERSION}/gap-${GAP_VERSION}.tar.gz" > gap.tar.gz
   ```
   If all went well you should see output similar to 
   ```
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                   Dload  Upload   Total   Spent    Left  Speed
     0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
   100  482M  100  482M    0     0  1823k      0  0:04:31  0:04:31 --:--:-- 2105k
   ```
   and when using the `ls` command to list files in the current directory, you should see a file called `gap.tar.gz`.

4. Unpack the archive:
   ```bash
   tar -xvzf gap.tar.gz
   ```
   if all went well the `ls` command should now reveal a new folder called `gap-4.15.1` (or whatever the relevant version is).
   You can now `rm gap.tar.gz` to remove the archive. 
5. Change into the gap directory and run the configure and make scripts:
   ```bash
   cd gap-${GAP_VERSION}
   ./configure
   make -j8
   ```
   replacing the 8 in the `-j8` by the number of cores you want to use.
   If all goes well, make should finish with without errors and running
   `./gap` gives the GAP prompt (you can quit from the GAP prompt by
   typing `quit;`).
6. We are not quite done yet, since some of the optional packages need to be
   compiled before they can be used. In order to do so run
   ```bash
   cd pkg
   ../bin/BuildPackages.sh
   ```
7. To test the package compilation, run `../gap` and within the GAP prompt write
   ```gap
   SetInfoLevel(InfoPackageLoading, 4);
   LoadPackage("Semigroups");
   ```
   If the package loads without errors, the compilation has likely been successful.
8. Otherwise you may see an error similar to the following:
   ```
   #I  Semigroups: entering LoadPackage 
   #I  Semigroups: PackageAvailabilityInfo for version 5.5.4
   #I  Semigroups: the kernel module is not compiled, 
   #I              the package cannot be loaded.
   #I  Semigroups: PackageAvailabilityInfo: the AvailabilityTest function returned false
   #I  Semigroups: PackageAvailabilityInfo: no installed version fits
   #I  Semigroups: return from LoadPackage, package is not available
   fail
   ```
   If this is the case then `quit;` the GAP session and perform the following steps to
   compile the `Semigroups` package manually
   ```bash
   cd semigroups
   ./configure
   make -j4
   ```
   compilation of the semigroups package is quite memory intensive, and may get killed
   if the computer runs out of memory. If so try compiling again setting a lower 
   number of threads when running make, e.g. `make -j2` or even just `make`.
9. To run GAP from an arbitrary folder on your computer you currently need to write
   `~/gap-$GAP_VERSION/gap`. To avoid having to do this execute the following:
   ```bash
   mkdir -p ~/.local/bin
   ln -s ~/gap-${GAP_VERSION}/gap ~/.local/bin/gap
   ```
   This will add the gap executable to the local executable bin. To make it available, we need to make sure
   the `~/.local/bin` directory is in your `PATH`. On a Linux machine this can be done by
   ```bash
   echo 'if ! [[ "$PATH" =~ "$HOME/.local/bin:" ]] then PATH="$HOME/.local/bin:$PATH"; fi' >> ~/.bashrc
   source ~/.bashrc
   ```
   On a Mac do this instead:
   ```bash
   echo 'if ! [[ "$PATH" =~ "$HOME/.local/bin:" ]] then PATH="$HOME/.local/bin:$PATH"; fi' >> ~/.zshrc
   source ~/.zshrc
   ```
   Test this works by typing `gap` in the terminal, if all went well it should open a GAP prompt.

#### EXPERIMENTAL Install using Julia

It has recently become possible to install GAP using the
[Julia](https://julialang.org/) programming language. This installation path is
currently experimental but can be much quicker than the method detailed in
the [Common install steps](#common-install-steps) section.

If you already installed GAP and `Semigroups` using the instructions from
the section [Common install steps](#common-install-steps), then skip this
section.

For Windows users, it is still required to install `wsl` and run the following steps
from the `ubuntu` subsystem, as detailed in the section [Windows](#windows).
Linux and Windows users (in the `ubuntu` prompt) should then run
```bash
sudo apt-get update
sudo apt-get install curl
```
and Mac users should run
```bash
brew update
brew install curl
```
to install the required prerequisites.

We follow the Julia install instructions from
[the Julia website](https://julialang.org/downloads/).

1. Install Julia by running
   ```bash
   curl -fsSL https://install.julialang.org | sh
   ```
   if you are on Linux or Windows (through the `ubuntu` prompt), run
   ```bash
   source ~/.bashrc
   ```
   on Mac run
   ```bash
   source ~/.zshrc
   ```
   you should now be able to run Julia by typing `julia` in the prompt.
   Yo ucan exit the Julia prompt by typing `exit()`.
2. Run `julia` to get a Julia prompt and run
   ```julia
   using Pkg; Pkg.add("GAP")
   ```
   this should install the [`GAP.jl`](https://github.com/oscar-system/GAP.jl)
   Julia package.
   If all went well, within the Julia prompt typing
   ```julia
   using GAP; GAP.prompt();`
   ```
   This should start a GAP prompt. In the GAP prompt type
   ```gap
   SetInfoLevel(InfoPackageLoading, 4);
   LoadPackage("Semigroups");
   ```
   To check that the `Semigroups` package is available.
   Exit the GAP prompt by typing `quit;`, which should 
   return you to the Julia prompt.
   Exit the Julia prompt too via `exit()`.
3. We will now create a script which will allow us to start the gap prompt by
   simply typing `gap` in the base shell. To do this first run
   ```bash
   mkdir -p ~/.local/bin
   ```
   Afterwards, if you are on a Linux machine, then run
   ```bash
   echo 'if ! [[ "$PATH" =~ "$HOME/.local/bin:" ]] then PATH="$HOME/.local/bin:$PATH"; fi' >> ~/.bashrc
   source ~/.bashrc
   ```
   On a Mac do this instead:
   ```bash
   echo 'if ! [[ "$PATH" =~ "$HOME/.local/bin:" ]] then PATH="$HOME/.local/bin:$PATH"; fi' >> ~/.zshrc
   source ~/.zshrc
   ```
4. Finally, open `julia` and within the Julia prompt type
   ```julia
   using GAP; GAP.Setup.create_gap_sh("~/.local/bin/", "gap");
   ```
   Then `exit()` the Julia prompt. You should now be able to start a GAP
   session by typing `gap` in your prompt.

### The GAP session

## Analysis of finite semigroups



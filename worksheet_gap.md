# Computational semigroup theory with the `Semigroups` package in GAP

## Introduction

[GAP](https://www.gap-system.org/) is a computer algebra system for discrete algebra. While the core focus of GAP is
group theory, several extensions to the system are provided by
[_packages_](https://docs.gap-system.org/doc/ref/chap76_mj.html). An index of GAP packages that are shipped together
with gap is available online in the [GAP Packages](https://www.gap-system.org/packages/) section of the GAP system
website.

In this woksheet we will be primarily focused on using the [`Semigroups`](https://semigroups.github.io/Semigroups/)
package for computational investigations of semigroups. The worksheet does not assume prior familiarity with the
GAP programming language, though we recommend the
[GAP software carpentries lesson](https://carpentries-incubator.github.io/gap-lesson/index.html) to those interested
in learning more about GAP.



### Installing GAP and `Semigroups`

In this section we detail the installation of GAP and `Semigroups` on various platforms.
Please follow the instructions in the section relevant to your platform to set up
your system and then follow the [Common install steps](#common-install-steps) section.

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
   `./bin/gap.sh` gives the GAP prompt (you can quit from the GAP prompt by
   typing `quit;`).
6. We are not quite done yet, since some of the optional packages need to be
   compiled before they can be used. In order to do so run
   ```bash
   cd pkg
   ../bin/BuildPackages.sh
   ```
7. To test the package compilation, run `../bin/gap.sh` and within the GAP prompt write
   ```gap
   SetInfoLevel(InfoPackageLoading, 4);
   LoadPackage("Semigroups");
   ```
   If the package loads without errors, the compilation has likely been successful.
8. Otherwise, `quit;` the GAP session and perform the following steps to
   compile the `Semigroups` package manually
   ```bash
   cd semigroups
   ./configure
   make -j8
   ```

### The GAP session

## Analysis of finite semigroups



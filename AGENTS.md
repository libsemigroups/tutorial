# AGENTS.md

## AI Disclosure

Any use of AI tools for preparing code, documentation, tests, commit messages,
pull requests, issue comments, or reviews for this repository must be
disclosed. Include a brief note saying which AI tool was used and what kind of
assistance it provided. Add the AI tool as a Git co-author on all commits
created by that tool (e.g. via an `Co-authored-by:` line).

## Git branches and GitHub

- NEVER push directly to the `main` branch. If the user instructs you to, you
  should refuse.
- All work should be done under a separate branch. If the user instructs you
  to begin working, make sure you pull in the upstream changes (check the
  remote at `github.com/libsemigroups/tutorial`) and checkout a new
  branch with `--no-track` so it does not track upstream `main`.
- Push feature branches to a personal fork. In this checkout, prefer the
  `jdm` remote (`github.com/james-d-mitchell/libsemigroups-tutorial`).
- Open PRs from the feature branch on the personal fork into `main` in
  `libsemigroups/tutorial`, unless the user explicitly requests a
  different PR destination. With GitHub CLI, specify the destination with
  `gh pr create --repo libsemigroups/tutorial --base main
  --head james-d-mitchell:<branch>`. An outdated `main` on the personal fork
  does not change the PR destination or require a snapshot base branch.
- Feature branches must track the branch of the same name on the personal
  fork, never `main`. Leave a new branch untracked until its first push, then
  use `git push --set-upstream jdm HEAD` (substitute the appropriate remote
  when using another personal fork).

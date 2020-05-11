## pre-commit-sbt
Fast pre-commit hooks for sbt plugins.

For pre-commit: see https://github.com/pre-commit/pre-commit \
For sbt: https://www.scala-sbt.org/1.x/docs

These hooks aim to run faster and avoid starting new sbt
instances for every run. This is achieved by using [sbt language server](https://www.scala-sbt.org/1.x/docs/sbt-server.html)
and a [client for it](https://github.com/anivanch/sbt-client-py).

## Example
Add the following to your `.pre-commit-config.yaml`
```
-   repo: https://github.com/anivanch/pre-commit-sbt
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: sbt-compile
    -   id: sbt-scalafmt
    -   id: sbt-scalastyle
    -   id: sbt-scapegoat
```

## Tips
To see the process id of sbt instance created by sbt-client you can add log file for
your hooks, e.g.
```
hooks:
-   id: sbt-compile
    log_file: pre-commit-logs
```
and find a line simmilar to
```
INFO:SbtClient:Sbt process with pid=47502 created
```

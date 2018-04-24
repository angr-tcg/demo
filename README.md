angr-tcg demo
=============

## Setup

Setup angr-dev:
* Download and set up [angr-dev](https://github.com/angr/angr-dev)
* Move to angr dir (`cd angr-dev/angr`)
* Add angr repo (`git remote add tcg https://github.com/angr-tcg/angr`)
* Fetch latest branches from tcg remote (`git fetch tcg`)
* Checkout tcg branch (`git checkout tcg`)

Setup pytcg:
* See [pytcg repo](https://github.com/angr-tcg/pytcg)

## Run demo

```
workon angr
python test.py
```

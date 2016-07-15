[![Build Status](https://travis-ci.org/rafaelhenrique/quake_log_parser.svg?branch=master)](https://travis-ci.org/rafaelhenrique/quake_log_parser)

# quake_log_parser
Quake log parser based on logfile of quake

**This project runs on Python>=3.4**

* Exercise extracted from: https://gist.github.com/alissonsales/2262296e199146d608df

## Installation

Create a virtualenv (use ``virtualenvwrapper``):

```
$ mkvirtualenv quake_log_parser
```

Install requirements:

```
$ make requirements
```

## Run tests

Full test with coverage:

```
$ make test
```

Test specific function or class:

```
$ make test-matching test=TestTask1
```

## Execute project

```
$ python run.py
```

# hello-world-bundle

[![Build Status](https://img.shields.io/github/workflow/status/batect/hello-world-bundle/Pipeline/master)](https://github.com/batect/hello-world-bundle/actions?query=workflow%3APipeline+branch%3Amaster)
[![License](https://img.shields.io/github/license/batect/batect.svg)](https://opensource.org/licenses/Apache-2.0)

A sample bundle for [batect](https://batect.dev).

It is intended to demonstrate a basic development experience for creating a bundle, including an automated test setup.

## Usage

### Setup

Add the following to your `batect.yml`:

```yaml
include:
  - type: git
    repo: https://github.com/batect/hello-world-bundle.git
    ref: 0.2.0
```

### Tasks

#### `say-hello`

Prints 'Hello world!' to the console.

## Development

Run `./batect --list-tasks` to see a list of available tasks for this project.

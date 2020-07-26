# hello-world-bundle

A sample bundle for [batect](https://batect.dev).

## Setup

Add the following to your `batect.yml`:

```yaml
include:
  - type: git
    repo: https://github.com/batect/hello-world-bundle.git
    ref: 0.1.0
```

## Tasks

### `say-hello`

Prints 'Hello world!' to the console.

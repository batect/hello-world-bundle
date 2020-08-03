# hello-world-bundle

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

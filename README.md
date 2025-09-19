# vsleep ⏳

A **verbose sleep** command-line tool with a progress bar.  
Think `sleep`, but you actually see the countdown.

---

## Features

- Drop-in replacement for `sleep` with **visual feedback**.
- Accepts raw seconds (`vsleep 60`) or flags (`-H`, `-m`, `-s`).
- Graceful interrupt handling with `Ctrl+C`.
- Prebuilt binaries for **Linux**, **macOS**, and **Windows**.

---

## Installation

### Prebuilt binary

Download the latest from [Releases](https://github.com/boraxpr/vsleep/releases):

```bash
curl -L https://github.com/boraxpr/vsleep/releases/download/v0.1.0/vsleep-linux-amd64 -o /usr/local/bin/vsleep
chmod +x /usr/local/bin/vsleep
vsleep -m 5
````

### Run from source

Requires Python 3.8+.

```bash
git clone https://github.com/boraxpr/vsleep.git
cd vsleep
pip install -r requirements.txt
python main.py -m 1
```

---

## Usage

```bash
# Sleep for 60 seconds
vsleep 60

# Sleep for 5 minutes
vsleep -m 5

# Sleep for 1 hour 30 minutes
vsleep -H 1 -m 30
```

Example output:

```
Sleeping |███████████▉                        | 45/120 [37%] in 45s (1.0/s)
```

Interrupt anytime with `Ctrl+C`.

---

## Development

Build a standalone binary with [Nuitka](https://nuitka.net/):

```bash
python -m nuitka main.py \
  --onefile \
  --standalone \
  --include-package=alive_progress \
  --include-package=grapheme \
  --include-package-data=alive_progress \
  --include-package-data=grapheme \
  --assume-yes-for-downloads \
  --output-filename=vsleep
```

---

## License

This project is licensed under the [MIT License](LICENSE).

### Third-Party Licenses

This project bundles the following MIT-licensed libraries:

* [alive-progress](https://github.com/rsalmei/alive-progress)
* [grapheme](https://github.com/alvinlindstam/grapheme)

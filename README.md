# Async Serial

This is example code showing you how to do asynchronous serial communication such as ASCII-over-serial, as is common in scientific settings. There is an accompanying article here:

* TBD

## Usage

This code relies on the experimental [`pyserial-asyncio`][pyserial-asyncio] library, which at this time only supports Unix-based systems (Linux, macOS, etc). As explained in the article, you'll need the tool [`socat`][socat] to create virtual serial ports so that you don't need a real device to try out the code.

### Install the dependencies

Clone this repository:

```bash
git clone https://github.com/zmitchell/async-serial.git
```

The dependencies are managed with [`pipenv`][pipenv], the new officially sanctioned packaging tool for Python. Install the dependencies via:

```bash
pipenv install
```

This will create a virtual environment and install the dependencies listed in the [`Pipfile`](Pipfile) into it.

### Run the code

You run the code in the virtual environment created by `pipenv` via

```bash
pipenv run python3 async_serial_protocol.py
```

or

```bash
pipenv run python3 async_serial_streams.py
```

## License

Licensed under either of

 * Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license ([LICENSE-MIT](LICENSE-MIT) or http://opensource.org/licenses/MIT)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally
submitted for inclusion in the work by you, as defined in the Apache-2.0
license, shall be dual licensed as above, without any additional terms or
conditions.

[pyserial-asyncio]: http://pyserial-asyncio.readthedocs.io/en/latest/index.html
[socat]: http://www.dest-unreach.org/socat/
[pipenv]: https://github.com/pypa/pipenv

# Contributing to this project

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to this project and its packages.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [tejas.prabhu29@gmail.com](mailto:tejas.prabhu29@gmail.com)

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for this project. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check already created issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.


## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :non-potable_water: `:non-potable_water:` when plugging memory leaks
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :green_heart: `:green_heart:` when fixing the CI build
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies
    * :shirt: `:shirt:` when removing linter warnings


### Python Styleguide

* Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) for general python coding guidelines.
* For Docstrings follow [PEP257](https://www.python.org/dev/peps/pep-0257/)
* Try to stick to using single quotes for string, except in cases where using double quotes is more readable 
* If you need to import lots of names from a module or package, and they won’t all fit in one line (without making the line too long), then use parentheses to spread the names across multiple lines.
* Use [Flake8](http://flake8.pycqa.org/en/latest/index.html) to check Python code style.
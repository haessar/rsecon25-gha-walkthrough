# CI workflows
Files with suffix `_X.<ext>` or `_XY.<ext>` found in `draft` directories throughout this repository correspond to lesson `X`, part `Y` as described below. For example, `.github/draft/ci_41.yml` is the first CI workflow for Lesson 4.

### Lesson 0 - Basic CI workflow
Incrementally build a simple CI yaml for fixed python version (3.10)

### Lesson 1 - Python version matrix
* User request Python 3.9 so implement a version matrix. Show all CI pass
* New user requests Python 3.12, add to version matrix. Show CI fail due to distutils
* Implement pyproject.toml with setuptools and show CI pass

### Lesson 2 - System dependency and caching
* Add “genomics” package with tests. Show CI failing due to lack of bedtools binary (despite running OK on local pytest)
* Add explicit bedtools dependency install and show CI pass, noting the fact that the workflow runs are starting to take a long time to complete. Add a note to the README to install bedtools if using Linux.
* Add apt caching and pip caching, run workflow and compare the time difference

### Lesson 3 - Type checking
* Decide to implement type checking with mypy, so add it to dev deps and pyproject.toml
* Note that linting errors with Flake8 extension in vscode are being picked up, yet no problems picked up by mypy extension, therefore assume good to push.
* Note that CI run fails due to type errors, make corrections to typing in sum_nested_ints, and show CI pass.
* Reflect that CI can catch things you might take for granted and avoid them going to prod.

### Lesson 4 - Version pinning
* Make “improvement” to our sum_nested_ints function to make use of numpy
* Add numpy unpinned to pyproject.toml and unknowingly add numpy attributes that are explicitly version >=2. CI workflow passes
* User complains that they get following error: `AttributeError: module 'numpy' has no attribute 'isdtype'. Did you mean: 'dtype’?`
* Note that user has numpy <2, do a CI run with their numpy version fixed and show repeated failure.
* Pin numpy to >=2 in pyproject.toml. Note the importance of versioning for reproduceability.
* Show creation of manual release

### Lesson 5 - OS matrix
* User complains that an error is thrown when using macOS.
* Add OS matrix with macOS and ubuntu. CI fails when trying to use the cache APT packages step
* Add an “if” gate so that it only runs with ubuntu. This time, it still fails but due to the tests.
* Add an additional “if” gate for macOS to ensure brew installs bedtools. Now CI passes.
* Add a note to the README to install bedtools if using macOS

# CD workflows

### Lesson 6 - Deploy to PyPI on release
* Write new CD workflow to build and deploy package to PyPI on published release.
* Talk through setting of token in GitHub interface.
* Create a new manual release v0.0.2 reflecting earlier change in README with a note saying: “compatibility with macOS”.
* Merge in Lesson 5 PR, confirming CI workflow passes.
* Watch as CD workflow is triggered and passes.
* Log in to PyPI to see new version of package
* Pitfall: Give example of “auto-versioning” that I attempted with Companion, and how it makes things inflexible.

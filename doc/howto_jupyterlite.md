# Init the site

```
$ uv run jupyter lite init --lite-dir lite_dir --contents contents --output-dir build
```

# Build the site

```
$ uv run jupyter lite build --lite-dir lite_dir --contents contents --output-dir build
```

# Serve locally to test

```
$ uv run jupyter lite serve --lite-dir lite_dir --output-dir build
```

# Build and serve

```
rm .jupyterlite.doit.db; rm build/;  uv run jupyter lite build --lite-dir lite_dir --contents contents --output-dir build ; uv run jupyter lite serve --lite-dir lite_dir --output-dir build
```

# Clean notebook output

$ uv run python -m nbconvert --ClearOutputPreprocessor.enabled=True --inplace contents/exercises/00_intro/*.ipynb **/*.ipynb
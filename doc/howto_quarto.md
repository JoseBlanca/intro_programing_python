# Quarto

## Creating a Website


```
$ quarto create project website mysite
```

Every website has a _quarto.yml config file that provides website options as well as defaults for HTML documents created within the site. 

If you are using VS Code or RStudio, the Preview button (VS Code), or Render button (RStudio), automatically renders and runs quarto preview in an embedded window.
You can also do the same thing from the Terminal if need be.

To render (but not preview) a website, use the quarto render command, which will render the website into the _site directory by default.

By default, all valid Quarto input files (.qmd, .ipynb, .md, .Rmd) in the project directory will be rendered, save for ones with:

- A file or directory prefix of . (hidden files)
- A file or directory prefix of _ (typically used for non top-level files, e.g. ones included in other files)
- Files named README.md or README.qmd

If you don’t want to render all of the target documents in a project, or you wish to control the order of rendering more precisely, you can add a project: render: [files] entry to your project metadata.

You can also use the prefix ! to ignore some files or directories in the render list.

### Linking

When creating links between pages in your site, you can provide the source file as the link target (rather than the .html file). You can also add hash identifiers (#) to the source file if you want to link to a particular section in the document. 

```
[about](about.qmd)
[about](about.qmd#section)
```

### Navigation

To add top-navigation to a website, add a navbar entry to the website config in _quarto.yml.

To add side navigation to a website, add a sidebar entry to the website section of _quarto.yml. 
There are two styles of side navigation available: “docked” which shows the navigation in a sidebar with a distinct background color, and “floating” which places it closer to the main body text.

If you have a website with several pages in a section or subsection, it is often convenient to offer the user the ability to navigate to the next page (or previous page) at the bottom of the page that they’ve just finished reading. You can enable this using:

```
website:
  page-navigation: true
```


## Quarto-live

To use the quarto-live extension in your own documents, run the following command in a terminal with a Quarto project as the working directory:

```
$ quarto add r-wasm/quarto-live
```

Set the live custom format in your Quarto document's YAML header.

```
---
format: live-html
---
```

The default rendering engine used by Quarto is jupyter.


Add an interactive code block into your document using {pyodide} (for Python code) code block types:


```{pyodide}
for x in range(5):
  print(x ** 2)
```

Setting edit: false will create a read-only cell.

Initial code cell contents will be automatically executed.
However, this autorun feature can be disabled by setting autorun: false.

```{webr}
#| autorun: false
123 + 456
```

Autocompletion code suggestions can be enabled with the code cell option completion: true.

```{webr}
#| completion: true
n_mean <- 120
n_sd <- 5

# Type "n_" to see context aware suggestions
```

Initial editor contents are stored and can be recalled at any time by clicking the “Start Over” button. If required, the “Start Over” button can be disabled by setting the startover: false cell option.

Setting the timelimit code cell option will set a time limit for code execution, in seconds.
The default time limit is 30 seconds and setting timelimit: 0 will disable the limit.

The editor height can be controlled through the min-lines and max-lines code cell options. 

To install packages as part of the document WebAssembly startup process, add a packages key to your document’s YAML header, under the key corresponding to your chosen WebAssembly engine.

```
---
format: live-html
pyodide:
  packages:
    - matplotlib
    - numpy
    - seaborn
---
```

### Create an Exercise

To designate a webr block as an exercise set the exercise cell option, giving it a unique label.

```{webr}
#| exercise: ex_1
1 + 2 + 3 + ______
```

Add hints and solutions to your exercise in the form of fenced blocks. The blocks should set the .hint or .solution class. Then, link the blocks to your exercise by setting the exercise attribute.

Linked exercises will display UI button elements to reveal hints and solutions. Multiple hints and solutions blocks can be linked; hints will be revealed progressively and all solutions at once.

You may prefer to show exercise hints and solutions in the form of a tabbed panel. This can be achieved by wrapping your fenced .hint and .solution blocks as part of a tabset panel block.

## render

To preview while creating the site:

$ quarto preview

To render the web site:

$ quarto render

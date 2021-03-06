---
output: github_document
bibliography: "references.bib"
---

<!-- README.md is generated from README.Rmd. Please edit that file -->



# Link Genius
Link Genius is an open-source and user-friendly record linkage/de-duplication tool. Browse its [source code](https://github.com/ISSACCorp-COS/LinkGenius), or read this document for a tutorial on using this tool for Record linkage.


# Introduction

Record linkage (or de-duplication) is an essential component of many projects and programs. If an individual is reported as a case by more than one data source, or reported at multiple times, it is vital to link records so that an individual will not be counted as multiple incident cases. There are powerful algorithms that can automatically detect matches in many situations. However, these software tools are often proprietary or require programming/coding skills that may not be available in every state or jurisdiction. The goal of this project is to provide a free and easy-to-use solution that can strengthen public health expertise, as this tool can be used across programs, and users who cannot write code can still use the same underlying packages and algorithms as more technically inclined users do.

Motivating example: CDC’s Autism and Developmental Disabilities Monitoring (ADDM) Network currently supports autism surveillance in different states. States receive information from various medical and educational providers, and states must link records to ensure each child is counted once and that all critical data elements are linked to the child’s record. Link Genius has been designed to support this use case without undue dependencies on future updates to SAS, Microsoft Windows, or other software that could jeopardize the functioning of the tool, and therefore the surveillance program.


# Project Goals

This section outlines the initial Link Genius project goals.

* The initial Link Genius project goal is to develop an R package that provides an R Shiny front-end to the high-performance record linking package fastLink:
    * Functionality to include the ability to facilitate linkage parameters (select variables used for linkages), identify data sets to be used, manually verify and review results, and export the resulting matched and non-matched data.
    * Documentation to instruct users on its use with a “getting started” vignette.
    * This public GitHub repository for the code, as well as for tracking issues and feature requests from end-users.


# Link Genius Tutorial

You can quickly and easily try out Link Genius via a demonstration Rmd here:  

[Tool Demo](https://github.com/ISSACCorp-COS/LinkGenius/blob/master/vignettes/LinkGeniusDemo_v0_2_0.Rmd)

TODO: The following documentation is missing and/or boilerplate. This is a work in progress.

The outline of this tutorial is as follows:

1. Create a new R package with R Studio
    - Set up the fundamental package infrastructure
2. Describe the package
    - Edit DESCRIPTION and readme files
3. Add data to package
    - Add raw data, preprocessing scripts, and an R data object
4. Create and add functions
    - Create and document functions
    - Dependencies
5. Document the package
    - Describe the package, its functions, and data, in a machine- and human-readable format



## Create functions

Functions in R packages are portable, such that others can install the package from their R console, load it, and start using the functions immediately. Packages can also depend on other packages (and be depended on), such that R automatically installs any requirements for your functions to work appropriately. Functions within R packages are documented in a standardized manner, and the documentation for a function can be viewed in R (e.g. try `?mean`) or online.

Learning and following R conventions for declaring functions has a pedagogical benefit to the researcher and may improve their practices. There is also a reuse benefit: Functions can be difficult to find in old scripts, but easy to find and load if they are called from an existing package. Thus, formally including one's functions in R packages facilitates reproducibility and sharing.

To include functions in your package, place the functions' scripts in files in the "R" directory. When you first created your package, that directory was created with an example `hello.R` script. Open that file in R Studio's text editor, and delete all the text above the function. Then, in the R Studio menu, click "Code" -> "Insert Roxygen Skeleton". That creates template documentation into the function's file, which you can then manually fill to describe your function. `exampleRPackage` includes an example function, whose source looks like this:


```
#' Personal greeting
#'
#' @description Greet a person and appropriately capitalize their name.
#'
#' @param name Your name (character string; e.g. "john doe").
#'
#' @return A character string, capitalized to title case.
#' @export
#'
#' @examples
#' hello("james bond")
hello <- function(name = "your name") {
    name <- stringr::str_to_title(name)
    print(paste("Hello,", name))
}
```

This function, as was the data set above, is documented with [roxygen2](https://roxygen2.r-lib.org/index.html) syntax. Many of the fields are similar from the above section on data documentation. Here, we also have `@param` fields, these describe what the function's arguments are. The `@return` field describes what the function will return. `@export` indicates that the function should be exported from your package; that is, made available when you attach the package with `library()`. There is also an `@examples` field that can include executable examples of how to use your function. Below the function's description is the actual code.

For more information on writing functions in R packages, see <http://r-pkgs.had.co.nz/r.html>.

## Finish documentation and build package

We are almost ready with the minimal example package. The only remaining steps are to finish documenting the package, and then to build and install it on your computer. 

Your package is now documented in the DESCRIPTION file, and the functions and data are documented in their respective files in the R/ directory. The data and functions were documented with [roxygen2](https://roxygen2.r-lib.org/) syntax, which must subsequently be translated into R's documentation files in the man/ directory, and their dependencies must be listed in the NAMESPACE file. 

Fortunately, you don't need to do that manually. First, ensure that R Studio generates documentation with roxygen. Go to Tools -> Project Options... -> Build Tools, and ensure that "Generate documentation with roxygen" is checked, and that "Automatically run roxygen when running install and restart" is checked in the subsequent "Configure" menu. Then, delete the two files, man/hello.Rd and NAMESPACE, which R Studio created automatically when you started your package. Finally, in R Studio's "Build" tab, click "Install and Restart".

Doing so automatically writes the documentation in man/, and the appropriate dependencies and your package's exported functions into the NAMESPACE file, which you subsequently never need to (or should) edit manually. After this, whenever you have edited your documentation, clicking "Install and Restart" will update the documentation files. To read more about documenting your data and functions, please visit <http://r-pkgs.had.co.nz/man.html>.

Having clicked "Install and Restart" you have also, rather obviously, installed your package and restarted R. If, following this tutorial, you created the `hello()` function and `exampleData` data sets, they are now available to you when the package is attached:


```r
library(linkGenius)
#> Error in library(linkGenius): there is no package called 'linkGenius'
hello("my name")
#> Error in hello("my name"): could not find function "hello"
head(exampleData)
#> Error in head(exampleData): object 'exampleData' not found
```

And you can view their help pages by prepending their names with a question mark:


```r
?hello
?exampleData
```


# Advanced (optional) steps

## Sharing the R package

### GitHub

The easiest way to share the package is to create the R package as a Git repository and share it on GitHub (@VuorreCuratingResearchAssets2018; <https://happygitwithr.com/>; <http://r-pkgs.had.co.nz/git.html>). If you followed the tutorial above, Git is already initialized in the package's repository. After connecting the local Git repository to GitHub, you can use R Studio's Git panel to stage, commit, push, and pull changes. Once the package's source code is pushed to GitHub, others can install the package. For example, you can install the example package created in this tutorial:


```r
devtools::install_github("mvuorre/exampleRPackage")
```

The above command, when executed in R, downloads and installs the `exampleRPackage` from GitHub user `mvuorre`. You can view this example R package's source code on GitHub: <https://github.com/mvuorre/exampleRPackage>.

### Open Science Framework

If you have connected the package's GitHub repository to an OSF project, you can also install the package from OSF, as done below for this example package:


```r
temporary_file <- tempfile(fileext = ".tar.gz")
download.file("https://osf.io/mqd6f/download", destfile = temporary_file)
install.packages(temporary_file, repos = NULL)
```

## Creating a website for the R package

Once the package's source code is hosted on GitHub, you can showcase its contents as a website. For example, you can view exampleRPackage's website at <https://mvuorre.github.io/exampleRPackage/>. To create websites from your packages, you need the [pkgdown](https://pkgdown.r-lib.org) R package [@wickham_pkgdown:_2017]. After installing that package, set up the required files for the website:


```r
use_pkgdown()
```

Then, To create the website, run:


```r
library(pkgdown)
build_site()
```

The website is now available at `docs/index.html`. You can open it and view it locally. However, you will certainly want to upload the website somewhere so that others can access it as well.  The easiest option is to host it on GitHub. 

Here, we assume that you have created the package in a local Git repository and have pushed the repository to GitHub. Push all the current changes to GitHub, and then go to the package's GitHub website, click "Settings", and scroll down to "GitHub Pages". There, click on the "Source" pull-down menu that currently says "None", and choose the "master branch /docs folder". Save the changes. After a little while, the page will be visible at https://username.github.io/packagename. For example, `exampleRPackage`'s website is at <https://mvuorre.github.io/exampleRPackage>.

There are many options for customizing the website; see <https://pkgdown.r-lib.org>.

## Other content 

Up to this point, our package has contained only code and data. However, typical research products make use of those to create narrative documents. R packages can contain vignettes, which show example uses of the package's data and functions, and are distributed with the package. However, many more kinds of narrative documents can be shared along the R package's source code, and included on the website, such as manuscript PDFs created with R Markdown.

Here, we create an article that shows an example analysis of the dataset contained in our exampleRPackage. When completed, the document will render as a subpage of the package's website (see above).


```r
usethis::use_article("Example-Analysis")
```

Then, after editing the contents of that file, re-run `build_site()`, and the document will be rendered as a webpage on the package's website.

The content we just added resulted in a website, but you could also include PDF manuscripts whose source code is R Markdown, or many other kinds of documents. For details, see the [pkgdown](https://hadley.github.io/pkgdown/) and [R Markdown](https://rmarkdown.rstudio.com/) websites.

# Further Reading

## Online Resources

- <http://r-pkgs.had.co.nz/>: Website of Hadley Wickham's R Packages book [@WickhamPackagesOrganizeTest2015].
- [Writing an R package from scratch](https://hilaryparker.com/2014/04/29/writing-an-r-package-from-scratch/): A short and good blog post on how to create minimal R packages
- [Writing R Extensions](https://cran.r-project.org/doc/manuals/r-release/R-exts.html): The official R documentation on writing R packages. This is the complete and definitive set of instructions on how to write R packages. It is almost unreadable in it's comprehensiveness, and unnecessary for small R packages.
- <https://happygitwithr.com/>: A guide for using Git with R and R Studio

## References


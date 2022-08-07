# STARBLAST VIEWER

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

> A tool that can augment papers with external information to improve reading experience.

## Table of Contents

- [Sections](#sections)
  - [Title](#title)
  - [Short Description](#short-description)
  - [Background](#background)
  - [Install](#install)
  - [Usage](#usage)
  - [Thanks](#thanks)
  - [Contributing](#contributing)
- [Documentation](#documentation)
  - [Scope](#scope) 
  - [UI](#ui)
  - [Features](#features)
  - [Database](#database)
  - [Machine Learning](#machine_learning)

## Sections

### Title
### Document viewer with enhanced reading expirence 
**Status:** Required.

**Requirements:**
- Title must match repository, folder and package manager names - or it may have another, relevant title with the repository, folder, and package manager title next to it in italics and in parentheses. For instance:

  ```markdown
  # Standard Readme Style _(standard-readme)_
  ```

  If any of the folder, repository, or package manager names do not match, there must be a note in the [Long Description](#long-description) explaining why.

**Suggestions:**
- Should be self-evident.

### Short Description
**Status:** Required.

**Requirements:**
- Must not have its own title.
- Must be less than 120 characters.
- Must not start with `> `
- Must be on its own line.
- Must match the description in the packager manager's `description` field.
- Must match GitHub's description (if on GitHub).

**Suggestions:**
- Use [gh-description](https://github.com/RichardLitt/gh-description) to set and get GitHub description.
- Use `npm show . description` to show the description from a local [npm](https://npmjs.com) package.

### Background
**Status:** Optional.

**Requirements:**
- Cover motivation.
- Cover abstract dependencies.
- Cover intellectual provenance: A `See Also` section is also fitting.

### Install
**Status:** Required by default, optional for [documentation repositories](#definitions).

**Requirements:**
- Code block illustrating how to install.

**Subsections:**
- `Dependencies`. Required if there are unusual dependencies or dependencies that must be manually installed.

**Suggestions:**
- Link to prerequisite sites for programming language: [npmjs](https://npmjs.com), [godocs](https://godoc.org), etc.
- Include any system-specific information needed for installation.
- An `Updating` section would be useful for most packages, if there are multiple versions which the user may interface with.

### Usage
**Status:** Required by default, optional for [documentation repositories](#definitions).

**Requirements:**
- Code block illustrating common usage.
- If CLI compatible, code block indicating common usage.
- If importable, code block indicating both import functionality and usage.

**Subsections:**
- `CLI`. Required if CLI functionality exists.

**Suggestions:**
- Cover basic choices that may affect usage: for instance, if JavaScript, cover promises/callbacks, ES6 here.
- If relevant, point to a runnable file for the usage code.

### Thanks
**Status**: Optional.

**Requirements:**
- Must be called `Thanks`, `Credits` or `Acknowledgements`.

**Suggestions:**
- State anyone or anything that significantly helped with the development of your project.
- State public contact hyper-links if applicable.

### Contributing
**Status**: Required.

**Requirements:**
- State where users can ask questions.
- State whether PRs are accepted.
- List any requirements for contributing; for instance, having a sign-off on commits.

**Suggestions:**
- Link to a CONTRIBUTING file -- if there is one.
- Be as friendly as possible.
- Link to the GitHub issues.
- Link to a Code of Conduct. A CoC is often in the Contributing section or document, or set elsewhere for an entire organization, so it may not be necessary to include the entire file in each repository. However, it is highly recommended to always link to the code, wherever it lives.
- A subsection for listing contributors is also welcome here.


## Documentation

### Scope
>Phase 1 document 1.2  

The goal of our project is to create a machine-learning assisted web application that improves news & research article reading for usersby providing them features which involve document editing, commenting and sharing with in a private space,along with automatic summarization of text,thereby augmenting a shift from a passive reading process to an interactive and collaborative experience.

### UI
- Index page  
- Log in / Sign up window  
- Readable articles list  
- Article reading interface  
- Auto-generated summation  
- Comment / Discussion section  

### Features
>Phase 1 document 2.2  

- Allow users to register and login their account.  
- Allow users to search papers discussion if they have been uploaded on the website in its user profile section.  
- Allow users to upload files locally and view them on the website.  
- Allow users to obtain a summary of the paper through machine learning (ML) and text analysis.  
- Automatically highlight important terms in the paper through ML and also allow the user to interactively highlight terms.  
- Allow users to communicate and participate in discussions around the papers via a system where the healthiest post obtains the highest points. (StackOverflow like). Those discussions are visible to all users.  
- Providing explanations and hyperlinks when cursor hovering over highlighted terms and  mentions.

### Database

### Machine Learning

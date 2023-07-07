# Python Template Repository for CI/CD with FormalM

This repository is a template for implementing a robust CI/CD pipeline 
with FormalM integration. **FormalM** integrates `GenAI` for **Code Security** and **Code
Quality Assurance** and is configured to work with GitHub's Continuous Integration.

FormalM currently supports `Python`, `Scala`, `Kotlin`, `Terraform`, and `Kubernetes`
and includes plugins for Test Coverage Checker (`scoverage`, `coverage`), Linters
(`scalafmt`, `scalafix`, `ruff`), and Misconfigurations Checker (`trivy`).

## How to create a new repository from this template

Follow the steps below to create a new repository using this template.

1. Click on the green "Use this template" button above the file list in this repository.
2. In the "Owner" dropdown, select the account you want to create the repository in.
3. Type a name and an optional description for your repository.
4. Choose to make your new repository either public or private.
5. If you want to include all branches for the new repository, click to select "Include all branches".
6. Click "Create repository from template".

After you've created your repository from this template, you can customize it as needed. Please configure the settings and parameters to match your project's needs.

## Sharing Scores with Dropbox

The aim of this project is to have a tool to automatize the process of generating an HTML code containing a music score, just ready to be shared in Wordpress.

This project has been desinged to be used together with the Wordpress Plugin: [Restricted User Access](https://es.wordpress.org/plugins/restrict-user-access/). 
More details in how to use in the [setup](#setup) section.

A score is composed by:
  - Title.
  - Link to the song of it.
  - A list of instruments with their corresponding Dropbox link.
  
### Setup

#### Dropbox API

This project uses the [Dropbox API for Python](https://www.dropbox.com/developers/documentation/python). 
So an App is needed (please check [here](https://www.dropbox.com/developers/apps/create)). Once the app is created, you will need to save the App key and App secret and setup them as enviroment variables:

```powershell
$env:DROPBOX_APP_KEY = "<APP_KEY>"
$env:DROPBOX_APP_SECRET = "<APP_SECRET>"
```

After that, we need to generate the `refresh_token`. For this, use the helper `dropboxAPI.py` module and follow the steps:

```powershell
> poetry run python src/dropboxAPI.py
```

Then, save it as another environment var:
```powershell
$env:DROPBOX_REFRESH_TOKEN = "<REFRESH_TOKEN>"
```

#### Restrict User Access

As mentioned before, this project has been designed to be used with the Wordpress Plugin [Restricted User Access](https://es.wordpress.org/plugins/restrict-user-access/).
Basically, the plugins offers the possibility to add access rules to the users, allowing them to see or not specific content by specifiying restrict-levels.

##### Config

The [application.conf](src/application.conf) contains a JSON object that contains a list of items. Each item have the following properties:
- `name`. Represents the name that will be used to identify in the folder the correct file/folder to be shared.
- `restrict-level`. Represents the restrict level defined in the plugin that reffers to this item. It will be necessary to use the same values as defined in the plugin.
- `publishName`. Represents the name that will appear in the Wordpress entry.

### Run

This project uses `Poetry`, so once configured, you can launch the program by calling:

```powershell
> poetry run python src/generateScore.py
```

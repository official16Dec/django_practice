## Django Learning
I have started learing about django-framework over python.

--------------------------------------------------------------------------------

### Configuring SSH to local project directory

**Check for existing SSH keys** :

 `>ls -al ~/.ssh`

  - If id_rsa, or id_ed25519 files are available in pair with .pub file, we need to skip next step.

**Generate a new SSH key pair** :

`>ssh-keygen -t ed25519 -C "abc123@gmail.com"`

 - Configure passphrases if required.

**Add SSH key to SSH Agent** :

 - Start the SSH agent in the background

   `>eval "$(ssh-agent -s)"`

 - Add private key to the ssh-agent

   `>ssh-add ~/.ssh/id_ed25519`

**Copy and add public to Git hosting** :

 - copy : `>cat ~/.ssh/id_ed25519.pub`

 - add/paste key to Git setting SSH section.


--------------------------------------------------------------------------------

 ### Creating first django project

 ***Setup virtual environment for the project***

 - `>python3 -m venv myenv`

 ***Activate virtual environment***

 - `source myenv/bin/activate`

 ***Install Django ***

 - `>pip install django`

 ***Perform create project command***

 - `>django-admin startproject projectname`

--------------------------------------------------------------------------------

### Creating app

- The django project is a collection of apps.
- We can create a separate modular app for a specific purpose.
- This app will contain, it's own business logic.

`>cd <main_project_directory>`
`>django-admin startapp <app_name>`

--------------------------------------------------------------------------------

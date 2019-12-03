{{ cookiecutter.role_title | title }}
=========
[![Galaxy](https://img.shields.io/badge/galaxy-{{ cookiecutter.galaxy_username }}.{{ cookiecutter.role_name }}-blue.svg?style=flat)](https://galaxy.ansible.com/{{ cookiecutter.galaxy_username }}/{{ cookiecutter.role_name }})
[![Build Status](https://travis-ci.com/{{ cookiecutter.travis_username }}/{{ cookiecutter.repo_name }}.svg?branch=master)](https://travis-ci.com/{{ cookiecutter.travis_username }}/{{ cookiecutter.repo_name }})

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `` | `` |  |


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

    - hosts: all
      roles:
         - {{ cookiecutter.galaxy_username }}.{{ cookiecutter.role_name }}

License
-------

{{ cookiecutter.license }}

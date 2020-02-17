# Ansible Role Cookiecutter #

This is a [cookiecutter project] for creating [Ansible roles]. It includes tests using [Molecule], [Ansible Lint], and [YAML Lint] to work with [Travis CI].

To use this, first install `cookiecutter`, then run `cookiecutter gh:samdoran/cookiecutter-ansible-role` and answer the prompts.

You can also use Molecule to initialize a new role using this template by running `molecule init template --url https://github.com/samdoran/cookiecutter-ansible-role`.

Or use Cookiecutter directly: `cookiecutter gh:samdoran/cookiecutter-ansible-role`.

## Development Workflow ##

Molecule uses Docker by default to spin up local containers for testing. I have created [several containers] that have Ansible installed and work well for testing Ansible roles. Feel free to use them or change to your own in `molecule/default/molecule.yml`.

To test your role, you first need to install Molecule by running `pip install molecule`, or using your package manager of choice.

Next, run `molecule test`. This will run the entire default test scenario, which creates a test container, runs the linters, runs the role twice, then destroys the container.

I frequently find I want to interact with the test instance rather than destroying it. To create a test instance, run your role, then leave the container running, run `molecule converge`. You can then interact with the container using `docker exec -it [container name] bash`. To rerun your role against the existing container, just run `molecule converge` again.

Once you are done with the container, run `molecule destroy` to remove it.

You can also run `molecule lint`, `molecule idempotence`, etc. to just run a specific test if desired.

### Customizing the Test ###

The default scenario runs `molecule/default/playbook.yml`. You can customize this playbook to suit your needs. I usually add some tasks before and after the role to do setup and validate services. I find this easier than writing tests in Python, which Molecule supports.

The `molecule.yml` file is setup to accept three environment variables:

`MOLECULE_DISTRIBUTION`: controls the distribution to test against
`MOLECULE_COMMAND`: the command to run inside the container
`MOLECULE_PLAYBOOK`: the name of the playbook to run

Valid values for `MOLECULE_DISTRIBUTION` based on how I name my test containers are:
    - centos6
    - centos7 (the default)
    - rhel6
    - rhel7
    - ubuntu14
    - ubuntu16
    - ubuntu18
    - debian8
    - debian9
    - fedora27
    - fedora28
    - fedora29

For example, to test your role on RHEL 7, run `env MOLECULE_DISTRIBUTION=rhel7 molecule test`.

## TravisCI ##

The included `.travis.yml` file uses a test matrix to test various distributions. It will run `molecule test` on each of the distributions.


## Thanks ##

A special thank you to [Jeff Geerling] for being a trailblazer with Molecule (and Ansible role testing in general). I would be lost without his amazing work.

[cookiecutter project]: https://github.com/audreyr/cookiecutter
[Ansible roles]:https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html
[molecule]: https://molecule.readthedocs.io
[Ansible Lint]: https://docs.ansible.com/ansible-lint/
[YAML Lint]:https://yamllint.readthedocs.io/en/stable/
[Travis CI]: https://travis-ci.org
[several containers]: https://quay.io/user/samdoran
[Jeff Geerling]: https://www.jeffgeerling.com/blog/2018/testing-your-ansible-roles-molecule

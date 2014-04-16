# Notes

```
kashrut init <- creates the config template for the project
kashrut validate <- validates yaml syntax, check if the files exists defined in the scripts/hooks sections
kashrut build <- runs the scripts defined under the build section (injects the required env variables)
kashrut deploy

```

## build

```
...
```

## deploy

using variables defined in kashrut.yml within the playbooks:

```
$ ansible-playbook --extra-vars "@/tmp/kashrut_exported_vars-201404161111.json"

---
- hosts: ${host}
  gather_facts: False
  user: root
  serial: ${kashrut.deploy.variables.serial}
  any_errors_fatal: ${kashrut.deploy.variables.any_errors_fatal}

tasks:
  - command: /bin/echo {{ kashrut.facts.service }}

  - include: {{ kashrut.deploy.hooks.pre }}
    vars:
      kashrut: {{ kashrut }}

    - name: kill -9
      action: shell kill -9 {{ running_pid.stdout }}
      when: down|failed and kashrut.deploy.variables.allow_kill9 != false
      ignore_errors: True

```

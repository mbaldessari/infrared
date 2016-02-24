---

options:
    verbose:
        help: 'Verbosity level'
        short: v
        action: count
        default: 0

subparsers:
    virsh:
        help: Provision systems using 'virsh'
        options:
            hypervisor:
                type: str
                help: Hypervisor
                required: True
            network:
                type: str
                help: Network
                default: default
            image:
                type: str
                help: An image to provision the systems with
                default: rhel
            topology:
                type: str
                help: 'Provision topology (default: __DEFAULT__)'
                default: all-in-one
            dry-run:
                action: store_true
                help: Only generate settings, skip the playbook execution stage
            cleanup:
                action: store_true
                help: Clean up environment at the end
            input-files:
                action: append
                type: str
                help: Settings file to be merged first
                short: n
            output-file:
                type: str
                short: o
                help: 'Name for the generated settings file (default: stdout)'
            extra-vars:
                action: append
                short: e
                help: Extra variables to be merged last
                type: str

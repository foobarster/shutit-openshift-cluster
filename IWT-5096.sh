/usr/bin/python /usr/local/bin/shutit build -l debug -d bash --echo --interactive 0 -m shutit-library/vagrant:shutit-library/virtualbox -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster test_config_dir test_multi_node_colocated_etcd -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster ose_version 3.6.1-1.0.008f2d5 -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster ose_major_version 3.6 -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster cookbook_branch master -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster chef_yum_cookbook_version latest -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster chef_iptables_cookbook_version latest -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster chef_selinux_policy_cookbook_version latest -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster chef_compat_resource_cookbook_version latest -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster inject_compat_resource false -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster chef_deploy_method solo -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster chef_deploy_containerized false -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster do_upgrade_13_14 false -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster do_upgrade_14_15 false -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster do_upgrade_15_36 false -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster do_upgrade_36_37 true -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster do_upgrade_37_39 false -s tk.shutit.shutit_openshift_cluster.shutit_openshift_cluster openshift_docker_image_version v3.6.1 --nocolor --echo 
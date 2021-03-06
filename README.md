# Ansible Linux based Java role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-java.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-java.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-java)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/41825.svg?style=flat)](https://galaxy.ansible.com/jetune/java)



Ansible role used to install Java (OpenJDK/Oracle JDK [not yet]) on Linux based Operating System.
<a href="https://www.kube-cloud.com/"><img width="300" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="200" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://openjdk.java.net/"><img width="250" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/OpenJDK_logo.svg/1280px-OpenJDK_logo.svg.png" /></a>

# Supported Java Implementation

* Open JDK 7/8/9/10/11/12

# Supported OS

* CentOS 6/7
* RedHat 6/7
* Ubuntu Trusty/Xenial/Bionic
* Debian Jessie/Strech

# Usage

* Install Role ``` ansible-galaxy install jetune.java ```
* use in your playbook
```
- hosts: all

  roles:
    - jetune.java

  vars:
    
    # If you want to install from a specific repository (e.g. for Ubuntu)
	__repositories:
 		- repo: ppa:openjdk-r/ppa
 		  
 		  # Possible Debian/CentOS/RedHat
		  os: Ubuntu
		  
		  # OS Major version
		  v_major: 18
	
 	# JDK packages to install from repo (Open JDK version 8, install alrenative with priority 100 )
 	from_repo: true
 	v_major: 8
 	alternative_priority: 100
 	implementation: OPENJDK
```

* Sample variables as follow

```

# Repository to use (for apt install)
__repositories:
 - repo: ppa:openjdk-r/ppa
   os: Debian
   v_major: 18

# JDK packages to install from repo version 8
from_repo: true
v_major: 8
alternative_priority: 100
implementation: OPENJDK
is_default: true

# JDK packages to install version 7 - update 75 - build 13
from_repo: false
implementation: OPENJDK
v_major: 7
v_minor: 75
build: 13
os: linux
arch: x64
date: 18_dec_2014
checksum: md5:538acd35c6cf6977fa19d21ab2c17b0a
alternative_priority: 200
is_default: false

# JDK packages to install version 8 - update 40 - build 25
from_repo: false
implementation: OPENJDK
v_major: 8
v_minor: 40
build: 25
os: linux
arch: x64
date: 10_feb_2015
checksum: md5:4980716637f353cfb27467d57f2faf9b
alternative_priority: 300
is_default: false

# JDK packages to install version 9 - update 0.4
from_repo: false
implementation: OPENJDK
v_major: 9
v_minor: 0.4
build:
os: linux
arch: x64
checksum: sha256:39362fb9bfb341fcc802e55e8ea59f4664ca58fd821ce956d48e1aa4fb3d2dec
alternative_priority: 400
is_default: false

# JDK packages to install version 10 - update 0.2 - build 13
from_repo: false
implementation: OPENJDK
v_major: 10
v_minor: 0.2
build: 13
hash: 19aef61b38124481863b1413dce1855f
os: linux
arch: x64
checksum: sha256:f3b26abc9990a0b8929781310e14a339a7542adfd6596afb842fa0dd7e3848b2
alternative_priority: 600
is_default: false

# JDK packages to install version 11 - update 0.1 - build 13
from_repo: false
implementation: OPENJDK
v_major: 11
v_minor: 0.1
build: 13
os: linux
arch: x64
checksum: sha256:7a6bb980b9c91c478421f865087ad2d69086a0583aeeb9e69204785e8e97dcfd
alternative_priority: 800
is_default: true

```

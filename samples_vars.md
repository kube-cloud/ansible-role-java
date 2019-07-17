---
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

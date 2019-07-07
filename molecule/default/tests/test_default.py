import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_installed(host):

    # Java Home Dirctory
    java_home = host.file('/usr/lib/jvm/java-11.0.1-openjdk')

    # Java Downloaded file
    java_archive = host.file('/tmp/openjdk-11.0.1.tar.gz')

    # Check that Java Archive exists
    assert java_archive.exists

    # Check that Java Archive is File
    assert java_archive.is_file

    # Check that Java Home exists
    assert java_home.exists

    # Check that Java Home is Directory
    assert java_home.is_directory

    # Run Java version
    java_version_run = host.run('java -version')

    # Assert that run os OK
    assert java_version_run.rc == 0

    # java -version result:
    #  openjdk version "1.8.0_161"
    #  OpenJDK Runtime Environment 18.9 (build 11.0.1+13)
    #  OpenJDK 64-Bit Server VM 18.9 (build 11.0.1+13, mixed mode)
    # First Split result:
    #  java version "1.8.0_161"
    # Second Split result
    #  "1.8.0_161"
    java_version = java_version_run.stderr.split('\n')[0].split(' ')[2]

    # Get Java implementation
    java_implementation = java_version_run.stderr.split('\n')[0].split(' ')[0]

    # Assert that version is Java 11
    assert java_version == "\"11.0.1\""

    # Assert that version is Java implementation is OpenJDK
    assert java_implementation == "openjdk"

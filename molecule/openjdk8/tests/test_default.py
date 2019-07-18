import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_installed(host):

    # Java expected version major
    java_major = '8'

    # Java expected version minor
    java_minor = '40'

    # Java expected version
    java_version = java_major + '.' + java_minor

    # Java expected implementation
    java_impl = 'openjdk'

    # Java Home Path
    java_home_path = '/usr/lib/jvm/java-{}-openjdk'.format(java_version)

    # Java archive file
    java_archive_path = '/tmp/openjdk-{}.tar.gz'.format(java_version)

    # Java Home Dirctory
    java_home = host.file(java_home_path)

    # Java Downloaded file
    java_archive = host.file(java_archive_path)

    # Check that Java Archive exists
    assert java_archive.exists

    # Check that Java Archive is File
    assert java_archive.is_file

    # Check that Java Home exists
    assert java_home.exists

    # Check that Java Home is Directory
    assert java_home.is_directory

    # Execute the Java Home Script
    assert host.run(". /etc/profile.d/java_home.sh").rc == 0

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
    java_version_ext = java_version_run.stderr.split('\n')[0].split(' ')[2]

    # Get Java implementation
    java_impl_ext = java_version_run.stderr.split('\n')[0].split(' ')[0]

    # Assert on version major
    assert java_version_ext.find(java_major) >= 0

    # Assert on version minor
    assert java_version_ext.find(java_minor) >= 0

    # Assert that version is Java implementation is OpenJDK
    assert java_impl_ext == java_impl

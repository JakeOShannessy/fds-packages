%global commit  71f02560677bb87dace8c81f2e5b817d24e70c46
%global repo    fds
%global this_version 6.7.5
%global version_suffix %{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 0}
%global gnu_string mpi_gnu_linux
%global intel_string impi_intel_linux
%global build_dir Build
%global openmpi_build_command ./make_fds.sh
%global intelmpi_build_command ./make_fds.sh

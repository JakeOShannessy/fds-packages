%global version_suffix %{this_version}
%global version_dir %{this_version}
%global script_suffix %{this_version}
%global arch_suffix _64
%{!?build_openmpi:%global build_openmpi 0}
%{!?build_mpich:%global build_mpich 0}
%{!?build_intelmpi:%global build_intelmpi 1}
%{!?build_docs:%global build_docs 0}
%global gnu_string mpi_gnu_linux
%global intel_string mpi_intel_linux
%global build_dir Build
%global openmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make MPIFORT=mpifort VPATH="../../Source" -f ../makefile "$target"
%global intelmpi_build_command \
 dir=$(pwd) \
 target=${dir##*/} \
 make MPIFORT=mpiifort VPATH="../../Source" -f ../makefile "$target"

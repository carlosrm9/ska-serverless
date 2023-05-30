# Fission Set-Up Guide
This is a installation guide to set up Fission platform in your local machine to run a catalog of radioastronomy functions. This installation need the following prerequisites:
* Docker. Installation instructions can be found at https://docs.docker.com/engine/install/ubuntu/
* KinD. Installation instructions can be found at https://kind.sigs.k8s.io/docs/user/quick-start/
* kubetcl. Installation instructions can be found at  https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

## Cluster Set-Up
Firstly, we create a cluster with the desired configuration to run Fission in it. We can use 

# Fission Set-Up Guide
This is a installation guide to set up Fission platform in your local machine to run a catalog of radioastronomy functions. 
## Prerequisites
This installation need the following prerequisites:
* Docker. Installation instructions can be found at https://docs.docker.com/engine/install/ubuntu/
* KinD. Installation instructions can be found at https://kind.sigs.k8s.io/docs/user/quick-start/
* kubetcl. Installation instructions can be found at  https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

## Cluster Set-Up
Firstly, we create a cluster with the desired configuration to run Fission in it. We can use `ska-severless/Fission/Cluster-SetUp/KinD/config.yaml` to create a KinD cluster where we mount a local folder with a cluster folder, (`/mnt/data` to `/host`). To do so, we run
```
kind create cluster --config config.yaml
```
We also want to have a common storage between all the nodes of the cluster, so all the functions can work together. This is done creating a Persistent Volume linked to `/host`. To do this, we use the files in `ska-severless/Fission/Cluster-SetUp/PV/` and run 
```
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
```

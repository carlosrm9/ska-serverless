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

## Fission
To install Fission follow the intructions at https://fission.io/docs/installation/. It has been tested to work fine with Helm installation.

## Environment and Functions creation
To install CASA functions, inside `ska-severless/Fission/casa-spec` run
```
fission spec apply --wait
```
This will trigger the package creation to build the environment and the different CASA functions along with its route to be run.
To install wsclean, `ska-severless/Fission/wsclean-spec` run
```
fission spec apply --wait
```

## Function usage
If you followed all the previous steps, now you can run any of the installed functions. All the files needed for the function to work must be at `/mnt/data` and there will be the output after running them. To run a function, first we need to set up a environment variable:
```
export FISSION_ROUTER=$(sudo kubectl get nodes -o jsonpath='{ $.items[0].status.addresses[?(@.type=="InternalIP")].address }'):$(sudo kubectl -n fission get svc router -o jsonpath='{ ...nodePort }')
```
Then, to run the function just run: 
```
curl -X POST -d "$(cat parameters-<function>.json)" -H "Content-Type: application/json" "http://${FISSION_ROUTER}/<function>"
```
where `<function>` is the name of the function to be run and parameters-<function>.json its parameters in a json file. Examples of parameters-<function>.json can be found at `ska-serverless/Fission/functions`.

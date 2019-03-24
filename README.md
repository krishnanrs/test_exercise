# test_exercise
A simple test exercise for deploying the [bookinfo](https://istio.io/docs/examples/bookinfo/) sample application in a kubenetes cluster, running unit tests, benchmarking using [wrk2](https://github.com/giltene/wrk2) and cleaning up the deployment.

## requirements
 - Local kubenetes deployment using [Docker Desktop] (https://www.docker.com/products/docker-desktop), [minikube] (https://kubernetes.io/docs/tasks/tools/install-minikube/) or equivalent
 - Python 2.7 or later
 - [wrk2](https://github.com/giltene/wrk2) for benchmarking the product page API
 
 ## How-To
 
 To run the full end-to-end suite for deploying the application, running unit tests, benchmarking and cleanup, simply invoke the `bookinfo.sh` wrapper script.
 
 ```
 $ ./bookinfo.sh 
Deploying Bookinfo application
[DEBUG] Running cmd: "kubectl -n default apply -f https://raw.githubusercontent.com/istio/istio/release-1.1/samples/bookinfo/platform/kube/bookinfo.yaml"
[DEBUG] Running cmd: "kubectl get deployments"
[DEBUG] Running cmd: "kubectl get service book-info"
[DEBUG] Running cmd: "kubectl -n default expose deployment productpage-v1 --type=NodePort --name=book-info"
Waiting 30 secs for application to initialize
[INFO] Running unit tests
[INFO] Running benchmark tests
Running 30s test @ http://localhost:30570/api/v1/products
  2 threads and 100 connections
  Thread calibration: mean lat.: 4187.743ms, rate sampling interval: 15515ms
  Thread calibration: mean lat.: 4179.274ms, rate sampling interval: 15499ms
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    17.42s     5.06s   26.20s    56.72%
    Req/Sec   126.00      0.00   126.00    100.00%
  Latency Distribution (HdrHistogram - Recorded Latency)
 50.000%   17.37s 
 75.000%   21.81s 
 90.000%   24.64s 
 99.000%   26.00s 
 99.900%   26.18s 
 99.990%   26.20s 
 99.999%   26.21s 
100.000%   26.21s 

  Detailed Percentile spectrum:
       Value   Percentile   TotalCount 1/(1-Percentile)

    8953.855     0.000000            3         1.00
   10534.911     0.100000          505         1.11
   12107.775     0.200000         1006         1.25
       .
     <snip>
       .
     718.847     0.999756         5010      4096.00
     718.847     0.999780         5010      4551.11
     729.599     0.999805         5011      5120.00
     729.599     1.000000         5011          inf
#[Mean    =      396.916, StdDeviation   =       76.441]
#[Max     =      729.088, Total count    =         5011]
#[Buckets =           27, SubBuckets     =         2048]
----------------------------------------------------------
  7477 requests in 30.00s, 3.86MB read
Requests/sec:    249.19
Transfer/sec:    131.65KB

[DEBUG] Running cmd: "kubectl get service book-info"
[DEBUG] Running cmd: "kubectl -n default delete service book-info"
[DEBUG] Running cmd: "kubectl delete -n default -f https://raw.githubusercontent.com/istio/istio/release-1.1/samples/bookinfo/platform/kube/bookinfo.yaml"
```

To invoke individual steps and to test it out, use the `kude-deploy` python script with the appropriate options:

```
$ python kube-deploy -h
usage: kube-deploy [-h] [-v] [-n NAMESPACE] [-f DEPLOYMENTFILE]
                   [-s SERVICENAME] [-e NODEPORT]
                   action

Launch or delete kubernetes services using yaml resource templates

positional arguments:
  action                deploy, delete or show a deployment

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Be more verbose about what kube-deploy is doing.
                        (default: False)
  -n NAMESPACE, --namespace NAMESPACE
                        The namespace to use for deployments. Defaults to
                        default namespace (default: default)
  -f DEPLOYMENTFILE, --deploymentfile DEPLOYMENTFILE
                        File or URL containing the application deployment
                        template (default: None)
  -s SERVICENAME, --servicename SERVICENAME
                        Service name to use for the deployment (default: book-
                        info)
  -e NODEPORT, --nodeport NODEPORT
                        Expose deployment with a Nodeport (default: None)
  ```

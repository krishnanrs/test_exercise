# test_exercise
A simple test exercise for deploying the [bookinfo](https://istio.io/docs/examples/bookinfo/) sample application in a kubenetes cluster, running unit tests, benchmarking using [wrk2](https://github.com/giltene/wrk2) and cleaning up the deployment.

## requirements
 - Local kubenetes deployment using [Docker Desktop] (https://www.docker.com/products/docker-desktop), [minikube] (https://kubernetes.io/docs/tasks/tools/install-minikube/) or equivalent
 - Python 2.7 or later
 - [wrk2](https://github.com/giltene/wrk2) for benchmarking the product page API
 
 ## How-To
 
 To run the full end-to-end suite for deploying the application, running unit tests, benchmarking and cleanup, simply invoke the `bookinfo.sh` wrapper script.
 
 ```$ ./bookinfo.sh 
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
   13967.359     0.300000         1506         1.43
   15802.367     0.400000         2008         1.67
   17367.039     0.500000         2506         2.00
   18137.087     0.550000         2759         2.22
   19021.823     0.600000         3008         2.50
   19922.943     0.650000         3259         2.86
   20905.983     0.700000         3508         3.33
   21807.103     0.750000         3764         4.00
   22315.007     0.775000         3886         4.44
   22790.143     0.800000         4010         5.00
   23166.975     0.825000         4136         5.71
   23543.807     0.850000         4260         6.67
   24231.935     0.875000         4386         8.00
   24477.695     0.887500         4453         8.89
   24641.535     0.900000         4512        10.00
   24772.607     0.912500         4573        11.43
   24969.215     0.925000         4646        13.33
   25165.823     0.937500         4700        16.00
   25247.743     0.943750         4737        17.78
   25313.279     0.950000         4764        20.00
   25427.967     0.956250         4796        22.86
   25542.655     0.962500         4828        26.67
   25591.807     0.968750         4856        32.00
   25657.343     0.971875         4872        35.56
   25739.263     0.975000         4891        40.00
   25772.031     0.978125         4903        45.71
   25837.567     0.981250         4918        53.33
   25903.103     0.984375         4934        64.00
   25919.487     0.985938         4941        71.11
   25952.255     0.987500         4950        80.00
   25968.639     0.989062         4957        91.43
   26017.791     0.990625         4968       106.67
   26050.559     0.992188         4974       128.00
   26066.943     0.992969         4979       142.22
   26083.327     0.993750         4980       160.00
   26099.711     0.994531         4984       182.86
   26116.095     0.995313         4989       213.33
   26132.479     0.996094         4996       256.00
   26132.479     0.996484         4996       284.44
   26132.479     0.996875         4996       320.00
   26148.863     0.997266         4998       365.71
   26165.247     0.997656         5004       426.67
   26165.247     0.998047         5004       512.00
   26165.247     0.998242         5004       568.89
   26165.247     0.998437         5004       640.00
   26181.631     0.998633         5006       731.43
   26181.631     0.998828         5006       853.33
   26198.015     0.999023         5010      1024.00
   26198.015     0.999121         5010      1137.78
   26198.015     0.999219         5010      1280.00
   26198.015     0.999316         5010      1462.86
   26198.015     0.999414         5010      1706.67
   26198.015     0.999512         5010      2048.00
   26198.015     0.999561         5010      2275.56
   26198.015     0.999609         5010      2560.00
   26198.015     0.999658         5010      2925.71
   26198.015     0.999707         5010      3413.33
   26198.015     0.999756         5010      4096.00
   26198.015     0.999780         5010      4551.11
   26214.399     0.999805         5011      5120.00
   26214.399     1.000000         5011          inf
#[Mean    =    17416.073, StdDeviation   =     5058.621]
#[Max     =    26198.016, Total count    =         5011]
#[Buckets =           27, SubBuckets     =         2048]
----------------------------------------------------------

  Latency Distribution (HdrHistogram - Uncorrected Latency (measured without taking delayed starts into account))
 50.000%  379.39ms
 75.000%  439.55ms
 90.000%  487.17ms
 99.000%  644.61ms
 99.900%  710.14ms
 99.990%  718.85ms
 99.999%  729.60ms
100.000%  729.60ms

  Detailed Percentile spectrum:
       Value   Percentile   TotalCount 1/(1-Percentile)

     269.823     0.000000            1         1.00
     318.463     0.100000          506         1.11
     336.639     0.200000         1013         1.25
     351.231     0.300000         1506         1.43
     363.519     0.400000         2009         1.67
     379.391     0.500000         2508         2.00
     388.863     0.550000         2757         2.22
     400.383     0.600000         3007         2.50
     412.927     0.650000         3265         2.86
     424.191     0.700000         3508         3.33
     439.551     0.750000         3762         4.00
     445.183     0.775000         3884         4.44
     450.303     0.800000         4015         5.00
     455.935     0.825000         4135         5.71
     462.847     0.850000         4267         6.67
     472.063     0.875000         4387         8.00
     478.463     0.887500         4449         8.89
     487.167     0.900000         4510        10.00
     495.103     0.912500         4576        11.43
     507.391     0.925000         4636        13.33
     526.335     0.937500         4698        16.00
     540.671     0.943750         4730        17.78
     551.423     0.950000         4761        20.00
     571.903     0.956250         4792        22.86
     590.847     0.962500         4824        26.67
     601.599     0.968750         4857        32.00
     606.207     0.971875         4871        35.56
     611.327     0.975000         4887        40.00
     616.447     0.978125         4904        45.71
     622.079     0.981250         4919        53.33
     628.735     0.984375         4934        64.00
     631.295     0.985938         4942        71.11
     634.879     0.987500         4949        80.00
     642.559     0.989062         4958        91.43
     649.727     0.990625         4965       106.67
     654.847     0.992188         4972       128.00
     665.599     0.992969         4976       142.22
     668.671     0.993750         4980       160.00
     674.815     0.994531         4984       182.86
     693.759     0.995313         4988       213.33
     700.415     0.996094         4992       256.00
     700.927     0.996484         4994       284.44
     703.487     0.996875         4996       320.00
     705.535     0.997266         4998       365.71
     707.071     0.997656         5001       426.67
     709.119     0.998047         5002       512.00
     709.631     0.998242         5004       568.89
     709.631     0.998437         5004       640.00
     710.143     0.998633         5006       731.43
     710.143     0.998828         5006       853.33
     716.799     0.999023         5007      1024.00
     716.799     0.999121         5007      1137.78
     717.823     0.999219         5008      1280.00
     717.823     0.999316         5008      1462.86
     718.335     0.999414         5009      1706.67
     718.335     0.999512         5009      2048.00
     718.335     0.999561         5009      2275.56
     718.847     0.999609         5010      2560.00
     718.847     0.999658         5010      2925.71
     718.847     0.999707         5010      3413.33
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
[DEBUG] Running cmd: "kubectl delete -n default -f https://raw.githubusercontent.com/istio/istio/release-1.1/samples/bookinfo/platform/kube/bookinfo.yaml"```

To invoke individual steps and to test it out, use the `kude-deploy` python script with the appropriate options:
```$ python kube-deploy -h
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
                        Expose deployment with a Nodeport (default: None)```

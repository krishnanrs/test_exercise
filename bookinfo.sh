#!/bin/bash

function deploy()
{
    python kube-deploy -v deploy -f https://raw.githubusercontent.com/istio/istio/release-1.1/samples/bookinfo/platform/kube/bookinfo.yaml -e productpage-v1
    if [ $? -ne 0 ]; then
        return 1
    else
        return 0
    fi
}

function cleanup()
{
    python kube-deploy -v delete -f https://raw.githubusercontent.com/istio/istio/release-1.1/samples/bookinfo/platform/kube/bookinfo.yaml
    if [ $? -ne 0 ]; then
        echo "Failed to delete the Bookinfo application"
        echo "Please check the logs and retry the deployment"
        exit 4
    else:
        echo "Cleaned up Bookinfo application"
    fi
}

echo "Deploying Bookinfo application"
deploy
if [ $? -ne 0 ]; then
    echo "Failed to deploy Bookinfo application"
    echo "Please check the logs and retry the deployment"
    exit 1
fi

echo "Waiting 30 secs for application to initialize"
sleep 30
python kube-deploy run-tests
if [ $? -ne 0 ]; then
    echo "Failed running Unit tests against Bookinfo application"
    echo "Please check the logs and retry the deployment. Cleaning up..."
    cleanup
    exit 2
fi

python kube-deploy benchmark
if [ $? -ne 0 ]; then
    echo "Failed running Benchmark tests against Bookinfo APIs"
    echo "Please check the logs and retry the deployment"
    cleanup
    exit 3
fi

cleanup

# CSIT Mini Challenge 2024 Nov | Kubernetes

## Task 1: The Murder Weapon
Peter had a gaping hole in his stomach yet there were barely any blood splatters around the
room. Detective Kay suggests that Peter had been murdered before he was moved to the bed. What could have caused such a gruesome wound? Search the house and find the murder
weapon. Help Detective Kay search the house with the investigation unit and find the missing murder weapon. Your Task:
- Follow the instructions to create a Kubernetes Deployment
- Find clues about the murder weapon in the Deployment Pod
- Deploy the Pod successfully to retrieve the murder weapon flag in its logs

Create a Deployment with the name investigation-unit using the image sachua/task-1:v0.0.1 in the default namespace.

```
kubectl create deployment investigation-unit --image=sachua/task-1:v0.0.1 --namespace=default
$ deployment.apps/investigation-unit created
```

Nice job! You have successfully configured your pod and found the weapon!

You can view the weapon by checking the logs on the pod using the command:
```
kubectl logs -n default deployment/investigation-unit
```

Retrieve the Flag by running
```
kubectl logs -n default deployment/investigation-unit | sed 's/.*: //'
```

Save the output for submission!

```
kubectl logs -n default deployment/investigation-unit
$ THE WEAPON IS A: Katana

kubectl logs -n default deployment/investigation-unit | sed 's/.*: //'
$ Katana
```

___
<div style="page-break-after: always;"></div>

## Task 2: An Elusive Fingerprint
You found the weapon tucked neatly under the carpet in the study next door, but will there be a DNA lead? If we can retrieve a strand of hair or even a partial fingerprint, maybe we will be closer to finding the murderer! Help Detective Kay and the analysis unit uncover any possible DNA leads. Your Task:
- Follow the instructions to create a Kubernetes Deployment and mount the encrypted file to the Pod
- Deploying the Pod successfully will run the program to decrypt the file, allowing you to retrieve the DNA evidence by checking its logs
- Obtain the flag by generating an MD5 hash of the DNA

The encrypted file is located at /mnt/data on this node's filesystem. Create a Deployment with the name analysis-unit using the image sachua/task-2:v0.0.1 in the default namespace. Mount the directory /mnt/data to the container.

```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
	name: analysis-unit
	namespace: default
spec:
	replicas: 1
	selector:
		matchLabels:
			app: analysis-unit
	template:
		metadata:
			labels:
				app: analysis-unit
		spec:
			containers:
				- name: analysis-container
				image: sachua/task-2:v0.0.1
				volumeMounts:
					- mountPath: "/mnt/data"
					name: pv-storage
			volumes:
				- name: pv-storage
				hostPath:
					path: "/mnt/data"
EOF
```

```
kubectl logs -n default deployment/analysis-unit | sed 1d | md5sum | awk '{print $1}'
$ c33b083af53411171863163a79f6450c
```

___
<div style="page-break-after: always;"></div>

## Task 3: Identify The Culprit
The murder weapon and a fingerprint are exactly what we need. Is it enough to narrow down the culprit? Help Detective Kay connect the dots by transmitting the first two pieces of evidence to the command center and deduce your culprit! Your Task:
- Expose port 80 on the previous two Kubernetes Deployments as Services
- Follow the instructions to create a new Kubernetes Deployment
- Ensure the new Kubernetes Deployment can access port 80 of the two Kubernetes Services
- Deploying the Pod successfully allows you to retrieve the culprit flag by checking its logs

```
kubectl create deployment command-center --image=sachua/task-3:v0.0.1 --namespace=default
$

kubectl expose deploy investigation-unit --name investigation-unit --port 80
$

kubectl expose deploy analysis-unit --name analysis-unit --port 80
$

kubectl logs -n default deployment/command-center
$ THE CULPRIT IS: Tan Ah Kow

controlplane $ kubectl logs -n default deployment/command-center | grep -im 1 culprit | sed 's/.*: //'
$ Tan Ah Kow
```

___

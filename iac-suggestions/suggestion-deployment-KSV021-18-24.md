kubernetes/configs/deployment.yaml

#### Runs with low group ID

The problem was that the container 'nginx' of Deployment 'nginx-deployment' was not set to run with a group ID greater than 10000. To solve this, I added the 'runAsGroup' field to the 'securityContext' section of the container configuration and set it to 10001.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 0
          runAsGroup: 10001
```
kubernetes/configs/deployment.yaml

#### Runs with low user ID

The problem was that the container 'nginx' of Deployment 'nginx-deployment' was running with a user ID of 0, which is the root user. This can lead to conflicts with the host's user table. To solve this, I set the 'securityContext.runAsUser' to 10001, which is an integer greater than 10000.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 10001
```
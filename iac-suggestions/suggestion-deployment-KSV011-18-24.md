kubernetes/configs/deployment.yaml

#### CPU not limited

The problem was that the CPU limit was not set for the container 'nginx' of the Deployment 'nginx-deployment'. To solve this, I added the 'resources.limits.cpu' field under the 'containers[].resources' section and set the limit value to '0.5'.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 0
        resources:
          limits:
            cpu: 0.5
```
kubernetes/configs/deployment.yaml

#### Runs as root user

'runAsNonRoot' forces the running image to run as a non-root user to ensure least privileges.
Container 'nginx' of Deployment 'nginx-deployment' should set 'securityContext.runAsNonRoot' to true
Set 'containers[].securityContext.runAsNonRoot' to true.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 0
          runAsNonRoot: true
```
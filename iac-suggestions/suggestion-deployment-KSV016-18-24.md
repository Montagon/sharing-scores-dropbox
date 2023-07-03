kubernetes/configs/deployment.yaml

#### Memory requests not specified

The problem was that the memory requests were not specified for the 'nginx' container. To solve this, I added the 'resources.requests.memory' field under the 'containers[].resources' section and set it to '256Mi'. This allows the scheduler to make better decisions about resource allocation and contention.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 0
        resources:
          requests:
            memory: 256Mi
```
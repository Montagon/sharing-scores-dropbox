kubernetes/configs/deployment.yaml

#### CPU requests not specified

The problem was that the CPU requests were not specified for the 'nginx' container of the 'nginx-deployment' Deployment. To solve this, I added the 'resources.requests.cpu' field under the 'containers' section and set it to '100m' to request 100 milliCPU.

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
            cpu: '100m'
```
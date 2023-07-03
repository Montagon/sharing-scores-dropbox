kubernetes/configs/deployment.yaml

#### Root file system is not read-only

The problem was that the root file system was not read-only. To solve this, we added the 'readOnlyRootFilesystem' field to the 'securityContext' section of the 'nginx' container and set it to 'true'.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 0
          readOnlyRootFilesystem: true
```
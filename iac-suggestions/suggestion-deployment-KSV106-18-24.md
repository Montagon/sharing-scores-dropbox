kubernetes/configs/deployment.yaml

#### Container capabilities must only include NET_BIND_SERVICE

The problem was that the container was not dropping all capabilities and only adding the NET_BIND_SERVICE capability. To solve this, I added the 'capabilities' section under 'securityContext' and set 'drop' to 'ALL' and 'add' to 'NET_BIND_SERVICE'.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 0
          capabilities:
            drop:
              - ALL
            add:
              - NET_BIND_SERVICE
```
kubernetes/configs/deployment.yaml

#### Default Seccomp profile not set

The problem was that the seccomp profile was not set. To solve it, I added the 'seccompProfile' field under 'securityContext' and set its 'type' to 'RuntimeDefault'.

```suggestion
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
        securityContext:
          allowPrivilegeEscalation: false
          runAsUser: 0
          seccompProfile:
            type: RuntimeDefault
```
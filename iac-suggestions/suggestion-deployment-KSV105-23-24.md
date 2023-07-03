kubernetes/configs/deployment.yaml

#### Containers must not set runAsUser to 0

The problem was that the 'runAsUser' value was set to 0, which means the container was running with root privileges. To solve this, I changed the 'runAsUser' value to 1000, which is a non-zero integer and ensures that the container does not run as root.

```suggestion
          allowPrivilegeEscalation: false
          runAsUser: 1000
```
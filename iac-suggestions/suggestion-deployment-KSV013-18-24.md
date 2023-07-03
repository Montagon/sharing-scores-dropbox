kubernetes/configs/deployment.yaml

#### Image tag ':latest' used

The problem was that the image tag was not specified for the container 'nginx' of Deployment 'nginx-deployment'. I solved it by adding the image tag ':1.16' to the image field.

```suggestion
- name: nginx
  image: nginx:1.16
  ports:
  - containerPort: 80
  securityContext:
    allowPrivilegeEscalation: false
    runAsUser: 0
```
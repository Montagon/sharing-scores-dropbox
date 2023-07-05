iac-suggestions/suggestion-deployment-KSV003-5-6.md

#### Default capabilities not dropped

The problem is that the container 'nginx' of Deployment 'nginx-deployment' should drop all default capabilities and add only those that are needed for its execution. To solve this, we need to add 'ALL' to 'securityContext.capabilities.drop' in the configuration file.

```suggestion
Add 'ALL' to containers[].securityContext.capabilities.drop.
```
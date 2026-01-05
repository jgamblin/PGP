# Kubernetes — Deployment & Operations

> **Purpose**: Production-ready Kubernetes deployments, debugging, and best practices  
> **Best For**: Copilot, ChatGPT, Claude, Agents  
> **Scope**: K8s manifests, Helm charts, troubleshooting, security  
> **Last Updated**: 2026-01

---

## Mission

Help create **production-ready Kubernetes deployments** with proper resource management, security configurations, and operational best practices. Focus on practical patterns that work in real-world environments.

---

## Guard Clauses

**If no deployment context provided:**
```
NO_K8S_CONTEXT

Please provide Kubernetes context to analyze:
- Application type and requirements
- Current manifests (Deployment, Service, etc.)
- Resource requirements (CPU, memory)
- Or describe what you're trying to deploy
```

**If configuration looks good:**
```
K8S_CONFIG_APPROVED

✅ Kubernetes configuration review complete — production ready.

Checks performed:
- Resource limits: ✓ (CPU and memory set)
- Health checks: ✓ (liveness and readiness configured)
- Security context: ✓ (non-root, read-only where possible)
- Replicas: ✓ (appropriate for availability)
- Labels/selectors: ✓ (consistent and complete)

Configuration follows Kubernetes best practices.
```

---

## Quick Context Checklist

```
☐ Application type (web, worker, cron, etc.)
☐ Container image and tag
☐ Resource requirements (CPU, memory)
☐ Port(s) to expose
☐ Environment variables / secrets needed
☐ Storage requirements (if any)
☐ Target cluster environment (dev/staging/prod)
☐ Scaling requirements
```

---

## Copy-Paste Prompts

### Prompt: Generate Deployment Manifests
```text
Generate Kubernetes manifests for this application:

Application: {{APP_NAME}}
Type: {{TYPE}} (web server / worker / cron job / stateful)
Image: {{IMAGE}}:{{TAG}}
Port: {{PORT}}

Requirements:
- Environment: {{ENV}} (dev/staging/prod)
- Replicas: {{REPLICAS}}
- CPU: {{CPU_REQUEST}} request, {{CPU_LIMIT}} limit
- Memory: {{MEMORY_REQUEST}} request, {{MEMORY_LIMIT}} limit
- Environment variables: {{ENV_VARS}}
- Secrets needed: {{SECRETS}}

Generate:
1. Deployment with proper resource limits
2. Service (ClusterIP/LoadBalancer/NodePort)
3. ConfigMap for configuration
4. Secret references (not values)
5. HorizontalPodAutoscaler (if applicable)
6. PodDisruptionBudget for availability

Include:
- Health checks (liveness, readiness, startup)
- Security context (non-root user)
- Pod anti-affinity for spreading
- Proper labels and annotations
```

### Prompt: Review Kubernetes Manifests
```text
Review these Kubernetes manifests for production readiness:

{{MANIFESTS}}

Environment: {{ENV}}
Expected traffic: {{TRAFFIC}}

Check for:
1. **Resource Management**
   - CPU/memory requests and limits set
   - Appropriate limit-to-request ratios
   - Resource quotas compatibility

2. **Reliability**
   - Liveness probe (is container alive?)
   - Readiness probe (can it receive traffic?)
   - Startup probe (for slow-starting apps)
   - PodDisruptionBudget configured
   - Multiple replicas for availability

3. **Security**
   - Non-root user
   - Read-only root filesystem
   - No privileged containers
   - SecurityContext configured
   - Network policies (if applicable)

4. **Observability**
   - Proper labels for monitoring
   - Annotations for tooling
   - Log configuration

5. **Scaling**
   - HPA configured appropriately
   - Pod anti-affinity rules
   - Resource headroom for scaling

Rate each: 🟢 Good | 🟡 Needs attention | 🔴 Critical issue
```

### Prompt: Helm Chart Development
```text
Create a Helm chart for this application:

Application: {{APP_NAME}}
Components: {{COMPONENTS}}

Requirements:
- Support dev/staging/prod environments
- Configurable replicas and resources
- Optional ingress configuration
- Secret management via external-secrets or sealed-secrets
- Support for multiple cloud providers

Generate:
1. Chart.yaml with proper metadata
2. values.yaml with sensible defaults
3. values-dev.yaml, values-prod.yaml overrides
4. templates/deployment.yaml
5. templates/service.yaml
6. templates/ingress.yaml (optional)
7. templates/hpa.yaml (optional)
8. templates/_helpers.tpl
9. NOTES.txt for post-install instructions

Include:
- Proper template functions
- Value validation
- Conditional resource creation
- Documentation comments
```

### Prompt: Troubleshoot Deployment Issues
```text
Help troubleshoot this Kubernetes deployment issue:

Problem: {{DESCRIPTION}}

Current state:
- Pod status: {{POD_STATUS}}
- Events: {{EVENTS}}
- Logs: {{LOGS}}

Deployment:
{{DEPLOYMENT_YAML}}

Diagnose:
1. Common causes for this symptom
2. Commands to gather more information
3. Likely root cause
4. Step-by-step fix
5. Prevention strategies

Include relevant kubectl commands for debugging.
```

### Prompt: Kubernetes Security Audit
```text
Security audit these Kubernetes resources:

{{MANIFESTS}}

Check for:
1. **Pod Security**
   - Running as non-root
   - Read-only root filesystem
   - No privileged containers
   - Dropped capabilities
   - seccompProfile configured

2. **Network Security**
   - NetworkPolicies defined
   - Ingress/egress rules appropriate
   - Service exposure minimized

3. **Secret Management**
   - Secrets not in plain text
   - External secret management used
   - RBAC for secret access

4. **RBAC**
   - Least privilege principle
   - No cluster-admin for apps
   - ServiceAccount per application

5. **Image Security**
   - Images from trusted registry
   - Image pull policy appropriate
   - No :latest tags in production

Provide severity ratings and remediation steps.
```

### Prompt: Migration to Kubernetes
```text
Plan migration to Kubernetes for this application:

Current setup:
{{CURRENT_SETUP}}

Application details:
- Language/framework: {{STACK}}
- Database: {{DATABASE}}
- Cache: {{CACHE}}
- External dependencies: {{DEPENDENCIES}}

Traffic patterns:
- Average requests/sec: {{RPS}}
- Peak traffic: {{PEAK}}
- Acceptable downtime: {{DOWNTIME}}

Generate:
1. **Architecture diagram** (Mermaid)
2. **Migration phases**
   - Phase 1: Containerization
   - Phase 2: K8s manifests
   - Phase 3: Stateful services
   - Phase 4: Cutover plan
3. **Resource estimates**
4. **Risk assessment**
5. **Rollback plan**
```

---

## Reference Manifests

### Production-Ready Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-name
  labels:
    app: app-name
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: app-name
  template:
    metadata:
      labels:
        app: app-name
        version: v1
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      serviceAccountName: app-name
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000
      containers:
        - name: app
          image: registry/app:v1.2.3
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
              name: http
          env:
            - name: APP_ENV
              value: "production"
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: app-secrets
                  key: db-password
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
          livenessProbe:
            httpGet:
              path: /health/live
              port: http
            initialDelaySeconds: 10
            periodSeconds: 10
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /health/ready
              port: http
            initialDelaySeconds: 5
            periodSeconds: 5
            failureThreshold: 3
          startupProbe:
            httpGet:
              path: /health/live
              port: http
            initialDelaySeconds: 0
            periodSeconds: 5
            failureThreshold: 30
          volumeMounts:
            - name: tmp
              mountPath: /tmp
            - name: config
              mountPath: /app/config
              readOnly: true
      volumes:
        - name: tmp
          emptyDir: {}
        - name: config
          configMap:
            name: app-config
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    app: app-name
                topologyKey: kubernetes.io/hostname
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app: app-name
```

### Service with Health Checks
```yaml
apiVersion: v1
kind: Service
metadata:
  name: app-name
  labels:
    app: app-name
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app: app-name
```

### HorizontalPodAutoscaler
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-name
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app-name
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
        - type: Pods
          value: 4
          periodSeconds: 15
      selectPolicy: Max
```

### PodDisruptionBudget
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app-name
spec:
  minAvailable: 2  # or use maxUnavailable: 1
  selector:
    matchLabels:
      app: app-name
```

### NetworkPolicy (Default Deny + Allow Specific)
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-name-network-policy
spec:
  podSelector:
    matchLabels:
      app: app-name
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: api-gateway
      ports:
        - protocol: TCP
          port: 8080
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - protocol: TCP
          port: 5432
    - to:  # Allow DNS
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
```

---

## Debugging Commands

```bash
# Pod status and events
kubectl get pods -l app=app-name
kubectl describe pod <pod-name>
kubectl get events --sort-by='.lastTimestamp'

# Logs
kubectl logs <pod-name> --tail=100
kubectl logs <pod-name> --previous  # crashed container
kubectl logs -l app=app-name --all-containers

# Shell into container
kubectl exec -it <pod-name> -- /bin/sh

# Resource usage
kubectl top pods -l app=app-name
kubectl top nodes

# Network debugging
kubectl run debug --rm -it --image=nicolaka/netshoot -- /bin/bash

# Check endpoints
kubectl get endpoints app-name

# Rollout status
kubectl rollout status deployment/app-name
kubectl rollout history deployment/app-name
kubectl rollout undo deployment/app-name

# Scale
kubectl scale deployment/app-name --replicas=5

# Port forward for debugging
kubectl port-forward svc/app-name 8080:80
```

---

## Resource Guidelines

### Sizing Recommendations
| App Type | CPU Request | CPU Limit | Memory Request | Memory Limit |
|----------|-------------|-----------|----------------|--------------|
| Web API (Node/Python) | 100m | 500m | 128Mi | 512Mi |
| Web API (Java/Go) | 200m | 1000m | 256Mi | 1Gi |
| Background Worker | 100m | 500m | 128Mi | 512Mi |
| Cache (Redis) | 100m | 500m | 128Mi | 256Mi |
| Database (PostgreSQL) | 500m | 2000m | 512Mi | 4Gi |

### Limit-to-Request Ratios
- **CPU**: 2x-5x (allows bursting)
- **Memory**: 1x-2x (OOM kills if exceeded)
- **Production**: Keep ratios tighter for predictability

---

## Best Practices

### Reliability
- Always set resource requests and limits
- Use all three probe types (liveness, readiness, startup)
- Configure PodDisruptionBudget for voluntary disruptions
- Use pod anti-affinity for spreading across nodes/zones
- Set appropriate replica counts (minimum 3 for production)

### Security
- Run as non-root user
- Use read-only root filesystem
- Drop all capabilities, add only what's needed
- Use NetworkPolicies to restrict traffic
- Never store secrets in manifests — use external secret management

### Operations
- Use labels consistently for all resources
- Tag images with specific versions (never `:latest` in prod)
- Implement proper health check endpoints
- Configure HPA for auto-scaling
- Use namespaces to isolate environments

### Cost Optimization
- Right-size resource requests based on actual usage
- Use Vertical Pod Autoscaler for recommendations
- Consider spot/preemptible instances for non-critical workloads
- Implement cluster autoscaling

---

## Report Template

```markdown
# Kubernetes Deployment Review — {{APP_NAME}}

**Date**: {{DATE}}
**Cluster**: {{CLUSTER}}
**Namespace**: {{NAMESPACE}}

## Summary

| Category | Status | Issues |
|----------|--------|--------|
| Resources | 🟢/🟡/🔴 | {{COUNT}} |
| Reliability | 🟢/🟡/🔴 | {{COUNT}} |
| Security | 🟢/🟡/🔴 | {{COUNT}} |
| Scaling | 🟢/🟡/🔴 | {{COUNT}} |

## Resource Analysis

| Container | CPU Req | CPU Lim | Mem Req | Mem Lim | Status |
|-----------|---------|---------|---------|---------|--------|

## Issues Found

### Critical
{{CRITICAL_ISSUES}}

### High Priority
{{HIGH_ISSUES}}

### Recommendations
{{RECOMMENDATIONS}}

## Corrected Manifests
{{CORRECTED_YAML}}
```

---

## Severity Guide

| Level | Icon | Examples |
|-------|------|----------|
| **Critical** | 🔴 | Running as root, no resource limits, secrets in plain text, privileged containers |
| **High** | 🟠 | No health checks, single replica in prod, no PDB, :latest tag |
| **Medium** | 🟡 | No HPA, missing pod anti-affinity, overly permissive network |
| **Low** | 🟢 | Missing labels, suboptimal resource ratios, no annotations |

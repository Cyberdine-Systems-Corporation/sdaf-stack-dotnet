# Relación de componentes

```mermaid
flowchart TB
    core["sdaf-core\n(constitución + Gate 0)"]
    pack["pack.yaml\nsdaf-stack-dotnet"]

    subgraph agents ["Agentes de extensión"]
        frontend["frontend"]
        domainApp["domain-application\n(fusión domain+application)"]
        infra["infrastructure\n(stub)"]
    end

    subgraph skills ["Skills"]
        slice["csharp-adr006-slice"]
        blazor["blazor-bff-slice"]
        aspire["aspire-local-run"]
    end

    subgraph playbooks ["Playbooks"]
        standards["coding-standards-csharp"]
        vslice["vertical-slice-cqrs"]
    end

    consumer["Consumidor\n(submodule pinneado + sdaf.config.yaml)"]

    core --> pack
    pack --> agents
    pack --> skills
    pack --> playbooks
    domainApp --> slice
    frontend --> blazor
    slice --> vslice
    slice --> standards
    blazor --> standards
    pack --> consumer
    consumer --> core

    classDef core fill:#d0e3f8,stroke:#1e4d8b,color:#1e4d8b
    classDef stub fill:#e9ecef,stroke:#6c757d,color:#6c757d
    class core core
    class infra stub
```

## Lectura del diagrama

- `sdaf-core` manda sobre Gate 0 y el handbook Approved; el pack nunca lo sustituye.
- `pack.yaml` es el manifest que declara qué agentes, skills y playbooks aporta este overlay.
- `infrastructure` está marcado como **stub**: solo se activa bajo demanda humana explícita (ver [ADR-0002](adr/0002-infrastructure-stub.md)).
- El **consumidor** materializa el pack (symlinks, no copias) y vuelve a cerrar el ciclo contra `sdaf-core` en cada PBI.

## Relacionado

| Destino | Por qué |
|---------|---------|
| [Arquitectura](index.md) | Árbol del pack y contrato con sdaf-core |
| [ADR](adr/index.md) | Por qué domain+application está fusionado y por qué infrastructure es stub |
| [Adopción](../adoption/index.md) | Cómo se materializa este grafo en un consumidor |

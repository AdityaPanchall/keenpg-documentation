---
title: Features
hide:
  - toc
---

<div class="kp-hero" markdown>

# KeenPGO that never sleeps because we are keen for your Postgres

keenPGO runs open-source PostgreSQL on Kubernetes and keeps it fast, safe and
always on. You describe the database you want. keenPGO builds it, watches it,
repairs it and keeps it that way.Provide a User Interface console with operator.

[Get started :material-arrow-right:](quickstart.md){ .md-button .md-button--primary }
[Installation guides :material-book-open-variant:](Installation/index.md){ .md-button }

</div>

---

## :material-eye-outline: At a glance

<div class="grid cards" markdown>

-   :material-elephant:{ .lg .middle } **100% open-source PostgreSQL**

    ---

    Your data stays in standard PostgreSQL, and you
    can leave at any time with `pg_dump`.

-   :material-timer-sand:{ .lg .middle } **Failover in seconds**

    ---

    When a server dies, a replica takes over automatically and the old one
    heals and rejoins without anyone being paged.

-   :material-backup-restore:{ .lg .middle } **Restore to any point in time**

    ---

    Rewind your database to the moment before a mistake, not just to last
    night's backup.

-   :material-puzzle:{ .lg .middle } **Extensions included**

    ---

    pgvector, PostGIS, pg_partman, pgaudit, pg_cron and more are ready to
    switch on.

</div>

---

## :material-heart-pulse: Always on

<div class="grid cards" markdown>

-   :material-heart-pulse:{ .lg .middle } **Self-monitoring clusters**

    ---

    Every cluster watches its own health. Failed instances are detected and
    replaced without manual work.

    [:octicons-arrow-right-24: How failover works](architecture/ha.md)

-   :material-source-branch-sync:{ .lg .middle } **Automatic failover**

    ---

    A healthy replica is promoted to primary and applications reconnect to
    the same address.

-   :material-shield-sync:{ .lg .middle } **Synchronous replication**

    ---

    For data you cannot afford to lose, require a replica to confirm each
    write before it is acknowledged.

-   :material-update:{ .lg .middle } **Rolling updates**

    ---

    Settings changes, minor upgrades and node maintenance are applied one
    instance at a time to avoid downtime.

</div>

!!! success "Built to a standard"
    Every keenPGO cluster is built and run to these targets:
    **5 seconds or less** from a dead server to a new primary, with nobody
    paged.

---

## :material-backup-restore: Backup and recovery

<div class="grid cards" markdown>

-   :material-clock-time-four:{ .lg .middle } **Point-in-time recovery**

    ---

    Continuous archiving lets you restore to any second within your
    retention window.

-   :material-calendar-sync:{ .lg .middle } **Scheduled backups**

    ---

    Define schedules and retention once. keenPGO takes care of the rest.

-   :material-cloud-upload:{ .lg .middle } **Off-cluster storage**

    ---

    Keep backups outside the cluster, so they survive even if the cluster
    does not. `<List supported storage types.>`

-   :material-content-copy:{ .lg .middle } **Clone and restore**

    ---

    Create a new cluster from a backup for testing, reporting or recovery.

    [:octicons-arrow-right-24: Backup and restore](backups.md)

</div>

---

## :material-shield-lock: Security and compliance

<div class="grid cards" markdown>

-   :material-lock:{ .lg .middle } **Encrypted connections**

    ---

    TLS protects data in transit between applications and the database.

-   :material-account-key:{ .lg .middle } **User and access management**

    ---

    Declare users, roles and database access in the cluster definition.

-   :material-clipboard-text-search:{ .lg .middle } **Audit logging**

    ---

    Record who did what with pgaudit, to support compliance reviews.

-   :material-shield-check:{ .lg .middle } **Protected at every layer**

    ---

    Security covers networking, credentials, storage and access.

    [:octicons-arrow-right-24: Security](security.md)

</div>

---

## :material-hammer-wrench: Built for builders

Launch, scale, fail over and rewind with whichever tool suits your team.

=== ":material-kubernetes: Kubernetes YAML"

    Declare a cluster and let the operator do the work.

    ```yaml title="Kubernetes YAML"
    apiVersion: <api-group>/<version>
    kind: <ClusterKind>
    metadata:
      name: orders
    spec:
      instances: 3
    ```

=== ":material-console: CLI"

    ```sh title="CLI"
    # <Replace with your real CLI command>
    keenpg create cluster orders --instances 3
    ```

=== ":material-monitor-dashboard: Console"

    ```text title="Console"
    Please visit the below Youtube video for walkthrough of keenpgo console
    ```

Everything you can do by hand, keenPGO can also do on its own.

---

## :material-puzzle: Extensions and workloads

<div class="grid cards" markdown>

-   :material-map-marker-radius:{ .lg .middle } **Geospatial**

    ---

    Location queries and mapping with PostGIS.

-   :material-table-split-cell:{ .lg .middle } **Partitioning and scheduling**

    ---

    Manage big tables with pg_partman and run jobs inside the database with
    pg_cron.

-   :material-chart-line:{ .lg .middle } **Query insight**

    ---

    Find slow queries with pg_stat_statements.

</div>

???+ info "Included extensions"

    - :material-check-circle:{ .kp-check } pgvector
    - :material-check-circle:{ .kp-check } PostGIS
    - :material-check-circle:{ .kp-check } pg_partman
    - :material-check-circle:{ .kp-check } pg_stat_statements
    - :material-check-circle:{ .kp-check } pgaudit
    - :material-check-circle:{ .kp-check } pg_cron
    - :material-check-circle:{ .kp-check } pgcrypto

---

## :material-tune-variant: Run it your way

| | :material-kubernetes: keenPGO on Kubernetes | :material-monitor-multiple: keenPG Automation |
|---|---|---|
| :material-server: **Runs on** | Kubernetes, OpenShift, OKD, Rancher | Your virtual machines |
| :material-target: **Best for** | Container-based platforms | Teams running PostgreSQL on VMs |
| :material-cog: **Management** | Operator and cluster definitions | Automated cluster setup |
| :material-book-open-page-variant: **Documentation** | You are here | `<Link when available>` |

[Install on your platform :material-arrow-right:](Installation/index.md){ .md-button }

---

## :material-swap-horizontal: Leave proprietary licences behind

Moving from a proprietary database to open-source PostgreSQL does not mean
rewriting your business. A typical migration follows four stages:

<div class="grid cards" markdown>

-   :material-magnify:{ .lg .middle } **1. Assess**

    ---

    review schema, code and dependencies

-   :material-swap-horizontal:{ .lg .middle } **2. Convert**

    ---

    translate objects and application code

-   :material-test-tube:{ .lg .middle } **3. Test**

    ---

    validate behaviour and performance

-   :material-flag-checkered:{ .lg .middle } **4. Cut over**

    ---

    switch with minimal downtime

</div>

Ask our team about a migration plan for your database.

---

## :material-headset: Support from people who run it

<div class="grid cards" markdown>

-   :material-headset:{ .lg .middle } **24×7 engineers**

    ---

    Postgres engineers on call around the clock, every day of the year.

-   :material-clock-fast:{ .lg .middle } **15-minute first response**

    ---

    A human engineer responds to critical issues within 15 minutes on
    24×7 plans.

-   :material-calendar-star:{ .lg .middle } **3 extra years of patches**

    ---

    Every PostgreSQL version receives three additional years of patches, so
    you upgrade on your schedule.

-   :material-account-tie:{ .lg .middle } **A named Technical Account Manager and Engineer**

    ---

    Early-access customers get a Technical Account Manager for smooth support and relation with the customers also one engineer who knows their setup.

</div>

---

## :material-rocket-launch: Ready to try it?

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Follow the quickstart**

    ---

    A running cluster in minutes.

    [:octicons-arrow-right-24: Quickstart](quickstart.md)

-   :material-lifebuoy:{ .lg .middle } **Talk to an engineer**

    ---

    Ask about the database you already run.

    [:octicons-arrow-right-24: Book a demo](https://keenpg.in/contact?intent=expert)

</div>
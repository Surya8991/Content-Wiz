---
title: Designing Scalable Data Pipelines for Machine Learning Applications
published: true
description: A model is only as good as the pipeline feeding it. Here is what separates a production-grade ML data pipeline from a notebook that happens to work.
tags: machinelearning, dataengineering, mlops, python
---

Most ML projects do not fail because the model is wrong. They fail because the data pipeline feeding the model cannot survive contact with production. A notebook that trains a model on a clean CSV proves nothing about whether that model can get fresh, correct, timely data once real users and real systems are involved.

Data engineering and ML engineering are converging fast, and the teams that treat pipeline design as a first-class discipline ship faster and break less often than teams that treat it as plumbing.

## Batch vs Streaming: Choosing the Right Processing Model

The first architectural decision is whether your pipeline processes data in batches or as a continuous stream, and this choice shapes everything downstream.

Batch pipelines process accumulated data on a schedule: hourly, daily, or triggered by an event like a file landing in storage. They suit training pipelines, periodic feature recomputation, and any workload where a few hours of staleness is acceptable. Batch systems are simpler to reason about, easier to debug, and cheaper to run because you are not paying for always-on compute.

Streaming pipelines process events as they arrive, typically through a message broker like Apache Kafka, AWS Kinesis, or Google Pub/Sub. They fit use cases where prediction freshness matters: fraud detection, recommendation systems reacting to a user's last three clicks, or dynamic pricing. Streaming introduces real complexity: you need to handle out-of-order events, late-arriving data, and windowing logic, and your infrastructure runs continuously rather than on a schedule.

Most production ML systems do not pick one model exclusively. A common pattern is the lambda architecture, where a batch layer computes accurate historical features and a streaming layer computes approximate real-time features, with both feeding the same model through a shared feature store. Choosing streaming when batch would do adds operational cost without benefit. Choosing batch when the business need is real-time inference produces a model that answers questions users already stopped asking.

## Feature Stores: Closing the Training-Serving Gap

The single most common bug in production ML is training-serving skew: a feature computed one way during training and a slightly different way during inference. A model trained on a seven-day rolling average and served with a feature pipeline that computes a five-day average will degrade silently, and the failure often looks like model drift rather than a pipeline bug.

Feature stores exist to close this gap. Tools like Feast, Tecton, and the feature store components inside Databricks and SageMaker let a team define a feature once and serve it consistently to both the training job and the online inference endpoint. The store typically splits into an offline store for large-scale batch training data and an online store, usually a low-latency key-value database like Redis or DynamoDB, for real-time lookups at inference time.

A feature store also solves a second problem: feature reuse across teams. Without one, every model team recomputes the same customer lifetime value or session-length feature with slightly different logic, and nobody can explain why two models disagree. A shared, versioned feature definition removes that ambiguity and cuts the time it takes to stand up a new model that reuses existing signals.

## Data Versioning, Lineage, and Reproducibility

A model trained six months ago on data that no longer exists in its original form is not reproducible, and that is a compliance and debugging problem, not just an inconvenience. When a stakeholder asks why a model made a specific prediction, the answer often requires reconstructing the exact training dataset, the exact feature transformations, and the exact code version used at that point in time.

Data versioning tools like DVC, LakeFS, and Delta Lake's time travel feature let you snapshot datasets the way Git snapshots code. Combine that with lineage tracking, which records how each dataset was derived from upstream sources through which transformations, and you get an audit trail that answers "where did this number come from" without archaeology.

Lineage matters even more once a pipeline breaks. When a downstream metric looks wrong, lineage tooling like OpenLineage or Marquez lets an engineer trace the anomaly back through every transformation step to the source table, instead of grepping through scattered scripts and hoping someone remembers the logic.

## Schema Drift and Data Quality at Scale

Upstream systems change without warning. A product team renames a column, an event schema adds a new required field, or a third-party API silently changes a data type from integer to string. In a small pipeline, someone notices immediately. In a pipeline processing millions of rows a day across dozens of sources, that change propagates before anyone catches it, and the first sign of trouble is a model producing nonsense predictions.

Schema drift detection needs to be automated, not manual. Tools like Great Expectations, Deequ, and Soda Core let teams define expectations (this column is never null, this value falls within this range, this categorical field only contains these values) and run them as part of every pipeline execution. A failed expectation should stop the pipeline before bad data reaches a training job or a serving layer, not after a model has already been retrained on corrupted inputs.

According to the Great Expectations 2024 State of Data Quality report, data quality issues remain one of the top cited causes of delayed ML deployments among surveyed data teams, ahead of model performance problems. Data quality is not a nice-to-have check bolted on at the end. It is the layer that decides whether everything built on top of it can be trusted.

## Orchestration: Where the Pipeline Actually Runs

None of the above matters if there is no reliable system scheduling, retrying, and monitoring the pipeline. Orchestration tools coordinate dependencies between tasks, handle failures, and give engineers visibility into what ran, what failed, and why.

Apache Airflow remains the most widely adopted orchestrator, with DAGs defined in Python and a large ecosystem of operators for connecting to databases, cloud storage, and ML platforms. Dagster takes a more asset-centric approach, treating datasets and features as first-class objects with typed contracts between steps, which catches integration errors earlier than Airflow's task-centric model. Kubeflow Pipelines targets teams already running on Kubernetes and wanting orchestration that spans both data preparation and model training in the same DAG, with native support for GPU scheduling.

The right choice depends less on feature checklists and more on team context: existing infrastructure, the skill set already on the team, and whether the primary need is generic data movement (Airflow) or ML-specific workflow tracking (Kubeflow).

## From Notebook to Production: The Gap Nobody Budgets For

A notebook proves an idea works on a fixed dataset at a single point in time. Production requires that same logic to run correctly on data that changes shape, arrives late, occasionally goes missing, and gets processed by multiple people who did not write the original notebook.

Closing that gap means turning notebook cells into tested, parameterized, version-controlled functions, adding monitoring and alerting for both pipeline health and data quality, and building retry and backfill logic for the inevitable day something fails at 2 a.m. It also means separating the "figure out if this is a good idea" work, which stays fast and exploratory, from the "make this reliable in production" work, which follows the same engineering discipline as any other critical service. Teams that skip this transition end up with a fragile pipeline nobody wants to touch, and every new feature request becomes a fresh risk of breaking training or serving in production.

Building this discipline early costs less than rebuilding a pipeline after it has already caused a bad model deployment. Structured [data engineering training](https://www.edstellar.com/topic/data-engineering-training) helps teams build these skills before the pipeline becomes the bottleneck.

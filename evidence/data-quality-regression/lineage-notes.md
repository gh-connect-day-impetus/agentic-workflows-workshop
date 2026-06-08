# Lineage Notes

Recent lineage change:

```text
source.invoice_export
  -> staging.invoice_reconciliation
  -> mart.revenue_health_daily
  -> dashboard.revenue_health
```

The staging step added a deduplication rule using the latest update timestamp. The source export does not guarantee timestamp ordering within a batch.


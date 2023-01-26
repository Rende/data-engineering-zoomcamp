```bash
aydan.rende@de-zoomcamp-instance:~/data-engineering-zoomcamp/week_1_basics_n_setup/1_terraform_gcp/terraform$ terraform plan
var.project
  Your GCP Project ID

  Enter a value: de-zoomcamp-2023-XXXXXX


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + labels                     = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "europe-west6"
      + project                    = "de-zoomcamp-2023-XXXXXX"
      + self_link                  = (known after apply)

      + access {
          + domain         = (known after apply)
          + group_by_email = (known after apply)
          + role           = (known after apply)
          + special_group  = (known after apply)
          + user_by_email  = (known after apply)

          + dataset {
              + target_types = (known after apply)

              + dataset {
                  + dataset_id = (known after apply)
                  + project_id = (known after apply)
                }
            }

          + routine {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + routine_id = (known after apply)
            }

          + view {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + table_id   = (known after apply)
            }
        }
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EUROPE-WEST6"
      + name                        = "dtc_data_lake_de-zoomcamp-2023-XXXXXX"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }

          + condition {
              + age                   = 30
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }

      + website {
          + main_page_suffix = (known after apply)
          + not_found_page   = (known after apply)
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
aydan.rende@de-zoomcamp-instance:~/data-engineering-zoomcamp/week_1_basics_n_setup/1_terraform_gcp/terraform$ terraform apply
var.project
  Your GCP Project ID

  Enter a value: de-zoomcamp-2023-XXXXXX


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "trips_data_all"
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + labels                     = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "europe-west6"
      + project                    = "de-zoomcamp-2023-XXXXXX"
      + self_link                  = (known after apply)

      + access {
          + domain         = (known after apply)
          + group_by_email = (known after apply)
          + role           = (known after apply)
          + special_group  = (known after apply)
          + user_by_email  = (known after apply)

          + dataset {
              + target_types = (known after apply)

              + dataset {
                  + dataset_id = (known after apply)
                  + project_id = (known after apply)
                }
            }

          + routine {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + routine_id = (known after apply)
            }

          + view {
              + dataset_id = (known after apply)
              + project_id = (known after apply)
              + table_id   = (known after apply)
            }
        }
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EUROPE-WEST6"
      + name                        = "dtc_data_lake_de-zoomcamp-2023-XXXXXX"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }

          + condition {
              + age                   = 30
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }

      + website {
          + main_page_suffix = (known after apply)
          + not_found_page   = (known after apply)
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_storage_bucket.data-lake-bucket: Creation complete after 1s [id=dtc_data_lake_de-zoomcamp-2023-XXXXXX]
google_bigquery_dataset.dataset: Creation complete after 1s [id=projects/de-zoomcamp-2023-XXXXXX/datasets/trips_data_all]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
aydan.rende@de-zoomcamp-instance:~/data-engineering-zoomcamp/week_1_basics_n_setup/1_terraform_gcp/terraform$ terraform destroy
var.project
  Your GCP Project ID

  Enter a value: de-zoomcamp-2023-XXXXXX

google_storage_bucket.data-lake-bucket: Refreshing state... [id=dtc_data_lake_de-zoomcamp-2023-XXXXXX]
google_bigquery_dataset.dataset: Refreshing state... [id=projects/de-zoomcamp-2023-XXXXXX/datasets/trips_data_all]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be destroyed
  - resource "google_bigquery_dataset" "dataset" {
      - creation_time                   = 1674745664212 -> null
      - dataset_id                      = "trips_data_all" -> null
      - default_partition_expiration_ms = 0 -> null
      - default_table_expiration_ms     = 0 -> null
      - delete_contents_on_destroy      = false -> null
      - etag                            = "lDebMcCkJvlLVN1o79Ef8A==" -> null
      - id                              = "projects/de-zoomcamp-2023-XXXXXX/datasets/trips_data_all" -> null
      - labels                          = {} -> null
      - last_modified_time              = 1674745664212 -> null
      - location                        = "europe-west6" -> null
      - project                         = "de-zoomcamp-2023-XXXXXX" -> null
      - self_link                       = "https://bigquery.googleapis.com/bigquery/v2/projects/de-zoomcamp-2023-XXXXXX/datasets/trips_data_all" -> null

      - access {
          - role          = "OWNER" -> null
          - user_by_email = "de-zoomcamp-sa@de-zoomcamp-2023-XXXXXX.iam.gserviceaccount.com" -> null
        }
      - access {
          - role          = "OWNER" -> null
          - special_group = "projectOwners" -> null
        }
      - access {
          - role          = "READER" -> null
          - special_group = "projectReaders" -> null
        }
      - access {
          - role          = "WRITER" -> null
          - special_group = "projectWriters" -> null
        }
    }

  # google_storage_bucket.data-lake-bucket will be destroyed
  - resource "google_storage_bucket" "data-lake-bucket" {
      - default_event_based_hold    = false -> null
      - force_destroy               = true -> null
      - id                          = "dtc_data_lake_de-zoomcamp-2023-XXXXXX" -> null
      - labels                      = {} -> null
      - location                    = "EUROPE-WEST6" -> null
      - name                        = "dtc_data_lake_de-zoomcamp-2023-XXXXXX" -> null
      - project                     = "de-zoomcamp-2023-XXXXXX" -> null
      - public_access_prevention    = "inherited" -> null
      - requester_pays              = false -> null
      - self_link                   = "https://www.googleapis.com/storage/v1/b/dtc_data_lake_de-zoomcamp-2023-XXXXXX" -> null
      - storage_class               = "STANDARD" -> null
      - uniform_bucket_level_access = true -> null
      - url                         = "gs://dtc_data_lake_de-zoomcamp-2023-XXXXXX" -> null

      - lifecycle_rule {
          - action {
              - type = "Delete" -> null
            }

          - condition {
              - age                        = 30 -> null
              - days_since_custom_time     = 0 -> null
              - days_since_noncurrent_time = 0 -> null
              - matches_prefix             = [] -> null
              - matches_storage_class      = [] -> null
              - matches_suffix             = [] -> null
              - num_newer_versions         = 0 -> null
              - with_state                 = "ANY" -> null
            }
        }

      - versioning {
          - enabled = true -> null
        }
    }

Plan: 0 to add, 0 to change, 2 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

google_storage_bucket.data-lake-bucket: Destroying... [id=dtc_data_lake_de-zoomcamp-2023-XXXXXX]
google_bigquery_dataset.dataset: Destroying... [id=projects/de-zoomcamp-2023-XXXXXX/datasets/trips_data_all]
google_bigquery_dataset.dataset: Destruction complete after 1s
google_storage_bucket.data-lake-bucket: Destruction complete after 1s

Destroy complete! Resources: 2 destroyed.
```
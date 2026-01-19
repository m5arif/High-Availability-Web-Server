 IaC, Cloud Knowledge, and Reliability.

The Folder Structure

my-terraform-project/
├── modules/
│   ├── vpc/               # Networking module
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── ec2/               # Compute module
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── main.tf                # The entry point that calls modules
├── variables.tf           # Global variables
├── outputs.tf             # What the user gets back (e.g., Load Balancer IP)
├── provider.tf            # Provider versions (AWS, etc.)
├── .gitignore             # Critical! (See Step 3)
└── README.md              # The most important file

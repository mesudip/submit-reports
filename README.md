# submit-reports

GitHub Action to submit Allure reports to Allure Report Host using GitHub OIDC.

## Quick Start
```yaml
permissions:
  contents: read
  id-token: write
  checks: write

steps:
  - uses: actions/checkout@v6
  - uses: ./
    with:
      server-url: your-host
      path: allure-results
      report-type: allure
      report-name: unit-tests
      branch: ${{ github.ref_name }}
```

## Inputs
- `server-url` (required): report host only (with or without scheme). Examples: `your-host`, `https://your-host`, `localhost:8080`
- `path` (required): `allure-results` directory or `.zip`
- `report-name` (optional, default: stable `github.job`-based name)
- `branch` (optional)
- `report-type` (optional, default `allure`)
- `audience` (optional, defaults to resolved host[:port])
- `project-name` (optional; for OIDC it must match token repository when provided)
- `api-key` (optional fallback)
- `publish-commit-check` (optional, default `true`): publish a commit check with report details
- `check-name-prefix` (optional, default `Test Report`)

## Outputs
- `report-version-id`
- `report-url`
- `report-url-absolute`
- `project-name`
- `report-name`
- `total`, `passed`, `failed`, `broken`, `skipped`, `unknown` (allure parsing stats)

## Commit Checklist Integration
- The action publishes a GitHub Check Run on the commit (default enabled).
- Check title includes the report name.
- For `allure` type, summary includes pass/fail/broken/skipped/unknown counts.
- Summary includes a direct link to the uploaded report page.
- Workflow must grant `checks: write` permission.

## Security Note
- The action does not send unsigned GitHub context metadata for trust decisions.
- Backend trust should come from the signed OIDC JWT claims.

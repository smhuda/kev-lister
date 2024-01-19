# kev-lister
This python program grabs the CISA Known Exploited Vulnerability (KEV) list from CISA and parses only the list of CVEs in plaintext for ingestion on other tools.

## Usage
```normal
python kev-lister.py
```
## Description
This will grab the CISA KEV list from <https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json> and then parse the CVEs in plaintext in the format of `kev-cves-{current_date}.txt`.
The aim is for the CVE list to be used as part of other tool stacks for monitoring.

## Reason of writing this
The reason of writing this is so this python program can be taken and automated to run weekly or monthly basis, to grab the latest KEV CVE listing to ingest on tools.

## Contributing
Contributions, issues, and feature requests are welcome! 

If you liked this or if it helped you in any way

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/smhuda)

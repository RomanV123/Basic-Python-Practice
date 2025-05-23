from urllib.parse import urlparse
import re
import tldextract  # type: ignore

url = input("Enter a URL to check: ").strip()

if not url:
    print("❌ No URL provided.")
else:
    parsed = urlparse(url)
    scheme = parsed.scheme
    netloc = parsed.netloc

    if netloc.count('.') > 3:
        print("⚠️ Too many subdomains — might be spoofing a site")

    if scheme != "https":
        print("⚠️ Does not use HTTPS — suspicious")

    if re.match(r'\d+\.\d+\.\d+\.\d+', netloc):
        print("⚠️ Uses an IP address — suspicious")

    extracted = tldextract.extract(url)
    print("Domain:", extracted.domain)
    print("Suffix:", extracted.suffix)
    print("Subdomain:", extracted.subdomain)







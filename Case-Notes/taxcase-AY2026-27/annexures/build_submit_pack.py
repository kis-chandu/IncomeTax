import base64, markdown, pathlib, re
D = pathlib.Path("/home/user/taxcase-AY2026-27"); R = pathlib.Path("/home/user/IncomeTax"); OUT = D/"submit-pack"; OUT.mkdir(exist_ok=True)
CSS = """<style>
@page { size: A4; margin: 14mm 12mm; }
body { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 10pt; color:#111; line-height:1.42; }
h1 { font-size: 13.5pt; border-bottom: 2px solid #333; padding-bottom:4px;}
h2 { font-size: 11.5pt; border-bottom: 1px solid #999; padding-bottom:2px; margin-top:16px;}
h3 { font-size: 10.5pt; margin-top:12px;}
table { border-collapse: collapse; width: 100%; margin: 6px 0 12px; font-size: 8.6pt; }
th, td { border: 1px solid #888; padding: 3px 5px; vertical-align: top; }
th { background: #eee; }
pre { font-family: 'Courier New', monospace; font-size: 6.4pt; white-space: pre-wrap; word-wrap: break-word; line-height:1.25; }
img.pg { display:block; max-width:100%; page-break-after: always; }
.hdr { color:#444; font-size:8.5pt; margin-bottom:10px;}
</style>"""
def html(title, body_md, pre=None, cls=""):
    body = f"<pre>{pre}</pre>" if pre is not None else markdown.markdown(body_md, extensions=['tables'])
    (OUT/f"{title}.html").write_text(f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title>{CSS}</head><body class='{cls}'>{body}</body></html>", encoding='utf-8')
    print("built", title)
# 1. LETTER (slice: COVER LETTER .. before SUBMISSION NOTES)
txt = (D/"07-REPLY-DRAFT-142(1).md").read_text()
txt = txt[txt.index("## COVER LETTER"):]
txt = txt[:txt.index("### SUBMISSION NOTES")]
html("P1-Reply-Letter-142(1)-AY2025-26", txt)
# 2. 26AS text -> printable
t26 = (R/"FY2024-25_AY2025-26/03-AIS-TIS/Form26AS-AY2025-26-TRACES-onDemand-req200524931.txt").read_text(errors='replace')
html("P2B-Form26AS-AY2025-26", "", pre="FORM 26AS — ANNUAL TAX STATEMENT — AY 2025-26 (PAN on file)\nAs downloaded from TRACES/e-Filing portal (on-demand request 200524931)\n" + "="*100 + "\n" + t26)
# 3. P2-C as-filed computation
html("P2C-Computation-As-Filed-AY2025-26", """# ANNEXURE P2-C — COMPUTATION OF TOTAL INCOME AS FILED, AY 2025-26
**Ack 522131170310725 dated 31-Jul-2025 · ITR-2 · Old regime**
| Particulars | ₹ |
|---|---|
| Gross salary (Form 16) | 40,23,083 |
| Less: exempt u/s 10 (as filed) | 1,34,184 |
| Less: standard deduction u/s 16(ia) | 50,000 |
| Less: professional tax u/s 16(iii) | 2,400 |
| **Income from salaries** | **38,36,499** |
| Income from house property (24(b) capped) | (2,00,000) |
| Capital gains — VDA u/s 115BBH (as filed) | 113 |
| Income from other sources (dividend 8,009 + savings interest 8,505 + deposit interest 4,807 + equipment-lease rental 12,240 + platform interest 38,170) | 71,731 |
| **Gross total income** | **37,08,343** |
| VI-A: 80C 1,50,000 · 80CCD(1B) 50,000 · 80D 25,000 · 80EEA 1,50,000 · 80TTA 8,505 | 3,83,505 |
| **Total income (as filed)** | **33,24,840** |
| Tax thereon (incl. VDA @30%: ₹34) | 8,09,952 |
| Health & Education Cess @4% | 32,398 |
| **Total tax (as filed)** | **8,42,350** |
| TDS claimed in return | 9,75,885 |
| **Refund as filed** | **1,33,540** |
*Note: Σ TDS per Form 26AS (P2-B) = ₹9,75,916.14; the additional ₹31.14 is now claimed in the corrected computation (Annexure Z). Corrected figures are separately placed at Annexure Z — this annexure reproduces only the as-filed position.*""")
# 4-5. P3-B, P8-B verbatim
html("P3B-Narration-Index-FY2024-25", (D/"annexures/ANNEXURE-P3B-NARRATION-INDEX.md").read_text())
html("P8B-VDA-Trade-Extract", (D/"annexures/ANNEXURE-P8B-VDA-EXTRACT.md").read_text())
# 6. Z sanitized
z = (D/"annexures/ANNEXURE-Z-CORRECTED-COMPUTATION.md").read_text().replace(" (OPTION B final)", "").replace("ANNEXURE Z — CORRECTED COMPUTATION OF TOTAL INCOME, AY 2025-26", "ANNEXURE Z — CORRECTED COMPUTATION OF TOTAL INCOME, AY 2025-26")
z = re.sub(r"\n> Internal note.*$", "", z, flags=re.S)
html("Z-Corrected-Computation-AY2025-26", z)
# 7. P5-A deed + foreclosure images
hdr = "<h1>ANNEXURE P5-A — PROPERTY & LOAN DOCUMENT EXTRACTS (demand #5)</h1><p class='hdr'>Registered Absolute Sale Deed BNS-I-5063-2021-22 (16-Aug-2021) — Flat C-114, Mukunda Brundhavan, Kodigehalli, Bengaluru (RERA PRM/KA/RERA/1251/446/PR/200121/003220). Purchasers: Chandrakant Gorai &amp; Priyanka Gorai · Consideration ₹44,26,500. p1: title/sellers · p2: developer · p3: purchasers · p6: consideration &amp; property. Final page: SBI foreclosure letter 18-Jan-2025 (outstanding ₹42,01,075; closure value ₹42,19,245).</p>"
imgs = ""
base = R/"FY2024-25_AY2025-26/07-HomeLoan-SBI-Loan-40108253827/SaleDeed-Extracts"
for f in sorted(base.glob("*.jpg")) + [R/"FY2024-25_AY2025-26/07-HomeLoan-SBI-Loan-40108253827/SBI-HL-Foreclosure-Letter-18Jan2025-ClosureValue-4219245.jpg"]:
    b = base64.b64encode(f.read_bytes()).decode()
    imgs += f"<img class='pg' src='data:image/jpeg;base64,{b}'/>"
(OUT/"P5A-SaleDeed-Foreclosure-Extracts.html").write_text(f"<!doctype html><html><head><meta charset='utf-8'>{CSS}</head><body>{hdr}{imgs}</body></html>", encoding='utf-8')
print("built P5A")
# 8. P5 interest derivation note
html("P5-Interest-Derivation-Note", """# P5 (supporting) — HOUSING-LOAN INTEREST DERIVATION, FY 2024-25
**Loan: SBI HL 40108253827 (sanctioned 31-Mar-2021, ₹44L) → refinanced by HDFC Ltd takeover loan 703764316 on 18-Feb-2025 (closure value ₹42,19,245 per SBI foreclosure letter 18-Jan-2025; outstanding ₹42,01,075).**
| Period | Source | Interest ₹ | Basis |
|---|---|---|---|
| Oct-2024 | SBI CASLOAN ledger (enclosed) — **actual** | 33,035 | Bank's own posting @9.25% |
| Nov-2024 | SBI CASLOAN ledger — **actual** | 31,987 | Bank's own posting |
| Dec-2024 | SBI CASLOAN ledger — **actual** | 33,059 | Bank's own posting |
| **Oct–Dec 2024 sub-total** | | **98,081** | |
| Apr–Sep 2024 & Jan–18 Feb 2025 | **Derived** | ≈ 2,41,000 | CASLOAN-measured rate 9.25% applied on the declining balance (≈₹45.6L → ₹42.2L), consistent with SBI's FY2023-24 **actual** full-year interest certificate of ₹3,98,319 (enclosed) |
| **SBI FY 2024-25 (up to foreclosure)** | | **≈ 3,39,000** | |
| 18-Feb→31-Mar-2025 | HDFC takeover loan — **derived** (₹42,19,245 × ~8.8–9% × 41 days) | ≈ 30,000 | Exact per HDFC loan statement (furnished on requisition) |
| **Total FY 2024-25 housing-loan interest** | | **≈ 3,69,000** | |
| **Claimed: 24(b) ₹2,00,000 + 80EEA ₹1,50,000 = ₹3,50,000** | | **≤ 3,69,000 ✓** | Interest actually accrued exceeds the aggregate claim |
| Repayment (own income) | SBI a/c …8384: 11 EMI × ₹31,000 + 6 part-prepay × ₹10,000 = ₹4,01,000, funded by 11 own UPI × ₹45,000 from salary a/c HDFC …3550 | | Bank-proven |""")
print("ALL DONE")
